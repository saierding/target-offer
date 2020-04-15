
#  fixed window size

nums = [1, 3, 42, -2, 88]
max_sum = 0

for arr_len in range(1, len(nums) + 1):
    for i in range(0, len(nums) - arr_len + 1):
        cur_sum = sum(nums[i:i + arr_len])
        max_sum = max(cur_sum, max_sum)

print(max_sum)


# fixed start index
nums = [1, 3, 42, -2, 88]
max_sum = 0

for i in range(len(nums)):
    for j in range(i, len(nums)):
        cur_sum = sum(nums[i:j+1])
        max_sum = max(cur_sum, max_sum)

print(max_sum)


# fixed start index,  O(N^2)

nums = [1]
max_sum = nums[0]
tmp_sum = 0
for i in range(len(nums)):
    tmp_sum = 0
    # cur_sum = 0
    for j in range(i, len(nums)):
        cur_sum = tmp_sum + nums[j]
        tmp_sum = cur_sum
        max_sum = max(tmp_sum, max_sum)
print(max_sum)


# dp algorithm, O(N)
import time


def maxsubarray(nums):
    max_sofar = 0
    max_sum = float('-inf')
    for num in nums:
        max_sofar = max(max_sofar + num, num)
        max_sum = max(max_sum, max_sofar)
    return max_sum


start = time.time()
nums = [1, 3, 42, -2, 88]
results = maxsubarray(nums)
end = time.time()
wa_time = end - start
print(results)
print(wa_time)