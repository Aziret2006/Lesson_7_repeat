user_data = input("Enter any data: ")
lengths = len(user_data)

print(f"Your data length is {lengths}")

for i in user_data:
    print(i)

print('--'*20)
count = 0
while count < lengths:
    print(user_data[count])
    count += 1
