import sys

input = sys.stdin.readline


direction = [(0,0), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]

N, M = map(int, input().split(' '))

water = [ ]
for _ in range(N):
   water.append(list(map(int, input().split(' '))))

cloud = [(0, N-1), (1, N-1), (0, N-2), (1, N-2)]
diag_dir = [(-1,-1), (-1, 1), (1, -1), (1, 1)]

def water_copy(water, cur_x, cur_y):
   cnt = 0
   for i in range(4):
      diag_coord_y = cur_y + diag_dir[i][1]
      diag_coord_x = cur_x + diag_dir[i][0]
      try:
         if diag_coord_x != -1 and diag_coord_y != -1:
            cnt += 1 if water[diag_coord_y][diag_coord_x] else 0
      except:
         cnt += 0
   water[cur_y][cur_x] += cnt
   return

def cloud_move(cloud, dir, dist):
   moved = []
   for (x, y) in cloud:
      x = (x + direction[dir][0]*dist)%N
      y = (y + direction[dir][1]*dist)%N
      water[y][x] += 1
      moved.append((x,y))
   for (x,y) in moved:
      water_copy(water, x, y)

   new_cloud = []     
   for x in range(N):
      for y in range(N):
         if (x, y) not in moved:
            if water[y][x] >= 2:
               new_cloud.append((x, y))
               water[y][x] -= 2

   return new_cloud 
   
for _ in range(M):
   dir, dist = map(int, input().rstrip().split(' '))
   cloud = cloud_move(cloud, dir, dist)


print(sum(sum(water[i]) for i in range(N)))


