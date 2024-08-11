def show_sum():
    num=list(map(int,input().split(" ")))
    sum_=sum(num)
    return sum_
print(show_sum())
def calculate_average(numbers):
  
    total_sum = sum_(numbers)
    num_elements = get_list_length(numbers)
    if num_elements == 0:
        return 0.0  
    return total_sum / num_elements
