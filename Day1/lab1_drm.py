def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  digits = []
  while num>0:
	digits.append(str(num%2))
	num/=2
  digits.reverse()
  return ''.join(digits)

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0' 
  digits = []
  while num>0:
	digits.append(str(num%base))
	num/=base
  digits.reverse()
  return ''.join(digits)

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0 
  result = []
  for i in range(0,len(string)):
	result.append(int(string[i])*(base**(len(string)-i-1)))
  return result

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  if str1=="0" or base1 <= 0 : return 0
  result1 = []
  for i in range(0,len(str1)):
	result1.append(int(str1[i])*(base1**(len(str1)-i-1)))
  if str2=="0" or base2 <= 0 : return 0
  result2 = []
  for i in range(0,len(str2)):
	result2.append(int(str2[i])*(base2**(len(str2)-i-1)))
  return sum(result1) + sum(result2)
  
def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  if str1=="0" or base1 <= 0 : return 0
  result1 = []
  for i in range(0,len(str1)):
	result1.append(int(str1[i])*(base1**(len(str1)-i-1)))
  if str2=="0" or base2 <= 0 : return 0
  result2 = []
  for i in range(0,len(str2)):
	result2.append(int(str2[i])*(base2**(len(str2)-i-1)))
  return sum(result1) * sum(result2)

def romanify(num):
  """given an integer, return the Roman numeral version"""
  if num<=0: return '0'
  numerals = []
  while num>999:
	numerals.append("M")
	num-=1000
  while num>899:
	numerals.append("CM")
	num-=900
  while num>499:
	numerals.append("D")
	num-=500
  while num>399:
	numerals.append("CD")
	num-=400
  while num>99:
	numerals.append("C")
	num-=100
  while num>89:
	numerals.append("XC")
	num-=90
  while num>49:
	numerals.append("L")
	num-=50
  while num>39:
	numerals.append("XL")
	num-=40
  while num>9:
	numerals.append("X")
	num-=10
  while num>8:
	numerals.append("IX")
	num-=9
  while num>4:
	numerals.append("V")
	num-=5
  while num>3:
	numerals.append("IV")
	num-=4
  while num>0:
	numerals.append("I")
	num-=1
  return ''.join(numerals)
  result = ""
  return result
  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.