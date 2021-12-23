from collections import defaultdict
from common.input import get_input_path_str
from common.output import print_output
from heapq import heapify, heappush, heappop

def main():
    grid, end = read_input()
    risks = defaultdict(lambda: None, {(0, 0): 0})
    traverse(grid, (0, 0), set(), risks, end)
    result = risks[end]
    print_output(__file__, result)


def traverse(grid, curr, visited, risks, end):
    next_nodes = [(risk, coords) for coords, risk in risks.items()]
    heapify(next_nodes)

    while next_nodes:
        _, curr = heappop(next_nodes)
        if curr == end:
            return
        if curr in visited:
            continue

        visited.add(curr)

        neighbors = adjacent(curr, end)
        for node in neighbors:
            old_risk = risks[node]
            new_risk = risks[curr] + grid[node]
            if old_risk is None or new_risk < old_risk:
                risks[node] = new_risk

        for node in neighbors - visited:
            heappush(next_nodes, (risks[node], node))


def adjacent(curr, end):
    r, c = curr
    neighbors = set()
    if 0 < r:
        neighbors.add((r-1, c))
    if r < end[0]:
        neighbors.add((r+1, c))
    if 0 < c:
        neighbors.add((r, c-1))
    if c < end[0]:
        neighbors.add((r, c+1))
    return neighbors


def read_input():
    with open(get_input_path_str(__file__), 'r') as f:
        grid = defaultdict(lambda: 0)
        lines = f.read().strip().split('\n')

        rows = len(lines)
        cols = len(lines[0])
        end = (rows*5-1, cols*5-1)

        for ri, row in enumerate(lines*5):
            for ci, risk in enumerate(row.strip()*5):
                adj_risk = int(risk) + ri//rows + ci//cols
                if adj_risk > 9:
                    adj_risk %= 9

                grid[(ri, ci)] = adj_risk

        return grid, end


if __name__ == '__main__':
    main()
