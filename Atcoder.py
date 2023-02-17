# # # # # # # # # # # # # # # # print("Hello world")
# # # # # # # # # # # # # # # # print("Japan is gonna be qualified")
# # # # # # # # # # # # # # # k = int(input())
# # # # # # # # # # # # # # # h = 21
# # # # # # # # # # # # # # # m = 0
# # # # # # # # # # # # # # # h += k // 60
# # # # # # # # # # # # # # # m += k % 60
# # # # # # # # # # # # # # # if m >= 10:
# # # # # # # # # # # # # # #     print(f'{h}:{m}')
# # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # #     print(f'{h}:0{m}')

# # # # # # # # # # # # # # # A,B=map(int,input().split())
# # # # # # # # # # # # # # # print(A|B)

# # # # # # # # # # # # # # x,y,z = map(int, input().split())
# # # # # # # # # # # # # # if x > 0 and y > 0:
# # # # # # # # # # # # # #     if x < y:
# # # # # # # # # # # # # #         print(x)
# # # # # # # # # # # # # #     elif z < y:
# # # # # # # # # # # # # #         if z < 0:
# # # # # # # # # # # # # #             print(abs(z)*2+x)
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             print(x)
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         print(-1)
# # # # # # # # # # # # # # elif x > 0 and y < 0:
# # # # # # # # # # # # # #     print(x)
# # # # # # # # # # # # # # elif x < 0 and y > 0:
# # # # # # # # # # # # # #     print(abs(x))
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #     if x > y:
# # # # # # # # # # # # # #         print(abs(x))
# # # # # # # # # # # # # #     elif z > y:
# # # # # # # # # # # # # #         if z > 0:
# # # # # # # # # # # # # #             print(z*2+abs(x))
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             print(x)
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         print(-1)

# # # # # # # # # # # # # # ans = []
# # # # # # # # # # # # # # def dfs(now,pre):
# # # # # # # # # # # # # #     global ans
# # # # # # # # # # # # # #     global done
# # # # # # # # # # # # # #     ans.append(now)
# # # # # # # # # # # # # #     done[now] = True
# # # # # # # # # # # # # #     print(ans)
# # # # # # # # # # # # # #     for to in connected[now]:
# # # # # # # # # # # # # #         print(ans)
# # # # # # # # # # # # # #         print(to, now, pre)
# # # # # # # # # # # # # #         if to != pre:
# # # # # # # # # # # # # #             dfs(to,now)
# # # # # # # # # # # # # #             ans.append(now)
# # # # # # # # # # # # # #             done[now] = True
# # # # # # # # # # # # # #         elif to == y:
# # # # # # # # # # # # # #             ans.append(to)
# # # # # # # # # # # # # #             print(*ans)
# # # # # # # # # # # # # #             exit()
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             ans.pop(-1)

# # # # # # # # # # # # # # n,x,y = map(int, input().split())
# # # # # # # # # # # # # # connected = [[] for i in range(n+1)]
# # # # # # # # # # # # # # done = [False for i in range(n+1)]
# # # # # # # # # # # # # # for i in range(n-1):
# # # # # # # # # # # # # #     u,v = map(int, input().split())
# # # # # # # # # # # # # #     connected[u].append(v)
# # # # # # # # # # # # # #     connected[v].append(u)
# # # # # # # # # # # # # # print(connected)
# # # # # # # # # # # # # # dfs(x,-1)

# # # # # # # # # # # # # n,x,y = map(int, input().split())
# # # # # # # # # # # # # connect = [[] for i in range(n+1)]
# # # # # # # # # # # # # for i in range(n-1):
# # # # # # # # # # # # #     u,v = map(int, (input().split()))
# # # # # # # # # # # # #     connect[u].append(v)
# # # # # # # # # # # # #     connect[v].append(u)
# # # # # # # # # # # # # dist = [-1]*(n+1)
# # # # # # # # # # # # # dist[x] = 0
# # # # # # # # # # # # # from collections import deque
# # # # # # # # # # # # # q = deque()
# # # # # # # # # # # # # q.append(x)
# # # # # # # # # # # # # while len(q) > 0:
# # # # # # # # # # # # #     now = q.popleft()
# # # # # # # # # # # # #     for to in connect[now]:
# # # # # # # # # # # # #         if dist[to] == -1:
# # # # # # # # # # # # #             dist[to] = dist[now]+1
# # # # # # # # # # # # #             q.append(to)
# # # # # # # # # # # # # ans = deque()
# # # # # # # # # # # # # cnt = dist[y]
# # # # # # # # # # # # # now = y
# # # # # # # # # # # # # while 0 < cnt:
# # # # # # # # # # # # #     ans.appendleft(now)
# # # # # # # # # # # # #     for to in connect[now]:
# # # # # # # # # # # # #         if dist[to] == cnt-1:
# # # # # # # # # # # # #             cnt -= 1
# # # # # # # # # # # # #             now = to
# # # # # # # # # # # # # ans.appendleft(x)
# # # # # # # # # # # # # print(*ans)

# # # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # # chars = "ABCDEF"
# # # # # # # # # # # # # ans = ""
# # # # # # # # # # # # # while n > 0:
# # # # # # # # # # # # #     tmp = n % 16
# # # # # # # # # # # # #     n //= 16
# # # # # # # # # # # # #     if tmp > 9:
# # # # # # # # # # # # #         ans += chars[tmp-10]
# # # # # # # # # # # # #     else:
# # # # # # # # # # # # #         ans += str(tmp)
# # # # # # # # # # # # # ans = ans[::-1]
# # # # # # # # # # # # # if len(ans) < 2:
# # # # # # # # # # # # #     ans = "0" + ans
# # # # # # # # # # # # # if len(ans) < 2:
# # # # # # # # # # # # #     ans = "0" + ans
# # # # # # # # # # # # # print(ans)

# # # # # # # # # # # # # n,q = map(int, input().split())
# # # # # # # # # # # # # grids = []
# # # # # # # # # # # # # for i in range(n):  
# # # # # # # # # # # # #     l,*a = tuple(map(int, input().split()))
# # # # # # # # # # # # #     grids.append(a)
# # # # # # # # # # # # # for i in range(q):
# # # # # # # # # # # # #     s,t = map(int, input().split())
# # # # # # # # # # # # #     print(grids[s-1][t-1])

# # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # alist = list(map(int, input().split()))
# # # # # # # # # # # # alist = set(alist)
# # # # # # # # # # # # leng = len(alist)
# # # # # # # # # # # # double = n-leng
# # # # # # # # # # # # for i in range(1,10**9+1):
# # # # # # # # # # # #     if i in alist:
# # # # # # # # # # # #         leng -= 1
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         if double > 1:
# # # # # # # # # # # #             double -= 2
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             if leng > 1:
# # # # # # # # # # # #                 leng -= 2
# # # # # # # # # # # #                 alist = set(list(alist)[:n-2])
# # # # # # # # # # # #                 n -= 2
# # # # # # # # # # # #             else:
# # # # # # # # # # # #                 print(i-1)
# # # # # # # # # # # #                 exit()

# # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # alist = list(map(int, input().split()))
# # # # # # # # # # # # print(sum(alist))

