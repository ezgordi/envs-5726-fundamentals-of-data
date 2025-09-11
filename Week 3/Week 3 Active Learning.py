


def is_population_disabled ( disabled: float, total_population : float) -> bool:
    if disabled / total_population < 0.1:
        return False
    else:
        return True

#print(is_population_disabled (disabled=0, total_population=32))
#print(is_population_disabled (disabled=52, total_population=392))


def is_gp_religious_or_academic (gp):
    if 'Mosque' or 'Church' in gp:
        return True
    elif 'School' or 'Institute' or 'Education' or 'Faculty' in gp:
        return True
    else:
        return False

#print(is_gp_religious_or_academic('Faculty Of Earth Sciences and Mining'))
#print(is_gp_religious_or_academic('Almorada Church'))
print(is_gp_religious_or_academic('Health Insulation Building'))
