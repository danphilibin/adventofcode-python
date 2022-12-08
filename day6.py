import helper

def main():
  input = helper.get_input(6)[0]

  # for x in range(0, len(input)):
  #   if len(set(input[x-4:x])) == 4:
  #     print('answer 1:', x)
  #     break

  # for x in range(0, len(input)):
  #   if len(set(input[x-14:x])) == 14:
  #     print('answer 2:', x)
  #     break

  for idx, n in enumerate([4, 14]):
    for x in range(0, len(input)):
      if len(set(input[x-n:x])) == n:
        print('answer', str(idx + 1) + ':', x)
        break

main()