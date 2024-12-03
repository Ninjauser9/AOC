#AOC Day 1 part 2- hystorian hysteria
#BCL
#compare lists and pair numbers from each list with their relatively closest match from the other list. 
#find the distance between the values and produce a total distance between the lists
'''
For example:
origin:    ->      reorder:   ->   distance:   ->  total:
3   4              1  3            2               11
4   3              2  3            1
2   5              3  3            0
1   3              3  4            1
3   9              3  5            2
3   3              4  9            5
'''




#variables
#need to convert the string? 
listOne = []
listTwo = []
distance = []
dTotal = 0

#open the file to use
with open("input.txt") as my_file:
    #print(my_file.readlines())

    for item in my_file.readlines():
        splitItems = item.split()
        listOne.append(int(splitItems[0]))
        listTwo.append(int(splitItems[1]))

print(listOne)
print(listTwo)

orderOne = sorted(listOne)
orderTwo = sorted(listTwo)
print(f"order one:{orderOne}")
print(f"order two:{orderTwo}")

#encompassed by a loop to go through the list
#iterate through the list of ordered to calculate the distance between the numbers
for count, oitem1 in enumerate(orderOne):
        oitem2 = orderTwo[count]
        distance = oitem1 - oitem2
        dTotal = dTotal + abs(distance)

print(dTotal)



#for len(distance):
#totD = distance
#dtotal = dtotal + totD
#print(dtotal)

'''
-DECOMPOSITION-
take string from file -> split into array ->
reorder strings -> enumerate for clarity ->
compare index distance -> running total ->
output total  distance
'''