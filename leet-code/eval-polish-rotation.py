def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for el in tokens:  
            if el not in {"+", "-", "*", "/"}: stack.append(int(el))
            else: 
                second_el = stack.pop()
                first_el = stack.pop()

                if el == '+': stack.append(second_el + first_el)
                elif el == '-': stack.append(first_el - second_el)
                elif el == '/': stack.append(int(first_el / second_el))
                else: stack.append(first_el * second_el)
        return stack.pop()