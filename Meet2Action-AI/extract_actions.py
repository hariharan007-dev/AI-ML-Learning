import spacy
import re

nlp = spacy.load("en_core_web_sm")

text = """
Harry will prepare the presentation by tomorrow.
Harry will collect the dataset by Friday.
Harry will test the machine learning model on Saturday.
We will review the final results on Monday.
"""

doc = nlp(text)

for sentence in doc.sents:

    sentence_text = sentence.text.strip()

    # Find the person
    person = None

    for entity in sentence.ents:
        if entity.label_ == "PERSON":
            person = entity.text

    # Check whether this sentence contains an action
    if person and "will" in sentence_text.lower():

        task = sentence_text.split("will", 1)[1].strip()

        # Find deadline
        deadline = "Not mentioned"

        match = re.search(
            r"\b(by|on|before)\s+(tomorrow|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b",
            task,
            re.IGNORECASE
        )

        if match:
            deadline = match.group(2)

            # Remove deadline from the task
            task = task[:match.start()].strip()

        # Remove unnecessary punctuation
        task = task.rstrip(".")

        print("Person   :", person)
        print("Task     :", task)
        print("Deadline :", deadline)
        print("-" * 35)