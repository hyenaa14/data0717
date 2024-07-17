num=[1,2,3,4,5]
def mean_list(x):
    result = 0
    for i in num:
        result = result + i
    avg = result / len(x)
    return avg


num=list(range(2,3))
print(mean_list(num))
result=0
for i in num:
    result=result+i
avg=print(result/len(num))

