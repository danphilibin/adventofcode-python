import helper

def main():
  lines = helper.get_input(4)
  lines = lines.splitlines()

  containedCount = 0
  overlapCount = 0

  for line in lines:
    [g1, g2] = line.split(',')

    # how could i cast these to ints here?
    # a = g1.split('-')
    # b = g2.split('-')

    # if int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1]):
    #   count += 1
    # elif int(b[0]) >= int(a[0]) and int(b[1]) <= int(a[1]):
    #   count += 1

    [a1, a2] = list(map(int, g1.split('-')))
    [b1, b2] = list(map(int, g2.split('-')))

    # if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
      # containedCount += 1


    # correct, but let's play with ranges again
    
    # incorrect - this does not include same-number pairs
    # r1 = range(a1, a2)
    # r2 = range(b1, b2)

    r1 = range(a1, a2 + 1)
    r2 = range(b1, b2 + 1)

    if ((a1 in r2) and (a2 in r2)) or ((b1 in r1) and (b2 in r1)):
      containedCount += 1

    if (b1 in r1) or (b2 in r1) or (a1 in r2) or (a2 in r2):
      overlapCount += 1

    
  print('answer 1:', containedCount)
  print('answer 2:', overlapCount)

  # ChatGPT told me I could do this, but I don't think this works lol
  # r1 = range(10, 18)
  # r2 = range(12, 14)
  # print(r2 in r1) -> True

main()