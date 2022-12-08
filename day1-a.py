import argparse


def main():
    args = parse_args()

    lines = open(args.filename, "r").read()

    elves = lines.split("\n\n")

    totals = []

    for elf in elves:
        total = 0

        for num in elf.split("\n"):
            total += int(num)

        totals.append(total)

    totals.sort()

    print("answer 1:", totals[-1:][0])

    topThree = totals[-3:]

    topThreeTotal = 0

    for num in topThree:
        topThreeTotal += num

    print("answer 2:", topThreeTotal)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="the name of the file to process")
    return parser.parse_args()


main()
