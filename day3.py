import helper

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def main():
  # using a helper this time
  lines = helper.get_input(3)
  lines = lines.splitlines()

  total = 0

  for line in lines:
    l = len(line)

    # split the string in half (strings will always be even)
    p1 = line[0:l//2]
    p2 = line[l//2:l]

    item = ''

    # find characters that appear in both strings
    for c in p1:
      if c in p2:
        item = c

    total += alphabet.index(item.lower()) + 1

    if item.capitalize() == item:
      total += 26
  
  print('answer 1:', total)

  total = 0

  # group lines into groups of 3
  for i in range(0, len(lines), 3):
    group = lines[i:i+3]

    item = ''

    for c in group[0]:
      if c in group[1] and c in group[2]:
        item = c

    total += alphabet.index(item.lower()) + 1

    if item.capitalize() == item:
      total += 26
  
  print('answer 2:', total)
    

# note: double slash is integer division
# print(10/3) # 3.3333333333333335
# print(10//3) # 3

main()
