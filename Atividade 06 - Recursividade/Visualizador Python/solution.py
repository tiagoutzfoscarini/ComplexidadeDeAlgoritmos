from visualizer import Puzzle, blue_problem, white_problem, gap

@Puzzle
def solve_puzzle(gap, blocks, used=[]):
    if gap == 0:
        return True
    if len(blocks) == 0 or gap < 0:
        return False

    throw_away = solve_puzzle(gap, blocks[1:], used)
    use = solve_puzzle(gap-blocks[0], blocks[1:], used+[blocks[0]])
    return use or throw_away


# print solve_puzzle(gap, blue_problem)
print solve_puzzle(gap, white_problem)
