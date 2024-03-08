n = int(input())
nums = list(map(int, input().split()))
nums.sort()
days = int(input())
for i in range(days):
    target = int(input())
    count = 0
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target >= nums[mid]:
            count += ((mid - left) + 1)
            left = mid + 1
        else:
            right = mid - 1

    print(count)

