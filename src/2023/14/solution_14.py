from functools import reduce
from utils import measure_t, open_local

Mat = list[list[str]]

def read_mat(data: str) -> Mat:
    return [[c for c in row] for row in data.splitlines()]

def dump_mat(mat: Mat) -> str:
    return "\n".join(["".join(row) for row in mat])

def tilt(mat: Mat, direction: str) -> None:
    h = len(mat)
    w = len(mat[0])

    if direction == "N" or direction == "S":
        if direction == "N":
            i_range = lambda: range(0, h-1, 1)
            k_range = lambda _i: range(_i+1, h, 1)
        else:
            i_range = lambda: range(h-1, -1, -1)
            k_range = lambda _i: range(_i-1, -1, -1)

        for i in i_range():
            for j in range(0, w):
                if mat[i][j] != ".": continue
                for k in k_range(i):
                    if mat[k][j] == ".": continue
                    if mat[k][j] == "O": mat[i][j], mat[k][j] = mat[k][j], mat[i][j]
                    break
    elif direction == "W" or direction == "E":
        if direction == "W":
            i_range = lambda: range(0, w-1, 1)
            k_range = lambda _i: range(_i+1, w, 1)
        else:
            i_range = lambda: range(w-1, -1, -1)
            k_range = lambda _i: range(_i-1, -1, -1)

        for i in i_range():
            for j in range(0, h):
                if mat[j][i] != ".": continue
                for k in k_range(i):
                    if mat[j][k] == ".": continue
                    if mat[j][k] == "O": mat[j][i], mat[j][k] = mat[j][k], mat[j][i]
                    break

def cycle(mat: Mat) -> None:
    tilt(mat, "N")
    tilt(mat, "W")
    tilt(mat, "S")
    tilt(mat, "E")

def load_cycles(mat: Mat, rounds: int) -> int:
    hashmap = {}
    loads = []
    seq_start_idx, seq_len = -1, 0

    for i in range(rounds):
        hsh = hash(dump_mat(mat))

        if hsh in hashmap.keys():
            seq_start_idx = hashmap[hsh]
            seq_len = i - seq_start_idx
            break

        hashmap[hsh] = i
        loads.append(calc_load(mat))

        cycle(mat)

    if seq_start_idx == -1:
        return loads[len(loads)-1]

    return loads[seq_start_idx:][(rounds-seq_start_idx) % seq_len]

def calc_load(mat: Mat) -> int:
    return sum([
        reduce(lambda acc, c: acc+len(mat)-i if c == "O" else acc, row, 0)
        for i, row in enumerate(mat)
    ])


if __name__ == "__main__":
    m: Mat

    with open_local(__file__, "input.txt") as f:
        m = read_mat(f.read())

    @measure_t
    def part1() -> int:
        tilt(m, "N")
        return calc_load(m)

    @measure_t
    def part2() -> int:
        return load_cycles(m, 1000000000)

    print("Answer 1: {}, time = {:.3f}s".format(*part1()))
    print("Answer 2: {}, time = {:.3f}s".format(*part2()))