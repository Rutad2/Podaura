from flask import Flask, render_template, request
from textblob import TextBlob
from podcasts import podcast_recommendations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    mood = None
    suggestions = []

    if request.method == "POST":
        user_input = request.form["moodtext"]
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        if polarity > 0.2:
            mood = "happy"
        elif polarity < -0.2:
            mood = "sad"
        elif polarity < 0.2 and polarity > -0.2:
            mood = "neutral"
        else:
            mood = "angry"

        suggestions = podcast_recommendations.get(mood, [])

    return render_template("index.html", mood=mood, suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)
