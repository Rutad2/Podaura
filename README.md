# Podaura

Podaura is a mood-based podcast recommendation web app built at HooHacks 2025.

## What it does

- Users enter how they’re feeling
- It analyzes their mood using TextBlob (sentiment analysis)
- Based on the detected mood (happy, sad, angry, neutral), it suggests podcasts
- Podcasts are curated manually for each emotion

## Technologies Used

- Python (Flask)
- TextBlob (for mood detection)
- HTML/CSS
- Git + GitHub

## How to Run It

```bash
git clone https://github.com/Rutad2/Podaura.git
cd Podaura
cd podaura
pip install flask textblob
python -m textblob.download_corpora
python app.py
