from collections import deque

def check_match_parenthesis(input):
  letters = deque(input)

  lenLetters = len(letters)
  parentheses = deque()
  while (lenLetters - 1 >= 0):
    if (letters[-1] == ')' or letters[-1] == '('):
      parentheses.append(letters[-1])

    letters.pop()
    lenLetters -= 1
  
  lenParentheses = len(parentheses)
  matched = False
  startParenthesis = False
  numStartParenthesis = 0
  while(lenParentheses - 1 >= 0):
    if (parentheses[-1] == '('):
      numStartParenthesis += 1
      startParenthesis = True
      matched = False
    else:
      numStartParenthesis -= 1

    if (parentheses[-1] == ')' and startParenthesis == True):
      matched = True
      startParenthesis = False

    parentheses.pop()
    lenParentheses -= 1

  return (matched and numStartParenthesis == 0)

if check_match_parenthesis(")asd("):
  print("Matched!")
else:
  print("Not matched")