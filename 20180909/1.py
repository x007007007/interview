from collections import OrderedDict

def get_sort_ele_pool_map(ele_pool):
    sorted_pool = [(str(ele), (ele, index)) for index, ele in enumerate(ele_pool)]
    sorted_pool.sort(key=lambda x: x[1][0])
    return OrderedDict(sorted_pool)

def get_indices(ele_pool, ele_sum):
    left_offset = 0
    right_offset = len(ele_pool) - 1
    left_step = 1
    while ele_sum <= ele_pool[right_offset]:
        right_offset -= 1
    if right_offset == 0:
        raise ValueError

    while True:
        just_sum = ele_pool[left_offset] + ele_pool[right_offset]
        if just_sum == ele_sum:
            return [left_offset, right_offset]
        elif just_sum > ele_sum:
            right_offset -= 1
            if left_offset > 0:
                left_step = -1
        elif just_sum < ele_sum:
            left_step = 1

        left_offset += left_step

        if left_offset >= right_offset:
            raise ValueError("connot find indices of {}")

def get_unsort_indices(ele_pool, ele_sum):
    trans_map = get_sort_ele_pool_map(ele_pool)
    sorted_pool = [v[0] for v in trans_map.values()]
    k1, k2 = get_indices(sorted_pool, ele_sum)
    return trans_map[str(sorted_pool[k1])][1], trans_map[str(sorted_pool[k2])][1]


if __name__ == "__main__":
    print get_indices([3, 9, 18, 26, 29, 53], 18)
    print get_unsort_indices([3, 9, 18, 25, 27, 28, 31, 37, 41, 43, 47 ,51, 57, 53], 71)