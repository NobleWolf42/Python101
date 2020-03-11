seconds = int(input("Please enter seconds: "))
print("Seconds:", seconds)
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print(hours, "hr", minutes, "min", seconds, "sec")

print("Hello", "world", sep=":")

