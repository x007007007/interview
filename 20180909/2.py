import itertools

tranc_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkf",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


def iter_solution(input_str):
    chuck_pool = [tranc_map[char] for char in input_str]
    chuck_size_pool = [len(chuck) for chuck in chuck_pool]
    chuck_offset_pool = [0] * len(chuck_pool)
    overflow = 0
    yield "".join([chuck[0] for chuck in chuck_pool])
    while overflow != 1:
        for chuck_bit in range(len(chuck_pool)):
            chuck_size = chuck_size_pool[chuck_bit]

            if chuck_bit == 0:
                chuck_offset_pool[chuck_bit] += 1
            chuck_offset_pool[chuck_bit] += overflow
            overflow = 0
            if chuck_offset_pool[chuck_bit] >= chuck_size:
                chuck_offset_pool[chuck_bit] -= chuck_size
                overflow = 1
        yield "".join(chuck[chuck_offset_pool[bit]] for bit, chuck in enumerate(chuck_pool))


def get_list(imput_str):
    res = []
    for v in iter_solution(imput_str):
        res.append(v)
    return res


print get_list("234234297")