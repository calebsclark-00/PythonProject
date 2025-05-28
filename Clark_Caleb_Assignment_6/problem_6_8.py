#Create a main function
def main():
    print(f"{'Celcius':10s}{'Fahrenheit':10s}{'Fahrenheit':>13s}{'Celcius':>10s}")
    #Display the top divider
    print('-' * 40)
    k = 0
    #Initialize Celcius and Fahrenheit
    Celcius = 1.0
    Fahrenheit = 20.0
    #Create a while loop to iterate through untill 10
    while k < 10:
        print(Celcius, "\t", fahrenheitToCelcius(Fahrenheit), " | ", Fahrenheit, "\t", celciusToFahrenheit(Celcius))
#Function to convert celcius To Fahrenheit
def celciusToFahrenheit(Celcius):
    Celcius = (5 / 9) * (Fahrenheit - 32)
    return Celcius
#Function to convert fahrenheit To Celcius
def fahrenheitToCelcius(Fahrenheit):
    Fahrenheit = (9 / 5) * (Celcius + 32)
    return Fahrenheit
#Invoke the main function
main()
