#Importing os for file parsing and deletion.
import os

#Importing datetime to determine the files age
#and whether they should be deleted.
from datetime import datetime

#This is the start of the path.
#Everything in this directory will be parsed
toplevel = input("Please enter the path of the folder where the parsing will begin."
                 "Remember that everything in that folder which is older than the date specified will be deleted."

month, day ,year = input("Please enter the date which all files before "
                         "will be deleted in the format: "
                         "month, day, year. Please enter all as nunbers.").split() 
#Defining functions for the rest of the program

#Given a filepath, this will check to creaton date of the file
#and delete it if it wasn't created after a certain date
def datecheck(filepath):
     secs = os.path.getmtime(filepath)
     filedatetime = datetime.fromtimestamp(secs)
     if filedatetime < datetime(2012,1,1):
          print(filedatetime)
          os.remove(filepath)
          print("The file,", file, " has been deleted")

#Setting up the main program loop
def main():
     for root, dirs, files in os.walk(toplevel):
          for file in files:
               path = os.path.join(root, file)
               datecheck(path)

#Calling main() to begin the program
main()


