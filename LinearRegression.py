#Define a fucntion for linear regression
def linear_regression(x,y):
  n = len(x)
  x_sum = sum(x)
  y_sum = sum(y)
  xy_sum = sum([xi*yi for xi,yi in zip(x,y)])
  x_squared_sum = sum([xi**2 for xi in x])

  #Calculate b1(or slope) and b0(or intercept) using the mathematical formulae
  b1 = (n*xy_sum - x_sum*y_sum)/(n*x_squared_sum - x_sum**2)
  b0 = (y_sum-b1*x_sum)/n

  return b1, b0

#driver
x = [5,6,8,10]
y = [11,11,15,24]

b1, b0 = linear_regression(x,y)

print("Slope",b1)
print("Intercept",b0)
