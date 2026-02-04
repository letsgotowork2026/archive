# n = int(input())

# list_ = []
# for i in range(n):
#     list_.append(float(input()))

# max_ = max(list_)

# list__ = []
# for i in range(len(list_)-1):
#     temp = float(list_[i] * list_[i+1])
#     list__.append(temp)
#     if temp > max_:
#         max_ = temp

# for i in range(3, n):
#     if i % 2 == 1:
#         for k in range(n-i):
#             temp = list__[k] * list_[k+2]
#             if temp > max_:
#                 max_ = temp
#     else :
#         for k in range (len(list__) - i//2):
#             temp = list__[k] * list__[k+1]
#             if temp > max_:
#                 max_ = temp
        

# print("%.3f"%max_)

n=int(input())
data=[]
dp=[]
for i in range(n):
    data.append(float(input()))
    if i==0:
        dp.append(data[0])
    else:
        dp.append(max(dp[i-1]*data[i], data[i]))
print('%.3f' % max(dp))