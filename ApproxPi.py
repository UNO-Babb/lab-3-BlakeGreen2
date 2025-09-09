#ApproxPi.py
#Name: Blake Green 
#Date: 9/8/2025
#Assignment: Approximating Pi
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  decimalAmt = int(input("Enter the number of decimal places you would like up to 10: "))
  start = time.time()
  #calculate pi using the approximation technique
  num = 3.1415926535
  multiplier = 10 ** decimalAmt
  largenum = 3.1415926535 * multiplier
  smallnum = int(largenum) / multiplier
  print(smallnum)
  #Loop until the level of percision is reached

  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
