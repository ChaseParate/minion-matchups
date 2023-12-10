from dataclasses import dataclass
from typing import Generator


@dataclass(frozen=True)
class Weapon:
    name: str


@dataclass(frozen=True)
class Minion:
    name: str
    weaknesses: set[Weapon]


Solution = list[Weapon]


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
        for weapon, minion in zip(solution, minions):
            print(f"{minion.name} is defeated by {weapon.name}.")
        print()


def solve(weapons: dict[str, Weapon], minions: list[Minion]) -> list[Solution]:
    available_weapons = set(weapons.values())
    return list(solve_recursive(minions, 0, available_weapons, []))


def solve_recursive(
    minions: list[Minion],
    minion_index: int,
    available_weapons: set[Weapon],
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
            new_prefix.append(weapon)

            yield from solve_recursive(
                minions, minion_index + 1, new_available_weapons, new_prefix
            )


if __name__ == "__main__":
    main()
