import pickle

# TODO
model_path = "models/d_tree4.pkl"


with open(model_path, 'rb') as f:
    d_tree_4 = pickle.load(f)


def predict(sample):
    return d_tree_4.predict(sample).tolist()[0]