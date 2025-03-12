# python (continue statements) 
# Program to skip the current iteration using continue statements


# Loop through numbers from 0 to 9
for i in range(10):
    # Check if the current number is even
    if i % 2 == 0:
        # Skip the current iteration if the number is even
        continue

    # Print the current number (only odd numbers will be printed)
    print(i)

print("Loop completed.")


