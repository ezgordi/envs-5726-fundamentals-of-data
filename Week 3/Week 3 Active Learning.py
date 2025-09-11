


def is_population_disabled ( disabled: float, total_population : float) -> bool:
    if disabled / total_population < 0.1:
        return False
    else:
        return True

print(is_population_disabled (disabled=0, total_population=32))
print(is_population_disabled (disabled=52, total_population=392))


def is_gp_religious_or_academic (Gathering_point : str):
    gathering_point= set(['Mosque, Church, School, Institute, Education, Faculty'])
    if 'Church' in is_gp_religious_or_academic():
        return True
    else:
        return False

print(is_gp_religious_or_academic('Almorada Church'))
