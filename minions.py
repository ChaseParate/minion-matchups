from dataclasses import dataclass
from typing import Generator


@dataclass(frozen=True)
class Weapon:
    name: str


@dataclass(frozen=True)
class Minion:
    name: str
    weaknesses: set[Weapon]


Solution = list[tuple[Weapon, Minion]]


def main() -> None:
    weapons = {
        name: Weapon(name)
        for name in [
            "Jump",
            "Hammer",
            "Fire Flower",
            "Ice Flower",
            "Light Box",
            "FLUDD",
            "Blue Shell",
        ]
    }

    minions = [
        Minion(name, {weapons[name] for name in weaknesses})
        for name, weaknesses in [
            ("Paragoomba", ["Jump", "FLUDD"]),
            ("Dry Bones", ["Ice Flower", "Light Box"]),
            ("Pokey", ["Hammer", "Fire Flower", "Blue Shell"]),
            ("Piranha Plant", ["Hammer", "Fire Flower", "Ice Flower"]),
            ("Cooligan", ["Jump", "Fire Flower"]),
            ("Boo", ["Light Box", "Blue Shell"]),
            ("Lava Bubble", ["Ice Flower", "FLUDD"]),
        ]
    ]

    solutions = solve(weapons, minions)
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for weapon, minion in solution:
            print(f"{minion.name} is defeated by {weapon.name}.")
        print()


def solve(weapons: dict[str, Weapon], minions: list[Minion]) -> list[Solution]:
    available_weapons = set(weapons.values())
    return list(solve_recursive(minions, available_weapons, 0, []))


def solve_recursive(
    minions: list[Minion],
    available_weapons: set[Weapon],
    minion_index: int,
    prefix: Solution,
) -> Generator[Solution, None, None]:
    if minion_index == len(minions):
        yield prefix
        return

    minion = minions[minion_index]

    for weapon in minion.weaknesses:
        if weapon in available_weapons:
            new_available_weapons = available_weapons - {weapon}

            new_prefix = prefix.copy()
            new_prefix.append((weapon, minion))

            for solution in solve_recursive(
                minions, new_available_weapons, minion_index + 1, new_prefix
            ):
                yield solution


if __name__ == "__main__":
    main()
