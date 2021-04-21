import sys

for line in sys.stdin:
    line = line.strip().split()
    ans = []
    for i in range(1, len(line) - 1):
        if line[i] > line[0] and len(line[i]) <= len(line[-1]):
            ans.append(line[i])
    print(' & '.join(ans))