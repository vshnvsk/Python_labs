#!/usr/bin/env python3
import cgi
import cgitb
import math

cgitb.enable()

form = cgi.FieldStorage()
num1 = form.getvalue("num1")
num2 = form.getvalue("num2")
k1 = form.getvalue("k1")
b1 = form.getvalue("b1")
k2 = form.getvalue("k2")
b2 = form.getvalue("b2")


# Task 1
try:
    if num1 is not None and num2 is not None:
        num1 = float(num1)
        num2 = float(num2)
        if num1 > num2:
            division_result = num1 / num2
        else:
            division_result = num2 / num1
except ValueError:
    division_result = "Invalid value"


# Task 2
try:
    if k1 is not None and k2 is not None:
        k1 = float(k1)
        k2 = float(k2)
        if k1 != k2:
            tan_theta = abs((k2 - k1) / (1 + k1 * k2))
            angle = math.degrees(math.atan(tan_theta))
        else:
            angle = 0
except ValueError:
    division_result = "Invalid value"


print("Content-type: text/html\n")
print("<html><body>")
print(f"<h1>Results</h1>")
print(f"<p>Dividing a larger number by a smaller one: {division_result}</p>")
print(f"<p>The angle between the lines: {angle:.2f} degrees</p>")
print("</body></html>")

# python3 -m http.server --cgi 8000
# http://localhost:8000/html/index.html