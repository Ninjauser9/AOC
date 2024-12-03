#variables
pReports = []
report = []
aReports = [] 
dReports = []
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
        print(f"report{report}")
        #each level in Report to be compared to each other as int
        count = 1
        for level in report:
            if count < 4:
                levelnext = int(report[count])
            #level is a string
            print(f"level {level}")
            print(f"levelnext {levelnext}")
            count += 1
        if int(level) > levelnext:
            print(f"ascending {level},{levelnext}")
            aReports.append(report)
        else:
            print(f"descending {level},{levelnext}")
            dReports.append(report)
#check if every item in the list is 
print(f"Desc{dReports}")
print(f"Asce{aReports}")

#check for safe level changes

#increment safe report counter

#output safe reports