import math


def main():
    num_people, num_letter = map(int, input().split())
    num_number = max(1,math.ceil(math.log10(num_people / pow(26, num_letter))))
    print(num_number)


main()