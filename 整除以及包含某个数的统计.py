# me='飞飞'
# me=input("请输入")
# print('我是{}'.format(me))
# print(type(me))
# x=1
# while x!=0:
#     x = int(input('输入行数，0退出：'))
#     for a in range(1,x+1):
#         j=x
#         while j>=a:
#             print(' ',end='')
#             j-=1
#             pass
#         k=1
#         while k<=a:
#             print('*',end='')
#             k+=1
#             pass
#         print()
#     pass
# pass
s=int(input('输入一个总数：'))
y=int(input('输入一个除数：'))
n=0
for x in range(1,s):
    if x%y==0:
        print(x,end=' ')
        n+=1
        pass
    elif str(x)[-1]==str(y):
        print(x,end=' ')
        n+=1
        pass
pass
print()
print('统计结束，总计{}个能够被{}整除以及尾数包含{}的整数'.format(n,y,y))


