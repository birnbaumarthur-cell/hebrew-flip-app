import streamlit as st
import requests

# Function to flip Hebrew text
def flip_hebrew(text):
    return text[::-1]

# Streamlit UI
st.title("Hebrew Flip App")

book = st.text_input("Book (e.g., Genesis)")
chapter = st.text_input("Chapter number")
start_verse = st.text_input("Start verse (leave empty for full chapter)")
end_verse = st.text_input("End verse (leave empty if single verse or full chapter)")

if st.button("Flip Hebrew"):
    if not book or not chapter:
        st.warning("Please enter book and chapter.")
    else:
        # Build API URL
        if start_verse:
            if end_verse:
                url = f"https://www.sefaria.org/api/texts/{book}.{chapter}.{start_verse}-{end_verse}?lang=he"
            else:
                url = f"https://www.sefaria.org/api/texts/{book}.{chapter}.{start_verse}?lang=he"
        else:
            url = f"https://www.sefaria.org/api/texts/{book}.{chapter}?lang=he"

        # Fetch data
        response = requests.get(url)
        if response.status_code != 200:
            st.error("Error fetching text from Sefaria.")
        else:
            data = response.json()
            hebrew_texts = data.get("he", [])
            if isinstance(hebrew_texts, str):
                hebrew_texts = [hebrew_texts]  # single verse

            st.subheader("Flipped Hebrew")
            for i, verse in enumerate(hebrew_texts, start=int(start_verse) if start_verse else 1):
                st.text(f"{i}: {flip_hebrew(verse)}")
