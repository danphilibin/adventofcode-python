import numpy as np

# unfinished


def main():
    input = open("./input/day8.txt", "r").read()
    lines = input.split("\n")

    total_lines = len(lines)
    line_len = len(lines[0])

    chars = [int(n) for n in input if n != "\n"]
    arr = np.array(chars).reshape(line_len, total_lines)

    visible = 0

    for row_idx, line in enumerate(lines):
        for col_idx, h in enumerate([int(n) for n in line]):
            if row_idx == 0 or row_idx == total_lines - 1:
                visible += 1
                continue

            if col_idx == 0 or col_idx == line_len - 1:
                visible += 1
                continue

            prev_nums_in_column = arr[:row_idx, col_idx]
            next_nums_in_column = arr[row_idx + 1 :, col_idx]
            prev_nums_in_row = arr[row_idx, :col_idx]
            next_nums_in_row = arr[row_idx, col_idx + 1 :]

            if (
                (h > prev_nums_in_column).all()
                or (h > next_nums_in_column).all()
                or (h > prev_nums_in_row).all()
                or (h > next_nums_in_row).all()
            ):
                visible += 1
                if row_idx == 3:
                    print("adding", h, "at", row_idx, col_idx, "to visible")
            else:
                if row_idx == 3:
                    print("not adding", h, "at", row_idx, col_idx, "to visible")

    print("answer 1:", visible)  # 1794


main()
