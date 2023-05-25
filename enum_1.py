num_list = [num for num in range(1, 11)]

def ind_func(num_list):
    for i, num in enumerate(num_list):
        print(f"{i}:{num}")

print(ind_func(num_list))