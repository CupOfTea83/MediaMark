import pandas
import json

dataset = pandas.read_csv('./anime.csv')[["MAL_ID", "Name", "Score", "Genres", "Type", "Episodes", "Aired", "Studios", "Rating"]]
dataset_synopsis = pandas.read_csv('./anime_with_synopsis.csv')[["MAL_ID", "sypnopsis"]]
dataset_merged = dataset.merge(dataset_synopsis, how='inner', on="MAL_ID")
dataset_merged["Studios"] = dataset_merged["Studios"].apply(lambda x: x.split(', '))
dataset_merged["Genres"] = dataset_merged["Genres"].apply(lambda x: x.split(', '))
dataset_no_text_dicts = dataset_merged[["Genres", "Type", "Episodes", "Aired", "Studios", "Rating"]].to_dict('records')

studios = []
genres = []
media_types = dataset_merged["Type"].unique().tolist()
ratings = dataset_merged["Rating"].unique().tolist()

for row in dataset_no_text_dicts:
    studios += row['Studios']
    genres += row['Genres']


with open('studios.json', 'w') as studios_file:
    json.dump(list(set(studios)), studios_file)

with open('media_types.json', 'w') as media_types_file:
    json.dump(media_types, media_types_file)

with open('ratings.json', 'w') as ratings_file:
    json.dump(ratings, ratings_file)

with open('genres.json', 'w') as genres_file:
    json.dump(list(set(genres)), genres_file)
