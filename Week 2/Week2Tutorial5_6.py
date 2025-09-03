import datetime

mybirthday = 'my birthday is month 05 day 07 and year 2001'
my_datetime = datetime.datetime.strptime(mybirthday, 'my birthday is month %m day %d and year %Y')
#print(my_datetime)


start_date = datetime.datetime(year=2001, month = 5, day = 7)
end_date = datetime.datetime(year=2001, month = 5, day = 28)
date_duration = end_date - start_date
#print(date_duration)



bird_list = ['American Crow', 'Baltimore Oriole', 'Blue Jay', 'Grasshopper Sparrow']
count_bird_list = [10, 7, 15, 41]


weather_string= 'Storms, Floods, Mass Movement, Earthquakes, Droughts'
weather_list = weather_string.split('! ')
#print(weather_list)

data_list = ['Storms', 'Floods', 'Mass Movement', 'Earthquakes', 'Droughts']
my_slice = data_list[1:3]
print(my_slice)