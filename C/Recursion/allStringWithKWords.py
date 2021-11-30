def generate_helper(l, n, k, cur_loc):
    if(cur_loc == n):
        print(l)
        return
    for i in range(1, k+1):
        l[cur_loc] = i
        generate_helper(l, n, k, cur_loc + 1)

    

def generate(n, k):
    l = [0] * n
    generate_helper(l, n, k, 0)

generate(4, 3)