arr=[1,4,56,78] 
t=int(input())
flag=False 
low=0 
high=len(arr)-1 
while low<=high:
    mid=(low+high)>>1

    if(arr[mid]==t):
        print(mid)
        flag=True 
        break
    elif arr[mid]<t:
        low=mid+1 
    elif arr[mid]>t:
        high=mid-1 
if flag==False:
    print("Target Not Found")