from collections import deque
import math

def print_queue(q):
  while (len(q) > 0):
    curr = q.popleft()
    print(curr)

def num_to_binary(num):
  binary_digit = [0]
  while (num > 0):
    if (binary_digit[len(binary_digit) - 1] == 0):
      binary_digit[len(binary_digit) - 1] = 1
    else:
      bd_len = len(binary_digit) - 1
      
      need_to_add = True
      while (bd_len > 0) and need_to_add:
        if (binary_digit[bd_len] == 1):
          binary_digit[bd_len] = 0
        else:
          binary_digit[bd_len] = 1
          need_to_add = False

        bd_len -= 1
      
      if (need_to_add):
        binary_digit.append(0)

    num -= 1

  return binary_digit
    

def decimal_binary_all_below(num):
  binaries = deque()
  start = 1
  while (start <= num):
    binaries.append(num_to_binary(start))

    start = start + 1
  
  print_queue(binaries)

decimal_binary_all_below(14)
