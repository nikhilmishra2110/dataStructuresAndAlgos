def check_sum(num_list):
    for i in num_list:
        for j in num_list:
            if i+j ==0:
                print (i,j)
                return True
    return False

print (check_sum([10, -14, 26, 5, -3, 13, -5]))
print (check_sum([10, -3, -5]))




def check_sum2(num_list):
    for first_num in range(len(num_list)):
        for second_num in range(first_num + 1, len(num_list)):
            if num_list[first_num] + num_list[second_num] == 0:
                return True
    return False


num_list = [10, -14, 26, 5, -3, 13, -5]
print(check_sum2(num_list))
