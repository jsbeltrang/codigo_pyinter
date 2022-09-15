def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    # print(squares)

    multiples = [x for x in range(1, 1000000) if x % 4 == 0 and x % 6 == 0 and x % 9 == 0]

    print(multiples)


if __name__ == "__main__":
    run()