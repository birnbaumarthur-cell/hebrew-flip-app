import streamlit as st

# Include fonts
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre&display=swap');
@font-face {
    font-family: 'Henri';
    src: url('path_to_your_henri_regular.woff2') format('woff2');
}
.hebrew {
    font-family: 'Frank Ruhl Libre', serif;
    font-size: 20px;
    direction: rtl;
}
.latin {
    font-family: 'Henri', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# Example Hebrew database
hebrew_texts = {
    "Genesis": {
        1: {
            1: "בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ",
            2: "וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ..."
        }
    },
    "Exodus": {
        1: {1: "וְאֵלֶּה שִׁמְעוֹן..."}
    }
}

# Sidebar selections
book = st.selectbox("Select Book", list(hebrew_texts.keys()))
chapter = st.number_input("Chapter number", min_value=1, step=1)
verse = st.number_input("Verse number", min_value=1, step=1)

# Fetch verse safely
verse_text = hebrew_texts.get(book, {}).get(chapter, {}).get(verse, "Verse not found")

# Display Hebrew with proper font
st.markdown(f"<div class='hebrew'>{verse_text}</div>", unsafe_allow_html=True)

# Download button
st.download_button(
    label="Download Hebrew Verse",
    data=verse_text,
    file_name=f"{book}_{chapter}_{verse}.txt",
    mime="text/plain"
)
