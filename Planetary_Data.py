import Data_Extraction as datex


names = ['Sun',
         'Mercury',
         'Venus',
         'Earth',
         'Mars',
         'Jupiter',
         'Saturn',
         'Uranus',
         'Neptune',
         'Moon',
         #'2024YR4'
         ]

masses = [1.989e30,
          3.285e23,
          4.867e24,
          5.972e24,
          6.39e23,
          1.898e27,
          5.683e26,
          8.681e25,
          1.024e26,
          7.348e22,
          #1
          ]

col_names = ['Earth_Col',
             'Moon_Col',
             '2024YR4_Col'
             ]

object_data = {}
fol = '/Users/finleyhill/Documents/University/Level 3/CP/Planetary Data/'

def load_body(name):
    return datex.out(fol+name+'.txt')

for name in names:
    object_data[name] = load_body(name)

col_data = {}
fol2 = '/Users/finleyhill/Documents/University/Level 3/CP/Collision Data/'

def load_body_col(name):
    return datex.out(fol2+name+'.txt')

for name in col_names:
    col_data[name] = load_body_col(name)