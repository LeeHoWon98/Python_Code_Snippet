n_li = [1, 2, 3, 4, 5]

result = [0] * (len(n_li)+1)

for i in range(len(n_li)):
    result[i + 1] = result[i] + n_li[i]

print(result)