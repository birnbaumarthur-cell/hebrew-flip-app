import streamlit as st
import requests

# Function to flip Hebrew text
def flip_hebrew(text):
    return text[::-1]

# Streamlit UI
st.title("Hebrew Flip App")

book = st.text_input("Book (e.g., Numbers)")
chapter = st.text_input("Chapter number")
verse = st.text_input("Verse number")  # only single verse

if st.button("Flip Hebrew"):
    if not book or not chapter or not verse:
        st.warning("Please enter book, chapter, and verse.")
    else:
        # Build API URL for single verse
        url = f"https://www.sefaria.org/api/texts/{book}.{chapter}.{verse}?lang=he"

        # Fetch data
        response = requests.get(url)
        if response.status_code != 200:
            st.error("Error fetching text from Sefaria.")
        else:
            data = response.json()
            hebrew_texts = data.get("he", [])

            # Ensure it’s a list
            if isinstance(hebrew_texts, str):
                hebrew_texts = [hebrew_texts]

            st.subheader(f"Flipped Hebrew: {book} {chapter}:{verse}")
            for v in hebrew_texts:
                st.text(flip_hebrew(v))
