

# 位运算
# 分糖果

def main():
    x = int(input())
    count = 0
    while x != 1:
        if x % 2 != 0 :
            if (x+1) //2 %2 == 0:
                x = x//4
                count += 1

            else:
                x = x %2
                count += 1
