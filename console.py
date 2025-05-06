from puzzle import (
    mandatory_correct,
    forbidden_correct,
    create_puzzle
)

def red_str(s: str) -> str:
    return f"\033[31m{s}\033[00m"

def green_str(s: str) -> str:
    return f"\033[32m{s}\033[00m"

def print_puzzle(mandatory: list[str], forbidden: list[str], length: int, guess: str = "") -> None:
    print("MANDATORY")
    if guess == "":
        print(" ".join(mandatory))
    else:
        print(f"{" ".join([green_str(m) if mandatory_correct(m, guess) else red_str(m) for m in mandatory])}")
    print("FORBIDDEN")
    if guess == "":
        print(" ".join(forbidden))
    else:
        print(f"{" ".join([green_str(f) if forbidden_correct(f, guess) else red_str(f) for f in forbidden])}")
    print("LENGTH")
    if guess == "":
        print(length)
    else:
        print(green_str(str(length)) if len(guess) == length else red_str(str(length)))

def main() -> None:
    LENGTH: int = 4
    solution, mandatory, forbidden = create_puzzle(LENGTH)
    print_puzzle(mandatory, forbidden, LENGTH)
    guess = input("> ")
    while guess != "":
        if guess == solution:
            print("CORRECT :)")
            print()
            solution, mandatory, forbidden = create_puzzle(LENGTH)
            print_puzzle(mandatory, forbidden, LENGTH)
        else:
            print_puzzle(mandatory, forbidden, LENGTH, guess)
        guess = input("> ")

if __name__ == "__main__":
    main()
