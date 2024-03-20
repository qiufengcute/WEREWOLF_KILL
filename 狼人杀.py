import random

y = ['女巫','平民','狼人','狼人','猎人','平民','平民','平民']
e = 1
x = []
xe = [0,0,0,0,0,0,0,0] # 0=活,1=死
exe = xe
for i in range(7):
    z = random.randint(1,len(y))
    x.append(y[z - 1])
    y.pop(z - 1)
my = y[0]
print(y,x,my,sep=',')

def bie():
    global x,xe,e,exe
    if xe[e - 1] == 0:
        if x[e] == '狼人':
            a = random.randint(1,sum(1 for i in xe if i == 0))
            xe[a - 1] = 1
        elif x[e] == '女巫':
            if exe != xe and random.randint(1,2) == 1:
                diff = [i for i, x in enumerate(xe) if x not in exe]
                xe[diff] = 0
            if random.randint(1,2) == 1:
                while True:
                    ee = random.randint(1,len(xe))
                    if xe[ee] != 1:
                        break
                xe[ee] = 1
        elif x[e] == '猎人':
            b = random.randint(1,sum(1 for i in xe if i == 0))
            for index, player in enumerate(x):
                if player == '猎人':
                    if xe[index] == 1:
                        xe[b - 1] = 1

def player():
    global x,xe,e,exe
    if xe[0] == 0:
        if x[e] == '狼人':
            a = int(input('请输入要杀死的玩家序号(目前有',sum(1 for i in xe if i == 0),'人活着)：'))
            counter = 0
            for inde, item in enumerate(xe):
                if item == '0':
                    counter += 1
                    if counter == a:
                        break
            xe[inde] = 1
        elif x[e] == '女巫':
            if exe != xe:
                pd = input('今晚有人死了，你要救吗(y/n)')
                if pd == 'y':
                    diff = [i for i, x in enumerate(xe) if x not in exe]
                    xe[diff] = 0
            ppd = input('你要用毒药吗(y/n)')
            if ppd == 'y':
                ee = int(input('你要毒谁'))
                counter = 0
                for ind, item in enumerate(xe):
                    if item == '0':
                        counter += 1
                        if counter == ee:
                            break
                xe[ind] = 1
        elif x[e] == '猎人':
            b = int('如果今晚你死了，你要杀谁')
            for index, player in enumerate(x):
                if player == '猎人':
                    if xe[index] == 1:
                        counter = 0
                        for ix, item in enumerate(xe):
                            if item == '0':
                                counter += 1
                                if counter == a:
                                    break
                        xe[ix] = 1
    else:
        print('你死了，无法执行操作！')

def look():
    global x,xe
    counter = 0
    for pp, item in enumerate(x):
        if item == '狼人':
            counter += 1
            if counter == 1:
                break
    counter = 0
    for p, item in enumerate(x):
        if item == '狼人':
            counter += 1
            if counter == 2:
                break
    if xe[p] == 1 and xe[pp] == 1:
        input('好人胜利！')
        exit()
    for i in range(len(xe)):
        if i == p or i == pp:
            continue
        if xe[i] == 0:
            return False
    input('坏人胜利！')
    exit()

while True:
    if e == 1:
        player()
    else:
        bie()
    if e == 8:
        e = 1
    else:
        e += 1
    look()