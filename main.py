from random import randint

def mandatory_correct(mandatory_rule: str, guess: str) -> bool:
    if len(mandatory_rule) != 2:
        return False
    if mandatory_rule[0] == "|":
        if len(guess) < 1:
            return False
        return guess[0] == mandatory_rule[1]
    if mandatory_rule[1] == "|":
        if len(guess) < 1:
            return False
        return guess[-1] == mandatory_rule[0]
    return mandatory_rule in guess

def forbidden_correct(forbidden_rule: str, guess: str) -> bool:
    if len(forbidden_rule) != 2:
        return False
    if forbidden_rule[0] == "|":
        if len(guess) < 1:
            return False
        return guess[0] != forbidden_rule[1]
    if forbidden_rule[1] == "|":
        if len(guess) < 1:
            return False
        return guess[-1] != forbidden_rule[0]
    return forbidden_rule not in guess

def create_puzzle(length: int) -> tuple[str, list[str], list[str]]:
    if not 2 <= length <= 9:
        raise Exception("Puzzles must have a length of 2 to 9")
    numbers = [str(n) for n in range(length)]
    solution = ""
    while len(numbers) > 0:
        solution += numbers.pop(randint(0, len(numbers) - 1))
    mandatory = []
    forbidden = []
    for i in range(length):
        begin_rule = "|" + str(i)
        if str(i) == solution[0]:
            mandatory.append(begin_rule)
        else:
            forbidden.append(begin_rule)

        end_rule = str(i) + "|"
        if str(i) == solution[-1]:
            mandatory.append(end_rule)
        else:
            forbidden.append(end_rule)

        for j in range(length):
            if i == j:
                continue
            rule = str(i) + str(j)
            if rule in solution:
                mandatory.append(rule)
            else:
                forbidden.append(rule)
    return solution, mandatory, forbidden

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
    LENGTH: int = 3
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
