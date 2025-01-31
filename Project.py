#Weather_Data is a file that contains weather information from 1-12 in the year of 2012. However I belive that this code can work for any year if the formating of the excel file is similar
#-although keep in mind that this code does not account for leap years and also you have to have the same type of timing and dates...
infile = open('Weather_Data.csv' , 'r')

textRead = infile.read()
allRows = textRead.split("\n")
infile.close()
#initializes the lists in order for later use. The months list is the only preset one because nobody is making new months
months = ["", "January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
wDate = []
wTime = []
wAMPM = []
wTemp = []
wDewPoint = []
wHumidity = []
wWindSpeed = []
wVisibility = []
wPressure = []
wWeather = []

#asks the user to input a 1 for yes or 0 for no in order to have either fahrenheit or celsius 
units = int(input("Would you like your tempature to be in Fahrenheit (1) or Celsius (0)? : "))
#typical fahrenheit to celsius calculations, you can look it up if it doesnt really make sense but x is just a universal value added to the temperature during conversion
#fahrenheit is = 1 and x = 0 are kind of redundant but they just dont do anything if they fire
if units == 1:
    x = 32
    fahrenheit = 9/5
else:
    x = 0
    fahrenheit = 1
#What this does is essentially adds to the lists above with the correct data in the columns and rows of the csv file.
#it also checks to make sure that there are no blank spaces within the data and if there is any funny buisness involving quotations and commas within the excel spreadsheet
for i in allRows:
    weatherData = i.split(",")
    if not i.strip():
        continue
    if len(weatherData) < 10:
        weatherData.extend([''] * (10-len(weatherData)))
    elif len(weatherData) > 10:
        weatherData = weatherData[:10]
    wDate.append(weatherData[0])
    wTime.append(weatherData[1])
    wAMPM.append(weatherData[2])
    wTemp.append(weatherData[3])
    wDewPoint.append(weatherData[4])
    wHumidity.append(weatherData[5])
    wWindSpeed.append(weatherData[6])
    wVisibility.append(weatherData[7])
    wPressure.append(weatherData[8])
    wWeather.append(weatherData[9])
#This is an almost unnessecary section of the code which involves removing the 0 index of the lists that just have the titles that were on the csv file
#I assigned them to variables in order to use them later but never ended up doing that. Instead this serves as a removal of the 0 index making sure the code runs smoothly.
dateTitle = wDate.pop(0)
timeTitle = wTime.pop(0)
ampmTitle = wAMPM.pop(0)
tempTitle = wTemp.pop(0)
dewTitle = wDewPoint.pop(0)
humidityTitle = wHumidity.pop(0)
windSpeedTitle = wWindSpeed.pop(0)
visibilityTitle = wVisibility.pop(0)
pressureTitle = wPressure.pop(0)
weatherTitle = wWeather.pop(0)

#this section of code involves the code prompting the user for a response and based off of that response it checks to make sure that it has a valid
#date, time, and hour in order to find the exact piece of the csv file that needs to be examined. foundDate is innocent until guilty in this regard. 
foundDate = False
while not foundDate:
    #pitfalls that make sure the user enters an actual date
    monthFinder = int(input("Enter a month to search for (1-12): "))
    dayFinder = int(input("Enter a day to search for (1-31): "))
    hourFinder = int(input("Enter a time of day to search for (0 to 23 for 0:00 to 23:00): "))
    ampmFinder = input("AM or PM: ")
    foundDate = True
    print("\n")
    if monthFinder < 1 or dayFinder > 31 or monthFinder > 12 or dayFinder < 1 or hourFinder < 0 or hourFinder > 23:
        foundDate = False
        print("Please enter a valid month/day/hour")
    elif monthFinder in {2, 4, 6, 9, 11} and dayFinder > 30:
        foundDate = False
        print("Please enter a valid month/day/hour")
    elif monthFinder == 2 and dayFinder > 29:
        foundDate = False
        print("Please enter a valid month/day/hour")

#This is a rudementary way of finding the correct indexes based upon the strings being analysed.
#its kind of complicated but in order to describe it ill do this
#lets say that you have a date like 1/1/2012 this says that the day (1) is equal  to position 2
#but if we had a date like 12/1/2012 then the day postion has shifted over one and is now 3.
#This gets more complicated with dates such as 11/11/2012 or 2/23/2012 and so on. 
if monthFinder > 9 and dayFinder > 9:
    monthRight = 2
    monthLeft = 0
    dayRight = 5
    dayLeft = 3
elif monthFinder > 9 and dayFinder < 10:
    monthRight = 2
    monthLeft = 0
    dayRight = 4
    dayLeft = 3
elif monthFinder < 10 and dayFinder > 9:
    monthRight = 1
    monthLeft = 0
    dayRight = 4
    dayLeft = 2
elif monthFinder < 10 and dayFinder < 10:
    monthRight = 1
    monthLeft = 0
    dayRight = 3
    dayLeft = 2
if hourFinder > 9:
    timeRight = 2
    timeLeft = 0
elif hourFinder < 10:
    timeRight = 1
    timeLeft = 0
    
i = 0
total = 0
count = 0
endLoop = False
while not endLoop:
    #This all checks to make sure that the exact values are found in the csv files and are located with the use of string indexes based upon entries in the list.
    #variables like monthLeft and dayRight are defined in the code above and basically just represent the indexes of the positions of the strings.
    if wDate[i][monthLeft: monthRight] == str(monthFinder) and wDate[i][dayLeft:dayRight] == str(dayFinder) and wTime[i][timeLeft:timeRight] == str(hourFinder) and wAMPM[i] == ampmFinder:
        print(wDate[i],wTime[i], wAMPM[i])
        endLoop = True
        #Ends the loops so its not infinite
        if units == 1:
            #units == 1 means that the user has decided they want fahrenheit instead of celsius which just changes some temperature calculations
            print("The Temperature in Fahrenheit on {} was: {:.2f} Degree(s)".format(wDate[i],(float(wTemp[i]) * fahrenheit) + x))
            print("")
            #This section of code finds the average temperature of the month provided. For example if the user enters the month december (12) then it will find the average temp of that month
            for l in range(len(wTemp)):
                if wDate[l][monthLeft:monthRight] == str(monthFinder):
                    total = total + abs(float(wTemp[l]))
                    count += 1
            total = (total * fahrenheit) + x
            total = total / count
            print("The average temperature for the month of {} was {:.2f} Degrees Fahrenheit".format(months[monthFinder], total))
            moreWeatherData = input("Would you like to know more relevant weather data for {} at {} {}? ('yes' or 'no')".format(wDate[i], wTime[i], wAMPM[i]))
            moreWeatherData.lower()
            if moreWeatherData == 'yes' or moreWeatherData == 'y':
                #This just prints all of the data in the indexes if the user wishes to have more data about the day they entered 
                print("")
                print("Dew point temp in Fahrenheit: {} ".format((float(wDewPoint[i]) * fahrenheit) + x))
                print("Humidity % : {} ".format(wHumidity[i]))
                print("Wind Speed in km/h: {} ".format(wWindSpeed[i]))
                print("Visibility: {}".format(wVisibility[i]))
                print("Pressure in kPa: {}".format(wPressure[i]))
                print("Weather type: {}".format(wWeather[i]))
                
        else:
            #Exact same thing as above however it is in celsius right now
            #This may be redundant but this is just the way I figured it out and made sense in my head
            print("The Temperature in Celsius on {} was: {} Degree(s)".format(wDate[i],wTemp[i]))
            print("")
            for l in range(len(wTemp)):
                if wDate[l][monthLeft:monthRight] == str(monthFinder):
                    total = total + abs(float(wTemp[l]))
                    count += 1
            total = total / count
            print("The average temperature for the month of {} was {:.2f} Degrees Celsius".format(months[monthFinder], total))
            moreWeatherData = input("Would you like to know more relevant weather data for {} at {} {}? ('yes' or 'no')".format(wDate[i], wTime[i], wAMPM[i]))
            moreWeatherData.lower()
            if moreWeatherData == 'yes' or moreWeatherData == 'y':
                print("")
                print("Dew point temp in Celsius: {} ".format(wDewPoint[i]))
                print("Humidity % : {} ".format(wHumidity[i]))
                print("Wind Speed in km/h: {} ".format(wWindSpeed[i]))
                print("Visibility: {}".format(wVisibility[i]))
                print("Pressure in kPa: {}".format(wPressure[i]))
                print("Weather type: {}".format(wWeather[i]))
    else:
        #Indexes the i value in the while loop
        i += 1

