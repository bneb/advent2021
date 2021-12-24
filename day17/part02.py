from common.input import get_input_path_str
from common.output import print_output
from day17.part01 import check_all_trajectories, read_input


def main():
    minx, maxx, miny, maxy = read_input()
    trajectories = check_all_trajectories(minx, maxx, miny, maxy)
    result = len(trajectories)
    print_output(__file__, result)


if __name__ == '__main__':
    main()
