
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

    key_words = { 'Mosque, School', 'Institute', 'Education', 'Faculty', 'Church'} #key words set

    gp_list = set(gp.split( ))

    intersection_key_words_gp = gp_list.intersection(key_words)

    if intersection_key_words_gp:
        return True
    else:
        return False

print(is_gp_religious_or_academic('Faculty Of Earth Sciences and Mining'))
print(is_gp_religious_or_academic('Almorada Church'))
print(is_gp_religious_or_academic('Health Insulation Building'))



def get_sanitation_priority (ratio,disabled,total_population,gp):
    is_ratio_met = is_min_ratio_toilets_to_people_met(ratio)
    is_disabled = is_population_disabled (disabled, total_population)
    is_gp = is_gp_religious_or_academic (gp)

    #print(is_ratio_met)
    #print(is_disabled)
    #print(is_gp)

    if not is_ratio_met and is_disabled and is_gp:
        return 'High Priority'

    elif is_ratio_met and not is_disabled and not is_gp:
        return 'Low Priority'

    else:
        return 'Medium Priority'




#print(get_sanitation_priority(ratio= '1t/49p',disabled = 52, total_population = 392, gp = 'Faculty-Students Dwelling'))
#print(get_sanitation_priority(ratio='1t/29p', disabled = 0, total_population = 178, gp = 'Mohamad Ali Abbas Secondary School For Girls'))
#print(get_sanitation_priority(ratio = '1t/17p', disabled = 0, total_population= 52, gp = 'Alsalam Old Mosque'))
#print(get_sanitation_priority(ratio= '1t/16p', disabled = 0, total_population= 12, gp = 'Nile Club'))
#print(get_sanitation_priority(ratio= '1t/395p', disabled = 0, total_population= 1580, gp = 'Town Park (Almuntazah)'))
