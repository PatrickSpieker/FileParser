#Importing os for file parsing and deletion.
import os

#Importing datetime to determine the files age
#and whether they should be deleted.
from datetime import datetime


#Defining functions for the rest of the program

#Given a filepath, this will check to creaton date of the file
#and delete it if it wasn't created after a certain date
def datecheck(filepath, month, day, year):
     secs = os.path.getmtime(filepath)
     filedatetime = datetime.fromtimestamp(secs)
     if filedatetime < datetime(year,month,day):
          print(filedatetime)
          os.remove(filepath)
          print("The file,", file, " has been deleted")

#Setting up the main program loop
def main():
     #This is the start of the path.
     #Everything in this directory will be parsed
     toplevel = input("Please enter the path of the folder where the parsing will begin."
                 "Remember that everything in that folder which has not been modified before the date specified will be deleted."
     print("Next, you will need to set a date so that the program can delete all files in the folder before it.")
     year = input("Please enter a year: ")
     month = input("Please enter a month (1-12): ")
     day = input("Please enter a day: ")            
     for root, dirs, files in os.walk(toplevel):
          for file in files:
               path = os.path.join(root, file)
               datecheck(path, month, day, year)

#Calling main() to begin the program
main()


