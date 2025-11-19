# Hebrew text database (example, you can expand as needed)
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
    # Simple character-level flip
    return text[::-1]

# User input
book = input("Book (e.g., Numbers): ").strip()
chapter = int(input("Chapter number: ").strip())
start_verse = int(input("Start verse: ").strip())
end_verse_input = input("End verse (leave empty if single verse): ").strip()
end_verse = int(end_verse_input) if end_verse_input else start_verse

# Check if book/chapter exist
if book not in hebrew_texts:
    print("Book not found in local database.")
else:
    if chapter not in hebrew_texts[book]:
        print("Chapter not found in local database.")
    else:
        output = []
        for verse in range(start_verse, end_verse + 1):
            if verse in hebrew_texts[book][chapter]:
                flipped = flip_hebrew(hebrew_texts[book][chapter][verse])
                output.append(f"{verse}: {flipped}")
            else:
                output.append(f"{verse}: Verse not found")
        print("\nFlipped Hebrew:\n")
        for line in output:
            print(line)

import streamlit as st

st.title("Hebrew Flip Tool")

book = st.text_input("Book (e.g., Numbers)")
chapter = st.text_input("Chapter number")
start_verse = st.text_input("Start verse")
end_verse = st.text_input("End verse (optional)")

if st.button("Flip Hebrew"):
    if book and chapter and start_verse:
        flipped_text = get_flipped_hebrew(book, chapter, start_verse, end_verse)
        st.text_area("Flipped Hebrew", value=flipped_text, height=400)
    else:
        st.warning("Please fill in book, chapter, and start verse.")
