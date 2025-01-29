arr1=[10,89,9,56,4,80,8]
int_min=arr1[0]
int_max=arr1[0]
for i in range(1,len(arr1)):
    if arr1[i]>int_max:
        int_max=arr1[i]
    if arr1[i]<int_min:
        int_min=arr1[i]
        

second_min=arr1[0]
second_max=arr1[0]
for i in range(1,len(arr1)):
    if arr1[i]!=int_max:
        if arr1[i]>second_max:
            second_max=arr1[i]
    
    if arr1[i]!=int_min:
        if arr1[i]<second_min:
            second_min=arr1[i]
    

print(f"second minimum is {second_min}")
print(f"second maximum is {second_max}")
    
    
