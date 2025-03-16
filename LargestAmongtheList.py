# Find the largest no in the array without using sort()

arr=[32,4,67,34,45,23,2,7]
arrlength=len(arr)
for i in range(0,arrlength):
    for j in range(0,arrlength):
        if i==0:
            continue
        if arr[i]>arr[j]:
            continue
        else:
            arr[i]=arr[j]
#  Now the List sorted in ascending order without using sort()
largest=arr[arrlength-1]
print(largest)
