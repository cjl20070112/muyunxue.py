dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]
n = int(input())
grid = [input().strip() for _ in range(n)]
target = "yizhong"
vis = [[0]*n for _ in range(n)]

def check(x, y, d):
    for i in range(7):
        nx = x + dx[d]*i
        ny = y + dy[d]*i
        if nx <0 or nx >=n or ny <0 or ny >=n or grid[nx][ny] != target[i]:
            return False
    return True

def mark(x, y, d):
    for i in range(7):
        nx = x + dx[d]*i
        ny = y + dy[d]*i
        vis[nx][ny] = 1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'y':
            for d in range(8):
                if check(i, j, d):
                    mark(i, j, d)

for i in range(n):
    s = ""
    for j in range(n):
        s += grid[i][j] if vis[i][j] else "*"
    print(s)