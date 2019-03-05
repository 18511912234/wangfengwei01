a=[1,2,23]
test_a=len(a)
for i in range(test_a-1):
    for j in range(test_a-i-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

