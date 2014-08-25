def reverse(string):
    left_ptr = 0
    right_ptr = len(string) - 1
    while left_ptr < right_ptr:
        # swap
        temp = string[left_ptr]
        string[left_ptr] = string[right_ptr]
        string[right_ptr] = temp
        
        # step towards middle
        left_ptr += 1
        right_ptr -= 1
    print string

reverse(['a', 'b', 'c', 'd'])