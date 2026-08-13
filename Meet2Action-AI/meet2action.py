import whisper
import spacy
import re

# Load models
whisper_model = whisper.load_model("base")
nlp = spacy.load("en_core_web_sm")

# Get audio file
audio_file = input("Enter audio file name: ")

# -------------------------
# 1. AUDIO → TEXT
# -------------------------

result = whisper_model.transcribe(audio_file)
transcript = result["text"]

print("\n===== TRANSCRIPT =====")
print(transcript)


# -------------------------
# 2. TEXT → ACTION ITEMS
# -------------------------

doc = nlp(transcript)

print("\n===== ACTION ITEMS =====")

for sentence in doc.sents:

    sentence_text = sentence.text.strip()
    lower_text = sentence_text.lower()

    person = None

    # Find person
    for entity in sentence.ents:
        if entity.label_ == "PERSON":
            person = entity.text
            break

    # Find sentences that look like action items
    action_words = [
        "will",
        "please",
        "need to",
        "should",
        "must"
    ]

    is_action = any(word in lower_text for word in action_words)

    if is_action:

        # -------------------------
        # Find person
        # -------------------------

        if person is None:
            person = "Not identified"

        # -------------------------
        # Find deadline
        # -------------------------

        deadline = "Not mentioned"

        deadline_pattern = (
            r"\b(by|on|before)\s+"
            r"(tomorrow|today|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b"
        )

        match = re.search(
            deadline_pattern,
            sentence_text,
            re.IGNORECASE
        )

        if match:
            deadline = match.group(2)

        # -------------------------
        # Extract task
        # -------------------------

        task = sentence_text

        if "will" in lower_text:
            task = re.split(r"\bwill\b", task, maxsplit=1, flags=re.IGNORECASE)[1]

        elif "please" in lower_text:
            task = re.split(r"\bplease\b", task, maxsplit=1, flags=re.IGNORECASE)[1]

        elif "need to" in lower_text:
            task = re.split(r"\bneed to\b", task, maxsplit=1, flags=re.IGNORECASE)[1]

        elif "should" in lower_text:
            task = re.split(r"\bshould\b", task, maxsplit=1, flags=re.IGNORECASE)[1]

        elif "must" in lower_text:
            task = re.split(r"\bmust\b", task, maxsplit=1, flags=re.IGNORECASE)[1]

        # Remove deadline from task
        if match:
            task = task[:match.start()].strip()

        task = task.strip(" .,!?")

        print("\nPerson   :", person)
        print("Task     :", task)
        print("Deadline :", deadline)
        print("-" * 35)