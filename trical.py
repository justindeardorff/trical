"""
A simple program to write an iCal file to create a calendar for the Low Volume Base
Training Plan for trainerroad.com

-Justin Deardorff 2015
"""

import re
import datetime
from datetime import timedelta

#open output file
outfile = open("trcal.ics", "w+")

#defining iCal pieces for header, footer, and events
header = ["BEGIN:VCALENDAR\n",
		  "VERSION:2.0\n",
		  "X-WR-CALNAME: TrainerRoad.com LVBase\n",
		  "CALSCALE:GREGORIAN\n"]

footer = ["END:VCALENDAR"]		  

n1 = ["BEGIN:VEVENT\n",
	  "DTSTAMP:20141229T154143Z\n",
      "DTSTART;VALUE=DATE:"]
      #after inserting this, add date and line terminator

n2 = ["DTEND;VALUE=DATE:"]
     #after inserting this, add date and line terminator

n3 = ["SUMMARY:"]
      #after inserting this, add workout name and line terminator
       
n4 = ["END:VEVENT\n"]
	
	
			  
#generate ical header info and write to output file
outfile.writelines(header)	


#prompt user for plan start date
print "Please enter plan desired start date."
print "Tuesday start date recommended"
print "Enter date in the following format"
print "YYYYMMDD"
startdate = raw_input('>')


#validate input meets requirements
while len(startdate) != 8:
	print "Incorrect date format!"
	print "Enter date in the following format"
	print "YYYYMMDD"
	startdate = raw_input('>')

print "Enter input file name, include filename extension"
print "example.txt"
wrkfile = raw_input('>')
    
#open input file
infile = open(wrkfile, "r")

#declare counter variable for workout
workoutnum = 0

for line in infile:
	name, days = line.split(",",1) #splits infile into two variables called name and days
	name = str(name)
	days = int(days)+1
	outfile.writelines(n1)
	outfile.write(startdate + "\n")
	outfile.writelines(n2)
	outfile.write(startdate + "\n")
	outfile.writelines(n3)
	outfile.write(name)
	outfile.write("\n")
	outfile.writelines(n4)
	workoutnum+=1
	#insert function to calcuate next workout date
	prevdate = datetime.datetime.strptime(startdate, "%Y%m%d")
	startdate = prevdate + datetime.timedelta(days=days)
	startdate = startdate.strftime("%Y%m%d")


#when loop completes, write iCal file end syntax
outfile.write("END:VCALENDAR")

#close files
outfile.close()	  
#success message
print "iCal file created. %i workouts added to calendar." %workoutnum


#exit




