from calc import attack_table, armour_reduction, avg_damage

def ask(question, default):
    answer = input(f"{question} {default:.1f}: ")
    if answer == "":
        return default
    try:
        return float(answer)
    except (ValueError, KeyboardInterrupt):
        print(f"Using default value {default:.1f}")
        return default

your_level = ask("Your level", 25)
defence = ask("Defence", 5)
dodge = ask("Dodge", 5)
parry = ask("Parry", 5)
block = ask("Block", 6)
mob_level = ask("Mob level", 30)

results = attack_table(your_level=your_level, your_defense=defence, your_dodge=dodge, your_parry=parry, 
                       your_block=block, mob_level=mob_level)

for outcome in results:
    print(f"#" * round(results[outcome] / 2))
    print(f"{outcome}: {results[outcome]:.1f}")