from functools import reduce
def prime_gen():
    num = 2
    while True:
        flag = 0
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                flag = 1
                break
        if flag == 0:
            yield num
        num += 1


gen = prime_gen()
res = []
for i in range(20):
    res.append(next(gen))

res_map = list(map(lambda x: x ** 2, res))
sum_res_map = reduce(lambda a,b:a+b, res_map)
print(sum_res_map)


y = [num for num in range(30)]
print(y)

x = [i for i in range(1,200) if all(i%j != 0 for j in range(2,i))]
print(x)

z = {x:x**2 for x in range(20)}
print(z)

