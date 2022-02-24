#    ______                 __
#   / ____/________ _____  / /_  ___  _____     Version: Alpha 0.0.1
#  / / __/ ___/ __ `/ __ \/ __ \/ _ \/ ___/              Tested on Python 3.9
# / /_/ / /  / /_/ / /_/ / / / /  __/ /                  2022 Release
# \____/_/   \__,_/ .___/_/ /_/\___/_/
#               /_/                              Author: wiseolde
#       BASIC UNICODE GRAPHING TOOL
#
# Initialized Variables --------------------------------------------------------
xy =         {}  # Dictionary with x-values as the keys for y-values.
x =          []  # List containing all x-values.
y =          []  # List containing all y-values.
z =          0   # The counter for appending x-values.
negCount =   0   # The counter for graphing negative expressions.
xAxis =      []  # The list holding the values (labels) of the x-axis.
yAxis =      []  # The list holding the values (labels) of the y-axis.
scaleCount = 0   # The counter used for finding the scale values of the axes.

# Defined Functions ------------------------------------------------------------

# A help function that can be run in the interpreter for assistance to the user.
def help():
    print("Help Page:\n\tInput\n\t\texpression: Must contain the letter 'x' written in the format of y=\n\t\taxScale: Must be an integer value in between 5 and 100.\n\t\taxSize: Must be an integer between 5 and 100.\n\t\txyChoice: Must be a string, 'y' for yes, anything else for no.")
# This is a security fuction that protects eval() from running malicious code.
def evalExpr(exprSub):
    import string #  <--  local import
    for char in exprSub:
        if char not in "+-*/() " + string.digits:
            print("\nInputError: Please use only mathematical operators '+-*/() ' in your expression.")
            raise SystemExit
        else:
            return eval(exprSub)
# Checks if character 'x' was input in the expression and warns the user if not.
def xCheck(expression):
    for var in expression:
        if 'x' not in expression:
            print("\nInputError: Please use the variable(s) 'x' in your expression.")
            raise SystemExit
# Fills in whitespaces on the y-axis depending on the given scale.
def yAxisFill(yAxis):
    for num in range (1, axScale):
        yAxis.append(" ")

# Logo -------------------------------------------------------------------------

grapher = ("   ______                 __\n  / ____/________ _____  / /_  ___  _____\n / / __/ ___/ __ `/ __ \/ __ \/ _ \/ ___/\n/ /_/ / /  / /_/ / /_/ / / / /  __/ /\n\____/_/   \__,_/ .___/_/ /_/\___/_/\n               /_/\n")
print(grapher)

# Program Assistance -----------------------------------------------------------

print("Information")
print("\t- Please use the variable(s) 'x' in your expression to get a desired result.")
print("\t- Do not place a coefficent next to a variable, instead use '*' to indicate multiplication.")
print("\t- Do not use brackets next to numbers, variables or other brackets, instead use '*' to indicate multiplication.")
print("\t- Using characters other than mathematical operators will result in an error.\n")

print("For additional information and/or assistance, enter 'help()'.\n")

# Input Variables --------------------------------------------------------------

expression = str(input("Enter the expression to be graphed. y="))
xCheck(expression)  # checks for 'x'

axScale = int(input("Enter the scale of units on the axis. (5 is recommended): "))
if axScale > 100:   # max. input value
    axScale = 5     # default value
    print("WARNING: Input axis scale too large; reset to 5. (default)")
elif axScale < 5:   # min. input value
    axScale = 5     # default value
    print("WARNING: Input axis scale too small; reset to 5. (default)")

axSize = int(input("Enter the size of the graph. (50 is recommended): "))
if axSize > 100:    # max. input value
    axSize = 50     # default value
    print("WARNING: Input axis size is too large; reset to 50. (default)")
elif axSize < 5:    # min. input value
    axSize = 50     # default value
    print("WARNING: Input axis size is too small; reset to 50. (default)")

# Points Calculator ------------------------------------------------------------

for points in range(0, axSize):
    z += 1
    exprSub = expression.replace('x', "{0}".format(z))  # replaces 'x' with the value of 'z'
    y.append(evalExpr(exprSub))                         # evaluates and appends expression in list
    x.append(z)                                         # appends the values of 'z' in the list 'x'
    xy["{0}".format(z)] = evalExpr(exprSub)             # evaluates and appends both x and y-values
tuple(x)
tuple(y)    # converts lists to tuples to prevent changes

# Axis Modification ------------------------------------------------------------

while scaleCount < axSize:
    scaleCount += axScale
    xAxis.append(' '*(axScale*2-4))                     # appends whitespaces to 'xAxis'
    xAxis.append(scaleCount)                            # appends the values from 'scaleCount' every 'axScale'
    xAxisT = (' '*(axScale*2-1)+"|")*int(axSize/axScale)# appends incremented lines to 'xAxisT' (top part)
    yAxisFill(yAxis)                                    # function appends whitespaces to 'yAxis' 4 times
    yAxis.append(scaleCount)                            # appends the values from 'scaleCount'

xAxis = str(xAxis)          # converts xAxis to string
xAxis = xAxis.replace("''",'')  # -
xAxis = xAxis.replace("'",'')   # - -
xAxis = xAxis.replace('[','')   # - - > replaces list symbols after string conversion
xAxis = xAxis.replace(',','')   # - -
xAxis = xAxis.replace(']','')   # -

# Graphing Output --------------------------------------------------------------

graphTitle = 'Graph of y='
print("\n"+(axSize)*" "+"%s%2s"%(graphTitle, expression))    # graph title
while 1 <= z:
    z -= 1                  # counts from # to 1
    negCount -= 1           # counts from 0 to -#
    lineSp = (y[z] / x[z])  # finds line spaces
    if z == (axSize-1):
        print("  y\n\t⯅"+"  "*axSize+"🡭")      # graph header
    if (z/lineSp) > (axSize):
        print(str(yAxis[negCount])+"\t|")        # prevents positive lines from over-drawing
    elif lineSp > 0:
        print(str(yAxis[negCount])+"\t|"+"  "*int(z/lineSp)+"■")            # plots points for positive x coefficients
    elif lineSp <= 0 and (z/lineSp) <= (-axSize):
        print(str(yAxis[negCount])+"\t|"+"  "*int(negCount/lineSp)+"■")     # plots points for negative x coefficients
    else:
        print(str(yAxis[negCount])+"\t|")        # skips points for any other unknown reason
    if z == (axSize-axSize):
        print("\t|"+"__"*axSize+"⯈")    #
        print("\t"+xAxisT+"\tx")         #   - >   graph footer
        print("0\t  "+xAxis+"\n")        #

xyChoice = input("Do you wish to output the coordinates of the plotted points? (y/n): \n")
if xyChoice == 'y':                      # export points from the user's decision
    print("Point Coordinates:\n"+str(xy))
#-------------------------------------------------------------------------------










