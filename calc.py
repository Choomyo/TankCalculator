ORDER = ["miss", "dodge", "parry", "block", "crit", "crush"]

def attack_table(your_level, your_defense, your_dodge, your_parry, your_block, mob_level):
    defense_cap = 5 * your_level          # highest Defense for your level
    mob_weapon_skill = 5 * mob_level      # the mob's weapon skill
    level_penalty = 0.2 * max(0, mob_level - your_level)   # lost per level 

    chances = {
        "miss": max(0, 5 + (your_defense - defense_cap) * 0.04 - level_penalty),
        "dodge": max(0, your_dodge - level_penalty),
        "parry": max(0, your_parry - level_penalty),
        "block": max(0, your_block - level_penalty),
        "crit": max(0, 5 + (mob_weapon_skill - your_defense) * 0.04),
        "crush": max(0, (mob_weapon_skill - min(your_defense, defense_cap)) * 2 - 15)
                 if mob_level - your_level >= 3 else 0,
    }

    chance_left = 100.0

    results = {}

    for outcome in ORDER:
        results[outcome] = min(chances[outcome], chance_left)   # can't take ore than what's left
        chance_left -= results[outcome]
    results["hit"] = max(0, chance_left)
    return results

def armour_reduction(your_armour, mob_level):
    if mob_level < 60:
        divider = your_armour + 400 + 85 * mob_level
    else:
        divider = your_armour +467.5 * mob_level - 22167.5 #this will never get used for wow forever as 60 will be perma cap
    return min(75.0, 100 * your_armour / divider)

def avg_damage(results, mob_hit, armour_pct, block_value):
    hit_after_armour = mob_hit * (1 - armour_pct / 100) #opne normal hit after armour
    return (results["hit"] * hit_after_armour + results["crit"] * 2 * hit_after_armour + results["crush"] + results["block"] * max(0, hit_after_armour - block_value)) / 100


def main():
    results = attack_table(24, 128, 5.7, 5.3, 6, 30)  # your level, your defense, your dodge, your parry, your block, mob level
    for outcome, chance in results.items():
        print(f"{outcome:<6} {chance:5.1f}%")

    armour_pct = armour_reduction(1800, 30)
    print(f"Armour reduction: {armour_pct:.1f}")
    print(f"Average Damage: {avg_damage(results, 100, armour_pct, 0):.1f}")


if __name__ == "__main__":
    main()

