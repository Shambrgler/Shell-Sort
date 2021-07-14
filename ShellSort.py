total_count = 0

def intershellsort(nums, start, gap):
    tempcounty = 0
    for i in range(start + gap, len(nums), gap):
        j = i
        while (j - gap >= start) and (nums[j] < nums[j - gap]):
            #print("Swap " + str(nums[j]) + " with " + str(nums[j - gap]))
            temp = nums[j]
            nums[j] = nums[j - gap]
            nums[j - gap] = temp
            j = j - gap
            tempcounty += 1
            #print("Y", tempcounty)
    print(nums)
    return tempcounty
    

def shellsort(numbers, gaps, count):
    tempcountx = count
    for gap in gaps:
        for i in range(gap):
            tempcountx += intershellsort(numbers, i, gap)
            #print("X", tempcountx)
    return tempcountx

#numbers = [5,4,3,2,1]
numbers = [11,23,435,43,23,27,2435,34,456,32,54,24,976,56,94,3,7,543,8,45,463,325,954,23,75,26,85,32,9684,965,4,65,74,564,84,4,65,84,65,4,8,84,7,65,5,94,4]
gaps = [15,7,3,1]

total_count = shellsort(numbers, gaps, total_count)
print(total_count)
