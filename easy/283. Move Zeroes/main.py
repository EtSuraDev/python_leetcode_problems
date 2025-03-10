def moveZeroes(nums):
    zeros = 0
    for i in nums:
        if i == 0:
            zeros += 1
    if zeros > 0 :
        for i in range(zeros):
            nums.remove(0)
        nums += [0] * zeros
    return nums
            
print(moveZeroes([0]))
print(moveZeroes([0,1,0,3,12]))