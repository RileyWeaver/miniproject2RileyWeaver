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
 I acknowledge my commitment to upholding the principles of academic integrity.
'''

import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

df = pd.DataFrame(
{
        "Title": [
            "Elden Ring",
            "Hades",
            "The Legend of Zelda: Breath of the Wild",
        ],
        "Rating": [4.5, 4.3, 4.4],
        "Wishlist": ["4.8k", "3.6k", "2.6k"],
    }
)

print("Game Data:")
print(df)