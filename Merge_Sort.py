def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        s1=arr[:mid]
        b=arr[mid:]
        mergesort(s1)
        mergesort(b)
        i=j=k=0
        while i<len(s1) and j<len(b):
            if s1[i]<b[j]:
                arr[k]=s1[i]
                i+=1
            else:
                arr[k]=b[j]
                j+=1
            k=k+1
        while i<len(s1):
            arr[k]=s1[i]
            i+=1
            k+=1
        while j<len(b):
            arr[k]=b[j]
            j+=1
            k+=1
            
arr=[6,5,12,10,9,1]
mergesort(arr)
print(arr)
