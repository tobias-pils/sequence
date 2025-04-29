def create_puzzle(length: int) -> tuple[str, list[str], list[str]]:
    # ...
    return "123", ["|1", "12", "23", "3|"], ["|2", "|3", "13", "21", "31", "32", "1|", "2|"]

def print_puzzle(mandatory: list[str], forbidden: list[str]) -> None:
    print("MANDATORY")
    print(" ".join(mandatory))
    print("FORBIDDEN")
    print(" ".join(forbidden))

def main() -> None:
    solution, mandatory, forbidden = create_puzzle(3)
    print_puzzle(mandatory, forbidden)
    guess = input("> ")
    while guess != "":
        if guess == solution:
            print("CORRECT :)")
            print()
            solution, mandatory, forbidden = create_puzzle(3)
            print_puzzle(mandatory, forbidden)
        else:
            print("nope :(")
        guess = input("> ")

if __name__ == "__main__":
    main()
