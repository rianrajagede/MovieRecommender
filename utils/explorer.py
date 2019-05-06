"""

"""

import csv
import numpy as np

def load_csv(file_name):
    result = []
    with open(file_name,"r") as csvfile:
        reader = csv.reader(csvfile)

        for r in reader:
            result.append(r)
    return np.array(result)

# Load csv files
ratings = load_csv("movie_lens_data/ratings.csv")[1:]
movies1718 = load_csv("formatted_data/movies1718_all.csv")
idmovies1718 = movies1718[:,0]

# Find the best user to be picked for this case
totrat = [0]*611 # number of rating for each user for movies before 2017
m17rat = [0]*611 # number of rating for each user for movies between 2017-2018
updateduser = [] # list of user ids who rate movies between 2017-2018
for user in ratings:
    totrat[int(user[0])] += 1
    if user[1] in idmovies1718:
        updateduser.append(user[0])
        m17rat[int(user[0])] += 1
updateduser = set(updateduser)

print("Total user who rate 2017-2018 movies :", len(updateduser))
print()
print("The most of the given rating (2017-2018):", sorted(m17rat)[-1], "by", m17rat.index(sorted(m17rat)[-1]))
print("rating ratio movies (2017-2018) compared to all movies rated", m17rat.index(sorted(m17rat)[-1]), ":", totrat[m17rat.index(sorted(m17rat)[-1])])

