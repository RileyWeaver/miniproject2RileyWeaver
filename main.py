## INF601 - Advance Programming in Python
## Riley Weaver
## Mini Project 02

'''
INF601 - Programming in Python
Assignment: mini project 2
I,     Riley Weaver    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty,
 including but not limited to cheating, plagiarism, or the use of unauthorized materials. I have neither provided nor received unauthorized assistance
 and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result
 in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement,
 I acknowledge my commitment to upholding the principles of academic integrity
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("charts", exist_ok=True)

games = pd.read_csv("games.csv", index_col=0)

# top 3 Teams
team_counts = games['Team'].value_counts()

top_teams = team_counts.head(3)

print("Top 3 Teams: ")
print(top_teams)



#Distribution of ratings
ratings_amount = games['Rating'].value_counts().sort_index()

bins = np.arange(0, 5.0, 0.3)

count = np.arange(0, 500, 50)


print("Rating Distribution: ")
print((ratings_amount))


# Chart 1: Top 3 Teams chart
plt.figure(figsize = (8,6))

color_list = ['red', 'green', 'blue']

top_teams.plot(kind='bar', color=color_list)
plt.title('Top 3 Teams By Amount Of Games Popular')
plt.xlabel('Teams')
plt.xticks(rotation=0)
plt.ylabel('Frequency')
plt.savefig("charts/top_3_teams.png")



# Chart 2: Distribution of ratings chart
plt.figure(figsize = (8,6))
plt.hist(games['Rating'], bins=10, color='orange', edgecolor='black')
plt.xlabel('Rating')
plt.xticks(bins)
plt.ylabel('Count')
plt.yticks(count)
plt.title('Distribution of Ratings Among Popular Games')
plt.savefig('charts/rating_distribution.png')


