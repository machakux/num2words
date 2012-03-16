#!/usr/bin/env python3

__author__  = (
	'Machaku Banga',
	)

__license__ = 'Apache License, 2.0 (Apache-2.0)'
__version__ = '2012.03.16'

import sys
import re

ones=['','one','two','three','four','five','six','seven','eight','nine',]
teens=['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens=['','ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
hundreds=['','one hundred','two hundred','three hundred','four hundred','five hundred','six hundred','seven hundred','eight hundred','nine hundred']
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
					word += hundreds[hundred] 
					if ten:
						word+= ' and '+ tens[ten]
					if one and ten:
						word += ' '+ones[one]
					if one and not ten:
						word += ' and '+ones[one]
				else:
					word += hundreds[hundred]
			if 100> number >= 10:
				if 10< number < 20:
					teen = number-10
					word += teens[teen]
				else:
					ten = number//10
					one = number%10
					word += tens[ten]
					if one:
						word += ' '+ones[one]
			elif number<10:
				word += ones[number]
				
		return word
		
	def convert_to_words_order(self,number):
		order = self.get_order(number)
		hundred = number//pow(10,3*order)
		return self.convert_to_words_hundreds(hundred) +' '+rank[order]
		
	def convert_to_digits(self,snumber):
		word=''
		word_l=[]
		digits=list(snumber)
		for i in digits:
			if int(i)==0:
				word_l.append('zero')
			else:
				word_l.append(ones[int(i)])
		word=' '.join(word_l)
		return word
	
	def get_fraction_digits(self,integer=False):
		number_s=str(self.number)
		try:
			number_ls = re.split('[.]',number_s)
			digits = number_ls[1]
			if integer:
				digits = int(digits)
		except:
			digits = False
		return digits
	
	def convert_to_words(self):
		word=''
		fraction = self.get_fraction_digits()
		try:
			number_s=str(self.number)
			number_ls = re.split('[.]',number_s)
			self.number = int(number_ls[0])
		except:
			pass
		if self.number < 0:
			self.number = -self.number
			word += 'negative '
		if self.number==0:
			word += 'zero'
		number = self.number
		if number < 1000:
			word += self.convert_to_words_hundreds(number)
		else:
			if number%1000:
				terminator =' and '
			else:
				terminator =''
			while number >= 1000:
				order = self.get_order(number)
				digits_in_order = number//pow(10,3*order)
				value_in_order = (digits_in_order * pow(10,3*order))
				word += self.convert_to_words_order(number)
				number = number - value_in_order
				if number:
					word += ','
				if order >= 1 and number:
					word += ' '
			else:
				if terminator:
					word = word[:-2]
				word+=terminator
				word += self.convert_to_words_hundreds(number)
		if fraction:
			word+= ' point '+self.convert_to_digits(fraction)
		return word

try:
	for i in range(1,len(sys.argv)):
		try:
			no = Number(int(sys.argv[i]))
		except ValueError:
			no = Number(float(sys.argv[i]))
		print (no.convert_to_words())
except KeyError:
	pass
