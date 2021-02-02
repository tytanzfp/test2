# 猜3次，如果3次都错误，询问用户是否继续，输入y继续，输入n退出。
import random   # 使用随机数必须先导入
pwd = random.randint(1, 50)
flag = 'y'
while flag == 'y':
    for i in range(3):
        x = int(input('猜猜我多大了？(1~50)'))
        if x == pwd:
            print('恭喜你，猜对了！')
            flag = 'n'
            break
        elif x < pwd:
            print('猜小了,你还有%d次机会' % (2-i))
        else:
            print('猜大了,你还有%d次机会' % (2-i))
        pass
    else:
        if i == 2:
            print('尝试次数已用尽，还继续玩吗？y继续，n退出：')
            flag = input()
            pass
        pass
    pass
