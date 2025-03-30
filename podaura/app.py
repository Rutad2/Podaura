from flask import Flask, render_template, request
from textblob import TextBlob
from podcasts import podcast_recommendations

app = Flask(__name__)

# 🔍 Smart mood detection using keywords + sentiment fallback
def analyze_mood(user_input):
    text = user_input.lower()
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    # 🎯 Keyword-based detection first
    if any(word in text for word in ["angry", "furious", "rage", "irritated", "pissed", "annoyed"]):
        return "angry"
    elif any(word in text for word in ["stressed", "overwhelmed", "anxious", "tense", "burned out"]):
        return "stressed"
    elif any(word in text for word in ["sad", "depressed", "lonely", "cry", "hopeless"]):
        return "sad"
    elif any(word in text for word in ["melancholy", "meh", "empty", "low", "gray", "apathetic"]):
        return "melancholy"
    elif any(word in text for word in ["excited", "pumped", "ecstatic", "thrilled", "hyped"]):
        return "excited"
    elif any(word in text for word in ["relaxed", "chill", "calm", "peaceful", "zen"]):
        return "relaxed"
    elif any(word in text for word in ["happy", "joyful", "cheerful", "good", "great", "smiling"]):
        return "happy"

    # 🧠 Fallback to sentiment polarity
    if polarity > 0.6:
        return "excited"
    elif 0.3 <= polarity <= 0.6:
        return "happy"
    elif 0.1 <= polarity < 0.3:
        return "relaxed"
    elif -0.1 < polarity < 0.1:
        return "neutral"
    elif -0.3 <= polarity <= -0.1:
        return "melancholy"
    elif -0.6 <= polarity < -0.3:
        return "sad"
    elif polarity <= -0.6:
        return "angry"
    else:
        return "neutral"

@app.route("/", methods=["GET", "POST"])
def index():
    mood = None
    suggestions = []

    if request.method == "POST":
        user_input = request.form["moodtext"]
        mood = analyze_mood(user_input)
        suggestions = podcast_recommendations.get(mood, [])

    return render_template("index.html", mood=mood, suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)
