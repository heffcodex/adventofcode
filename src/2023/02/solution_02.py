from utils import open_local, measure_t


Results = list[tuple[int, int, int]] # [(R, G, B), ...]
Games = dict[int, Results]           # {game_id: Results}

def parse_games(text: str) -> Games:
    games = {}

    for line in text.splitlines():
        ident, results = line.removeprefix("Game ").split(":", 1)

        game_id = int(ident)
        game_results = []

        for _set in results.strip().split(";"):
            r = g = b = 0

            for color in _set.strip().split(","):
                color_count, color_name = color.strip().split(" ", 1)

                if color_name == "red": r = int(color_count)
                elif color_name == "green": g = int(color_count)
                elif color_name == "blue": b = int(color_count)

            game_results.append((r, g, b))

        games.update({game_id: game_results})

    return games

def possible_game_ids(games: Games, red: int, green: int, blue: int) -> list[int]:
    ids = []

    for game_id, results in games.items():
        ok = True

        for result in results:
            if result[0] > red or result[1] > green or result[2] > blue:
                ok = False
                break

        if ok:
            ids.append(game_id)

    return ids

def possible_12r_13g_14b_idsum(games: Games) -> int:
    return sum(possible_game_ids(games, 12, 13,14))

def calc_power(game_results: Results) -> int:
    max_r, max_g, max_b = game_results[0]

    for i in range(1, len(game_results)):
        max_r = max(max_r, game_results[i][0])
        max_g = max(max_g, game_results[i][1])
        max_b = max(max_b, game_results[i][2])

    return max_r * max_g * max_b

def calc_power_sum(games: Games) -> int:
    return sum(calc_power(results) for results in games.values())


if __name__ == "__main__":
    games_: Games
    parse_t: float

    with open_local(__file__, "input.txt") as f:
        games_, parse_t = measure_t(parse_games)(f.read())

    @measure_t
    def part1() -> int:
        return possible_12r_13g_14b_idsum(games_)

    @measure_t
    def part2() -> int:
        return calc_power_sum(games_)

    print("Parse time = {:.3f}s".format(parse_t))
    print("Answer 1: {}, time = {:.3f}s".format(*part1()))
    print("Answer 2: {}, time = {:.3f}s".format(*part2()))