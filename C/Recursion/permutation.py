
# Time complexity of permutation function:-  O(n!)
# Time complexity of permutation_helper function:- n (total combinations)
#                                                   C
#                                                     r


def swap(l, i, j):
    l[i], l[j] = l[j], l[i]


def permutation(l, cur, remaining_length):
    global res
    if len(l) < 2:
        print(l)
        return
    if remaining_length == 2:
        res.append(l)
        print(l)
        swap(l, -1, -2)
        print(l)
        res.append(l)
        swap(l, -1, -2)
    else:
        for i in range(cur, len(l)):
            swap(l, cur, i)
            permutation(l, cur + 1, len(l) - cur - 1)
            swap(l, cur, i)


def permutation_helper(l, count, cur, r, sublist=[]):
    if count > r:
        return
    elif count == r:
        permutation(sublist, 0, len(sublist))
        # print(sublist)
    elif cur >= len(l):
        return
    else:
        for i in range(cur, len(l)):
            sublist.append(l[i])
            count += 1
            permutation_helper(l, count, i + 1, r, sublist)
            sublist.pop()
            count -= 1


def generate_permutation_with_specific_length(l=[], r=None):
    if(r == None):
        r = len(l)
    if len(l) < r:
        return
    elif r <= 0:
        return
    elif len(l) == r:
        permutation(l, 0, len(l))
        return
    else:
        permutation_helper(l, 0, 0, r, [])


l = [1, 2, 3, 4, 5]
res = []
generate_permutation_with_specific_length(l, 3)
print(len(res))
