from utils import open_local, measure_t


def sum_real_digits(text: str) -> int:
    return sum(int("".join(tuple(c for c in line if c.isdigit())[i] for i in (0, -1))) for line in text.splitlines())

def sum_any_digits(text: str) -> int:
    repl = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    keys = sorted(repl.keys(), key=len)
    min_len = len(keys[0])
    max_len = len(keys[-1])
    nsum = 0

    for line in text.splitlines():
        llen = len(line)
        number = 0

        # forward:
        for pos in range(0, llen):
            if line[pos].isdigit():
                number = 10 * int(line[pos])
                break

            for off in range(min_len, max_len+1):
                if pos+off > llen:
                    break

                if line[pos:pos+off] in keys:
                    number = 10 * repl[line[pos:pos+off]]
                    break

            if number != 0:
                break

        # backward:
        for pos in range(llen-1, -1, -1):
            if line[pos].isdigit():
                number += int(line[pos])
                break

            for off in range(min_len, max_len+1):
                if pos-off < 0:
                    break

                if line[pos-off+1:pos+1] in keys:
                    number += repl[line[pos-off+1:pos+1]]
                    break

            if number % 10 != 0:
                break

        nsum += number

    return nsum


if __name__ == "__main__":
    txt: str

    with open_local(__file__, "input.txt") as f:
        txt = f.read()

    @measure_t
    def part1() -> int:
        return sum_real_digits(txt)

    @measure_t
    def part2() -> int:
        return sum_any_digits(txt)

    print("Answer 1: {}, time = {:.3f}s".format(*part1()))
    print("Answer 2: {}, time = {:.3f}s".format(*part2()))
