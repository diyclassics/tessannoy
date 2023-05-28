from tessannoy import TessAnnoyIndex
import pickle

data = pickle.load(open("data/tess_vectors.pkl", "rb"))

index = TessAnnoyIndex(data["vector"], data["name"], data["citation"])
index.build()
index.save("data/tessannoy.ann")
