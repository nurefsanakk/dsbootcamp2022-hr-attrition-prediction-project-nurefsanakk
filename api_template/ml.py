import pickle

# TODO
model_path = 'models/*****'


with open(model_path, 'rb') as f:
    d_tree_4 = pickle.load(f)


def predict(sample):
    return d_tree_4.predict(sample).tolist()[0]