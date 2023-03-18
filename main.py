import queen


def main():
    size = int(input('Enter the number of queens for the problem: '))
    q = queen.queens(size)
    q.start_solve(size)


if __name__ == "__main__":
    main()
