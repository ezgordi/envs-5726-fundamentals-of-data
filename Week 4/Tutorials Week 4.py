


dna_list = ['CATGCG', 'TAG', 'TGGTCAAT', 'GGTTA']
dna_length_list = []

for dna_sequence in dna_list:
   dna_length_list.append(len(dna_sequence))

print(dna_length_list)

import math
number_list = [2,4,5,10]
sqaured_number_list = []

for number in number_list:
    squared_number = int(math.pow(number,2))
    sqaured_number_list.append(squared_number)

print(sqaured_number_list)

pipe_lead_percentage_list = [0.11, 0.35, 0.13, 0.43, 0.87]
pipe_lead_table = []

for pipe_lead_percentage in pipe_lead_percentage_list:
    if pipe_lead_percentage < 0.25:
        lead_free_bool = True
    else:
        lead_free_bool = False


    headers = [['Pipe Lead Percentage', 'Is Pipe Lead Free?']]
    pipe_lead_table= headers + pipe_lead_table
    row = [pipe_lead_percentage, lead_free_bool]

for row in pipe_lead_table:
    print(row)