

# 位运算
# 分糖果

def main():
    x = int(input())
    count = 0
    while x != 1:
        if x ==3:
            count +=2
            break
        if x % 2 != 0 :
            if (x+1) //2 %2 == 0:
                x += 1
            else:
                x -= 1
            #     拿出一颗糖果或者放回一颗糖果
            count += 1
        # 模拟分糖果的操作
        x //= 2
        count +=1
    print(count)

main()