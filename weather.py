# Nathan Page
# 14 March 2018
# Simple program to get high temperature, low temperature, and percent chance of rain from NWS

# Version 1.0


# import useful modules 
import sys
import string
import datetime
import calendar
import time

# get Python version to determine if we can import requests module
version=sys.version[0]

if(version<'3'):
	print("Please use Python 3...I'm too lazy to figure out how to import requests with Python 2 \_(-_-)_/")
	quit()
else:
	import requests



# Weather assistant
# Gives weather report for the day

#  Weill have high, low, and chance_rain variables
print('How can I help you? ')

# check Python version to determine with input method to use
if(version<'3'):
	str1=raw.input('')
else:
	str1 = input('')

print('\n')

#prnt = "You entered: "+str1
#print(prnt)
#print('\n')

weather = str1.find('weather')  # could be find.string(str, beginning, end)

# find if a day was specified by the user (will implement this later)
day = str1.find('today'or'tomorrow'or'sunday'or'monday'or'tuesday'or'wednesday'or'thursday'or'friday'or'saturda')


current_day=time.strftime("%A")
current_time=time.strftime("%I:%M %P")

today = str1.find('today')
tomorrow = str1.find('tomorrow')

print("Today is "+current_day)


if weather != -1:
	url = 'https://forecast.weather.gov/MapClick.php?lat=35.532890000000066&lon=-82.83835999999997#.WqmxXScpDE8'		
	webpage=requests.get(url)
	
	#clean = BeautifulSoup(webpage.txt,'html.parser')
	if today !=-1:
		# Find high temperature for today
		today_temp = webpage.text.find('Today')
		if today_temp != -1:
			high = webpage.text.find('High:')	
			if high != -1:
				high_temp = webpage.text[high+6]+webpage.text[high+7]+webpage.text[high+8]
				print("Today is"+current_day)
				print("High temperature for today is ",high_temp," Degrees F for"+current_time)
				print('\n')		
			else:
				print("The high temperature for today is already passed")
				print('\n')
			# Find low temperature for today
			low = webpage.text.find('Low: ')
			if low != -1:
				low_temp = webpage.text[high+5]+webpage.text[high+6]+webpage.text[high+7]
				print("Today is"+current_day)				
				print("Low temperature for today is ",low_temp," Degrees F")
				print('\n')		
			else:
				print("The low temperature for today is already passed")
				print('\n')
		elif today_temp ==-1:
			tonight = webpage.text.find('Tonight')
			if tonight != -1:
				low = webpage.text.find('Low: ')
				if low != -1:
					low_temp = webpage.text[low+5]+webpage.text[low+6]+webpage.text[low+7]
					print("Low temperature for tonight is ",low_temp," Degrees F for Canton, NC")
					print('\n')		
				else:
					print("The low temperature for today is already passed")
					print('\n')
		elif tomorrow != -1:
			print("Who knows what tomorrow will bring...")
		else:
			print("You must specify a day")		
else: 
	print('You did not ask about the weather...')

