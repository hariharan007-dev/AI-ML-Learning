# Game Recommendation System

A content-based game recommendation system built using Python and Machine Learning.

The system takes a game title as input and recommends similar games based on their genres and development teams.

## How It Works

The recommendation system follows these steps:

1. Load the game dataset using Pandas.
2. Remove unnecessary columns from the dataset.
3. Remove duplicate game titles.
4. Combine the `Genres` and `Team` columns into a `features` column.
5. Convert the text features into numerical vectors using TF-IDF.
6. Calculate similarity between games using Cosine Similarity.
7. Find the games most similar to the selected game.
8. Display the top 10 recommendations through a Flask web application.

### Workflow

```text
Game Dataset
     ↓
Data Cleaning
     ↓
Genres + Team
     ↓
TF-IDF
     ↓
Cosine Similarity
     ↓
Similar Games
     ↓
Flask Web Application