# # # # # # # # # # # # n,m = map(int, input().split())
# # # # # # # # # # # # connected = [[] for i in range(n)]
# # # # # # # # # # # # for i in range(m):
# # # # # # # # # # # #     k,*X = map(int, input().split())
# # # # # # # # # # # #     for x in X:
# # # # # # # # # # # #         for j in X:
# # # # # # # # # # # #             connected[x-1].append(j)
# # # # # # # # # # # # ans = set([i for i in range(1,n+1)])
# # # # # # # # # # # # for connect in connected:
# # # # # # # # # # # #     if set(connect) != ans:
# # # # # # # # # # # #         print("no")
# # # # # # # # # # # #         exit()
# # # # # # # # # # # # print("Yes")

# # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # alist = list(map(int, input().split()))
# # # # # # # # # # # # odd = []
# # # # # # # # # # # # even = []
# # # # # # # # # # # # for a in alist:
# # # # # # # # # # # #     if a % 2 == 0:
# # # # # # # # # # # #         even.append(a)
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         odd.append(a)
# # # # # # # # # # # # ans = -1
# # # # # # # # # # # # odd.sort()
# # # # # # # # # # # # even.sort()
# # # # # # # # # # # # if len(odd) > 1:
# # # # # # # # # # # #     ans = max(ans,odd[-1]+odd[-2])
# # # # # # # # # # # # if len(even) > 1:
# # # # # # # # # # # #     ans = max(ans,even[-1]+even[-2])
# # # # # # # # # # # # print(ans)

# # # # # # # # # # # # def recur(n):
# # # # # # # # # # # #     if n == 0:
# # # # # # # # # # # #         ans = 1
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         ans = n*recur(n-1)
# # # # # # # # # # # #     return ans
    
# # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # print(recur(n))

# # # # # # # # # # # # x,k = input().split()
# # # # # # # # # # # # X = x[::-1]
# # # # # # # # # # # # k = int(k)
# # # # # # # # # # # # xlist = []
# # # # # # # # # # # # for x in X:
# # # # # # # # # # # #     xlist.append(int(x))
# # # # # # # # # # # # for i in range(k):
# # # # # # # # # # # #     if xlist[i] > 4:
# # # # # # # # # # # #         xlist[i] = 0
# # # # # # # # # # # #         tmp = i
        
# # # # # # # # # # # # a,b = map(int, input().split())
# # # # # # # # # # # # ans = round(b/a,3)
# # # # # # # # # # # # print('{:.03f}'.format(ans))

# # # # # # # # # # # # h,w = map(int, input().split())
# # # # # # # # # # # # Clist = []
# # # # # # # # # # # # for i in range(h):
# # # # # # # # # # # #     tmp = list(input())
# # # # # # # # # # # #     Clist.append(tmp)
# # # # # # # # # # # # ans = []
# # # # # # # # # # # # for i in range(w):
# # # # # # # # # # # #     cnt = 0
# # # # # # # # # # # #     for j in range(h):
# # # # # # # # # # # #         if Clist[j][i] == '#':
# # # # # # # # # # # #             cnt += 1
# # # # # # # # # # # #     ans.append(cnt)
# # # # # # # # # # # # print(*ans)

# # # # # # # # # # # # アプローチは合ってる
# # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # alist = list(map(int, input().split()))
# # # # # # # # # # # # connected = [[] for i in range(n*2+1)]
# # # # # # # # # # # # for i in range(n):
# # # # # # # # # # # #     connected[(i+1)*2-1].append(alist[i]-1)
# # # # # # # # # # # #     connected[(i+1)*2].append(alist[i]-1)
# # # # # # # # # # # # for i in range(n*2+1):
# # # # # # # # # # # #     tmp = i
# # # # # # # # # # # #     cnt = 0
# # # # # # # # # # # #     while connected[tmp]:
# # # # # # # # # # # #         tmp = connected[tmp][0]
# # # # # # # # # # # #         cnt += 1
# # # # # # # # # # # #     print(cnt)

# # # # # # # # # # # # n=int(input())
# # # # # # # # # # # # alist=[0]+list(map(int,input().split()))

# # # # # # # # # # # # ans=[0]*(2*n+2)

# # # # # # # # # # # # for i in range(1,n+1):
# # # # # # # # # # # #     ans[2*i]=ans[alist[i]]+1
# # # # # # # # # # # #     ans[2*i+1]=ans[alist[i]]+1
# # # # # # # # # # # # for i in range(1,2*n+2):
# # # # # # # # # # # #     print(ans[i])

# # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # H = list(map(int, input().split()))
# # # # # # # # # # # # print(H.index(max(H))+1)

# # # # # # # # # # # # MOD = 998244353 
# # # # # # # # # # # # a,b,c,d,e,f = map(int, input().split())
# # # # # # # # # # # # print((a*b*c-d*e*f)%MOD)

# # # # # # # # # # # # grids = []
# # # # # # # # # # # # for i in range(9):
# # # # # # # # # # # #     g_line = list(input())
# # # # # # # # # # # #     grids.append(g_line)
# # # # # # # # # # # # cnt = 0
# # # # # # # # # # # # for ay in range(9):
# # # # # # # # # # # #     for ax in range(9):
# # # # # # # # # # # #         for by in range(ay,9):
# # # # # # # # # # # #             for bx in range(ax+1,9):
# # # # # # # # # # # #                 if grids[ay][ax] == '#' and grids[by][bx] == '#':
# # # # # # # # # # # #                     cy = by+(bx-ax)
# # # # # # # # # # # #                     cx = bx-(by-ay)
# # # # # # # # # # # #                     dy = cy-(bx-cx)
# # # # # # # # # # # #                     dx = cx-(cy-by)
# # # # # # # # # # # #                     if 0<=cy<=8 and 0<=dy<=8 and 0<=cx<=8 and 0<=dx<=8:
# # # # # # # # # # # #                         if grids[cy][cx] == '#' and grids[dy][dx] == '#':
# # # # # # # # # # # #                             cnt += 1
# # # # # # # # # # # # print(cnt)

# # # # # # # # # # # # S = input()
# # # # # # # # # # # # ans = -1
# # # # # # # # # # # # for i,s in enumerate(S):
# # # # # # # # # # # #     if s == 'a':
# # # # # # # # # # # #         ans = i+1
# # # # # # # # # # # # print(ans)

# # # # # # # # # # # # n,m = map(int, input().split())
# # # # # # # # # # # # connected = [[] for i in range(n+1)]
# # # # # # # # # # # # for i in range(m):
# # # # # # # # # # # #     a,b = map(int, input().split())
# # # # # # # # # # # #     connected[a].append(b)
# # # # # # # # # # # #     connected[b].append(a)
# # # # # # # # # # # # for i in range(1,n+1):
# # # # # # # # # # # #     print(len(connected[i]), *sorted(connected[i]))

# # # # # # # # # # # # from itertools import permutations
# # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # P = tuple(map(int, input().split()))
# # # # # # # # # # # # prev = (0,0,0)
# # # # # # # # # # # # for i in permutations(list(i for i in range(1,n+1))):
# # # # # # # # # # # #     if i == P:
# # # # # # # # # # # #         print(*prev)
# # # # # # # # # # # #         exit()
# # # # # # # # # # # #     prev = i

# # # # # # # # # # # # N=int(input())
# # # # # # # # # # # # A=list(map(int,input().split()))

