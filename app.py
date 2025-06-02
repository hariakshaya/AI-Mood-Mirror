import streamlit as st
from transformers import pipeline
import random

# Mood-color mapping for background bloom
mood_colors = {
    "happy": "#FFFACD",     # LemonChiffon
    "sad": "#87CEFA",       # LightSkyBlue
    "angry": "#FF6F61",     # Coral Red
    "neutral": "#D3D3D3",   # LightGray
    "surprise": "#FFD700",  # Gold
    "fear": "#8A2BE2",      # BlueViolet
    "disgust": "#98FB98",   # PaleGreen
}

# Music & podcast suggestions per mood
music_links = {
    "happy": ["https://open.spotify.com/track/6fTt0CH2t0mdeB2gk1B9Sx"],  # Example links
    "sad": ["https://open.spotify.com/track/1u8c2t2Cy7UBoG4ArRcF5g"],
    "angry": ["https://open.spotify.com/track/1rqqCSm0Qe4I9rUvWncaom"],
    "neutral": ["https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT"],
    "surprise": ["https://open.spotify.com/track/3tCvdHVsEnrVKYkWcEkk2b"],
    "fear": ["https://open.spotify.com/track/3kVQVX9c69f81a7dtYeE9U"],
    "disgust": ["https://open.spotify.com/track/2p8IUWQDrpjuFltbdgLOag"],
}

quotes = {
    "happy": "Keep smiling, the world is brighter with you!",
    "sad": "It’s okay to feel sad. You’re doing your best.",
    "angry": "Take a deep breath — you’re stronger than you think.",
    "neutral": "Even calm days hold beauty. 🌿",
    "surprise": "Life’s full of surprises — embrace the magic!",
    "fear": "Courage is not the absence of fear but moving forward despite it.",
    "disgust": "Let go of what’s not meant for you. You deserve peace.",
}

journal_prompts = {
    "happy": "What made you smile today?",
    "sad": "What’s one small thing you can do to feel better?",
    "angry": "Write about what's frustrating you without judgment.",
    "neutral": "Describe your current state in three words.",
    "surprise": "What unexpected thing happened recently?",
    "fear": "What’s one fear you’d like to let go of?",
    "disgust": "Write about something you're ready to release emotionally.",
}

# Load NLP sentiment analysis pipeline
nlp = pipeline("sentiment-analysis")

# Streamlit App Config
st.set_page_config(page_title="AI Mood Mirror 🌈", layout="centered")

st.title("🪞 AI Mood Mirror")
st.markdown("Tell me how you're feeling today — I’m listening 💬")

# User input
user_input = st.text_area("Type your current feelings or emotions:")

if user_input:
    analysis = nlp(user_input)[0]
    label = analysis['label'].lower()

    # Simplify labels for mapping
    mood = "neutral"
    if "pos" in label:
        mood = "happy"
    elif "neg" in label:
        # Try inferring deeper emotion based on keywords
        if any(word in user_input.lower() for word in ["cry", "alone", "lost"]):
            mood = "sad"
        elif any(word in user_input.lower() for word in ["angry", "mad", "rage"]):
            mood = "angry"
        elif any(word in user_input.lower() for word in ["scared", "afraid"]):
            mood = "fear"
        elif any(word in user_input.lower() for word in ["gross", "ew", "disgust"]):
            mood = "disgust"
        else:
            mood = "sad"
    elif "neu" in label:
        mood = "neutral"

    # 🌈 Color bloom background
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {mood_colors[mood]};
        background-image: radial-gradient(circle at top left, white, {mood_colors[mood]});
        color: #1a1a1a;  /* Darker text */
    }}
    h1, h2, h3, h4, h5, h6, p {{
        color: #1a1a1a !important;  /* Override light color */
        text-shadow: 0px 0px 1px rgba(0, 0, 0, 0.1);
    }}
    .stTextInput > div > div > input {{
        background-color: #ffffff;
        color: #000000;
    }}
    .stTextArea textarea {{
        background-color: #ffffff;
        color: #000000;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

    # ✨ Show mood results
    st.success(f"**Detected Mood:** {mood.capitalize()}")

    st.subheader("💡 Motivational Quote")
    st.info(quotes[mood])

    st.subheader("📝 Journal Prompt")
    st.write(journal_prompts[mood])

    st.subheader("🎧 Music / Podcast Recommendation")
    for link in music_links[mood]:
        st.markdown(f"- [Listen here]({link})")

    st.balloons()
