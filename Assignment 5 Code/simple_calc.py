
"""
--------------------------------------------------------------------------
Simple Calculator
--------------------------------------------------------------------------
License:   
Copyright 2019 Teddy Hoisington

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Simple calculator that will do +, -, *, /, pow, mod, left shift, and right shift

  - Take in two numbers
  - Take in an operator
  - Perform calculation and output result
  - Repeat

Error conditions:
  - Invalid calculation
  - Invalid number
  - Invalid operator

  --> Results in program exit

--------------------------------------------------------------------------
"""
import sys
import operator

#cross Python 2 and 3 functionality


# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------
operators = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv,
    "l" : operator.lshift,
    "r" : operator.rshift,
    "e" : operator.pow,
    "m" : operator.mod
    
    
}

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

def get_user_input():
    """ Will return (number, number, operator) or (None, None, None) on error"""
    
    
    try:
        #checking whether running python 2.X or 3.X
        if sys.version_info[0] < 3:
            number1 = float(raw_input("Enter the first number:  "))
            number2 = float(raw_input("Enter the second number: "))
            op      = raw_input("Enter an operator (valid operators are +, -, *, /, l, r, e, and m): ")
        else:
            number1 = float(input("Enter the first number:  "))
            number2 = float(input("Enter the second number: "))
            op      = input("Enter an operator (valid operators are +, -, *, /, l, r, e, and m): ")
        
        return (number1, number2, op)
       
    except Exception as e: 
        print(e)
        print("Invalid Input!")
        return (None, None, None)

# End def

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == "__main__":
    while True:
        (number1, number2, op) = get_user_input()

        func = operators.get(op,None)
        
        if (number1 is None) or (number2 is None) or (func is None):
            print("Program Exiting")
            break
        else:
            #left shift and right shift operators don't work for floats
            if op == "r" or op == "l":
                number1 = int(number1)
                number2 = int(number2)
            print(func(number1, number2))
