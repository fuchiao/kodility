def solution(A):
    return sum(range(1, len(A)+2)) - sum(A)

if __name__ == "__main__":
    assert solution([2,1,3,5]) == 4, "Wrong"
    print("OK")
