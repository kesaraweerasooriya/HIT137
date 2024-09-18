global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers):
    local_variable = 5  # No need for the global variable here
    numbers = [1, 2, 3, 4, 5]  # Resetting the list

    while local_variable > 0:
        if local_variable % 2 == 0:  # Remove even numbers from the list
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers  # Return the updated list

my_set = {1, 2, 3, 4, 5}  # Set automatically removes duplicates
result = process_numbers(numbers=my_set)

def modify_dict():
    local_variable = 10  # Using a local variable here
    my_dict['key4'] = local_variable  # Adding a new key-value pair to the dictionary

modify_dict()  # Update the dictionary with the new key-value pair

def update_global():
    global global_variable  # Accessing the global variable to modify it
    global_variable += 10  # Increment the global variable by 10

update_global()  # Call the function to apply the global change

for i in range(5):
    i = i + 1  # Increment i first, then print it
    print(i)  # Output the current value of i

# Check if the set exists and the value of 'key4' in the dictionary is 10
if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")  # This message confirms the condition is satisfied

# Check if 5 is not part of the dictionary values
if 5 not in my_dict.values():  # Adding .values() ensures we're checking the values, not keys
    print("5 not found in the dictionary")  # Letting the user know 5 isn't in the dictionary

# Output the final results
print(global_variable)  
print(my_dict)  
print(my_set)  