# # # # # # # # # # # # for i in range(N-2,-1,-1):
# # # # # # # # # # # #     if A[i]>A[i+1]:
# # # # # # # # # # # #         for d in range(1,N):
# # # # # # # # # # # #             for k in range(i+1,N):
# # # # # # # # # # # #                 if A[i]-A[k]==d:
# # # # # # # # # # # #                     A[i],A[k]=A[k],A[i]
# # # # # # # # # # # #                     x=A[:i+1]
# # # # # # # # # # # #                     y=A[i+1:]
# # # # # # # # # # # #                     y.sort(reverse=True)
# # # # # # # # # # # #                     print(*x+y)
# # # # # # # # # # # #                     exit()

# # # # # # # # # # # # from collections import deque,defaultdict
# # # # # # # # # # # # N = int(input())
# # # # # # # # # # # # connected=defaultdict(list)
# # # # # # # # # # # # for i in range(N):
# # # # # # # # # # # #     a,b = map(int, input().split())
# # # # # # # # # # # #     connected[a].append(b)
# # # # # # # # # # # #     connected[b].append(a)
# # # # # # # # # # # # higheset = 1
# # # # # # # # # # # # visited = defaultdict(int)
# # # # # # # # # # # # q = deque()
# # # # # # # # # # # # q.append(1)
# # # # # # # # # # # # while len(q) > 0:
# # # # # # # # # # # #     now = q.popleft()
# # # # # # # # # # # #     if now > higheset:
# # # # # # # # # # # #         higheset = now
# # # # # # # # # # # #     for to in connected[now]:
# # # # # # # # # # # #         if visited[to] == 0:
# # # # # # # # # # # #             visited[to] = 1
# # # # # # # # # # # #             q.append(to)
# # # # # # # # # # # # print(higheset)

# # # # # # # # # # # # n,x = map(int, input().split())
# # # # # # # # # # # # plist = list(map(int, input().split()))
# # # # # # # # # # # # print(plist.index(x)+1)

# # # # # # # # # # # # n = int(input())
# # # # # # # # # # # # S = [input() for _ in range(n)]
# # # # # # # # # # # # if n != len(set(S)):
# # # # # # # # # # # #     print("No")
# # # # # # # # # # # #     exit()
# # # # # # # # # # # # first = ['H','D','C','S']
# # # # # # # # # # # # sec = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
# # # # # # # # # # # # for s in S:
# # # # # # # # # # # #     if s[0] not in first:
# # # # # # # # # # # #         print("No")
# # # # # # # # # # # #         exit()
# # # # # # # # # # # #     if s[1] not in sec:
# # # # # # # # # # # #         print("No")
# # # # # # # # # # # #         exit()
# # # # # # # # # # # # print("Yes")

# # # # # # # # # # # # from collections import defaultdict
# # # # # # # # # # # # N,Q = map(int, input().split())
# # # # # # # # # # # # connected = defaultdict(int)
# # # # # # # # # # # # for i in range(Q):
# # # # # # # # # # # #     t,a,b = map(int, input().split())
# # # # # # # # # # # #     if t == 1:
# # # # # # # # # # # #         connected[(a,b)] = 1
# # # # # # # # # # # #     elif t == 2:
# # # # # # # # # # # #         connected[(a,b)] = 0
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         if connected[(a,b)] == 1 and connected[(b,a)] == 1:
# # # # # # # # # # # #             print("Yes")
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             print("No")

# # # # # # # # # # # # h,w = map(int, input().split())
# # # # # # # # # # # # S = []
# # # # # # # # # # # # for i in range(h):
# # # # # # # # # # # #     s_line = list(input())
# # # # # # # # # # # #     S.append(s_line)
# # # # # # # # # # # # T = []
# # # # # # # # # # # # for i in range(h):
# # # # # # # # # # # #     t_line = list(input())
# # # # # # # # # # # #     T.append(t_line)
# # # # # # # # # # # # S.sort()
# # # # # # # # # # # # T.sort()
# # # # # # # # # # # # # for i in range(h):
# # # # # # # # # # # # #     if S[i].count('#') != T[i].count('#'):
# # # # # # # # # # # # #         print("No")
# # # # # # # # # # # # #         exit()
# # # # # # # # # # # # # print("Yes")
# # # # # # # # # # # # print(S,T)
# # # # # # # # # # # # if S == T:
# # # # # # # # # # # #     print("Yes")
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print("No")

# # # # # # # # # # # # 入力の受け取り
# # # # # # # # # # # H,W=map(int,input().split())

# # # # # # # # # # # # Sの記録
# # # # # # # # # # # S=[]
# # # # # # # # # # # # i~0~(H-1)
# # # # # # # # # # # for i in range(H):
# # # # # # # # # # #     # 入力の受け取り
# # # # # # # # # # #     Si=input()
# # # # # # # # # # #     # Sへ追加
# # # # # # # # # # #     S.append(Si)
    
# # # # # # # # # # # # Tの記録
# # # # # # # # # # # T=[]
# # # # # # # # # # # # i~0~(H-1)
# # # # # # # # # # # for i in range(H):
# # # # # # # # # # #     # 入力の受け取り
# # # # # # # # # # #     Ti=input()
# # # # # # # # # # #     # Tへ追加
# # # # # # # # # # #     T.append(Ti)

# # # # # # # # # # # # Sの各列ごとの要素記録
# # # # # # # # # # # Sc=[]
# # # # # # # # # # # # Tの各列ごとの要素記録
# # # # # # # # # # # Tc=[]

# # # # # # # # # # # # w=0~(W-1)
# # # # # # # # # # # for w in range(W):
# # # # # # # # # # #     # w列の要素
# # # # # # # # # # #     Mozi=""
# # # # # # # # # # #     # h~0~(H-1)
# # # # # # # # # # #     for h in range(H):
# # # # # # # # # # #         # Moziへh行w列の文字を追加
# # # # # # # # # # #         Mozi+=S[h][w]
# # # # # # # # # # #     # 記録
# # # # # # # # # # #     Sc.append(Mozi)

# # # # # # # # # # # # w=0~(W-1)
# # # # # # # # # # # for w in range(W):
# # # # # # # # # # #     # w列の要素
# # # # # # # # # # #     Mozi=""
# # # # # # # # # # #     # h~0~(H-1)
# # # # # # # # # # #     for h in range(H):
# # # # # # # # # # #         # Moziへh行w列の文字を追加
# # # # # # # # # # #         Mozi+=T[h][w]
# # # # # # # # # # #     # 記録
# # # # # # # # # # #     Tc.append(Mozi)
# # # # # # # # # # # # 並び替え
# # # # # # # # # # # Sc.sort()
# # # # # # # # # # # Tc.sort()

# # # # # # # # # # # # ScとTcが一致していれば
# # # # # # # # # # # if Sc==Tc:
# # # # # # # # # # #     # 「Yes」を出力
# # # # # # # # # # #     print("Yes")
# # # # # # # # # # # # そうでなければ
# # # # # # # # # # # else:
# # # # # # # # # # #     # 「No」を出力
# # # # # # # # # # #     print("No")

# # # # # # # # # # # S = input()
# # # # # # # # # # # T = input()
# # # # # # # # # # # for i in range(len(S)):
# # # # # # # # # # #     if S[i] != T[i]:
# # # # # # # # # # #         print(i+1)
# # # # # # # # # # #         exit()
# # # # # # # # # # # print(len(T))

