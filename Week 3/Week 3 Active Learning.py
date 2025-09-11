
def is_min_ratio_toilets_to_people_met (ratio):
    ratio_parts = ratio.split('/')
    toilet_part = ratio_parts[0]
    people_part = ratio_parts[1]

    toilets = int(toilet_part.replace('t', ''))
    people = int(people_part.replace('p', ''))

    ratio_value = toilets / people

    if ratio_value >= 1/20:
        return True
    else:
        return False

#print(is_min_ratio_toilets_to_people_met('1t/37p'))
#print(is_min_ratio_toilets_to_people_met('1t/12p'))




def is_population_disabled ( disabled: float, total_population : float) -> bool:
    if disabled / total_population < 0.1:
        return False
    else:
        return True

#print(is_population_disabled (disabled=0, total_population=32))
#print(is_population_disabled (disabled=52, total_population=392))


def is_gp_religious_or_academic (gp):
    if 'Mosque' in gp:
        return True
    elif 'Church' in gp:
        return True
    elif 'School' in gp:
        return True
    elif 'Institute' in gp:
        return True
    elif 'Education' in gp:
        return True
    elif 'Faculty' in gp:
        return True
    else:
        return False

#print(is_gp_religious_or_academic('Faculty Of Earth Sciences and Mining'))
#print(is_gp_religious_or_academic('Almorada Church'))
#print(is_gp_religious_or_academic('Health Insulation Building'))



def get_sanitation_priority (ratio,disabled,total_population,gp):
    ratio = is_min_ratio_toilets_to_people_met(ratio)
    disabled = is_population_disabled (disabled, total_population)
    gp = is_gp_religious_or_academic (gp)



    if not ratio >= 1/20 and is_population_disabled (disabled, total_population) <= 0.1:
        return 'High Priority'

    elif ratio >=1/20 and is_population_disabled (disabled, total_population) >= 0.1:
        return 'Low Priority'
    else:
        return 'Bad'



print(get_sanitation_priority(ratio= '1t/49p',disabled = 52, total_population = 392, gp = 'Faculty-Students Dwelling'))
print(get_sanitation_priority(ratio='1t/29p', disabled = 0, total_population = 178, gp = 'Mohamad Ali Abbas Secondary School For Girls'))


