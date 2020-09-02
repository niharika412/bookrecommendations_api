from flask import Flask
from flask_restful import Resource, Api, reqparse
import numpy
import pandas as pd

app = Flask(__name__)
api = Api(app)

recommendations={}

#loading saved cosine similarities
cosine_sim=numpy.load("cosine_sim.dat",allow_pickle=True)
indices=pd.read_pickle('indices')
books=pd.read_csv(r'books.csv',error_bad_lines = False)
books=books.dropna()


parser = reqparse.RequestParser()
parser.add_argument('query')

class get_recommendations(Resource):
	def get(self):
		args = parser.parse_args()
		user_query = args['query']
		title=user_query
		title=title.replace(' ','').lower()
		idx = indices[title]

	    # Get the pairwsie similarity scores of all movies with that movie
		sim_scores = list(enumerate(cosine_sim[idx]))

	    # Sort the movies based on the similarity scores
		sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

	    # Get the scores of the 10 most similar movies
		sim_scores = sim_scores[1:15]

	    # Get the movie indices
		movie_indices = [i[0] for i in sim_scores]

	    # Return the top 10 most similar movies
		list_books= list(books['original_title'].iloc[movie_indices])
		recommendations[title] = list_books

		return {title: recommendations[title]}

api.add_resource(get_recommendations, '/')

if __name__ == '__main__':
    app.run(debug=True)