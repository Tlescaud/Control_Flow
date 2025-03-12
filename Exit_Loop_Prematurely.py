# exits loop early using a break statement
# loop exits when a specific condition is met
# algorithms


# Program to exit a loop prematurely when a condition is met

# Define the condition to exit the loop

exit_condition = 56

# Loop through numbers from 0 to 100
for i in range(100):
    # Print the current number
    print(i)

    # Check if the current number meets the exit condition
    if i == exit_condition:
        print("Exit condition met. Breaking the loop.")
        break

print("Loop exited.")
