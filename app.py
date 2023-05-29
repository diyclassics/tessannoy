import pickle
import pandas as pd
import random

from tessannoy import TessAnnoyIndex

import streamlit as st

st.set_page_config(layout="wide")

st.title("TessAnnoy")
st.subheader("Vector-based verse search for CLTK-Tesserae texts")
st.text("*Only available currently for epic*")


@st.cache_data
def load_data():
    data = pickle.load(open("data/tess_vectors.pkl", "rb"))
    return data


data = load_data()
index = TessAnnoyIndex(data["vector"], data["name"], data["citation"])
index.load("data/tessannoy.ann")


if st.button("Show random verse"):
    random_item = random.randint(0, len(data["name"]) - 1)

    query = index.query(data["vector"][random_item], k=25)

    results = []
    for i, q in enumerate(query, 0):
        results.append(
            [
                i,
                q[0],
                q[1],
            ]
        )
    df = pd.DataFrame(results, columns=["Rank", "Citation", "Text"], index=None)

    st.dataframe(df, width=720)
