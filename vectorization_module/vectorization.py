from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
import scipy.sparse as sps
import numpy as np
import joblib


def vectorize_parameters(name,
                         description,
                         genres,
                         media_type,
                         episodes,
                         year,
                         studios,
                         rating):
    name_vectorizer = joblib.load('name_vectorizer.joblib')
    name_vectors = name_vectorizer.transform([name])

    description_vectorizer = joblib.load('description_vectorizer.joblib')
    description_vectors = description_vectorizer.transform([description])

    param_dict = [{
        "Name": name,
        "Genres": genres,
        "Type": media_type,
        "Episodes": episodes,
        "Year": year,
        "Studios": studios,
        "Rating": rating}]
    dict_vectorizer = joblib.load('dict_vectorizer.joblib')
    dict_vectors = dict_vectorizer.transform(param_dict).toarray()

    all_vectors = sps.hstack([name_vectors, description_vectors, dict_vectors]).todense()

    return all_vectors
