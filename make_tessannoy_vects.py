import numpy as np
from collections import defaultdict

from cltkreaders.lat import LatinTesseraeCorpusReader
import spacy

import pickle
from tqdm import tqdm

from latintools import preprocess

nlp = spacy.load("la_core_web_lg")

CR = LatinTesseraeCorpusReader()

files = [file for file in CR.fileids() if CR.metadata("genre", file) == "epic"]

data = {}

for file in tqdm(files):
    docrows = CR.doc_rows(file)
    for docrow in docrows:
        for citation, text in docrow.items():
            doc = nlp(preprocess(text))
            data[citation] = {"text": text, "vector": doc.vector}

citations = defaultdict(list)
names = defaultdict(list)
vectors = defaultdict(list)

for key, value in data.items():
    citations["citation"].append(key)
    names["name"].append(value["text"])
    vectors["vector"].append(value["vector"])

data = {
    "citation": np.array(citations["citation"]),
    "name": np.array(names["name"]),
    "vector": np.array(vectors["vector"]),
}

pickle.dump(data, open("data/tess_vectors.pkl", "wb"))
