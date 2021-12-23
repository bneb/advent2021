from collections import defaultdict
from common.input import get_input_path_str
from common.output import print_output


def main():
    grid, end = read_input()
    risks = defaultdict(lambda: None)
    risks[(0, 0)] = 0
    traverse(grid, (0, 0), set(), risks, end)
    result = risks[end]
    print_output(__file__, result)


def traverse(grid, curr, visited, risks, end):
    next_nodes = sorted(list(set(risks) - visited), key=lambda c: risks.get(c))
    while next_nodes:
        curr = next_nodes.pop(0)
        if curr in visited:
            continue

        visited.add(curr)
        neighbors = adjacent(curr) & set(grid)
        for node in neighbors:
            old_risk = risks[node]
            new_risk = risks[curr] + grid[node]
            if old_risk is None or new_risk < old_risk:
                risks[node] = new_risk

        next_nodes += sorted(neighbors, key=lambda n: risks[n])


def adjacent(curr):
    r, c = curr
    return {(r-1, c), (r+1, c), (r, c-1), (r, c+1)}


def print_grid(grid):
    miny = min([y for y, _ in grid])
    maxy = max([y for y, _ in grid])
    minx = min([x for _, x in grid])
    maxx = max([x for _, x in grid])
    maxl = max([len(str(v)) for v in grid.values()])

    for r in range(miny, maxy+1):
        row = ''
        for c in range(minx, maxx+1):
            v = grid.get((r, c))
            if v:
                row += format(v, ' ' + str(maxl+1) + 'd')
            else:
                row += ' '*(maxl+1)
        print(row)


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        grid = defaultdict(lambda: None)
        for ri, row in enumerate(f):
            for ci, risk in enumerate(row.strip()):
                end = (ri, ci)
                grid[(ri, ci)] = int(risk)

        return grid, end


if __name__ == '__main__':
    main()
