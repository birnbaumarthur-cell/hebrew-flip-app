import streamlit as st
import requests

# --------------------------
#  Hebrew Font + Styling
# --------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre&display=swap');
.hebrew {
    font-family: 'Frank Ruhl Libre', serif;
    font-size: 22px;
    direction: rtl;
    background-color: #f5f5f5;
    padding: 12px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------
# Book Categories
# --------------------------
torah = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy"
]

prophets = [
    "Joshua", "Judges", "Samuel I", "Samuel II",
    "Kings I", "Kings II", "Isaiah", "Jeremiah", "Ezekiel",
    "Hosea", "Joel", "Amos", "Obadiah", "Jonah", "Micah",
    "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi"
]

writings = [
    "Psalms", "Proverbs", "Job", "Song of Songs", "Ruth",
    "Lamentations", "Ecclesiastes", "Esther", "Daniel",
    "Ezra", "Nehemiah", "Chronicles I", "Chronicles II"
]

# --------------------------
# UI Layout
# --------------------------
st.title("Hebrew Text Fetcher (Sefaria)")

category = st.selectbox("Category:", ["Torah", "Prophets", "Writings"])

if category == "Torah":
    book = st.selectbox("Book:", torah)
elif category == "Prophets":
    book = st.selectbox("Book:", prophets)
else:
    book = st.selectbox("Book:", writings)

chapter = st.number_input("Chapter", step=1, min_value=1)
verse = st.number_input("Verse", step=1, min_value=1)

# --------------------------
# Fetch Text from Sefaria
# --------------------------
url = f"https://www.sefaria.org/api/texts/{book}.{chapter}.{verse}?lang=he&commentary=0&wrap=0"

try:
    r = requests.get(url)
    data = r.json()
    hebrew = data.get("he", "Verse not found")
except:
    hebrew = "Error fetching verse"

# --------------------------
# Display Hebrew
# --------------------------
st.markdown(f"<div class='hebrew'>{hebrew}</div>", unsafe_allow_html=True)

# --------------------------
# Copy Button
# --------------------------
st.code(hebrew, language=None)
