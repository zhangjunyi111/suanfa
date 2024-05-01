x = [90, 80, 70]
y = ['Ale', 'bob', 'linda']
z = {}
# breakpoint()
for i in range(len(x)):
    z[i] = list(zip(x, y))
print(z)

with open('a.txt', 'r') as f:
    ss = f.read()

ls = ss.split(',')
print(len(ls), ls)
result = []

if result is None:
    print('success')

indx_num = 0

indx_num += 1
"""Today is a nice day.
I think 123 is a lucky number.
"""