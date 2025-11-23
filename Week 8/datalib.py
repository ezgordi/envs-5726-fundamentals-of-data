from typing import List, Any

def convert_yesno_to_binary (table : List[tuple]) -> List[tuple]:
    the_class = type(table[0]) #get namedtuple class (washsurvey)

    binary_table = [] 

    for row in table: #convert to a list to modify
        binary_list = list(row) #can modify the values
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


#  calculate the variance btwn column. give me all the unique values per column
def convert_string_to_numeric(table: List[tuple]) -> List[tuple]:
    named_tuple_class = type(table[0])
    column_name_list = named_tuple_class._fields

    numeric_column_list = []
    for column_name in column_name_list:
        column_values = [getattr(row, column_name) #get data in rows of every column
                         for row in table]
        unique_non_numeric_column_values = set([column_value #find all non-numeric unique answers
                                                for column_value in column_values
                                                if not isinstance(column_value, (int, float, complex))])

        map_dict = {unique_value: index             #dict to hold the string value pair
                    for (index, unique_value) in enumerate(unique_non_numeric_column_values)}
        numeric_column_values = [map_dict[column_value] if column_value in map_dict else column_value #replace string w/ #'s
                                 for column_value in column_values]
        numeric_column_list.append(numeric_column_values)

    numeric_row_table = [list(column) for column in zip(*numeric_column_list)] #columns --> rows
    numeric_tuple_table = [named_tuple_class(*row) for row in numeric_row_table] #each row back to tuple washsurvey(G_1,...)
    return numeric_tuple_table



