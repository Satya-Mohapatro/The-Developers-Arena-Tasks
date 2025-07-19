temp = [28.5,30.3,27,8,29,31.4,30,26.7]

avg_temp = sum(temp)/len(temp)
min_temp = min(temp)
max_temp = max(temp)

print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Minimum Temperature: {min_temp:.2f}°C") 
print(f"Maximum Temperature: {max_temp:.2f}°C")