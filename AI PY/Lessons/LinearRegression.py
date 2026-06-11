x = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
y = [9000, 9200, 9300, 10000, 14300, 15000, 15400, 18000, 18700, 19000, 20000]
valX = 5
valY = 31000

xMean = sum(x)/len(x)
yMean = sum(y)/len(y)

devX = [i - xMean for i in x]
devY = [i - yMean for i in y]
devX2 = [i**2 for i in devX]
devXY = [devX[i] * devY[i] for i in range(len(devX))]

m = sum(devXY) / sum(devX2)
b = yMean - m * xMean
r = m * valX + b

x.append(valX)
y.append(valY)

percentError = [abs((y[i] - (m * x[i] + b)) / y[i]) * 100 for i in range(len(x))]
accuracy = 100 - sum(percentError) / len(percentError)

print("==========================================================================")
print(f"The predicted value for y is: {r:.2f}")
print(f"The model is off by {valY - r:.2f} from the actual value of {valY}.")
print(f"The accuracy of the model is: {accuracy:.2f}%")
print("==========================================================================")