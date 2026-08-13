from flask import Flask, render_template, request
import whisper
import spacy
import re
import os

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load AI models once
whisper_model = whisper.load_model("base")
nlp = spacy.load("en_core_web_sm")


@app.route("/", methods=["GET", "POST"])
def home():

    transcript = ""
    actions = []

    if request.method == "POST":

        # Get uploaded audio
        audio = request.files["audio"]

        # Save audio
        audio_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            audio.filename
        )

        audio.save(audio_path)

        # -------------------------
        # AUDIO → TEXT
        # -------------------------

        result = whisper_model.transcribe(audio_path)

        transcript = result["text"]

        # -------------------------
        # TEXT → ACTION ITEMS
        # -------------------------

        doc = nlp(transcript)

        for sentence in doc.sents:

            sentence_text = sentence.text.strip()
            lower_text = sentence_text.lower()

            person = None

            # Find person
            for entity in sentence.ents:
                if entity.label_ == "PERSON":
                    person = entity.text
                    break

            # Action words
            action_words = [
                "will",
                "please",
                "need to",
                "should",
                "must"
            ]

            is_action = any(
                word in lower_text
                for word in action_words
            )

            if is_action:

                if person is None:
                    person = "Not identified"

                # Find deadline
                deadline = "Not mentioned"

                pattern = (
                    r"\b(by|on|before)\s+"
                    r"(tomorrow|today|Monday|Tuesday|Wednesday|"
                    r"Thursday|Friday|Saturday|Sunday)\b"
                )

                match = re.search(
                    pattern,
                    sentence_text,
                    re.IGNORECASE
                )

                if match:
                    deadline = match.group(2)

                # Extract task
                task = sentence_text

                if "will" in lower_text:
                    task = re.split(
                        r"\bwill\b",
                        task,
                        maxsplit=1,
                        flags=re.IGNORECASE
                    )[1]

                elif "please" in lower_text:
                    task = re.split(
                        r"\bplease\b",
                        task,
                        maxsplit=1,
                        flags=re.IGNORECASE
                    )[1]

                elif "need to" in lower_text:
                    task = re.split(
                        r"\bneed to\b",
                        task,
                        maxsplit=1,
                        flags=re.IGNORECASE
                    )[1]

                elif "should" in lower_text:
                    task = re.split(
                        r"\bshould\b",
                        task,
                        maxsplit=1,
                        flags=re.IGNORECASE
                    )[1]

                elif "must" in lower_text:
                    task = re.split(
                        r"\bmust\b",
                        task,
                        maxsplit=1,
                        flags=re.IGNORECASE
                    )[1]

                if match:
                    task = task[:match.start()].strip()

                task = task.strip(" .,!?")

                actions.append({
                    "person": person,
                    "task": task,
                    "deadline": deadline
                })

    return render_template(
        "index.html",
        transcript=transcript,
        actions=actions
    )


if __name__ == "__main__":
    app.run(debug=True)