import streamlit as st

# Hebrew text database (example, expand as needed)
hebrew_texts = {
    "Numbers": {
        30: {
            2: "וַיְדַבֵּר מֹשֶׁה אֶל-רָאשֵׁי הַמַּטּוֹת, לִבְנֵי יִשְׂרָאֵל לֵאמֹר: זֶה הַדָּבָר, אֲשֶׁר צִוָּה יְהוָה.",
            3: "וְכִי יִשָּׂא אִישׁ אִשָּׁה..."
            # add more verses as needed
        }
    }
}

# Function to flip Hebrew text
def flip_hebrew(text):
    return text[::-1]

# Streamlit UI
st.title("Hebrew Text Flipper")

# Book selection
book = st.selectbox("Select Book", list(hebrew_texts.keys()))

# Chapter selection
chapter = st.number_input("Chapter number", min_value=1, step=1)

# Verse range selection
start_verse = st.number_input("Start verse", min_value=1, step=1)
end_verse = st.number_input("End verse (leave same as start for single verse)", min_value=start_verse, step=1)

# Flip button
if st.button("Flip Hebrew"):
    if book not in hebrew_texts:
        st.error("Book not found in local database.")
    elif chapter not in hebrew_texts[book]:
        st.error("Chapter not found in local database.")
    else:
        output = []
        for verse in range(start_verse, end_verse + 1):
            if verse in hebrew_texts[book][chapter]:
                flipped = flip_hebrew(hebrew_texts[book][chapter][verse])
                output.append(f"{verse}: {flipped}")
            else:
                output.append(f"{verse}: Verse not found")

        st.subheader("Flipped Hebrew:")
        for line in output:
            st.text(line)
