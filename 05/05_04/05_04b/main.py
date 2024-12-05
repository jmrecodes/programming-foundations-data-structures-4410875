from collections import deque
import math

def print_queue(q):
  while (len(q) > 0):
    curr = q.popleft()
    print(curr)

def num_to_binary(num):
  binary_digit = [0]
  while (num > 0):
    # If last digit is 0, simply set it to 1
    if (binary_digit[len(binary_digit) - 1] == 0):
      binary_digit[len(binary_digit) - 1] = 1
    else:
      # Complex carry-over mechanism
      bd_len = len(binary_digit) - 1
      need_to_add = True

      # Traverse digits from right to left
      while (bd_len > 0) and need_to_add:
        if (binary_digit[bd_len] == 1):
          # If digit is 1, set to 0 and continue

          binary_digit[bd_len] = 0
        else:
          # If digit is 0, set to 1 and stop carry-over

          binary_digit[bd_len] = 1
          need_to_add = False

        bd_len -= 1
      
      # If need to add new digit
      if (need_to_add):
        binary_digit.append(0)

    num -= 1

  return binary_digit
    

def decimal_binary_all_below(num):
  binaries = deque()

  start = 1

  # Traverse from 1 up to the input number
  while (start <= num):
    binaries.append(num_to_binary(start))

    start = start + 1
  
  print_queue(binaries)

# Print from 1 to 14 all of its binary representations
decimal_binary_all_below(14)
