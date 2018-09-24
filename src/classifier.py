import pycld2 as cld2
from pyfasttext import FastText

model = FastText('lid.176.bin')


def cld2_prediction(texts):
    return [cld2_predict_one(text) for text in texts]


def cld2_predict_one(text):
    try:
        return cld2.detect(text)[2][0][1]
    except:
        return "un"


def ft_prediction(texts):
    results = model.predict(texts)
    return [lang[0] if lang != [] else "un" for lang in results]
