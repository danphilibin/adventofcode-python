import numpy as np

# unfinished


def main():
    input = open("./input/day8.txt", "r").read()
    lines = input.split("\n")

    total_lines = len(lines)
    line_len = len(lines[0])

    # include the edges; subtract 4 for the corners
    visible = (line_len * 2) + (total_lines * 2) - 4

    chars = [int(n) for n in input if n != "\n"]
    arr = np.array(chars)

    print(arr.size)

    # print("ndim", arr.ndim)
    # print("shape", arr.shape)

    arr2 = arr.reshape(line_len, total_lines)

    for row_idx, line in enumerate(lines):
        if row_idx == 0 or row_idx == len(lines) - 1:
            continue

        prev_line = lines[row_idx - 1]
        next_line = lines[row_idx + 1]

        for col_idx, h in enumerate(map(int, line)):
            if col_idx == 0 or col_idx == len(line) - 1:
                continue

            # row = arr2[]

            if row_idx == 1:
                print(arr2[row_idx:, col_idx])

            # get the item in the matrix
            # print(">", arr2[row_idx, col_idx])

            if (
                int(line[col_idx - 1]) < h
                or int(line[col_idx + 1]) < h
                or int(prev_line[col_idx]) < h
                or int(next_line[col_idx]) < h
            ):
                visible += 1

    print("answer 1:", visible)

    # 7172 is too high
    # 6880 is too high


main()
