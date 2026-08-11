import re


def analyze_threat(message):

    indicators = []

    text = message.lower()

    # Prize / reward language
    prize_words = [
        "won", "winner", "prize", "reward",
        "cash", "bonus", "jackpot"
    ]

    if any(word in text for word in prize_words):
        indicators.append("Prize or reward language detected")

    # Urgency
    urgency_words = [
        "urgent", "immediately", "now",
        "act fast", "limited time",
        "final warning"
    ]

    if any(word in text for word in urgency_words):
        indicators.append("Urgent action requested")

    # Money
    money_words = [
        "£", "$", "€", "money",
        "payment", "cash", "bank"
    ]

    if any(word in text for word in money_words):
        indicators.append("Money-related content detected")

    # Phone number
    if re.search(r"\b\d{7,15}\b", message):
        indicators.append("Phone number detected")

    # URL
    if re.search(r"https?://|www\.", text):
        indicators.append("Suspicious link detected")

    # Claim language
    claim_words = [
        "claim", "collect",
        "receive", "selected"
    ]

    if any(word in text for word in claim_words):
        indicators.append("Claim/selection language detected")

    return indicators