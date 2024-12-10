import pandas
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
import scipy.sparse as sps
import joblib
import re

dataset = pandas.read_csv('./anime.csv')[["MAL_ID", "Name", "Score", "Genres", "Type", "Episodes", "Aired", "Studios", "Rating"]]
dataset.drop(dataset[dataset["Score"] == "Unknown"].index, inplace=True)
dataset_synopsis = pandas.read_csv('./anime_with_synopsis.csv')[["MAL_ID", "sypnopsis"]]
dataset_merged = dataset.merge(dataset_synopsis, how='inner', on="MAL_ID")
dataset_merged["Studios"] = dataset_merged["Studios"].apply(lambda x: x.split(', '))
dataset_merged["Genres"] = dataset_merged["Genres"].apply(lambda x: x.split(', '))
dataset_no_text_dicts = dataset_merged[["Genres", "Type", "Episodes", "Aired", "Studios", "Rating"]].to_dict('records')

scores = dataset_merged["Score"].values.astype('float64')
print(type(scores))
joblib.dump(scores, 'scores_np.joblib', compress=9)

year_aired = []
for index, row in dataset_merged.iterrows():
    year = re.search(r"[1,2]\d\d\d", row["Aired"])
    if year != None:
        year = year.group(0)
        year_aired.append({"MAL_ID":row["MAL_ID"], "Year": int(year)})
    else:
        year_aired.append({"MAL_ID":row["MAL_ID"], "Year": 0})

dataset_merged = dataset_merged.merge(pandas.DataFrame(year_aired), how='inner', on="MAL_ID")

name_vectorizer = CountVectorizer()
name_vectors = name_vectorizer.fit_transform(dataset_merged["Name"].values.astype('U'))
print(name_vectors.shape)
joblib.dump(name_vectorizer, 'name_vectorizer.joblib', compress=9)

description_vectorizer = CountVectorizer()
description_vectors = description_vectorizer.fit_transform(dataset_merged["sypnopsis"].values.astype('U'))
print(description_vectors.shape)
joblib.dump(description_vectorizer, 'description_vectorizer.joblib', compress=9)

dict_vectorizer = DictVectorizer()
dict_vectors = dict_vectorizer.fit_transform(dataset_no_text_dicts).toarray()
print(dict_vectors.shape)
joblib.dump(dict_vectorizer, 'dict_vectorizer.joblib', compress=9)

all_vectors = sps.hstack([name_vectors, description_vectors, dict_vectors]).todense()
print(type(all_vectors))
joblib.dump(all_vectors, 'vectors_np.joblib', compress=9)
