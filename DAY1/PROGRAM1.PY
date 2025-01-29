arr1=[12,34,56,77,8875,43,22,4,7,8]
int_min=arr1[0]
int_max=arr1[0]
for i in range(1,len(arr1)):
    if arr1[i]>int_max:
        int_max=arr1[i]
    if arr1[i]<int_min:
        int_min=arr1[i]
        
print(f"minimum is {int_min}")
print(f"maximum is {int_max}")
    