# Creating a stack using an array

stack = ["David", "John", "Mary", "Peter", "Grace"]

print("My Initial Stack:")
print(stack)


# 1. PUSH OPERATION
# Adding a new name to the stack

stack.append("Sarah")

print("After Push Operation:")
print(stack)


# 2. POP OPERATION
# Removing the last name from the stack

stack.pop()

print("After Pop Operation:")
print(stack)


# 3. PEEK OPERATION
# Checking the last name in the stack

print("Top Element is:")
print(stack[-1])


# 4. DISPLAY OPERATION
# Showing all the names in the stack

print("All Elements in Stack:")
print(stack)


# 5. SIZE OPERATION
# Counting the number of names

print("Total Number of Students:")
print(len(stack))


# 6. EMPTY OPERATION
# Checking if the stack is empty

print("Is the Stack Empty?")
print(len(stack) == 0)

# Expected Output:

My Initial Stack:
['David', 'John', 'Mary', 'Peter', 'Grace']

After Push Operation:
['David', 'John', 'Mary', 'Peter', 'Grace', 'Sarah']

After Pop Operation:
['David', 'John', 'Mary', 'Peter', 'Grace']

Top Element is:
Grace

All Elements in Stack:
['David', 'John', 'Mary', 'Peter', 'Grace']

Total Number of Students:
5

Is the Stack Empty?
False

# Explanation of the Operations:
# 1. Push: This means ad:ding a new item to the stack. In my program, I added Sarah to the list.
# 2. Pop: This means removing the last item added to the stack. In my program, Sarah was removed.
#3. Peek: This means checking the last item without removing it. In my program, Grace is the top element.
#4. Display: This means showing all the items inside the stack.
#5. Size: This means counting the number of items in the stack. My stack contains five students.
#6. Empty: This checks if the stack has anything inside it. My answer is False because the stack still contains five names.
