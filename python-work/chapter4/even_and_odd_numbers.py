# Even and Odd Numbers


# In this example, the range() function starts with the value 2 and then  adds 2 to that value. It adds 2 
# repeatedly until it reaches or passes the end value, 11, and produces this result:


even_numbers = list(range(2,11,2))
print(even_numbers)
# output: [2, 4, 6, 8, 10]

even_numbers = list(range(2,11,4))
print(even_numbers)
# output: [2, 6, 10]

odd_numbers = list(range(1,11,2))
print(odd_numbers)
# output: [1, 3, 5, 7, 9]
