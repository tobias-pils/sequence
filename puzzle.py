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

def create_all_rules (solution: str) -> tuple[list[str], list[str]]:
    length = len(solution)
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
    return mandatory, forbidden

def create_puzzle(length: int) -> tuple[str, list[str], list[str]]:
    if not 2 <= length <= 9:
        raise Exception("Puzzles must have a length of 2 to 9")
    numbers = [str(n) for n in range(length)]
    solution = ""
    while len(numbers) > 0:
        solution += numbers.pop(randint(0, len(numbers) - 1))
    mandatory, forbidden = create_all_rules(solution)
    return solution, mandatory, forbidden
