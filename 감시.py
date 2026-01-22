import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

cameras = []
covered = set() 

for y in range(N):
    for x in range(M):
        if board[y][x] == 6:
            covered.add((y, x))  
        elif 1 <= board[y][x] <= 5:
            cameras.append((board[y][x], y, x))
            covered.add((y, x))      


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

CCTV_DIR = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]],
}

def watch(y, x, dset):
    added = []
    for d in dset:
        dy, dx = dirs[d]
        ny, nx = y + dy, x + dx
        while 0 <= ny < N and 0 <= nx < M:
            if board[ny][nx] == 6:  
                break
            if (ny, nx) not in covered:
                covered.add((ny, nx))
                added.append((ny, nx))
            ny += dy
            nx += dx
    return added

ans = N*M+1

def dfs(idx):
    global ans
    if idx == len(cameras):
        ans = min(ans, N * M - len(covered))
        return

    t, y, x = cameras[idx]
    for dset in CCTV_DIR[t]:
        added = watch(y, x, dset)
        dfs(idx + 1)
        for p in added: 
            covered.remove(p)

dfs(0)
print(ans)
