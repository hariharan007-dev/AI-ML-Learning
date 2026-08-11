from flask import Flask, render_template, request

from recommend import recommend


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []
    game = ""

    if request.method == "POST":

        game = request.form["game"]

        recommendations = recommend(game)

    return render_template(
        "index.html",
        recommendations=recommendations,
        game=game
    )


if __name__ == "__main__":
    app.run(debug=True)