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

your_level = ask(f"Your level{"":<5}", 27)
defence = ask(f"Defence{"":<8}", 130)
dodge = ask(f"Dodge{"":<10}", 5)
parry = ask(f"Parry{"":<10}", 5)
block = ask(f"Block{"":<10}", 6)
mob_level = ask(f"Mob level{"":<6}", 30)
your_armour = ask(f"Your Armour{"":<6}", 1800)

results = attack_table(your_level=your_level, your_defense=defence, your_dodge=dodge, your_parry=parry, 
                       your_block=block, mob_level=mob_level)

for outcome in results:
    if outcome == "miss":
        print("-" * 30)
        print("Stats for you character")
        print("-" * 30)
    print(f"{outcome}: {"":<10}{results[outcome]:.1f}")    
    print(f"#" * round(results[outcome] / 2))

print(f"-" * 30)
armour_reduction = armour_reduction(mob_level=mob_level, your_armour=your_armour)
print(f"Your armour reduction against a level {mob_level} is {armour_reduction:.1f}")
print(f"-" * 30)