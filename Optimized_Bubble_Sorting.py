arr=[1,2,3,4]
n=len(arr)
for i in range(n):
    swapped=False
    for j in range(0,n-i-1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
            swapped=True
    if not swapped:
        break
print(arr)
