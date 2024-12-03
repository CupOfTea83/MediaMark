import pandas
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
import scipy.sparse as sps
import joblib
import itertools

dataset = pandas.read_csv('./anime.csv')[["MAL_ID", "Name", "Score", "Genres", "Type", "Episodes", "Aired", "Studios", "Rating"]]
dataset_synopsis = pandas.read_csv('./anime_with_synopsis.csv')[["MAL_ID", "sypnopsis"]]
dataset_merged = dataset.merge(dataset_synopsis, how='inner', on="MAL_ID")
dataset_no_text_dicts = dataset_merged[["Score", "Genres", "Type", "Episodes", "Aired", "Studios", "Rating"]].to_dict('records')

name_vectorizer = CountVectorizer()
name_vectors = name_vectorizer.fit_transform(dataset_merged["Name"].values.astype('U'))
print(name_vectors.shape)
joblib.dump(name_vectorizer, 'name_vectorizer.joblib', compress=9)

description_vectorizer = CountVectorizer()
description_vectors = description_vectorizer.fit_transform(dataset_merged["sypnopsis"].values.astype('U'))
print(description_vectors.shape)
joblib.dump(description_vectorizer, 'description_vectorizer.joblib', compress=9)

dict_vectorizer = DictVectorizer()
dict_vectors = dict_vectorizer.fit_transform(dataset_no_text_dicts)
print(dict_vectors.shape)
joblib.dump(dict_vectorizer, 'dict_vectorizer.joblib', compress=9)

all_vectors = sps.hstack([name_vectors, description_vectors, dict_vectors]) 

output_df = pandas.DataFrame(data=sps.csr_matrix.todense(all_vectors))
output_df.to_csv('prepared_data.csv', index=False)
#for (name, description, other) in zip(name_vectors, 
#                                      description_vectors, 
#                                      dict_vectors):
    #print(type(name))
    #print(name.shape[0])
    #print(name.shape[1])
    #print(type(description))
    #print(description.shape[0])
    #print(description.shape[1])
    #print(type(other))
    #print(other.shape[0])
    #print(other.shape[1])
    #all_vectors.append(sps.vstack([name[0], description[0], other[0]]))  

#with open('prepared_data.csv', mode='w') as csv_file:
#    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', 
#                            quoting=csv.QUOTE_MINIMAL)
#    csv_writer.writerows(all_vectors)