# # # # # # # # # # # from itertools import accumulate
# # # # # # # # # # # import bisect
# # # # # # # # # # # n,t = map(int, input().split())
# # # # # # # # # # # A = [0] + list(map(int, input().split()))
# # # # # # # # # # # A = list(accumulate(A))
# # # # # # # # # # # t %= A[-1]
# # # # # # # # # # # if t < A[-1]:
# # # # # # # # # # #     print(bisect.bisect_left(A,t),t-A[bisect.bisect_left(A,t)-1])
# # # # # # # # # # # else:
# # # # # # # # # # #     print(bisect.bisect_left(A,t),t)

# # # # # # # # # # # N = int(input())
# # # # # # # # # # # S = list(input())
# # # # # # # # # # # judge = False
# # # # # # # # # # # for i in range(N):
# # # # # # # # # # #     if S[i] == '"':
# # # # # # # # # # #         if judge:
# # # # # # # # # # #             judge = False
# # # # # # # # # # #         else:
# # # # # # # # # # #             judge = True
# # # # # # # # # # #     if not judge and S[i] == ',':
# # # # # # # # # # #         S[i] = '.'
# # # # # # # # # # # print(''.join(S))

# # # # # # # # # # # S = input()
# # # # # # # # # # # cnt = 0
# # # # # # # # # # # judge = False
# # # # # # # # # # # for i in range(len(S)-1):
# # # # # # # # # # #     if judge:
# # # # # # # # # # #         judge = False
# # # # # # # # # # #         continue
# # # # # # # # # # #     if (S[i],S[i+1]) == ('0','0'):
# # # # # # # # # # #         cnt += 1
# # # # # # # # # # #         judge = True
# # # # # # # # # # # print(len(S)-cnt)

# # # # # # # # # # # S = input()
# # # # # # # # # # # begin = []
# # # # # # # # # # # cnt = 1
# # # # # # # # # # # done = set()
# # # # # # # # # # # for i,s in enumerate(S):
# # # # # # # # # # #     if s == '(':
# # # # # # # # # # #         begin.append(i)
# # # # # # # # # # #     elif s == ')':
# # # # # # # # # # #         for j in range(begin[-cnt],i):
# # # # # # # # # # #             if S[j] != '(' and S[j] != ')' and S[j] in done:
# # # # # # # # # # #                 done.remove(S[j])
# # # # # # # # # # #         cnt += 1
# # # # # # # # # # #     else:
# # # # # # # # # # #         if s in done:
# # # # # # # # # # #             print("No")
# # # # # # # # # # #             exit()
# # # # # # # # # # #         else:
# # # # # # # # # # #             done.add(s)
# # # # # # # # # # # print("Yes")

# # # # # # # # # # # from collections import Counter
# # # # # # # # # # # n = int(input())
# # # # # # # # # # # A = list(map(int, input().split()))
# # # # # # # # # # # A = [a%200 for a in A] #200で割れている数という条件を利用していく
# # # # # # # # # # # cnt = 0
# # # # # # # # # # # A = Counter(A)
# # # # # # # # # # # for i in A.values():
# # # # # # # # # # #     if i > 2:
# # # # # # # # # # #         cnt += (((i)*(i-1))//2) #３個以上一致の要素があるなら組み合わせをつかう
# # # # # # # # # # #     else:
# # # # # # # # # # #         cnt += i-1 #それ以外なら単純に1をひく
# # # # # # # # # # # print(cnt)

# # # # # # # # # # S = input()
# # # # # # # # # # fSlis = []
# # # # # # # # # # nSlis = []
# # # # # # # # # # fS = 0
# # # # # # # # # # aN = 0
# # # # # # # # # # nS = 0
# # # # # # # # # # for i,s in enumerate(S):
# # # # # # # # # #     if s == 'o':
# # # # # # # # # #         fSlis.append(i+1)
# # # # # # # # # #         fS += 1
# # # # # # # # # #     elif s == '?':
# # # # # # # # # #         nSlis.append(i+1)
# # # # # # # # # #         nS += 1
# # # # # # # # # # print(fSlis, nSlis)
# # # # # # # # # # print(fS,nS)

# # # # # # # # # # def judge(tmp):
# # # # # # # # # #     for o in O:
# # # # # # # # # #         if o not in tmp:
# # # # # # # # # #             return False
# # # # # # # # # #     for x in X:
# # # # # # # # # #         if x in tmp:
# # # # # # # # # #             return False
# # # # # # # # # #     return True

# # # # # # # # # # S = input()
# # # # # # # # # # O = []
# # # # # # # # # # X = []
# # # # # # # # # # for i, s in enumerate(S):
# # # # # # # # # #     if s == 'o':
# # # # # # # # # #         O.append(str(i))
# # # # # # # # # #     elif s == 'x':
# # # # # # # # # #         X.append(str(i))
# # # # # # # # # # cnt = 0
# # # # # # # # # # for i in range(10000):
# # # # # # # # # #     tmp = str(i).zfill(4)
# # # # # # # # # #     if judge(tmp):
# # # # # # # # # #         cnt += 1
# # # # # # # # # # print(cnt)        

# # # # # # # # # # from collections import Counter
# # # # # # # # # # N = int(input())
# # # # # # # # # # A = list(map(int, input().split()))
# # # # # # # # # # B = list(map(int, input().split()))
# # # # # # # # # # C = list(map(int, input().split()))
# # # # # # # # # # A = Counter(A)
# # # # # # # # # # C = Counter(C)
# # # # # # # # # # cnt = 0
# # # # # # # # # # for i, b in enumerate(B):
# # # # # # # # # #     if b not in A:
# # # # # # # # # #         continue
# # # # # # # # # #     if i+1 not in C:
# # # # # # # # # #         continue
# # # # # # # # # #     cnt += A[b]*C[i+1]
# # # # # # # # # # print(cnt)

# # # # # # # # # # from collections import defaultdict
# # # # # # # # # # N,k = map(int, input().split())
# # # # # # # # # # friends = defaultdict(int)
# # # # # # # # # # cnt = k
# # # # # # # # # # for n in range(N):
# # # # # # # # # #     a,b = map(int, input().split())
# # # # # # # # # #     friends[a] += b
# # # # # # # # # # for a,b in sorted(friends.items(), key=lambda x: x[0]):
# # # # # # # # # #     if cnt >= a:
# # # # # # # # # #         cnt += b
# # # # # # # # # #     else:
# # # # # # # # # #         break
# # # # # # # # # # print(cnt)

# # # # # # # # # # from collections import deque
# # # # # # # # # # N,M = map(int, input().split())
# # # # # # # # # # connected = [[] for _ in range(N+1)]
# # # # # # # # # # for i in range(M):
# # # # # # # # # #     a,b = map(int, input().split())
# # # # # # # # # #     connected[a].append(b)
# # # # # # # # # # ans = N
# # # # # # # # # # for i in range(1,N+1):
# # # # # # # # # #     q = deque()
# # # # # # # # # #     q.append(i)
# # # # # # # # # #     done = [False]*(N+1)
# # # # # # # # # #     done[i] = True
# # # # # # # # # #     while len(q) > 0:
# # # # # # # # # #         now = q.popleft()
# # # # # # # # # #         for c in connected[now]:
# # # # # # # # # #             if done[c] == False:
# # # # # # # # # #                 q.append(c)
# # # # # # # # # #                 done[c] = True
# # # # # # # # # #                 ans += 1
# # # # # # # # # # print(ans)

