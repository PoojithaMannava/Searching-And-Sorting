arr=[1,3,456,67]
t=int(input())
flag=False
for i in range(0,len(arr)):
    if arr[i]==t:
        flag=True
        print("Target Found At Index:",i)
        
if flag==False:
    print("Target Not Found")
