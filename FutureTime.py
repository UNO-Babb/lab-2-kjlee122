#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour + 7
  currentMinute = now.minute

  

  #TODO:
  #Ask user for hours
  wantHour = input("What hour would you like to count down until? ")
  wantHour = int(wantHour)
  

  #Ask user for minutes
  wantMinute = input("What minute would you like to count down until? ")
  wantMinute = int(wantMinute)

  #Calculate the time after the user-supplied time has passed.
  moreMins = wantMinute
  moreHours = wantHour
  futureMins = (currentMinute + moreMins) % 60
  extraHour = (currentMinute + moreMins) // 60
  futureHour = (currentHour + moreHours + extraHour )
  print (futureHour,":",futureMins) 

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
