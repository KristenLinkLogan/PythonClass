#program to display a list of movies and their metadata in a comma-delimited list


movie_titles = ['Harold and Maude','The Princess Bride','Goonies','Run Lola Run','Mean Girls']
bechdel = [3,2,3,1,3]
imdb = [8.0,8.2,7.8,7.8,6.9]
genre = ['Comedy/Drama/Romance','Adventure/Comedy','Adventure/Comedy','Crime/Thriller','Comedy']
rating = ['GP','PG','PG','R','PG-13']

for title,rating,bech,imdb,genre in zip(movie_titles,rating,bechdel,imdb,genre):
	print "{0}, {1}, {2}, {3}, {4}".format(title,rating,bech,imdb,genre)
