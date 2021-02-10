import math
a=int(input('Enter the amount of rows :'))
b=int(input('Enter the amount of columns :'))
c=list(map(int,input('Coordinates of a point through which no path passes\nWrite columns and rows in order and separate them with space(columns rows) :').split(' ')))
#All routes
x=(math.factorial(a+b))/(math.factorial(a)*math.factorial(b))
#All paths that pass through the desired point
y=(math.factorial(c[0]+c[1]))/(math.factorial(c[1])*math.factorial(c[0]))
z=(math.factorial((b-c[0])+(a-c[1])))/(math.factorial(b-c[0])*math.factorial(a-c[1]))
#All routes that do not cross the desired point
print('All routes that do not cross the desired point are equal to %i'%int((x-(y*z))))