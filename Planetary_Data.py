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
         '2024YR4'
         ]

colours = ['orange',
           '#88a0a8',
           '#c79540',
           '#0b3f9e',
           '#b18842',
           '#dbd2ab',
           "#d5c166",
           '#7bdbd3',
           '#6560e0',
           'gray',
           'red']

linewidths = [0.8,
              0.8,
              0.8,
              0.8,
              0.8,
              1,
              1,
              1,
              1,
              1,
              1]

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
          1
          ]


object_data = {}
fol = '/Users/finleyhill/Documents/University/Level 3/CP/Planetary Data/dt=1day/'

def load_body(name): #dt=1day
    return datex.out(fol+name+'.txt')

for name in names:
    object_data[name] = load_body(name)

######


