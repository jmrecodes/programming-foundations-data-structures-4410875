from collections import deque

printer_queue = deque()
printer_queue.append("First to print.docx")
printer_queue.append("Second to print.pdf")
printer_queue.append("Last to print.xlxs")

while len(printer_queue) > 0:
  document = printer_queue.popleft()

  print(f'Printing {document}')
