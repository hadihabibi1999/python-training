#removin duplicate number in an array
list = [1, 4, 6, 8, 8, 5, 1, 8]
for num in list :
  counter = list.count(num)
  if counter > 1:
        place = list.index(num)
        del list[place]
print(list)
