my_list = [1,2,3,4,5,6]
new_1 = [n + 100 for n in my_list]
print(new_1)

new_2 = {k: n ** 3 for k, n in zip ("ABCDEFGHI" , range(1, 11) ) }
print(new_2)

new_3 = (n ** 5 for n in range(1, 1_000_000_000))
#print(new_3)

# for i in new_3:
#     print(i)

print(next(new_3))
print(next(new_3))
print(next(new_3))
print(next(new_3))