import string
#write a custom exception, then an inclusive test, then write the code for the following functions:

#Create your own exception		
class CustomException(Exception): 
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return self.value


def shout(txt):
	try:
		if txt.isupper():
			raise CustomException(1)
		else:
			print txt.upper()
	except AttributeError:
		raise AttributeError, "Must enter a text string!"
	except CustomException as e:
		raise CustomException, "Stop shouting!!!"

def reverse(txt):
	try:
		print txt[::-1]
	except AttributeError:
		raise AttributeError, "Must enter a text string!"

def reversewords(txt):
	try:
		words_list = txt.split()
		reverse_list = words_list[::-1]
		print ' '.join(reverse_list)
	except AttributeError:
		raise AttributeError, "Must enter a text string!"

def reversewordletters(txt):
	try:
		words_list = txt.split()
		i = range(0, len(words_list))
		reverse_list = []
		for i in words_list:
			reverse_list.append(i[::-1])
		print ' '.join(reverse_list)
	except AttributeError:
		raise AttributeError, "Must enter a text string!"

def piglatin(txt):
	try:
		words_list = txt.split()
		i = range(0, len(words_list))
		pig_latin = []
		for i in words_list:
			letters_list = i.split()
			j = range(0, len(letters_list))
			for j in letters_list:
				if j[0] not in 'aeiou' and j[1] not in 'aeiou' and j[2] not in 'aeiou' and j[3] not in 'aeiou' and j[4] not in 'aeiou' and j[5] not in 'aeiou' and j[6] not in 'aeiou':
					pig_latin.append(j[7:]+'ay'+j[0]+j[1]+j[2]+j[3]+j[4]+j[5]+j[6])
				elif j[0] not in 'aeiou' and j[1] not in 'aeiou' and j[2] not in 'aeiou' and j[3] not in 'aeiou' and j[4] not in 'aeiou' and j[5] not in 'aeiou':
					pig_latin.append(j[6:]+'ay'+j[0]+j[1]+j[2]+j[3]+j[4]+j[5])
				elif j[0] not in 'aeiou' and j[1] not in 'aeiou' and j[2] not in 'aeiou' and j[3] not in 'aeiou' and j[4] not in 'aeiou':
					pig_latin.append(j[5:]+'ay'+j[0]+j[1]+j[2]+j[3]+j[4])
				elif j[0] not in 'aeiou' and j[1] not in 'aeiou' and j[2] not in 'aeiou' and j[3] not in 'aeiou':
					pig_latin.append(j[4:]+'ay'+j[0]+j[1]+j[2]+j[3])
				elif j[0] not in 'aeiou' and j[1] not in 'aeiou' and j[2] not in 'aeiou':
					pig_latin.append(j[3:]+'ay'+j[0]+j[1]+j[2])
				elif j[0] not in 'aeiou' and j[1] not in 'aeiou':
					pig_latin.append(j[2:]+'ay'+j[0]+j[1])
				elif j[0] not in 'aeiou':
					pig_latin.append(j[1:]+'ay'+j[0])
				else:
					pig_latin.append(j + 'ay')
		print ' '.join(pig_latin)
	except AttributeError:
		raise AttributeError, "Must enter a text string!"

