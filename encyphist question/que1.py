def reverse_stack(stack):
    if not stack:
        return

    # Step 1: Pop the top element
    top = stack.pop()
    
    # Step 2: Reverse the remaining stack
    reverse_stack(stack)
    
    # Step 3: Insert the popped element at the bottom of the reversed stack
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    
    # Step 1: Pop the top element
    top = stack.pop()
    
    # Step 2: Insert the item at the bottom
    insert_at_bottom(stack, item)
    
    # Step 3: Push the popped element back onto the stack
    stack.append(top)

# Example usage
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  # Output: [5, 4, 3, 2, 1]
