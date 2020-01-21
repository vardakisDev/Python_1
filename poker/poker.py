#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://www.contrib.andrew.cmu.edu/~gc00/reviews/pokerrules
import itertools
import random
from operator import itemgetter
from collections import Counter
import numpy 

#Ελέγχει αν όλα είναι τα ίδια
# def Five_of_a_Kind(h):
# 	kinds=[c[0] for c in h]
# 	kinds=list(set(kinds))
# 	if len(kinds)==1:
# 		return kinds[0]
# 	else:
# 		return 0

def Five_of_a_Kind(kind,hand):
	
	kind=list(set(kinds))
	if(len(kinds)) == 1:
		return kinds[0] , 'five of a kind'
	else:
		return 0

def	Four_of_a_Kind(kind,hand):
	counter = Counter(kind)
	most_occur =counter.most_common(1)
	if(most_occur[0][1] == 4):
		return most_occur[0][0] , ' four of a kind'
	else:
		return 0


def	Three_of_a_Kind(kind,hand):
	counter = Counter(kind)
	most_occur =counter.most_common(1)
	if(most_occur[0][1] == 3):
		return most_occur[0][0] , ' three of a kind'
	else:  return 0 


def Full_House(kind, hand , number):
	count_number = Counter(number)
	most_number = count_number.most_common(2)
	if(most_number[0][1]==3) and most_number[1][1]==2:
			return most_number , 'full house'
		# else if we have three of a kind rule
	elif most_number[0][1]==2 and most_number[1][1]==2:
			 return most_number , 'pair of two'
	elif most_number[0][1]==2:
			return most_number ,  'pair'
	else: return 0

def Straight(kind,hand,number):
	number.sort()
	diff =list(numpy.diff(number))
	counter = Counter(kind)
	most_occur =counter.most_common(1)
	StraightFlash = 0
	isPair = 0 
	for i in range(0,len(diff)):
		# if some numberr in the list is 0 then it isnt a straight 
			StraightFlash+=diff[i]
			if diff[i] == 0:
				isPair += 1
	if StraightFlash == 4 and   most_occur[0][1]==5:
		return 'straight flush'
	elif most_occur[0][1]==5:
		return 'flush'
	else:
		return 0
def HighCard(hand):
	return hand[4][0]
		# if every number is diff by one then its a straight flash

def printhand(hand):
	print('1th |','2th |','3th |','4th |','5th  ')
	for i in range(0,len(hand)):
		if hand[i][0] == 14:
			print()
			print('A',hand[i][1],end="   ")
		elif hand[i][0] == 13:
			print('K',hand[i][1],end="   ")
		elif hand[i][0] == 12:
			print('Q',hand[i][1],end="   ")
		elif hand[i][0] == 11:
			print('J',hand[i][1],end="   ")
		else:
			if i==4:
				print(hand[i][0],hand[i][1])
			else:
				print(hand[i][0],hand[i][1],end="   ")

#Για να μη γράφουμε τα χαρτιά ας 
#φτιάξουμε την τράπουλα προγραμματιστικά
cards=[str(i) for i in range(1,14)] 
# cards+=["J","Q","K", "A"] #πρόσθεσε τις φιγούρες
suits=["S","H","D","C"] #βάλε τα χρώματα
deck=itertools.product(cards,suits) #Φτιάξε όλα τα φύλλα
deck=list(deck) #Ας τα έχω σε μία λίστα...
#Ας βάλουμε 2 τράπουλες
deck+=deck
#Ανακάτωσε την τράπουλα
random.shuffle(deck)
user_hand=[]
comp_hand=[]
#Μοίρασε τα χαρτιά
for i in range(1,6):
	user_hand+=[deck.pop()]
	comp_hand+=[deck.pop()]
# print("Τα χαρτιά σου είναι: ")
printhand(user_hand)

#by the rules betting occurs we are not ask to implement this might add latter 


#the player is asked if he wants to drop cards and then get back as many cards as he threw 
cards2change = input("Would you like to discard some of your cards  ? If so which , note that you can only discard up to 3 cards:")
if cards2change!='0':
	cards2change.strip()
	cards2change.split()
	cards2change = [int(i) for i in cards2change.split(',')]
	cards2change.sort(reverse=True)
	if len(cards2change)>0:
		for crd in cards2change:
			user_hand.pop(crd-1)
		for i in range(len(cards2change)):
			user_hand+=[deck.pop()]
#betting again
# convert the string numbers to ints to do some comprisons
print('Sorting your hand .....')
hand = list((int(x[0]) ,x[1]) for x in user_hand)
hand.sort()
print('Your hand is:')
printhand(hand)

kinds=[c[1] for c in hand]
numbers=[c[0] for c in hand]

print(Five_of_a_Kind(kinds,hand))
print(Four_of_a_Kind(kinds,hand))
print(Full_House(kinds,hand,numbers))
print(Straight(kinds,hand, numbers))
print(HighCard(hand))
printhand(hand)
#fuctions comparing cards take place
