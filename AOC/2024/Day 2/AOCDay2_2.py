#Day 2-2 Red-Nose Reports
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
isIncreasing = False
safecount = 0



#take input and determine if asc/desc
with open("test1.txt") as file:
    for reports in file.readlines():
        #reports is string
        report = list(map(int,reports.split()))
        #report is list
        print(f"report {report}")
        prev_level = report[0]
        

        
        if report[1] > prev_level:
            isIncreasing = True
        else:
            isIncreasing = False
        
        lives = 1
        for level in report[1:]:
            print(f"level: {level} prev_level: {prev_level} lives:{lives}")

            if isIncreasing == False and level > prev_level or isIncreasing == True and level < prev_level: #if the report isnt increasing or drecreasing go next
                print(f"break, lives: {lives}")
                if lives == 0:
                    break
            
            
            if abs(level - prev_level) >3 or abs(level - prev_level) == 0 : #check if increment is in parameters
                print(f"distance break, Lives: {lives}")
                if lives == 0:
                    break
                    
            lives -= 1
            prev_level = level
        else :
            safecount += 1
    

print(f"safecount: {safecount}")



#pt2
#introduce dampener(lives) if report fails more than once deem unsafe
#


#check if whole report follows ascending or descending 
#for report in isIncreasing:
    

#increment safe report counter

#output safe reports



'''
check if potentially ascending or descending
->
continue to check if asc or dsc and increment is safe
->
tally safe

'''










