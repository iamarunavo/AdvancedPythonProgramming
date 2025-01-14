for row in range(1,10):
    print(" " * row,end = "")
    for increasing in range(row,10):
        print(increasing,end = "")
    for decreasing in range(8, row-1, -1):
        print(decreasing,end = "")
        
    print("\n")
