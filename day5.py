import helper
import re
import copy

def main():
  input = helper.get_input(5)

  # get all the lines starting with [
  lines = []

  instructions_start = 0
    
  for idx, line in enumerate(input):
    if line[0] != '[':
      # there's an empty line between the stacks and instructions
      instructions_start = idx + 2
      break

    lines.append(line)

  # reverse them (bottom to top)
  lines.reverse()

  # sort into buckets
  stacks1 = {}

  for n in range(1, instructions_start + 1):
    stacks1[n] = list()

  # doesn't work because it doesn't account for spaces
  # for l in lines:
  #   chars = re.sub(r'\[|\]| ', '', str(l))
  #   for idx, c in enumerate(chars):
  #     stacks[str(idx)].append(c)

  for l in lines:
    charsWithValue = range(1, 9 * 4, 4)
    for idx, n in enumerate(charsWithValue):
      v = str(l)[n]
      if v and v != ' ':
        stacks1[idx + 1].append(v)

  instructions = input[instructions_start:]

  # note: these do not work, the lists are not copied:
  # stacks2 = stacks.copy()
  # stacks2 = dict(stacks)
  
  stacks2 = copy.deepcopy(stacks1)

  # 1. move one item at a time
  # for move in instructions:
    # parts = re.match(r'move (\d+) from (\d+) to (\d+)', move)
    # [_move, _from, _to] = list(map(lambda x: int(x), parts.groups()))

    # print(stacks[_from])

    # for i in range(0, _move):
      # l = stacks[_from].pop()
      # stacks[_to].append(l)

    # l = reversed(stacks[_from][_move*-1:])
  
    # stacks[_to].extend(list(l))
    # stacks[_from] = stacks[_from][:_move*-1]


  # res = []

  # for i in stacks:
    # if(len(stacks[i]) > 0):
      # res.append(stacks[i][-1])

  # print('answer 1:', ''.join(res))

  # 2. move all items at once and keep the order
  # for idx, move in enumerate(instructions):
    # parts = re.match(r'move (\d+) from (\d+) to (\d+)', move)
    # [_move, _from, _to] = list(map(lambda x: int(x), parts.groups()))

    # l = stacks9001[_from][_move*-1:]
  
    # stacks9001[_to].extend(list(l))
    # stacks9001[_from] = stacks9001[_from][:_move*-1]

    # got stuck in some nasty loops here as I learned how references in python work
    # if idx > 1:
      # break

  # res2 = []

  # for i in stacks9001:
    # if(len(stacks9001[i]) > 0):
      # res2.append(stacks9001[i][-1])

  # print('answer 2:', ''.join(res2))


  for move in instructions:
    parts = re.match(r'move (\d+) from (\d+) to (\d+)', move)
    [_move, _from, _to] = list(map(lambda x: int(x), parts.groups()))

    _taken = reversed(stacks1[_from][_move*-1:])
    stacks1[_to].extend(list(_taken))
    stacks1[_from] = stacks1[_from][:_move*-1]

    _taken = stacks2[_from][_move*-1:]
    stacks2[_to].extend(list(_taken))
    stacks2[_from] = stacks2[_from][:_move*-1]


  # getting a lil more familiar with lists
  # res1 = []
  # for stack in filter(lambda l: len(l), stacks1.values()):
    # res1.append(stack[-1])
  #
  # res2 = []
  # for stack in filter(lambda l: len(l), stacks2.values()):
  #   res2.append(stack[-1])

  # nice
  res1 = map(lambda f: f[-1], filter(lambda l: len(l), stacks1.values()))
  res2 = map(lambda f: f[-1], filter(lambda l: len(l), stacks2.values()))

  print('answer 1:', ''.join(res1))
  print('answer 2:', ''.join(res2))

main()