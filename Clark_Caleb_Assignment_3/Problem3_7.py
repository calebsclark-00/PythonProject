#cs1030
#Caleb
##700745292
#Asignment 3 3_7
'''
(random character)

use the time module to find an uppercase letter

'''
#import the time module
import time

#Converting the time into a character
#code = chr(int(time.time()) % 26 + 65)

#Display the results
print(f"ramdom uppercase letter is {chr(int(time.time()) % 26 + 65)}")
