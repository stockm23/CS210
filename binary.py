"""
Name: Matt Stock
File: binary.py
Project1

first zero means it's positive

a) 01101100 = 0 + 0 + 4 + 8 + 0 + 32 + 64 = 108

b) 01101100 = 4 + 8 + 32 + 64 = 108

c) same as a): 01101100 = 108


2.

a) TC 11001101 = - 00110011 = -(1 + 2 + 16 + 32) = -51 
first 1 means it's negative

b) 11001101 = -(1 + 4 + 8 + 64) = -77

c) 11001101 = 1 + 0 + 4 + 8 + 0 + 0+ 64 + 128 = 205

3.

a) 56 = 32 + 16 + 8 = 00111000

b) -43 = -(32 + 0 + 8 + 0 + 2 + 1) = TC of 00101011 = 11010101

c) - 1 = - (1) = TC of 00000001 = 11111111

4.

a) 56/16 = 3 R: 8
    3/16 = 0 R: 3

    56(dec) = 38(hex)

b) 438/16 = 27 R: 6
    27/16 = 1  R: 11 
    1/16  = 0  R: 1

    438(dec) = 1B6(hex)

c)  11010111(dec) = D7(hex)

    1: 13 = D
    2: 7


Functions for decimal/binary conversions.
"""

                     
   

def invert(bitString):
   """Returns the bit string with the bits inverted."""
   invertedString = ''
   for bit in bitString:
      if bit == '1':
         invertedString += '0'
      else:
         invertedString += '1'
   return invertedString


def unsignedDecimalToBinary(dec):
   """Takes an unsigned decimal as argument (int) and returns the binary equivalent of it in string form."""

   result = ""
   inverse = ""

   if dec == 0:
      return "0"

   while dec >= 1:
      inverse += str(dec % 2)
      dec = int(dec/2)
      
      

   counter = 0
   
   while counter < len(inverse):
      result += inverse[len(inverse)-1-counter]
      counter+=1
   

   return result

def unsignedBinaryToDecimal(string):
   """takes an unsigned binary string as argument and returns the decimal equivalent of it in int form."""


   result = 0
   counter = 0
   while counter < len(string):
      
      result += (int(string[len(string)-1-counter]))*(2**counter)
      counter+=1
   return result
      

def addOne(add):
   """takes a binary string as argument, adds one to the binary number, and returns the new binary string."""
   result = unsignedBinaryToDecimal(add) + 1
   result = unsignedDecimalToBinary(result)
   return result


def twosCompToDecimal (s):
   """takes a two's complement binary string as argument and returns the decimal equivalent of it in int form."""

            

   if s[0] == "0":
      result = unsignedBinaryToDecimal(s)
      return result
   else:
      result = invert(s)
      result2 = addOne(result)
      return (-1)*unsignedBinaryToDecimal(result2)


   
def decimalToTwosComp(d):
   """takes a decimal number in int form as argument and returns the binary equivalent of it as a string."""

   if d < 0:
      
      result = ("0" + unsignedDecimalToBinary((-1)*d))
      result = invert(result)
      result = addOne(result)
      return result
   else:
      return ("0" + unsignedDecimalToBinary(d))

def signExtend (s, bits):
   """takes a two's complement binary string and the number of bits as arguments and returns the sign extended version as a two's compliment binary string."""
   

   extend = bits - len(s)
   if extend > 0:
      if s[0] == "1":
         while extend > 0:
            s = "1" + s
            extend -= 1

      else:
         while extend > 0:
            s = "0" + s
            extend -= 1
         
      
   return s

   
         
      
   
   
      

def main():
   """Test bed for decimal/binary conversion functions."""
   print ("11001 ->", invert("00110"))

   print ("0 ->", unsignedBinaryToDecimal("0"))

   print ("6 ->", unsignedBinaryToDecimal("110"))

   print ("0 ->", unsignedDecimalToBinary(0))

   print ("110 ->", unsignedDecimalToBinary(6))

   print ("110 ->", addOne("101"))

   print ("5 ->", twosCompToDecimal("0101"))

   print ("-5 ->", twosCompToDecimal("1011"))

   print ("0101 ->", decimalToTwosComp(5))

   print ("1011 ->", decimalToTwosComp(-5))

   print ("00000101 ->", signExtend(decimalToTwosComp(5), 8))

   print ("11111011 ->", signExtend(decimalToTwosComp(-5), 8))

if __name__ == "__main__":
   main()
