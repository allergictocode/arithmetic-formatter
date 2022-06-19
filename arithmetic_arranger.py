def arithmetic_arranger(problems, solve = False):

    # variables
    start = True
    width = "    "
    top_line = bottom_line = dashes = solution_line = ''
    
    # rule 1
    if len(problems) > 5:
      return "Error: Too many problems."
      
    # start for loop
    for operation in problems:
      operand = operation.split()
      first = operand[0]
      op = operand[1]
      second = operand[2]

    # rule 3
      try:
        int(first)
        int(second)
      except ValueError:
        return "Error: Numbers must only contain digits."
        
    # rule 4
      if len(first) > 4 or len(second) > 4:
        return "Error: Numbers cannot be more than four digits."
        
    # rule 2
      if op == "+":
        result = str(int(first) + int(second))
      elif op == "-":
        result = str(int(first) - int(second))
      else:
        return "Error: Operator must be '+' or '-'."
    
     
    # output
      length = max(len(first), len(second)) + 2

      if start == True:
        top_line += first.rjust(length)
        bottom_line += op + second.rjust(length - 1)
        dashes += '-' * length
        if solve == True:
          solution_line += result.rjust(length)
        start = False
      else:
        top_line += first.rjust(length + 4)
        bottom_line += op.rjust(5) + second.rjust(length - 1)
        dashes += width + '-' * length
        if solve == True:
          solution_line += width + result.rjust(length)

    if solve == True:
      return top_line + '\n' + bottom_line + '\n' + dashes + '\n' + solution_line
    return top_line + '\n' + bottom_line + '\n' + dashes
