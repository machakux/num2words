#!/usr/bin/env python3

import sys

ones=['','one','two','three','four','five','six','seven','eight','nine',]
teens=['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','eighteen','nineteen']
tens=['','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
hundreds=['','one hundred','two hundred','three hunddred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
rank=['','thousand','million','billion','trillion','quadrillion','quintillion','sextillion','septillion','octillion','nonillion','decillion','undecillion','duodecillion','tredecillion','quattuordecillion','quindecillion','sexdecillion','septendecillion','octodecillion','novemdecillion','vigintillion']


class Number:
	
	def __init__(self,number):
		self.number = number
		if self.number is None:
			return ''
		else:
			try:
				int(self.number)
			except TypeError:
				return "Error. You didn't enter an interger."
	
	def get_order(self,number):
		order = 0
		while number >= 1000:
			order += 1
			number = number//1000
		return order
		
	def get_order_remainder(self,number):
		order = self.get_order(number)
		remainder = number%pow(10,3*order)
		return remainder
		
	def convert_to_words_hundreds(self,number):
		word = ''
		if number < 0:
			number -= number
			word += 'negative '
		if number==0:
			word += 'zero'
		if number <1000:
			if number >= 100:
				hundred = number//100
				hundredr = number%100
				if hundredr:
					if 10< hundredr < 20:
						teen = hundredr-10
						word += hundreds[hundred] +' and '+ teens[teen]
					else:
						ten = hundredr//10
						one = hundredr%10
					word += hundreds[hundred] +' and '+ tens[ten]+' '+ones[one]
				else:
					word += hundreds[hundred]
			if 100> number >= 10:
				if 10< number < 20:
					teen = number-10
					word += teens[teen]
				else:
					ten = number//10
					one = number%10
					word += tens[ten]+' '+ones[one]
			elif number<10:
				word += ones[number]
				
		return word
		
	def convert_to_words_order(self,number):
		order = self.get_order(number)
		hundred = number//pow(10,3*order)
		return self.convert_to_words_hundreds(hundred) +' '+rank[order]+','
	
	def convert_to_words(self):
		word=''
		if self.number < 0:
			self.number = -self.number
			word += 'negative '
		if self.number==0:
			word += 'zero'
		number = self.number
		if number < 1000:
			word += self.convert_to_words_hundreds(number)
			word += '.'
		else:
			if number%10000<=999:
				terminator =' and '
			else:
				terminator =''
			while number >= 1000:
				order = self.get_order(number)
				digits_in_order = number//pow(10,3*order)
				value_in_order = (digits_in_order * pow(10,3*order))
				word += self.convert_to_words_order(number)
				if order >= 1:
					word += ' '

				number = number - value_in_order
			else:
				if terminator:
					word = word[:-2]
				word+=terminator
				word += self.convert_to_words_hundreds(number)
			word+='.'
		return word

try:
	for i in range(1,len(sys.argv)):
		no = Number(int(sys.argv[i]))
		print (no.convert_to_words())
except KeyError:
	pass
