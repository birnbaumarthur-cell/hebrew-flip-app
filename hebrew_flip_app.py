import streamlit as st
import requests
import streamlit.components.v1 as components

# Hebrew books list
books = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "Samuel I", "Samuel II", "Kings I", "Kings II"
]

def flip_hebrew(text):
    return text[::-1]

st.title("Hebrew Flip App")

# Book selection
book = st.selectbox("Select Book", books)
chapter = st.text_input("Chapter number")
verse = st.text_input("Verse number")

if st.button("Flip Hebrew"):
    if not chapter or not verse:
        st.warning("Please enter chapter and verse.")
    else:
        ref = f"{book}.{chapter}.{verse}"
        url = f"https://www.sefaria.org/api/texts/{ref}?lang=he&commentary=0&context=0"
        response = requests.get(url)
        if response.status_code != 200:
            st.error("Error fetching text from Sefaria.")
        else:
            data = response.json()
            hebrew_text = data.get("he", [])
            if isinstance(hebrew_text, list):
                hebrew_text = hebrew_text[0] if hebrew_text else ""
            hebrew_text = hebrew_text.replace("\u200e", "").strip()
            flipped_text = flip_hebrew(hebrew_text)

            st.subheader(f"Flipped Hebrew: {book} {chapter}:{verse}")
            
            # Display flipped text with Henri Regular font
            custom_font_html = f"""
            <link href="https://fonts.googleapis.com/css2?family=Henri&display=swap" rel="stylesheet">
            <div style="font-family: 'Henri', sans-serif; font-size: 24px; direction: rtl;">
                {flipped_text}
            </div>
            """
            st.markdown(custom_font_html, unsafe_allow_html=True)

            # Copy button
            copy_button_code = f"""
            <script>
            function copyText() {{
                navigator.clipboard.writeText(`{flipped_text}`);
                alert("Copied to clipboard!");
            }}
            </script>
            <button onclick="copyText()">Copy Text</button>
            """
            components.html(copy_button_code, height=60)
