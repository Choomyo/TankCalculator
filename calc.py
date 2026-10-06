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

if __name__ == "__main__":
    results = attack_table(24, 128, 5.7, 5.3, 6, 24) #your level, your defense, your dodge, your parry, your block, mob level
    for outcome, chance in results.items():
        print(f"{outcome:<6} {chance:5.1f}%")

