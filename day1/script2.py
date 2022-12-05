import os

# rewrote after day 5 when I understand lists a bit better

def main():
  input_file = os.path.join(os.path.dirname(__file__), '..', 'input/day1.txt')
  lines = open(input_file, "r").read()
  
  totals = list(
    map(lambda elf: sum(map(int, elf.split('\n'))),
    lines.split('\n\n'))
  )

  totals.sort()

  print('answer 1:', totals[-1:][0])
  print('answer 2:', sum(totals[-3:]))

main()