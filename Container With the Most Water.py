
def container_with_most_water(height):
    max_area = 0
    start = 0
    end = len(height) - 1

    while start < end:
        width = end - start
        max_area = max(max_area, min(height[start], height[end]) * (width))
        
        # max_area = max(max_area, min(height[start], height[end]) * (width))
        if height[start] >= height[end]:
            end-=1
        else:
            start+=1

    return max_area

# Driver code
def main():
    heights = [
                [1, 8, 6, 2, 5, 4, 8, 3, 7], 
                [20, 30, 9, 69],
                [13, 18, 12, 8],
                [45, 32, 56, 99], [23, 20]
            ]
    index = 1
    for i in heights:
        print(str(index)+".\tHeights: "+str(i))
        print("\n\tMaximum Area: " + str(container_with_most_water(i)))
        index += 1
        print("-" * 100)


if __name__ == "__main__":
    main()