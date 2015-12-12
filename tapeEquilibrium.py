def solution(A):
    minDiff = 0
    p1 = 0
    p2 = sum(A)
    for i in range(1, len(A)):
        p1 += A[i-1]
        p2 -= A[i-1]
        diff = abs(p1 - p2)
        if i == 1:
            minDiff = diff
        elif minDiff > diff:
            minDiff = diff
    return minDiff

if __name__ == "__main__":
    assert solution([3,1,2,4,3]) == 1, "Something Wrong"
    print("OK")
