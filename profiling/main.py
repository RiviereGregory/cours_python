import timeit
from array import array

nb_samples = 44100
buf = array('h', b"\x00\x00" * nb_samples)

buf1 = array('h', b"\x00\x00" * nb_samples)
buf2 = array('h', b"\x00\x00" * nb_samples)
buf3 = array('h', b"\x00\x00" * nb_samples)
buf4 = array('h', b"\x00\x00" * nb_samples)
bufs = [buf1, buf2, buf3, buf4]


# AudioTrack
def func1():
    for i in range(0, nb_samples):
        buf[i] = 0
    return buf


def func2():
    return buf[0:nb_samples]


# Mixer
def func3():
    for i in range(0, nb_samples):
        buf[i] = 0
        for j in range(0, len(bufs)):
            buf[i] += bufs[j][i]


def func4():
    s = [sum(x) for x in zip(*bufs)]
    return array('h', s)


def func5():
    s = map(sum, zip(*bufs))
    return array('h', s)


# test perf amélioration Track
print(timeit.repeat(setup="from __main__ import func1",
                    stmt="func1()",
                    repeat=3,
                    number=100))
# result [0.6234613, 0.6776263, 0.5904319]

print(timeit.repeat(setup="from __main__ import func2",
                    stmt="func2()",
                    repeat=3,
                    number=100))
# result [0.0047751999999998684, 0.004936599999999958, 0.0047599999999998754]

# test perf amélioration Mixer
print(timeit.repeat(setup="from __main__ import func3",
                    stmt="func3()",
                    repeat=3,
                    number=100))
# result [10.398723700000001, 10.249962899999998, 10.9947302]

print(timeit.repeat(setup="from __main__ import func4",
                    stmt="func4()",
                    repeat=3,
                    number=100))
# result [1.5285160999999974, 1.569165500000004, 1.5684432000000044]

print(timeit.repeat(setup="from __main__ import func5",
                    stmt="func5()",
                    repeat=3,
                    number=100))
# result [1.361882399999999, 1.4573816999999991, 1.3631038999999987]
