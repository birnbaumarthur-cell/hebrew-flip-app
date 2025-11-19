import streamlit as st
import requests

def flip_hebrew(text):
    return text[::-1]

st.title("Hebrew Flip App")

book = st.text_input("Book (e.g., Numbers)")
chapter = st.text_input("Chapter number")
verse = st.text_input("Verse number")  # single verse only

if st.button("Flip Hebrew"):
    if not book or not chapter or not verse:
        st.warning("Please enter book, chapter, and verse.")
    else:
        ref = f"{book}.{chapter}.{verse}"
        url = f"https://www.sefaria.org/api/texts/{ref}?lang=he&commentary=0&context=0"
        response = requests.get(url)
        if response.status_code != 200:
            st.error("Error fetching text from Sefaria.")
        else:
            data = response.json()
            # 'he' contains a list; take only first string element
            hebrew_text = data.get("he", [])
            if isinstance(hebrew_text, list):
                hebrew_text = hebrew_text[0] if hebrew_text else ""
            # clean any stray invisible characters
            hebrew_text = hebrew_text.replace("\u200e", "").strip()
            st.subheader(f"Flipped Hebrew: {book} {chapter}:{verse}")
            st.text(flip_hebrew(hebrew_text))
