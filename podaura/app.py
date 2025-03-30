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

        # 🎭 More Mood Categories
        if polarity > 0.6:
            mood = "excited"
        elif 0.3 <= polarity <= 0.6:
            mood = "happy"
        elif 0.1 <= polarity < 0.3:
            mood = "relaxed"
        elif -0.1 < polarity < 0.1:
            mood = "neutral"
        elif -0.3 <= polarity <= -0.1:
            mood = "melancholy"
        elif -0.6 <= polarity < -0.3:
            mood = "sad"
        elif polarity <= -0.6:
            mood = "angry"
        else:
            mood = "stressed"

        # Fetch podcasts for the detected mood
        suggestions = podcast_recommendations.get(mood, [])

    return render_template("index.html", mood=mood, suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)
