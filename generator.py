import numpy as np


class LightFMGenerator:

    def __init__(self, model):
        self.model = model
        self.size = np.arange(model.item_embeddings.shape[0])

    def predict(self, user_id, count):
        scores = self.model.predict(user_id, self.size)
        top_items = np.argsort(-scores)
        top_results = top_items[0:count]

        return top_results
