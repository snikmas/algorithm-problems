def dailyTemperatures(temperatures: list[int]) -> list[int]:
    pass
    output = [0] * len(temperatures)
    stack = [] # pair: index, value
    for index, value in enumerate(temperatures):
        while stack and value > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            output[stackIndex] = (index - stackIndex)
        stack.append([value, index])
    return output



temperatures = [30,38,30,36,35,40,28]
print(dailyTemperatures(temperatures))
# Output: [1,4,1,2,1,0,0]

temperatures = [22,21,20]
print(dailyTemperatures(temperatures))

# Output: [0,0,0]