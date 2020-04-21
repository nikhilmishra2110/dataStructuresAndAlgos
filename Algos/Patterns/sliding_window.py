import math


def sum_window_average(k, arr):
    result = []
    for i in range(len(arr) - k + 1):
        sum = 0.0
        for j in range(i, i + k):
            sum += arr[j]
        result.append(sum / k)
    return result

def maximum_sum_window(k, arr):
    maximum_so_far = 0.0
    for i in range(len(arr) - k + 1):
        running_sum = 0.0
        for j in range(i, i+k):
            running_sum += arr[j]
        maximum_so_far = max(running_sum , maximum_so_far )
    return maximum_so_far

def find_averages_of_subarrays(K, arr):
    result = []
    window_sum = 0.0
    start = 0
    for i in range(len(arr)):
        window_sum+=arr[i]
        if i >=  K -1:
            result.append(window_sum/K)
            window_sum = window_sum - arr[start]
            start+=1
    return result


def max_sub_array_of_size_k(k, arr):
    print (k, arr)
    start = 0
    maximum_sum = 0.0
    window_sum = 0.0
    for i in range(len(arr)):
        window_sum = window_sum + arr[i]
        print ("window_sum = ", window_sum)
        if i >= k -1:
            maximum_sum = max(maximum_sum, window_sum)
            print ("\tmaximum_sum = ", maximum_sum)
            window_sum-=arr[start]
            print("\t\twindow_sum for next iteration= ", window_sum)
            start+=1
    return maximum_sum



def smallest_subarray_with_given_sum(s, arr):
    '''
    # window_sum = 0
    # start = 0
    # min_length = math.inf
    # for i in range(len(arr)):
    #     window_sum = window_sum + arr[i]
    #     while window_sum >= s:
    #         min_length =  min(min_length, i-start+1)
    #         window_sum-=arr[start]
    #         start+=1
    # return min_length'''
    start = 0
    window_sum = 0
    min_len = math.inf
    for i in range(len(arr)):
        window_sum = window_sum + arr[i]
        while window_sum >= s:
            min_len = min(min_len, i - start + 1)
            window_sum -= arr[start]
            start += 1

    return min_len


def longest_substring_with_k_distinct(str, k):
    char_frequency = {}
    window_start = 0
    max_length = 0
    # expand the window
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char]+=1

    # shrink from left
        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char]==0:
                del char_frequency[left_char]
            window_start+=1
        max_length = max(max_length, window_end-window_start+1)
    return max_length






def main():
  # result1 = sum_window_average(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  # result2 = maximum_sum_window(3, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  # result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  # print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  # print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  # print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  # print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
# print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

  # print("Averages of subarrays of size K optimized: " + str(result))
  # print("Averages of subarrays of size K: " + str(result1))
  # print("Maximum  of subarrays of size K: " + str(result2))
  # longest_substring_with_k_distinct("aabcaabcd", 3)

  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))



main()
