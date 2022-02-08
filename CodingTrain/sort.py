######################################################
def list_sort(input):
    n = len(input)
    i = 0
    origin = input[0]
    res = []
    if n <1:
        return res
    for i in range(n):
        is_made_swap = False 
        for j in range(n - i - 1):
            if input[j] < input[j + 1]:
                input[j], input[j + 1] = input[j + 1], input[j]
                is_made_swap = True
            if input[j] == input[j+1]:
                input.pop(j)
        if not is_made_swap:
            break
    return input

    

res = list_sort([1,3,4,5,2,3,3])
print(res)
            
            