# # # # # # # # # # a,b,c = map(int, input().split())
# # # # # # # # # # if c % 2 == 0:
# # # # # # # # # #     if abs(a) > abs(b):
# # # # # # # # # #         print(">")
# # # # # # # # # #     elif abs(a) < abs(b):
# # # # # # # # # #         print("<")
# # # # # # # # # #     else:
# # # # # # # # # #         print("=")
# # # # # # # # # # else:
# # # # # # # # # #     if a > b:
# # # # # # # # # #         print(">")
# # # # # # # # # #     elif a < b:
# # # # # # # # # #         print("<")
# # # # # # # # # #     else:
# # # # # # # # # #         print("=")

# # # # # # # # # # from collections import Counter

# # # # # # # # # # n = int(input())
# # # # # # # # # # A = list(map(int, input().split()))
# # # # # # # # # # A = Counter(A)
# # # # # # # # # # cnt = 0
# # # # # # # # # # ans = 0
# # # # # # # # # # for a in A.values():
# # # # # # # # # #     cnt += a
# # # # # # # # # #     ans += a*(n-cnt)
# # # # # # # # # # print(ans)

# # # # # # # # # # N = int(input())
# # # # # # # # # # combs = []
# # # # # # # # # # for i in range(N):
# # # # # # # # # #     t,l,r = map(int, input().split())
# # # # # # # # # #     if t == 1:
# # # # # # # # # #         combs.append([l,r])
# # # # # # # # # #     elif t == 2:
# # # # # # # # # #         combs.append([l,r-0.1])
# # # # # # # # # #     elif t == 3:
# # # # # # # # # #         combs.append([l+0.1,r])
# # # # # # # # # #     else:
# # # # # # # # # #         combs.append([l+0.1,r-0.1])
# # # # # # # # # # ans = 0
# # # # # # # # # # for i in range(N):
# # # # # # # # # #     for j in range(i+1,N):
# # # # # # # # # #         a,b = combs[i]
# # # # # # # # # #         c,d = combs[j]
# # # # # # # # # #         if a <= c and d <= b:
# # # # # # # # # #             ans += 1
# # # # # # # # # #         elif c <= a and b <= d:
# # # # # # # # # #             ans += 1
# # # # # # # # # #         elif c <= b and b<= d:
# # # # # # # # # #             ans += 1
# # # # # # # # # #         elif a <= d and d <= b:
# # # # # # # # # #             ans += 1
# # # # # # # # # # print(ans)

# # # # # # # # # # import bisect
# # # # # # # # # # n,k = map(int, input().split())
# # # # # # # # # # A = list(map(int, input().split()))
# # # # # # # # # # As = sorted(A)
# # # # # # # # # # cnt = k//n
# # # # # # # # # # k -= cnt*n
# # # # # # # # # # for a in A:
# # # # # # # # # #     if (bisect.bisect_left(As,a)+1) <= k:
# # # # # # # # # #         print(cnt+1)
# # # # # # # # # #     else:
# # # # # # # # # #         print(cnt)

# # # # # # # # # # n,k = map(int, input().split())
# # # # # # # # # # C = list(map(int, input().split()))
# # # # # # # # # # ans = 0
# # # # # # # # # # for i in range(n-k+1):
# # # # # # # # # #     tmp = len(set(C[i:i+k]))
# # # # # # # # # #     ans = max(ans,tmp)
# # # # # # # # # # print(ans)

# # # # # # # # # # from collections import Counter
# # # # # # # # # # n,k = map(int, input().split())
# # # # # # # # # # clist = list(map(int, input().split()))
# # # # # # # # # # counter = Counter(clist[:k])
# # # # # # # # # # ans = len(counter)
# # # # # # # # # # for i in range(k,n):
# # # # # # # # # #     left = clist[i-k]
# # # # # # # # # #     right = clist[i]
# # # # # # # # # #     counter[left] -= 1
# # # # # # # # # #     counter[right] += 1
# # # # # # # # # #     if counter[left] == 0:
# # # # # # # # # #         del counter[left]
# # # # # # # # # #     ans = max(ans, len(counter))
# # # # # # # # # # print(ans)

# # # # # # # # # # from collections import Counter
# # # # # # # # # # n,k = map(int, input().split())
# # # # # # # # # # C = list(map(int, input().split()))
# # # # # # # # # # Cnt = Counter(C[:k])
# # # # # # # # # # ans = len(Cnt)
# # # # # # # # # # for i in range(k,n):
# # # # # # # # # #     lef = C[i-k]
# # # # # # # # # #     rig = C[i]
# # # # # # # # # #     Cnt[lef] -= 1
# # # # # # # # # #     Cnt[rig] += 1
# # # # # # # # # #     if Cnt[lef] == 0:
# # # # # # # # # #         del Cnt[lef]
# # # # # # # # # #     ans = max(ans,len(Cnt))
# # # # # # # # # # print(ans)

# # # # # # # # # # MOD = 10 ** 9 + 7


# # # # # # # # # # def main():
# # # # # # # # # #     from collections import Counter

# # # # # # # # # #     S = input()
# # # # # # # # # #     T = '*chokudai'  # 0文字目は英小文字でない適当な記号にします
# # # # # # # # # #     dp = Counter()
# # # # # # # # # #     dp['*'] = 1
# # # # # # # # # #     for char in S:
# # # # # # # # # #         if char in T:
# # # # # # # # # #             char_prev = T[T.index(char) - 1]  # charの前の文字、iの前はa、cの前は*
# # # # # # # # # #             dp[char] += dp[char_prev]
# # # # # # # # # #             dp[char] %= MOD
# # # # # # # # # #             print(char,char_prev)
# # # # # # # # # #             print(dp)
# # # # # # # # # #     print(dp['i'])


# # # # # # # # # # if __name__ == '__main__':
# # # # # # # # # #     main()

# # # # # # # # # # MOD = 10**9+7
# # # # # # # # # # from collections import Counter
# # # # # # # # # # S = input()
# # # # # # # # # # Ans = "!chokudai"
# # # # # # # # # # Cnts = Counter()
# # # # # # # # # # Cnts['!'] = 1
# # # # # # # # # # for s in S:
# # # # # # # # # #     if s in Ans:
# # # # # # # # # #         sP = Ans[Ans.index(s)-1]
# # # # # # # # # #         Cnts[s] += Cnts[sP]
# # # # # # # # # #         Cnts[s] %= MOD
# # # # # # # # # # print(Cnts["i"])

# # # # # # # # # # import bisect
# # # # # # # # # # INF = 1<<60
# # # # # # # # # # N,M = map(int, input().split())
# # # # # # # # # # A = sorted(list(map(int, input().split())))
# # # # # # # # # # B = sorted(list(map(int, input().split())))
# # # # # # # # # # ans = INF
# # # # # # # # # # for a in A:
# # # # # # # # # #     tmp = bisect.bisect_right(B,a)
# # # # # # # # # #     if tmp == len(B):
# # # # # # # # # #         ans = min(ans,abs(a-B[tmp-1]))
# # # # # # # # # #     elif tmp == 0:
# # # # # # # # # #         ans = min(ans,abs(a-B[tmp]))
# # # # # # # # # #     else:
# # # # # # # # # #         ans = min(ans,min(abs(a-B[tmp]),abs(a-B[tmp-1])))
# # # # # # # # # # print(ans)

