arr=[1,3,0,2]
n=len(arr)
for i in range(0,n):
    for j in range(0,n-i-1):
        if(arr[j]>arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print("Array After Sorting:",arr)
