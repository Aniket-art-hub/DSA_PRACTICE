def equalStacks(h1, h2, h3):
    # Write your code here
    h1_sum=sum(h1)
    h2_sum=sum(h2)
    h3_sum=sum(h3)
    while (h1_sum != h2_sum) or (h2_sum != h3_sum):
        get_max_sum = max(h1_sum,h2_sum,h3_sum)
        print(get_max_sum)
        if h1_sum == get_max_sum:
            h1_sum = h1_sum-h1.pop(0)
        elif h2_sum == get_max_sum:
            h2_sum = h2_sum-h2.pop(0)
        else:
            h3_sum = h3_sum-h3.pop(0)
    return h1_sum