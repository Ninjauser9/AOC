#Day 2 Red-Nose Reports
#check the puzzles safety by determining if a report's levels increment or reduce by a "safe" amount
'''
must only increase level or decrease level per report but not both
must only change by at least 1 and at most 3 

example:
7 6 4 2 1 - safe
1 2 7 8 9 - unsafe 
9 7 6 2 1 - unsafe 
1 3 2 4 5 - unsafe
8 6 4 4 1 - unsafe 
1 3 6 7 9 - safe

safe reports = 2
'''
#variables
pReports = []
report = []
aReports = [] 
dReports = []
discard = []
levelnext = 0


#take input
with open("test1.txt") as file:
    #print(file.readlines())
    #check for ascending or descending order
    for pReports in file.readlines():
        #preport is str
        #print(type(pReports))
        report = pReports.split()
        #report is a list

        for levelnext in report:
            for level in report:
            

                levelnext = int(report[])
                difference = levelnext - level
                if difference > 3 or difference < -3:
                    discard.append
                else:
                    

#check for safe level changes

#increment safe report counter

#output safe reports



'''
for safe
if increment == <=3 and >=1


if asc:
    add to safepile
if desc:
    add to safepile
else:
    add to unsafepile



'''










