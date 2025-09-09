#TempConvert.py
#Name: Blake Green
#Date: 9/8/25
#Assignment: Converting temperatures


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = int(input("Enter a number of degrees Fahrenheit to be converted to Celsius: "))

  tempC = (tempF - 32) / 1.8
  tempC = round(tempC, 1)
  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
