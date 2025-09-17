# given a list of names create a new list where names longer than 5 letters are replaced with "long" and shorter ones stay the same. use conditional comprehension

names_list = ['Jessie', 'Sarah', 'Amanda', 'Christina' 'Jedediah', 'Alex' ]
names_list_length = ['Long' if len(name_length) > 5 else name_length for name_length in names_list]
print(names_list_length)

# gives a list of exam scores, crete a new list that replaces scores of 80 or higher with "pass" and all others with "retake"

exam_scores_list = [90, 100, 50, 81, 72, 69,]
exam_scores_status = ['Pass' if grade > 80 else 'Fail' for grade in exam_scores_list]
print(exam_scores_status)

# given a list of temperatures, create a new list with only temperatures above 60
temperatures_list = [100, 55, 79, 80, 48, 69]
moderate_temperature = [temperatures for temperatures in temperatures_list if temperatures > 69]
print(moderate_temperature)

# given a list of animals, create a new list that keeps the original name if it starts with 'c' or 'g' but changes it to 'other' otherwise

animal_list = ['dog', 'giraffe', 'cat', 'goldfish', 'finch']
animals_first_letter = [animal_name if animal_list[0] = 'c' or 'g' else 'Other' for animal_name in animal_list]
print(animals_first_letter)