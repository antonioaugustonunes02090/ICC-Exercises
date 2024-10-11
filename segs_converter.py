from sys import stdin

def segs_converter(time):
    time_format = list(map(int,time.split(':')))
    H, M, S = time_format
    segs = S + 60*M + H*60*60
    return segs

for line in stdin:
    print(segs_converter(line))
