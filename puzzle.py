from random import randint
from collections.abc import Generator

def mandatory_correct(mandatory_rule: str, guess: str) -> bool:
    if len(mandatory_rule) != 2 or len(guess) < 1:
        return False
    if mandatory_rule[0] == "|":
        return guess[0] == mandatory_rule[1]
    if mandatory_rule[1] == "|":
        return guess[-1] == mandatory_rule[0]
    return mandatory_rule in guess

def forbidden_correct(forbidden_rule: str, guess: str) -> bool:
    if len(forbidden_rule) != 2 or len(guess) < 2:
        return False
    if forbidden_rule[0] == "|":
        return guess[0] != forbidden_rule[1]
    if forbidden_rule[1] == "|":
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

def all_solutions(length: int, sub_solution: str) -> Generator[str]:
    if len(sub_solution) < length:
        for i in range(length):
            if str(i) in sub_solution:
                continue
            for solution in all_solutions(length, sub_solution + str(i)):
                yield solution
    else:
        yield sub_solution

def has_exactly_one_solution(length: int, mandatory: list[str], forbidden: list[str]) -> bool:
    first_solution = None
    for solution in all_solutions(length, ""):
        is_correct = True
        for rule in mandatory:
            if not mandatory_correct(rule, solution):
                is_correct = False
                break
        if not is_correct:
            continue
        for rule in forbidden:
            if not forbidden_correct(rule, solution):
                is_correct = False
                break
        if is_correct:
            if first_solution == None:
                first_solution = solution
            else:
                return False
    return first_solution != None

def create_puzzle(length: int) -> tuple[str, list[str], list[str]]:
    if not 2 <= length <= 9:
        raise Exception("Puzzles must have a length of 2 to 9")
    numbers = [str(n) for n in range(length)]
    solution = ""
    while len(numbers) > 0:
        solution += numbers.pop(randint(0, len(numbers) - 1))
    mandatory, forbidden = create_all_rules(solution)
    failed_removals = 0
    while True:
        m_len = len(mandatory)
        f_len = len(forbidden)
        if m_len == 0 and f_len == 0:
            break
        elif f_len > 0 and (m_len == 0 or randint(0, 2) != 0):
            to_remove = 0
            if f_len > 1:
                to_remove = randint(0, f_len - 1)
            if has_exactly_one_solution(
                length, mandatory, forbidden[:to_remove] + forbidden[to_remove + 1:]
            ):
                forbidden.pop(to_remove)
                failed_removals = 0
            else:
                if failed_removals < 3:
                    failed_removals += 1
                else:
                    break
        else:
            to_remove = 0
            if m_len > 1:
                to_remove = randint(0, m_len - 1)
            if has_exactly_one_solution(
                length, mandatory[:to_remove] + mandatory[to_remove + 1:], forbidden
            ):
                mandatory.pop(to_remove)
                failed_removals = 0
            else:
                if failed_removals < 3:
                    failed_removals += 1
                else:
                    break

    if not has_exactly_one_solution(length, mandatory, forbidden):
        raise Exception("Puzzle generation failed")

    return solution, mandatory, forbidden
