ORDER = ["miss", "dodge", "parry", "block", "crit", "crush"]

def attack_table(level, defence, dodge, parry, block, mob_level):
    cap = 5 * level
    skill = 5 * mob_level
    red = 0.2 * max(0, mob_level - level)

    raw = {"miss": max(0, 5 + (defence - cap) * 0.04 - red),
           "dodge": max(0, dodge - red),
           "parry": max(0, parry - red),
           "block": max(0, block - red),
           "crit": max(0, (skill - min(defence, cap)) * 0.04),
           "crush": max(0, (skill - min(defence, cap)) * 2 - 15)
                if mob_level - level >= 3 else 0,
    }

    print(raw)

    left = 100

    t = {}

    for k in ORDER:
        t[k] = min(raw[k], left)
        left -= t[k]
    t["hit"] = max(0, left)
    return t

if __name__ == "__main__":
    t = attack_table(22, 120, 5.8, 5.4, 5.0, 25)
    for k, v in t.items():
          print(f"{k:<6} {v:5.1f}%")
    



    

