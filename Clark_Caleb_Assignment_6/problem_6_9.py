#Create a main function
def main():
    print(f"{'Meters':10s}{'foot':10s}{'Meters':>13s}{'foot':>10s}")
    #Display the top divider
    print('-' * 40)
    k = 0
    #Initialize foot and meters
    foot = 1.0
    meters = 20.0
    #Create a while loop to iterate through untill 10
    while k < 10:
        print(foot, "\t", footToMeter(foot), " | ", meters, "\t", meterToFoot(meter))
#Fuction to convert foot to meter
def footToMeter(foot):
    meter = 0.305 * foot
    return meter
#Function to convert meter to foot
def meterToFoot(meter):
    foot = meter / 0.305
    return foot
#Invoke the main function
main()