# # # # # # # # # H,W,N = map(int, input().split())
# # # # # # # # # nums = []
# # # # # # # # # rows = []
# # # # # # # # # cols = []
# # # # # # # # # for i in range(N):
# # # # # # # # #     a,b = (map(int, input().split()))
# # # # # # # # #     rows.append(a)
# # # # # # # # #     cols.append(b)
# # # # # # # # #     nums.append([a,b])
# # # # # # # # # rows.sort()
# # # # # # # # # cols.sort()
# # # # # # # # # for a,b in nums:
# # # # # # # # #     print((rows.index(a))+1,(cols.index(b))+1)

# # # # # # # # H,W,N = map(int, input().split())
# # # # # # # # X = []
# # # # # # # # Y = []
# # # # # # # # for i in range(N):
# # # # # # # #     x,y = map(int, input().split())
# # # # # # # #     X.append(x)
# # # # # # # #     Y.append(y)
# # # # # # # # sortedX = sorted(set(X))
# # # # # # # # sortedY = sorted(set(Y))
# # # # # # # # ansX = {sortedX[i]: i+1 for i in range(len(sortedX))}
# # # # # # # # ansY = {sortedY[i]: i+1 for i in range(len(sortedY))}
# # # # # # # # for x,y in zip(X,Y):
# # # # # # # #     print(ansX[x], ansY[y])

# # # # # # # # INF = 1<<60
# # # # # # # # N = int(input())
# # # # # # # # S = list(map(int, input().split()))
# # # # # # # # T = list(map(int, input().split()))
# # # # # # # # dp = [INF]*N
# # # # # # # # dp[0] = T[0]
# # # # # # # # for i in range(1,N):
# # # # # # # #     dp[i] = min(dp[i-1]+S[i-1],T[i])
# # # # # # # # for i in range(N):
# # # # # # # #     dp[i] = min(dp[i-1]+S[i-1],T[i])
# # # # # # # # for d in dp:
# # # # # # # #     print(d)

# # # # # # # # from itertools import permutations
# # # # # # # # S,K = input().split()
# # # # # # # # S = list(S)
# # # # # # # # K = int(K)
# # # # # # # # arr = sorted(set(list(permutations(S,len(S)))))
# # # # # # # # print(arr)
# # # # # # # # print(''.join(list(arr[K-1])))

# # # # # # # # import math
# # # # # # # # N = int(input())
# # # # # # # # cN = N
# # # # # # # # ans = 'AA'
# # # # # # # # num = 2
# # # # # # # # if N == 1:
# # # # # # # #     print('A')
# # # # # # # #     exit()
# # # # # # # # elif N == 2:
# # # # # # # #     print(ans)
# # # # # # # #     exit()
# # # # # # # # if N % 2 == 1:
# # # # # # # #     tmp = int(math.sqrt(N))
# # # # # # # #     ans+= 'B'*(tmp-1)
# # # # # # # #     N -= 2**tmp
# # # # # # # #     ans += 'A'*N
# # # # # # # #     print(ans)
# # # # # # # # else:
# # # # # # # #     cnt = 0
# # # # # # # #     while N % 2 == 0:
# # # # # # # #         N /= 2
# # # # # # # #         cnt += 1
# # # # # # # #     N = int(N)
# # # # # # # #     if 2**cnt == cN:
# # # # # # # #         ans += 'B'*(cnt-1)
# # # # # # # #         print(ans)
# # # # # # # #         exit()
# # # # # # # #     tmp = int(math.sqrt(N))
# # # # # # # #     ans+= 'B'*(tmp-1)
# # # # # # # #     N -= 2**tmp
# # # # # # # #     ans += 'A'*N
# # # # # # # #     ans += 'B'*cnt
# # # # # # # #     print(ans)

# # # # # # # # X = input()
# # # # # # # # N = int(input())
# # # # # # # # # normal = 'abcdefghijklmnopqrstuvwxyz'
# # # # # # # # lis = list(input() for _ in range(N))
# # # # # # # # ans = [[] for _ in range(26)]
# # # # # # # # for l in lis:
# # # # # # # #     ans[X.index(l[0])].append(l)
# # # # # # # # for A in ans:
# # # # # # # #     if len(A) > 1:
# # # # # # # #         tmp = []

# # # # # # # X = input()
# # # # # # # D = dict()

# # # # # # # for i in range(26):
# # # # # # #     nxt = chr(i + ord('a'))
# # # # # # #     D[X[i]] = nxt
# # # # # # # n = int(input())
# # # # # # # ans = []
# # # # # # # for i in range(n):
# # # # # # #     S = input()
# # # # # # #     T = ""
# # # # # # #     for s in S:
# # # # # # #         T += D[s]
# # # # # # #     ans.append((T,S))
# # # # # # # ans.sort()
# # # # # # # for i in range(n):
# # # # # # #     print(ans[i][1])

# # # # # # # X = input()
# # # # # # # D = dict()
# # # # # # # for i in range(26):
# # # # # # #     tmp = chr(i+ord('a'))
# # # # # # #     D[X[i]] = tmp
# # # # # # # N = int(input())
# # # # # # # ans = []
# # # # # # # for i in range(N):
# # # # # # #     S = input()
# # # # # # #     tmp = ""
# # # # # # #     for s in S:
# # # # # # #         tmp += D[s]
# # # # # # #     ans.append((tmp,S))
# # # # # # # ans.sort()
# # # # # # # for i in range(N):
# # # # # # #     print(ans[i][1])

# # # # # # # from itertools import product
# # # # # # # N = list(input())
# # # # # # # ans = 0
# # # # # # # for i in range(len(N)-1):
# # # # # # #     bef = sorted(N[:i+1],reverse=True)
# # # # # # #     aft = sorted(N[i+1:],reverse=True)
# # # # # # #     ans = max(ans, int(''.join(bef))*int(''.join(aft)))
# # # # # # # print(ans)

# # # # # # # from itertools import product

# # # # # # # N = input()
# # # # # # # ans = 0
# # # # # # # def calc(pro):
# # # # # # #     bef = ""
# # # # # # #     aft = ""
# # # # # # #     for i in range(len(N)):
# # # # # # #         if pro[i]:
# # # # # # #             aft += N[i]
# # # # # # #         else:
# # # # # # #             bef += N[i]
# # # # # # #     if aft == "" or bef == "":
# # # # # # #         return 0
# # # # # # #     else:
# # # # # # #         return int(''.join(sorted(bef, reverse=True))) * int(''.join(sorted(aft, reverse=True)))
# # # # # # # for pro in product((0,1),repeat=len(N)):
# # # # # # #     tmp = calc(pro)
# # # # # # #     ans = max(ans,tmp)
# # # # # # # print(ans)

# # # # # # # N,M = map(int, input().split())
# # # # # # # hands = [list(input()) for _ in range(2*N)]
# # # # # # # for i in range(M):

# # # # # # N, M = map(int, input().split())
# # # # # # hands = []
# # # # # # for _ in range(2 * N):
# # # # # #     s = input()
# # # # # #     hands.append(s)

# # # # # # rank = [[0, i] for i in range(2 * N)]

# # # # # # # D[h1][h2]: じゃんけんでh1, h2を出して、h1が勝つなら1, h2が勝つなら2
# # # # # # D = {"G": {"C": 1, "P": 2},
# # # # # #     "C": {"P": 1, "G": 2},
# # # # # #     "P": {"G": 1, "C": 2}}

