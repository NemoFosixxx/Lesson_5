def odd_nums(max_num):
    n = 1
    while n <= max_num:
        yield n
        n += 2
        
odd_to_15 = odd_nums(15)
for i in odd_to_15:
     print(i)