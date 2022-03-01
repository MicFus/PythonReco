import pickle
from urllib.request import urlopen
import sys


def load_lightfm_hybrid_100k():
    print('loading the model', file=sys.stdout)

    modelUrl = "https://recommodels.blob.core.windows.net/models/lightfm_hybrid_model.obj"
    model = pickle.load(urlopen(modelUrl))

    print('model loaded', file=sys.stdout)
    return model
