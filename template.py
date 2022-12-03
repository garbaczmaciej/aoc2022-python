

def get_input() -> list:
    with open("input.txt", "r") as f:
        _in = [line for line in f.read().split("\n") if line.split()]

    return _in


def part1(_in: list) -> None:
    pass


def part2(_in: list) -> None:
    pass


def main() -> None:
    _in = get_input()
    part1(_in)
    part2(_in)


if __name__ == "__main__":
    main()
