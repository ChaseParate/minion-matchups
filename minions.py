from dataclasses import dataclass


@dataclass(frozen=True)
class Weapon:
    name: str


@dataclass(frozen=True)
class Minion:
    name: str
    weaknesses: set[Weapon]


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

    minions = {
        name: Minion(name, {weapons[name] for name in weaknesses})
        for name, weaknesses in [
            ("Paragoomba", ["Jump", "FLUDD"]),
            ("Dry Bones", ["Ice Flower", "Light Box"]),
            ("Pokey", ["Hammer", "Fire Flower", "Blue Shell"]),
            ("Piranha Plant", ["Hammer", "Fire Flower", "Ice Flower"]),
            ("Cooligan", ["Jump", "Fire Flower"]),
            ("Boo", ["Light Box", "Blue Shell"]),
            ("Lava Bubble", ["Ice Flower", "FLUDD"]),
        ]
    }

    solution = solve(weapons, minions)
    for weapon, minion in solution:
        print(f"{minion.name} is defeated by {weapon.name}.")


def solve(
    weapons: dict[str, Weapon], minions: dict[str, Minion]
) -> list[tuple[Weapon, Minion]]:
    return [(weapons["Jump"], minions["Paragoomba"])]


if __name__ == "__main__":
    main()
