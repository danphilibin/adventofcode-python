import helper
import re


def main():
    # note: readlines results in every line ending in \n
    input = open("./input/day7.txt", "r").read()
    lines = input.split("\n")

    # some rules:
    # - if line starts with $, is a command
    # - if line starts with a number, is the size of a file
    # - ls prints everything in the current directory, until the next $

    # asking for how many directories with a total size <= 100000

    folders = {}
    paths = []

    all_files_total = 0

    for line in lines:
        if line.startswith("$ cd"):

            name = line.replace("$ cd ", "")

            # maintain an array of the current path, to be used as keys in `folders`
            if name == "..":
                paths.pop()
            elif not name == "/":
                paths.append(name)

        else:
            path = "/".join(paths)

            if path not in folders:
                folders[path] = 0

            if re.match("^\d", line):
                folders[path] += int(line.split(" ")[0])

                all_files_total += int(line.split(" ")[0])

    folder_totals = [
        [folders[k] for k in folders.keys() if k.startswith(f)] for f in folders
    ]

    total = sum([sum(t) for t in folder_totals if sum(t) <= 100000])

    print("answer 1:", total)

    free_space = 70000000 - all_files_total
    space_needed = 30000000 - free_space

    candidates = [
        t for t in sorted([sum(t) for t in folder_totals]) if t >= space_needed
    ]

    print("answer 2:", candidates[0])


main()
