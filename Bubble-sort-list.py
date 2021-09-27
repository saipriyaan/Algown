numbers = [int(n) for n in input('Enter numbers: ').split()]


print("Before Sorting:",*numbers)

print("________________________________________________")


for i in range(len(numbers)-1):
    if(numbers[i]<numbers[i+1]):
        print("The value is correct")
    
    elif(numbers[i]>numbers[i+1]):
        stemp=numbers[i]
        numbers[i]=numbers[i+1]
        numbers[i+1]=stemp
        print("The value is corrected!")
    
print("After Sorting:",numbers)
print("Length of numbers:",len(numbers))




        