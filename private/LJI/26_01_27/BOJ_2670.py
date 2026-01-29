
N = int(input())

lst = [float(input()) for _ in range(N)]
 
for i in range(1, N):
    lst[i] = max(lst[i], lst[i]*lst[i-1])
    # max(새로 시작, 이어서 곱하기)

# 각 위치에서 끝나는 가장 큰 연속 곱을 계속 갱신하기 때문에
# 중간에서 시작하는 최적 구간도 자동으로 잡아 냄

# 앞에서 계속 곱해봤자 손해니까 다시 시작하는게 이득이야
 
print("{:.3f}".format(max(lst)))
        
