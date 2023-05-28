import re
import html
import unicodedata


# Helper function for preprocessing
def preprocess(
    text,
    lower=True,
    normalize=True,
    punctuation=False,
    numbers=False,
    unhyphenate=False,
    remove_lines=False,
    remove_spaces=False,
    entities=False,
    fill=" ",
):
    if not entities:
        text = html.unescape(text)

    if unhyphenate:
        text = re.sub(r"[-»—]\s?\n", "", text, flags=re.MULTILINE)

    if lower:
        text = text.lower()  # Lowercase

    if normalize:
        text = text.replace("V", "U").replace("v", "u")  # Normalize V/U

    if not punctuation:
        # Remove punctuation
        punctuation = "\"#$%&'()*+,/:;<=>@[\]^_`{|}~.?!«»—“-”"
        misc = "¡£¤¥¦§¨©¯°±²³´µ¶·¸¹º¼½¾¿÷·–‘’†•ↄ∞⏑〈〉（）"
        misc += punctuation
        translator = str.maketrans({key: fill for key in misc})
        text = text.translate(translator)

    if not numbers:
        # Remove numbers
        translator = str.maketrans({key: fill for key in "0123456789"})
        text = text.translate(translator)

    if remove_lines:
        text = " ".join(text.split("\n"))

    if remove_spaces:
        text = fill.join(text.split())

    # Fix spacing
    text = re.sub(" +", " ", text)

    text = unicodedata.normalize("NFC", text)

    return text.strip()
