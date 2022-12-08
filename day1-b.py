import helper

# rewrote after day 5 when I understand lists a bit better


def main():
    input = helper.get_input(1)

    totals = list(map(lambda elf: sum(map(int, elf.split("\n"))), input.split("\n\n")))

    totals.sort()

    print("answer 1:", totals[-1:][0])
    print("answer 2:", sum(totals[-3:]))


main()