# # # # # # for j in range(M):
# # # # # #     for i in range(N):
# # # # # #         p1 = rank[2 * i][1]  # 2*i位の選手番号
# # # # # #         p2 = rank[2 * i + 1][1] # 2*i+1位の選手番号
# # # # # #         h1 = hands[p1][j]  # p1がjラウンド目に出す手
# # # # # #         h2 = hands[p2][j]  # p2がjラウンド目に出す手
# # # # # #         if h1 == h2:  # あいこです
# # # # # #             continue
# # # # # #         else:
# # # # # #             winner = D[h1][h2]
# # # # # #             if winner == 1:
# # # # # #                 rank[2 * i][0] -= 1  # ここで勝ったほうの勝利カウントを-1すると、ソートが楽です
# # # # # #             else:
# # # # # #                 rank[2 * i + 1][0] -= 1
# # # # # #     rank.sort()  # 勝利カウントが小さい順（＝勝利数が多い順）に並び替える、同じなら選手番号が小さい順が上
# # # # # #     print(rank)

# # # # # # for i in range(2 * N):
# # # # # #     print(rank[i][1] + 1)

# # # # # # N,M = map(int, input().split())
# # # # # # hands = [input() for _ in range(2*N)]
# # # # # # rank = [[0,i] for i in range(2*N)]
# # # # # # power = {'G':{'C':1,'P':2},
# # # # # #             'C':{'P':1,'G':2},
# # # # # #             'P':{'G':1,'C':2}}
# # # # # # for i in range(M):
# # # # # #     for j in range(N):
# # # # # #         p1 = rank[j*2][1]
# # # # # #         p2 = rank[j*2+1][1]
# # # # # #         h1 = hands[p1][i]
# # # # # #         h2 = hands[p2][i]
# # # # # #         if h1 == h2:
# # # # # #             continue
# # # # # #         else:
# # # # # #             winner = power[h1][h2]
# # # # # #             if winner == 1:
# # # # # #                 rank[j*2][0] -= 1
# # # # # #             else:
# # # # # #                 rank[j*2+1][0] -= 1
# # # # # #     rank.sort()
# # # # # # for i in range(2*N):
# # # # # #     print(rank[i][1]+1)

# # # # # # from itertools import accumulate

# # # # # # N = int(input())
# # # # # # sts = []
# # # # # # qs = []
# # # # # # dt = []
# # # # # # for i in range(N):
# # # # # #     a,b = map(int, input().split())
# # # # # #     sts.append(a)
# # # # # #     qs.append(b)
# # # # # #     dt.append(a/b)
# # # # # # Adt = list(accumulate(dt))
# # # # # # print(dt,Adt,Adt[-1]/2)

# # # # # def main():
# # # # #     N = int(input())
# # # # #     L = []
# # # # #     sec = 0
# # # # #     for _ in range(N):
# # # # #         a, b = map(int, input().split())
# # # # #         L.append((a, b))
# # # # #         sec += a / b  #この導火線全体が燃えるのに、a / b 秒かかります
# # # # #     rem = sec / 2
# # # # #     ans = 0

# # # # #     for a, b in L:
# # # # #         if rem >= a / b:  # この導火線全体が燃えるかどうか
# # # # #             ans += a  # a cm進みます
# # # # #             rem -= a / b  # a / b 秒経過しました
# # # # #         else:
# # # # #             ans += rem * b  # 1秒あたりb cm 進むので、rem * b cm 燃えたところで 全体で S / 2 秒経過します
# # # # #             break
# # # # #         print(rem,ans)
# # # # #     print(ans)


# # # # # if __name__ == '__main__':
# # # # #     main()

# # # # # N = int(input())
# # # # # Sts = []
# # # # # sec = 0
# # # # # for i in range(N):
# # # # #     a,b = map(int,input().split())
# # # # #     Sts.append((a,b))
# # # # #     sec += a/b
# # # # # rem = sec/2
# # # # # ans = 0
# # # # # for a,b in Sts:
# # # # #     if a/b <= rem:
# # # # #         ans += a
# # # # #         rem -= a/b
# # # # #     else:
# # # # #         ans += rem*b
# # # # #         break
# # # # # print(ans)

# # # # N = int(input())
# # # # points = []
# # # # for i in range(N):
# # # #     x,y = map(int,input().split())
# # # #     points.append((x,y))
# # # # ans = 0
# # # # print(points)
# # # # for i in range(N):
# # # #     for j in range(i+1,N):
# # # #         for k in range(j+1,N):
# # # #             ixjx = abs(points[i][0]-points[j][0])
# # # #             iyjy = abs(points[i][1]-points[j][1])
# # # #             ixkx = abs(points[i][0]-points[k][0])
# # # #             iyky = abs(points[i][1]-points[k][1])
# # # #             jxkx = abs(points[j][0]-points[k][0])
# # # #             jyky = abs(points[j][1]-points[k][1])
# # # #             if ixjx == ixkx == jxkx == 0:
# # # #                 continue
# # # #             elif ixjx == ixkx == 0:
# # # #                 continue
# # # #             elif ixjx == jxkx == 0:
# # # #                 continue
# # # #             elif ixkx == jxkx == 0:
# # # #                 continue
# # # #             elif ixjx == 0:
# # # #                 if (iyky//ixkx) == (jyky//jxkx):
# # # #                     continue
# # # #             elif ixkx == 0:
# # # #                 if (iyjy//ixjx) == (jyky//jxkx):
# # # #                     continue
# # # #             elif jxkx == 0:
# # # #                 if (iyjy//ixjx) == (iyky//ixkx):
# # # #                     continue
# # # #             elif (iyky//ixkx) == (jyky//jxkx) == (iyjy//ixjx):
# # # #                 continue
# # # #             else:
# # # #                 ans += 1
# # # # print(ans)

# # # # N,M = map(int, input().split())
# # # # grids = []
# # # # for i in range(N):
# # # #     B = tuple(map(int, input().split()))
# # # #     grids.append(B)
# # # # for i in range(M):
# # # #     if grids[0][i] % 7 ==0 and i != M-1:
# # # #         print("No")
# # # #         exit
# # # # prevM = grids[0][0]-1
# # # # for i in range(M):
# # # #     prev = grids[0][i]
# # # #     if prev - prevM != 1:
# # # #         print("No")
# # # #         exit()
# # # #     prevM = prev
# # # #     for j in range(1,N):
# # # #         if grids[j][i] - prev != 7:
# # # #             print("No")
# # # #             exit()
# # # #         prev = grids[j][i]
# # # # print("Yes")

# # # # from collections import deque
# # # # N = int(input())
# # # # T = []
# # # # K = []
# # # # A = []
# # # # for _ in range(N):
# # # #     t,k,*a = list(map(int, input().split()))
# # # #     T.append(t)
# # # #     K.append(k)
# # # #     A.append(a)
# # # # q = deque()
# # # # ans = T[-1]
# # # # done = [False]*N
# # # # for a in A[-1]:
# # # #     q.append(a)
# # # # while q:
# # # #     need = q.popleft()
# # # #     if done[need-1] == False:
# # # #         done[need-1] = True
# # # #         ans += T[need-1]
# # # #         for a in A[need-1]:
# # # #             q.append(a)
# # # # print(ans)

# # # # import bisect
# # # # N,Q = map(int,input().split())
# # # # A = sorted(list(map(int, input().split())))
# # # # for i in range(Q):
# # # #     x = int(input())
# # # #     print(N-bisect.bisect_left(A,x))

# # # from itertools import permutations


# # # def judge():
# # #     def is_same_shape(P):
# # #         for i in range(N):
# # #             for j in range(N):
# # #                 if AB[P[i]][P[j]] != CD[i][j]: return False
# # #         return True

