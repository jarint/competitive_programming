import sys

def solve(m, x):
  ps = [1]
  for i in x:
    ps.append(ps[-1] + i)

  table = [ [("-",0)]*(ps[-1]+1) for i in range(m) ]
  table[0][x[0]] = ("U", x[0])
  for k in range(1,m):
    for t in range(ps[k+1]):
      # If we go down at kth step
      if ps[-1] >= t+x[k]:
        d,h = table[k-1][t+x[k]]
        if d != "-":
          table[k][t] = ("D", h)
      # if we go up at kth step
      if t >= x[k]:
        d,h = table[k-1][t-x[k]]
        h = max(h, t)
        if d != "-":
          curr_d, curr_h = table[k][t]
          if curr_d == "-" or curr_h > h:
            table[k][t] = ("U", h)

  # construct path
  path = []
  i = m-1
  curr = 0
  while i >= 0:
    d,h = table[i][curr]
    if d == "U":
      curr -= x[i]
    elif d == "D":
      curr += x[i]
    else:
      return "IMPOSSIBLE"
    path.append(d)
    i-=1
  return "".join(reversed(path))


line = lambda : sys.stdin.readline().strip()
n = int(line())
for i in range(n):
    m = int(line())
    x = list(map(int, line().split()))
    print(solve(m,x))
