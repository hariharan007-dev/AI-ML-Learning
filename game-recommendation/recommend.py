import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load dataset
data = pd.read_csv("data/games.csv")


# Remove unnecessary columns
data.drop(columns=[
    "Release Date",
    "Rating",
    "Times Listed",
    "Number of Reviews",
    "Reviews",
    "Plays",
    "Playing",
    "Backlogs",
    "Wishlist",
    "Unnamed: 0"
], inplace=True)


# Create features
data["features"] = (
    data["Genres"].fillna("") + " " +
    data["Team"].fillna("")
)


# Remove duplicate titles
data.drop_duplicates(subset="Title", inplace=True)

# Reset index
data.reset_index(drop=True, inplace=True)


# TF-IDF
vector = TfidfVectorizer()

x = vector.fit_transform(data["features"])


# Cosine similarity
similarity = cosine_similarity(x)


def recommend(game_title):

    matches = data[
        data["Title"].str.contains(
            game_title,
            case=False,
            na=False
        )
    ]

    if matches.empty:
        return []

    game_index = matches.index[0]

    scores = similarity[game_index]

    similar_games = list(enumerate(scores))

    similar_games = sorted(
        similar_games,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in similar_games[1:11]:

        recommendations.append({
            "title": data.iloc[index]["Title"],
            "score": round(score, 3)
        })

    return recommendations