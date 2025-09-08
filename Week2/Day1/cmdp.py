'''
5. `sys` → Sum from Command Line
Write a program using `sys.argv` to take three numbers from the command line and print their sum.
Sample Input (command line): 
python add.py 5 10 15

Sample Output:
Sum = 30
'''

import sys
s=0
for i in range(1,len(sys.argv)):
    s+=int(sys.argv[i])
print("Sum: ",s)