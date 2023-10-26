def product_except_self(nums):
    left = 0
    nums_len = len(nums)
    right = nums_len - 1
    left_product, right_product = 1, 1
    result = [1] * nums_len
    while left < nums_len and right > -1:
        result[left] *= left_product
        result[right] *= right_product

        left_product *= nums[left]
        right_product *= nums[right]

        left += 1
        right -= 1
    
    return result

def main():
    
    inputList = [[1, 5, 10], [3, 5, 0, -3, 1], [7, 8, 9, 10, 11], [2, -4, -8, -11, 11], [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5]]
    
    # For each input, print the input and its maximum depth
    for i in range(len(inputList)):
        print (str(i + 1) + '.\tnums:', inputList[i])
        print ('\tres:', product_except_self(inputList[i]))
        print ('-' * 100)

if __name__ == '__main__':
    main()