def get_starting_and_ending_position(nums: list,target:int) -> list:
    result = []
    start_position=-1
    end_position= -1
    for i in range(len(nums)):
        if nums[i] == target:
            result.append(i)
    if len(result) == 0:
        result = [start_position,end_position]
    elif len(result) == 1:
        result.append(result[0])
    return result


def get_starting_and_ending_position(nums: list,target:int) -> list:
    start_position = -1
    end_position = -1
    left_end, right_end = 0, len(nums) - 1
    while (left_end <= right_end):                              #For getting right part of target
        middle_position = left_end + (right_end - left_end) // 2
        if (nums[middle_position] < target):
            left_end = middle_position + 1
        elif (nums[middle_position] > target):
            right_end = middle_position - 1
        else:                                                   #In case target element is found at the middle index
            new_right_end = middle_position + 1
            new_left_end = middle_position - 1
            if (new_left_end >= left_end and new_right_end <= right_end and 
                nums[new_right_end] == target and nums[new_left_end] != target):
                start_position = left_end
                left_end = middle_position
            elif (new_left_end >= left_end and new_right_end <= right_end and  
                  nums[new_left_end] == target and nums[new_right_end] != target):
                end_position = right_end
                right_end = middle_position
            else:
                if (nums[left_end] == nums[right_end] == target):
                    return [left_end, right_end]
                elif (nums[left_end] != target):
                    left_end += 1
                elif (nums[right_end] != target):
                    right_end -= 1
    return [start_position, end_position]


