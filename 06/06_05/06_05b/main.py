from collections import deque

def check_match_parenthesis(input):
  letters = deque(input)

  lenLetters = len(letters)
  parentheses = deque()
  
  # Extract parentheses only
  while (lenLetters - 1 >= 0):
    if (letters[-1] == ')' or letters[-1] == '('):
      parentheses.append(letters[-1])

    letters.pop()
    lenLetters -= 1
  
  lenParentheses = len(parentheses)
  matched = False # All starting was paired with closing
  startParenthesis = False # Starting is found
  numStartParenthesis = 0 # Number of starting without closing

  # Determine if all starting was paired and how many are hanging (numStartParenthesis)
  while(lenParentheses - 1 >= 0):
    if (parentheses[-1] == '('):
      # Starting is found
      numStartParenthesis += 1
      startParenthesis = True
      matched = False
    else:
      # Closing is found
      numStartParenthesis -= 1

    if (parentheses[-1] == ')' and startParenthesis == True):
      # starting and closing is found
      matched = True
      startParenthesis = False

    parentheses.pop()
    lenParentheses -= 1

  # Returns true only when all starting are paired with closing and no hanging was found
  return (matched and numStartParenthesis == 0)

test_cases = [
    "()",            # Basic match
    "()ok",          # Match with extra text
    "(hello)",       # Match with text inside
    "((()))",        # Nested parentheses
    "(())",          # Nested match
    ")(",            # Reversed, unmatched
    "(()",           # Unbalanced - extra opening
    "())",           # Unbalanced - extra closing
    "(()())",        # Multiple nested matches
    "",              # Empty string
    "no parentheses" # No parentheses
]

for case in test_cases:
    print(f"Testing: {case}")
    print(check_match_parenthesis(case))