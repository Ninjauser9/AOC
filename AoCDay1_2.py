#AOC Day 1 part 2- hystorian hysteria
#BCL
#compare paired lists and determine the similarity score by adding up the left lists numbers similarty score
#similarity score(how many times a number in list 1 appears in list 2 and mulitplying number in list1 by occurences in list 2)
#then adding the total similarty scores of the lists

#variables
#need to convert the string? 
listOne = []
listTwo = []
distance = []
dTotal = 0
Tsimscore = 0


#open the file to use
with open("input.txt") as my_file:
    #print(my_file.readlines())

    for item in my_file.readlines():
        splitItems = item.split()
        #print(f"Sitems{splitItems}")
        listOne.append(int(splitItems[0]))
        listTwo.append(int(splitItems[1]))

#print(listOne)
#print(listTwo)

orderOne = sorted(listOne)
orderTwo = sorted(listTwo)
#print(f"order one:{orderOne}")
#print(f"order two:{orderTwo}")

for oitem1 in orderOne:
    count = 0
    for oitem2 in orderTwo:
        if oitem1 == oitem2:
            count += 1        
    Tsimscore = Tsimscore + (oitem1 * count)

print(Tsimscore)
'''
split and order the lists -> 
multiply item in order1 by the amount of times it appears in order 2

tested with 
3   4
4   3
2   5
1   3
3   9
3   3

simscore = 31
'''

