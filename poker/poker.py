#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://www.contrib.andrew.cmu.edu/~gc00/reviews/pokerrules
import itertools
import random
from operator import itemgetter
from collections import Counter
import numpy 




def Deck():
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
	return deck

def Give_cards(deck):
	hand=[]
	for i in range(1,6):
		hand+=[deck.pop()]
	return hand

def Discard(hand):
	cards2change = input("Would you like to discard some of your cards  ? If so which , note that you can only discard up to 3 cards:")
	if cards2change!='0':
		cards2change.strip()
		cards2change.split()
		cards2change = [int(i) for i in cards2change.split(',')]
		cards2change.sort(reverse=True)
		if len(cards2change)>0:
			for crd in cards2change:
				hand.pop(crd-1)
			for i in range(len(cards2change)):
				hand+=[deck.pop()]
			print('Your new hand is \n')
			PrintHand(hand)
	return hand

def Play(hand):
	hand = list((int(x[0]) ,x[1]) for x in hand)
	hand.sort()

	kinds=[c[1] for c in hand]
	isKind(kinds,hand)

def PrintHand(hand):
	print('1th |','2th |','3th |','4th |','5th  ')
	for i in range(0,len(hand)):
		if hand[i][0] == '14':
			print('A',hand[i][1],end="   ")
		elif hand[i][0] == '13':
			print('K',hand[i][1],end="   ")
		elif hand[i][0] == '12':
			print('Q',hand[i][1],end="   ")
		elif hand[i][0] == '11':
			print('J',hand[i][1],end="   ")
		else:
			if i==4:
				print(hand[i][0],hand[i][1])
			else:
				print(hand[i][0],hand[i][1],end="   ")

def	isKind(kind,hand):
		#numbers is all the values of a the cards for example if cards are 4 H , 8 C ---> number=[4,8]
		numbers=[c[0] for c in hand]
		count_number = Counter(numbers)
		most_number = count_number.most_common(1)
		if most_number[0][1]==5:
			print(most_number,'Five of a kind')
			return
		elif most_number[0][1]==4:
			print(most_number,'Four of a kind')
			return
		elif most_number[0][1]==3:
			print(most_number,'Three of a kind')
			return
		else:
			Full_House(kind, hand , numbers)

def Full_House(kind, hand , number):
	count_number = Counter(number)
	most_number = count_number.most_common(2)
	if(most_number[0][1]==3) and most_number[1][1]==2:
			print(most_number , 'full house')
			return
	elif most_number[0][1]==2 and most_number[1][1]==2:
			 print(most_number , 'pair of two')
			 return
	elif most_number[0][1]==2:
			print(most_number[0] ,  'pair')
			return
	else: Straight(kind,hand,number)

def Straight(kind,hand,number):
	number.sort()
	AceIsOne = 0
	#diff gives back all the remaing when whe reduce the list of numbers for example if number = [ 4, 6 , 10] --->>> diff = [ 2,4]
	diff =list(numpy.diff(number))

	#if the list is [1,1,1,13] it means that the ace has to play the role of 1 in a straight for example the sorted hand is 2 ,3 , 4 , A(14)
	# then the ace is supposed to be 1  and we will have a straight 
	if diff[3]==9:
		AceIsOne= 1
	counter = Counter(kind)

	#most_occur gives as the mostt occur kind in the foramt of a list ->>>  [('C', 1)]
	most_occur =counter.most_common(1)
	StraightFlush = 0
	for i in range(0,len(diff)):
		# if some numberr in the list is 0 then it isnt a straight 
			StraightFlush+=diff[i]
	#StraightFlush is the sum of the list of differnce , if it's =4 then all the cards are different by 1 
	# thereforth its a straight and if most occur = 5 then its a staight flush if not its a flush
	if StraightFlush == 4:
		if AceIsOne==0 and most_occur[0][1]==5:
			print('Royal Flush or Exodia')
			return
		elif most_occur[0][1]==5:
			print('Straight Flush')
			return
		else:
			print('Straight')
			return
	elif StraightFlush == 12 and AceIsOne ==1:
		if most_occur[0][1]==5:
			print('Straight Flush')
			return
		else:
			print('Straight')
	elif most_occur[0][1]==5:
		print('Flush')
		return
	else:
		HighCard(hand)


def HighCard(hand):
		if hand[4][0] == 14:
			print('High Card  A')
		elif hand[4][0] == 13:
			print('High Card  K')
		elif hand[4][0] ==12:
			print('High Card  Q')
		elif hand[4][0] == 11:
			print('High Card  J')
		else:
			print('High Card  ' ,hand[4][0])



deck = Deck()

user_hand = Give_cards(deck)
comp_hand = Give_cards(deck)

PrintHand(user_hand)
user_hand = Discard(user_hand)

print('Your hand is:')
Play(user_hand)

print("Comouter's hand is:")
Play(comp_hand)