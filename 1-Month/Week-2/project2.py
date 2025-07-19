data = [10,20,20,30,40,20,50,80,90,100]

cleaned_data = list(set(data))

filtered_data =[]
for num in cleaned_data:
    if num > 20:
        filtered_data.append(num)

print("Original Data:", data)
print("After Removing Duplicates:", cleaned_data)
print("After Filtering Values Greater Than 20:", filtered_data)