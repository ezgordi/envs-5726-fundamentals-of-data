green_bool = 'Greenfield'.startswith('Green')
#print(green_bool)

compare1 = 5 >=3
compare2 = 5!= 3
compare3 = 5 == 3

#print(compare1, compare2, compare3)

gm_risk_rating = 27.6
gm_motors_emissions_ambition = 'YES, MEETS ALL CRITERIA'

gm_sustainable = gm_risk_rating < 25 and gm_motors_emissions_ambition == 'YES, MEETS ALL CRITERIA'
#print(gm_sustainable)

Pipe_lead = 0.11
pipe_rating = 'Pipe is led free' if Pipe_lead < 0.25 else 'Pipe is NOT lead free'
#print(pipe_rating)

pfoa_ppt = 3
pfos_ppt = 11

if pfoa_ppt <4:
    print('PFOA concentration within regulatory standards')
    if pfos_ppt <10:
        print ('PFOS concentration within regulatory standards')
    else: print (' PFOS concentation NOT within regulatory standards')

else: print (' PFOA concentration NOT within regulatory standards')