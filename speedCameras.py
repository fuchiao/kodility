def longest_path_length(A, B):
    # init point list
    points = set(A+B)
    if -1 in points:
        points.remove(-1)
    pathLength = 0

    # iter point list for removing tip path, until no path in the map
    for i in points:
        # init remaining point list
        remainingPoints = set(A+B)
        if -1 in remainingPoints:
            remainingPoints.remove(-1)

        # find tip path in the map
        removePath = []
        for j in remainingPoints:
            if A.count(j) + B.count(j) == 1:
                if j in A:
                    removePath.append(A.index(j))
                elif j in B:
                    removePath.append(B.index(j))

        # remove path from list, and count path length
        for j in removePath:
            A[j] = -1
            B[j] = -1
        pathLength += 2

        # no path exists
        if len(A) == A.count(-1):
            break

    # only one path in the lastest remove list
    if len(removePath) == 1:
        pathLength -= 1

    # the last removed path is the best place for camera
    return pathLength, removePath[-1]
        
def solution(A, B, K):
    ret = 0
    while K >= 0:
        ret, cameraPath = longest_path_length(A.copy(), B.copy())
        A[cameraPath] = -1
        B[cameraPath] = -1
        K -= 1
    return ret


if __name__ == "__main__":
    # test case from task description
    assert solution([5,1,0,2,7,0,6,6,1], [1,0,7,4,2,6,8,3,9], 2) == 2, "Something Wrong"
    print("OK")
