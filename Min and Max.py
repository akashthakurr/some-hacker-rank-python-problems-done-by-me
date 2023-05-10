from numpy import array, min, max

print(
    max(
        min(array([[int(x) for x in input().split()] for _ in range([int(x) for x in input().split()][0])]), axis=1)
    )
)