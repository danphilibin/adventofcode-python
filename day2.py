import argparse

shapeToPoints = {
  'A': 1, 'B': 2, 'C': 3,
  'X': 1, 'Y': 2, 'Z': 3,
}

pointsFromPlay = {
  #     x, y, z
  'A': [3, 6, 0],
  'B': [0, 3, 6],
  'C': [6, 0, 3]
}

correctPlay = {
  #      L,   D,   W
  'A': ['Z', 'X', 'Y'],
  'B': ['X', 'Y', 'Z'],
  'C': ['Y', 'Z', 'X'],
}

letterToIndex = {
  'A': 0, 'B': 1, 'C': 2,
  'X': 0, 'Y': 1, 'Z': 2,
}

playToResult = {
  'X': 0, 'Y': 3, 'Z': 6
}

def result(them, me):
  return pointsFromPlay[them][letterToIndex[me]]

def result_2(a, b):
  play = correctPlay[a][letterToIndex[b]]
  return shapeToPoints[play] + playToResult[b]

def main():
  args = parse_args()

  guide = open(args.filename, "r").read()

  lines = guide.split('\n')

  totalPoints = 0

  shapeToPoints = {
    'A': 1, 'B': 2, 'C': 3,
    'X': 1, 'Y': 2, 'Z': 3,
  }

  for line in lines:
    plays = line.split(' ')
    totalPoints += shapeToPoints[plays[1]]
    totalPoints += result(plays[0], plays[1])

  print('answer 1:', totalPoints)

  totalPoints = 0

  for line in lines:
    plays = line.split(' ')
    totalPoints += result_2(plays[0], plays[1])
  
  print('answer 2:', totalPoints)    



def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("filename", help="the name of the file to process")
  return parser.parse_args()

main()