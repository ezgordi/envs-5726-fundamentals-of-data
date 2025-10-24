from typing import List, Any

def convert_yesno_to_binary (table : List[tuple]) -> List[tuple]:
    the_class = type(table[0]) #get namedtuple class (washsurvey)

    binary_table = [] 

    for row in table: #convert to a list to modify
        binary_list = list(row)
        binary_row_list = [] #store the values from each single row

        for value in binary_list:
            if value == 'Yes':
                binary_row_list.append(1)

            elif value in ['', 'No', 'Do not know', 'Do Not Know']:
                binary_row_list.append(0)

            else:
                binary_row_list.append(value)

        
        back_to_tuple = the_class(*binary_row_list) #go into WashSurvey, and go thhru each value in binary row list
        binary_table.append(back_to_tuple) #new table is new tuple

    return(binary_table)


def convert_string_to_number(table : List[tuple]) -> List[tuple]:
    stringclass = type(table[0])

    string_to_value_dict = {} #dict to map each string sentence to it's numberic valye
    next_num = 1
    string_to_number_table = []

    for row in table:
        values_list = list(row)

        for i, value in enumerate(values_list):
            if isinstance(value, (int, float)) or value == '':
                continue


            value = value.strip()
            if value not in string_to_value_dict:
                string_to_value_dict[value] = next_num
                next_num += 1

            values_list[i] = string_to_value_dict[value]

        string_to_number_table.append(stringclass(*values_list))

    return string_to_number_table




