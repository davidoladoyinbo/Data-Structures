# python program that performs the operation of a queue
```python
# Creating an empty queue
queue = []

# Adding items to the queue
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

# Display the queue
print("My Queue:", queue)

# Enqueue (Adding an item)
queue.append(60)
print("After Enqueue:", queue)

# Dequeue (Removing the first item)
queue.pop(0)th
print("After Dequeue:", queue)

# Peek (Showing the first item)
print("First Item:", queue[0])

# Rear (Showing the last item)
print("Last Item:", queue[-1])

# Checking if the queue is empty
if len(queue) == 0:
    print("Queue is Empty")
else:
    print("Queue is Not Empty")

# Checking the size of the queue
print("Queue Size:", len(queue))

# Checking if the queue is full
if len(queue) == 6:
    print("Queue is Full")
else:
    print("Queue is Not Full")

# Display all items
print("Final Queue:", queue)
```

#Explanation
- queue = [] creates an empty queue.
- append() adds a new item to the queue.
- pop(0) removes the first item from the queue.
- queue[0] shows the first item.
- queue[-1] shows the last item.
- len(queue) counts the items in the queue.
- if len(queue) == 0 checks if the queue is empty
