import pickle
from numerize import numerize
from sklearn.metrics.pairwise import cosine_similarity

df1 = pickle.load(open('data.pkl','rb'))

tfidf_matrix = pickle.load(open('matrix.pkl','rb'))

def id(movie):
    idx = df1.index[df1['title'] == movie][0]
    return df1.loc[idx, "id"]

def overview(id):
    idx = df1.index[df1['id'] == id][0]
    s = df1.loc[idx,"overview"]
    return s

def genere(id):
    idx = df1.index[df1['id'] == id][0]
    s = df1.loc[idx,"genres"]
    return s

def box_office(id):
    idx = df1.index[df1['id'] == id][0]
    s = int(df1.loc[idx,"revenue"])
    if s==0:
        return "Not Available"
    return numerize.numerize(s)

def budget(id):
    idx = df1.index[df1['id'] == id][0]
    s = int(df1.loc[idx,"budget"])
    if s==0:
        return "Not Available"
    return numerize.numerize(s)

def vote(id):
    idx = df1.index[df1['id'] == id][0]
    s = int(df1.loc[idx,"vote_average"])
    return f"{s}/10"

def year(id):
    idx = df1.index[df1['id'] == id][0]
    s = df1.loc[idx,"release_date"].split("-")
    return s[0]

def run_time(id):
    idx = df1.index[df1['id'] == id][0]
    mins = int(df1.loc[idx,"runtime"])
    hours = mins//60
    mins = mins%60
    return f"{hours}h  {mins}m"

def img_path(id):
    idx = df1.index[df1['id'] == id][0]
    return f'https://image.tmdb.org/t/p/w500/{df1.loc[idx, "poster_path"]}'

def back_path(id):
    idx = df1.index[df1['id'] == id][0]
    return f'https://image.tmdb.org/t/p/w500/{df1.loc[idx, "backdrop_path"]}'

def recommend(title):
    idx = df1.index[df1['title'] == title][0]
    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(
        cosine_similarity(
            tfidf_matrix,
            tfidf_matrix[idx])))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 9 most similar movies
    sim_scores = sim_scores[1:10]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 9 most similar movies
    result = df1.iloc[movie_indices]
    
    # filtering the movie ids and titles
    di = {}
    
    for i in range(9):
        di[result.iloc[i].id] = result.iloc[i].title
    return di