import streamlit as st
from transformers import pipeline
import random

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

# Mood-based recommendations
mood_data = {
    "POSITIVE": {
        "quote": [
            "Keep shining, the world needs your light!",
            "Your vibe attracts your tribe.",
            "Celebrate your wins, no matter how small!"
        ],
        "journaling": [
            "What made you smile today?",
            "Describe a moment when you felt proud recently.",
            "Write about someone who made your day better."
        ],
        "music": [
            "[Happy – Pharrell Williams](https://www.youtube.com/watch?v=ZbZSe6N_BXs)",
            "[Best Day of My Life – American Authors](https://www.youtube.com/watch?v=Y66j_BUCBMY)"
        ],
        "podcast": [
            "[The Daily Boost](https://www.dailyboost.com/)",
            "[Happier with Gretchen Rubin](https://gretchenrubin.com/podcasts/)"
        ]
    },
    "NEGATIVE": {
        "quote": [
            "You’ve survived 100% of your worst days so far.",
            "Tough times never last, but tough people do.",
            "It's okay to rest. Healing is not a race."
        ],
        "journaling": [
            "What’s one thing you want to let go of?",
            "Write a letter to yourself full of encouragement.",
            "What’s one act of self-care you can do today?"
        ],
        "music": [
            "[Let It Go – James Bay](https://www.youtube.com/watch?v=GsPq9mzFNGY)",
            "[Rise Up – Andra Day](https://www.youtube.com/watch?v=lwgr_IMeEgA)"
        ],
        "podcast": [
            "[The Mindful Kind](https://www.rachelkable.com/podcast)",
            "[Therapy Chat](https://www.therapychatpodcast.com/)"
        ]
    }
}

# Streamlit UI
st.set_page_config(page_title="AI Mood Mirror", layout="centered")
st.title("🪞 AI Mood Mirror")
st.markdown("Enter how you feel, and I’ll reflect support, quotes, journaling prompts, and media recommendations 🌈")

user_input = st.text_area("How are you feeling today?")

if user_input:
    result = sentiment_pipeline(user_input)[0]
    mood = result['label'].upper()

    st.subheader("🔍 Detected Mood:")
    st.write(f"**{mood.capitalize()}**")

    data = mood_data.get(mood, mood_data["POSITIVE"])

    st.subheader("🧘‍♀️ Journaling Prompt")
    st.write(random.choice(data["journaling"]))

    st.subheader("💬 Motivational Quote")
    st.write(random.choice(data["quote"]))

    st.subheader("🎵 Music Recommendation")
    st.markdown(random.choice(data["music"]), unsafe_allow_html=True)

    st.subheader("🎧 Podcast Suggestion")
    st.markdown(random.choice(data["podcast"]), unsafe_allow_html=True)

    st.markdown("---")
    st.success("Take a deep breath. You're doing great 🌟")
