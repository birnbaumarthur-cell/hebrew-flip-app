import streamlit as st

def flip_hebrew_text(text):
    """
    Flips Hebrew text for display purposes.
    """
    lines = text.split('\n')
    flipped_lines = [''.join(reversed(line)) for line in lines]
    return '\n'.join(flipped_lines)

st.set_page_config(page_title="Hebrew Flipper", layout="wide")
st.title("Hebrew Text Flipper")

# Input section
book = st.text_input("Book (e.g., Numbers)", "Numbers")
chapter = st.text_input("Chapter number", "30")
start_verse = st.text_input("Start verse", "2")
end_verse = st.text_input("End verse (leave empty for single verse)", "")

# Input Hebrew text
st.info("Paste Hebrew text for the selected range here:")
hebrew_input = st.text_area("Hebrew Text", height=300)

# Flip button
if st.button("Flip Hebrew"):
    if not hebrew_input.strip():
        st.error("Please paste the Hebrew text to flip.")
    else:
        flipped = flip_hebrew_text(hebrew_input)
        st.subheader(f"Flipped Hebrew Text ({book} {chapter}:{start_verse}" +
                     (f"-{end_verse}" if end_verse else "") + ")")
        st.text_area("Flipped Hebrew", flipped, height=300)
