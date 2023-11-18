import numpy as np


def main():
    input = open("./input/day8.txt", "r").read()
    lines = input.split("\n")

    total_lines = len(lines)
    line_len = len(lines[0])

    chars = [int(n) for n in input if n != "\n"]
    arr = np.array(chars).reshape(line_len, total_lines)

    visible = 0
    high_score = 0

    for row_idx, line in enumerate(lines):
        for col_idx, h in enumerate([int(n) for n in line]):
            local_score = 0

            prev_nums_in_column = arr[:row_idx, col_idx]
            next_nums_in_column = arr[row_idx + 1 :, col_idx]
            prev_nums_in_row = arr[row_idx, :col_idx]
            next_nums_in_row = arr[row_idx, col_idx + 1 :]

            scores = [0, 0, 0, 0]

            for dir_idx, l in enumerate(
                [
                    np.flip(prev_nums_in_column),
                    next_nums_in_column,
                    np.flip(prev_nums_in_row),
                    next_nums_in_row,
                ]
            ):
                for n in l:
                    scores[dir_idx] += 1

                    if n >= h:
                        break

            local_score = np.prod(scores)

            if local_score > high_score:
                high_score = local_score

            # count first and last row and column
            if (
                row_idx == 0
                or row_idx == total_lines - 1
                or col_idx == 0
                or col_idx == line_len - 1
            ):
                visible += 1
                continue

            if (
                (h > prev_nums_in_column).all()
                or (h > next_nums_in_column).all()
                or (h > prev_nums_in_row).all()
                or (h > next_nums_in_row).all()
            ):
                visible += 1

    print("answer 1:", visible)
    print("answer 2:", high_score)


main()
