#cs1030
#Caleb
##700745292
#Asignment 1 / problem 1.11
#Description Population Prediction

'''
1 birth every 7 seconds
1 death every 13 seconds
1 new immigrant every 45 seconds

population is 312032486
1 year is 365

'''

#Name constant for given population
POPULATION = 312032486

#Name constant for how many seconds in a year
YEAR= 365 * 86400

#Display the heading
print("The US census Bureau Projected Population")

#Display year 1 population
print("YEAR 1:", POPULATION + YEAR // 7 - YEAR // 13 + YEAR // 45)
print("YEAR 2:", POPULATION + 2 * YEAR // 7 - 2 * YEAR // 13 + 2 * YEAR // 45)
print("YEAR 3:", POPULATION + 3 * YEAR // 7 - 3 * YEAR // 13 + 3 * YEAR // 45)
print("YEAR 4:", POPULATION + 4 * YEAR // 7 - 4 * YEAR // 13 + 4 * YEAR // 45)
print("YEAR 5:", POPULATION + 5 * YEAR // 7 - 5 * YEAR // 13 + 5 * YEAR // 45)  
