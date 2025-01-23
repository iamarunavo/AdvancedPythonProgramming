def generate_divisible_by_3(lowerbound: int, upperbound: int) -> list[int]:
    mylist=[i for i in range(lowerbound, upperbound+1) if i%3==0]
    return mylist