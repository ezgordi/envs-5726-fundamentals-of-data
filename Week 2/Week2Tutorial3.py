tree1 = 'acer rubrum'
tree2 = 'acer griseum'
tree3 = 'quercus suber'

city1 = 'philly pa'
city2 = 'pittsburgh pa'
city3 = 'new york new york'

#print(tree1.startswith('acer'))
#print(tree2.startswith('acer'))
#print(tree3.startswith('acer'))
#print(city1.endswith('pa'))
#print(city2.endswith('pa'))
#print(city3.endswith('pa'))

dna = 'ATTGTTAACCGCG'
t_count = dna.count('T')
#print(t_count)

sequence_length = len(dna)
#print(sequence_length)

my_school = 'upenn'
#print(my_school[0])
#print(my_school[1])
#print(my_school[2])

phrase1= 'There are '
stat1 = ('2.9')
phrase2= " million trees in Philly"
sentence = phrase1 + str(stat1) + phrase2
#print(sentence)


stat2 = 2.9
multiplier = 100
sentence = f'There are {str(int(stat2*multiplier))} trees in Philly'
print(sentence)