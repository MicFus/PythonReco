import pickle
from urllib.request import urlopen


def load():
    modelUrl = "https://sarmodelmaster.blob.core.windows.net/models/finalized_model.sav"
    model = pickle.load(urlopen(modelUrl))
    return model


# class ModelLoader():
#     def __init__(self) -> None:
#         modelUrl = "https://sarmodelmaster.blob.core.windows.net/models/finalized_model.sav"
#         self.model = pickle.load(urlopen(modelUrl))