# # #     N, M = map(int, input().split())
# # #     AB = [[False] * N for _ in range(N)]
# # #     CD = [[False] * N for _ in range(N)]

# # #     for _ in range(M):
# # #         a, b = map(int, input().split())
# # #         a, b = a - 1, b - 1
# # #         AB[a][b] = True
# # #         AB[b][a] = True

# # #     for _ in range(M):
# # #         c, d = map(int, input().split())
# # #         c, d = c - 1, d - 1
# # #         CD[c][d] = True
# # #         CD[d][c] = True
# # #     print(AB,CD)
# # #     for perm in permutations(range(N)):
# # #         print(perm)
# # #         if is_same_shape(perm):
# # #             return True
# # #     return False


# # # print("Yes" if judge() else "No")

# # # N,X = map(int, input().split())
# # # ans = 0
# # # nums = []
# # # for i in range(N):
# # #     l,*A = list(map(int, input().split()))
# # #     tmp = []
# # #     if i == 0:
# # #         nums.append(A)
# # #     else:
# # #         for x in nums[i-1]:
# # #             for a in A:
# # #                 tmp.append(x*a)
# # #         nums.append(tmp)
# # # print(nums[-1].count(X))

# # # s = input()
# # # la = len(s) - len(s.lstrip('a'))
# # # ra = len(s) - len(s.rstrip('a'))
# # # if la > ra:
# # #     print("No")
# # #     exit()
# # # else:
# # #     s = "a"*(ra-la)+s
# # #     if s == s[::-1]:
# # #         print("Yes")
# # #     else:
# # #         print("No")

# # # MOD = 998244353
# # # N = int(input())
# # # # leng = ("1"+"0"*(len(N)-1))
# # # # lengs = ("1"+"0"*(len(N)-2))
# # # # ans = sum(list(i for i in range(1,int(leng)-int(lengs)+1)))
# # # # tmp = 0
# # # # print(ans)
# # # # ans += sum(list(i for i in range(1,int(N)-(int(leng)-2))))
# # # # print(ans)
# # # L = len(str(N))
# # # ans = 0
# # # for i in range(1,L+1):
# # #     tmp = min(N,10**i-1) - (10**(i-1)-1)
# # #     ans += ((tmp*(tmp+1))//2)
# # #     ans %= MOD
# # # print(ans)

# # # N,X = map(int, input().split())
# # # dp = [[False]*(X+1) for _ in range(N)]
# # # a,b = map(int, input().split())
# # # if a < X+1:
# # #     dp[0][a] = True
# # # if b < X+1:
# # #     dp[0][b] = True
# # # for i in range(1,N):
# # #     a,b = map(int, input().split())
# # #     for j in range(X+1):
# # #         if dp[i-1][j]:
# # #             if j+a < X+1:
# # #                 dp[i][j+a] = True
# # #             if j+b < X+1:
# # #                 dp[i][j+b] = True
# # # if dp[-1][-1]:
# # #     print("Yes")
# # # else:
# # #     print("No")

# # # def check(i,j,y,x):
# # #     cnt = 0
# # #     for _ in range(6):
# # #         if not (0<=i<N and 0<=j<N):
# # #             return False
# # #         cnt += S[i][j]
# # #         i += y
# # #         j += x
# # #     return cnt >= 4

# # # N = int(input())
# # # S = [[1 if c == "#" else 0 for c in input()] for _ in range(N)]
# # # moves = [(1,0),(0,1),(1,-1),(1,1)]
# # # for i in range(N):
# # #     for j in range(N):
# # #         for y,x in moves:
# # #             if check(i,j,y,x):
# # #                 print("Yes")
# # #                 exit()
# # # print("No")

# # # MOD = 998244353
# # # N = int(input())
# # # dp = [[0]*(11) for i in range(N+1)]
# # # for i in range(1,10):
# # #     dp[1][i] = 1
# # # for i in range(1,N):
# # #     for j in range(1,10):
# # #         dp[i+1][j] = (dp[i][j-1]+dp[i][j]+dp[i][j+1])%MOD
# # # print(sum(dp[N])%MOD)

# # # N = int(input())
# # # X = []
# # # Y = []
# # # for i in range(N):
# # #     x,y = map(int, input().split())
# # #     X.append(x)
# # #     Y.append(y)
# # # D = input()
# # # Rmins = {}
# # # Lmaxs = {}
# # # for i,d in enumerate(D):
# # #     if d == 'R':
# # #         if Y[i] in Rmins:
# # #             Rmins[Y[i]] = min(Rmins[Y[i]],X[i])
# # #         else:
# # #             Rmins[Y[i]] = X[i]
# # #     else:
# # #         if Y[i] in Lmaxs:
# # #             Lmaxs[Y[i]] = max(Lmaxs[Y[i]],X[i])
# # #         else:
# # #             Lmaxs[Y[i]] = X[i]
# # # for key, value in Rmins.items():
# # #     if key in Lmaxs:
# # #         if value <= Lmaxs[key]:
# # #             print("Yes")
# # #             exit()
# # # print("No")

# # N,K = map(int, input().split())
# # A = list(map(int, input().split()))
# # B = list(map(int, input().split()))
# # a_ok = True
# # b_ok = True
# # for i in range(N-1):
# #     aB,aN = A[i],A[i+1]
# #     bB,bN = B[i],B[i+1]
# #     an_ok,bn_ok = False, False

# # N,K,X = map(int, input().split())
# # A = list(map(int, input().split()))
# # ans = sum(A)
# # ables = 0
# # lefts = []
# # for a in A:
# #     ables += (a//X)
# #     lefts.append(a%X)
# # lefts.sort(reverse=True)
# # ans -= X * min(ables,K)
# # K -= min(ables,K)
# # ans -= sum(lefts[:K])
# # print(ans)

# MOD = 998244353
# N,M,K = map(int, input().split())
# dp = [[0]*(K+1) for _ in range(N+1)]
# dp[0][0] = 1
# for i in range(N):
#     for j in range(K):
#         for k in range(1,M+1):
#             if j+k > K:
#                 break
#             dp[i+1][j+k] += dp[i][j]
#             dp[i+1][j+k] %= MOD
# print(sum(dp[-1])%MOD)

# from itertools import product
# from collections import Counter

# def judge(pro):
#     St = ""
#     for i in range(N):
#         if pro[i]:
#             St += S[i]
#     Cnt = Counter(St)
#     return list(Cnt.values()).count(K)

# N,K = map(int, input().split())
# S = []
# for i in range(N):
#     s = input()
#     S.append(s)
# ans = 0
# for pro in product((0,1), repeat=N):
#     ans = max(ans, judge(pro))
# print(ans)

# from collections import deque

# N,Q = map(int, input().split())
# A = list(range(N+1))
# idx = list(range(N+1))
# for i in range(Q):
#     x = int(input())
#     fi = idx[x]
#     si = fi+1 if fi != N else fi-1
#     y = A[si]
#     A[fi],A[si] = A[si],A[fi]
#     idx[x] = si
#     idx[y] = fi
# print(*A[1:])

# N = int(input())
# done = set()
# ori = {}
# T = 0
# for i in range(N):
#     s,t = input().split()
#     t = int(t)
#     if s not in done:
#         done.add(s)
#         if not t in ori:
#             ori[t] = i
# print(sorted(ori.items(), reverse=True)[0][1]+1)

N = int(input())