import helper


def main():
    input = helper.get_input(6)[0]

    for idx, n in enumerate([4, 14]):
        for x in range(0, len(input)):
            if len(set(input[x - n : x])) == n:
                print("answer", str(idx + 1) + ":", x)
                break


main()
