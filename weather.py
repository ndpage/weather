import sys
import string
import requests
import lxml


# Weather assistant
# Gives weather report for the day
high
low
chance_rain
print('How can I help you? ')
str1 = raw_input('')

prnt = "You entered: "+str1
print(prnt)
print('\n')

weather = str1.find('weather')  # could be find.string(str, begiinning, end)
today = str1.find('today')
tomorrow = str1.find('tomorrow')
if weather != -1:
	if today !=-1:
		print("The high today with be %d and a low of %d with %d percent chance of rain")
		print('\n')
	elif tomorrow != -1:
		print("The high torromow with be %d and a low of %d with %d percent chance of rain")
		print('\n')
	else:
		print("The high today with be %d and a low of %d with %d percent chance of rain")
		print('\n')
else: 
	print('You did not ask about the weather...')

