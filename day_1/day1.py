

# Base_directory:
base_path = 'aoc2024/day_1/'

# Load input data.
def load_data():
    with open(base_path+'input.txt', 'r+') as inp:
        l_input = inp.read()
    return l_input

# Generate left and right lists. 
def get_list(input_data: str) -> tuple[list, list]:
    left, right = [], []
    temp_list = input_data.split('\n')
    for i in temp_list:
        a, b = i.split()
        left.append(a)
        right.append(b)
    return left, right

def day1_sol1(left:list, right: list) -> int:
    left.sort()
    right.sort()
    res = 0
    for a,b in zip(left, right):
        res += abs(int(a)-int(b))
    return res

def day1_sol2(left:list, right: list) -> int:
    dict_r = {}
    for r in right:
        dict_r[r] = dict_r.get(r, 0) + 1
    res = 0
    for l in left: 
        res += int(l)*dict_r.get(l, 0)
    return res


if __name__ == "__main__":
    inp = load_data()
    l, r = get_list(inp)
    print("Day1: part1", day1_sol1(l,r))
    print("Day1: part2", day1_sol2(l,r))