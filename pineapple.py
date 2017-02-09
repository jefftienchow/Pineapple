# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:29:49 2017

@author: Jeff
"""

import random

def create_hand():
    hand=[]
    list_suits=['S','H','D','S']
    list_num=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    list_cards=[]
    list_rand=[]
    for i in list_suits:
        for j in list_num:
            list_cards.append(j+' '+i)
    key={}
    for i in list_cards:
        key[list_cards.index(i)+1]=i
    while len(list_rand)<17:
        randint=random.randint(1,52)
        if randint not in list_rand:
            list_rand.append(randint)
    for num in list_rand:
        hand.append(key[num])
    return hand

def display_hand(hand,trigger):
    display=[]
    if trigger==1:
        for i in range(5):
            display.append(hand[i])
        return (display)
    if trigger>1:
        for i in range(3):
            display.append(hand[i+3*trigger-1])
        return (display)   

def is_of_a_kind(hand):
    list_cards=[]
    list_counts=[]
    card_dict={'A':14,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'X':0,'Y':-1 }
    for i in hand:
        splitted=i.split()
        card=splitted[0]
        list_cards.append(card)
    for i in list_cards:
        count=0
        for j in list_cards:
            if i==j:
                count+=1
        list_counts.append(count)
    if 4 in list_counts:
        for i in range(5):
            if list_counts[i]==4:
                four=card_dict[list_cards[i]]
        return [7,four]
    if 3 in list_counts:
        for i in range(5):
            if list_counts[i]==3:
                three=card_dict[list_cards[i]]
        return [3,three]
    if 2 in list_counts:
        for i in range(5):
            if list_counts[i]==2:
                two=card_dict[list_cards[i]]
        return [1,two]
    else: 
        return [-1,-1]

def is_full_house(hand):
    list_cards=[]
    list_counts=[]
    twocount=0
    current_max=0
    card_dict={'A':14,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'X':0,'Y':-1 }
    for i in hand:
        splitted=i.split()
        card=splitted[0]
        list_cards.append(card)
    for i in list_cards:
        count=0
        for j in list_cards:
            if i==j:
                count+=1
            if count==3:
                house=i
        list_counts.append(count)
    if 2 in list_counts:
        if 3 in list_counts:
            return [6,card_dict[house]]
        else:
            for i in list_counts:
                if i==2:
                    twocount+=1
            if twocount==4:
                for i in range(5):
                    if list_counts[i]==2:
                        if card_dict[list_cards[i]]>current_max:
                            current_max=card_dict[list_cards[i]]
                return [2, current_max]
            else:
                return [-1,-1]
    else: 
        return [-1,-1]
        
def is_flush(hand):
    list_suits=[]
    list_cards=[]
    flush=True
    card_dict={'A':14,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'X':0,'Y':-1}
    for i in hand:
        splitted=i.split()
        suit=splitted[1]
        list_suits.append(suit)
        card=splitted[0]
        list_cards.append(card_dict[card])
    list_cards.sort()
    for i in list_suits:
        for j in list_suits:
            if i!=j:
                flush=False
    if flush!=False:
        return [5,list_cards[4]]
    else:
        return [-1,-1]

def is_straight(hand):
    list_card=[]
    straight_one=True
    straight_two=True
    card_dict={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'X':0,'Y':-1 }
    for i in hand:
        splitted=i.split()
        card=splitted[0]
        list_card.append(card_dict[card])
    list_card.sort()
    for i in range(4):
        if list_card[i]!=list_card[i+1]-1:
            straight_one=False
    list_card_two=[]
    card_dict={'A':14,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'X':0,'Y':-1 }
    for i in hand:
        splitted=i.split()
        card=splitted[0]
        list_card_two.append(card_dict[card])
    list_card_two.sort()
    for i in range(4):
        if list_card_two[i]!=list_card_two[i+1]-1:
            straight_two=False
    if straight_one==True:
        high=list_card[4]
    if straight_two==True:
        high=list_card_two[4]
    if straight_one or straight_two:
        return [4,high]
    else:
        return [-1,-1]

def is_royal(hand):
    if is_straight(hand)[0]==4 and is_flush(hand)[0]==5 and is_straight(hand)[1]==14:
        return [9,15]
    elif is_straight(hand)[0]==4 and is_flush(hand)[0]==5:
        return [8, is_flush(hand)[1]]
    else: 
        return [-1,-1]
        
def high(hand):
    list_card=[]
    card_dict={'A':14,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'X':0,'Y':-1}
    for i in hand:
        splitted=i.split()
        card=splitted[0]
        list_card.append(card_dict[card])
    list_card.sort()
    return [0,list_card[4]]

def get_score(top, middle, bottom,fanta):
    top_score=0
    middle_score=0
    foul=False
    fantasy=False
    bottom_score=0
    top.append('X of Nothing')
    top.append('Y of Also_nothing')
    list_rows=[top,middle,bottom]
    reverse_dict={1:'A',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K',14:'A'}
    top_hand='nothing'
    middle_hand='nothing'
    bottom_hand='nothing'
    list_functions=[is_royal,is_full_house,is_of_a_kind,is_flush,is_straight,high]
    list_points=[]
    for i in list_rows:
        for j in list_functions:
            if j(i)[0]>=0:
                list_points.append(j(i))
                break
    top_list=list_points[0]
    mid_list=list_points[1]
    bottom_list=list_points[2]
    if top_list[0]==1 and top_list[1]>5:
        number=reverse_dict[top_list[1]]
        top_hand='pair of '+number
        top_score=top_list[1]-5
    if top_list[0]==1 and top_list[1]>11 and fanta==False:
        fantasy=True
    if top_list[0]==3:
        number=reverse_dict[top_list[1]]
        top_hand='three of a kind of '+number
        top_score=top_list[1]+8
        fantasy=True
    mid_dictionary={0:[0,'nothing'],1:[0,'nothing'],2:[0,'nothing'],3:[2,'three of a kind'],4:[4,'straight'],5:[8,'flush'],6:[12,'full house'],7:[20,'four of a kind'],8:[30,'straight flush'],9:[50,'royal flush']}
    if mid_list[0]>2:
        middle_score=(mid_dictionary[mid_list[0]])[0]
    bottom_dictionary={0:[0,'nothing'],1:[0,'nothing'],2:[0,'nothing'],3:[0,'nothing'],4:[2,'straight'],5:[4,'flush'],6:[6,'full house'],7:[10,'four of a kind'],8:[15,'straight flush'],9:[25,'royal flush']}
    if bottom_list[0]>3:
        bottom_score=(bottom_dictionary[bottom_list[0]])[0]
    if bottom_list[0]==mid_list[0] and bottom_list[1]<mid_list[1]:
        print ('Foul. Your score for this round is 0.')
        foul=True
    if mid_list[0]==top_list[0] and mid_list[1]<top_list[1]:
        print ('Foul. Your score for this round is 0.')
        foul=True
    if bottom_list[0]<mid_list[0] or mid_list[0]<top_list[0]:
        print ('Foul. Your score for this round is 0.')
        foul=True
    if bottom_list[0]>=7 and fanta==True:
        fantasy=True
    bottom_hand=(bottom_dictionary[bottom_list[0]])[1]
    middle_hand=(mid_dictionary[mid_list[0]])[1]
    if not foul:
        print ('Top score is: ',top_score,';',top_hand)
        print ('Middle score is: ',middle_score,';',middle_hand)
        print ('Bottom score is: ',bottom_score,';',bottom_hand)
        print ('Your score for this round is: ',top_score+bottom_score+middle_score)
        if fantasy==True:
            print ('Congratulations!You have reached fantasy land!')
            fantasyland()
        return top_score+bottom_score+middle_score
    else:
        return 0
        
def fantasyland():
    top=[]
    middle=[]
    bottom=[]
    hand=create_hand()[:14]
    while len(hand)>1:
        print (top)
        print (middle)
        print (bottom)
        print ('Your hand is: ',hand)
        choice=input('Select a card: ')
        if choice not in hand:
            print ('Card not in hand. Please try again. ')
        else:
            position=input('Select a position to place the card: ')
            if 'bottom' in position and len(bottom)==5:
                    print ('Bottom full. Please try again and select a different position')
            elif 'middle' in position and len(middle)==5:
                    print ('Middle full. Please try again and select a different position')
            elif 'top' in position and len(top)==3:
                    print ('Top full. Please try again and select a different position')
            elif 'bottom' in position:
                bottom.append(choice)
                hand.remove(choice)
            elif 'middle' in position:
                middle.append(choice)
                hand.remove(choice)
            elif 'top' in position:
                top.append(choice)
                hand.remove(choice)
            else: 
                print ('Not a valid position. Please choose from "top", "middle", or "bottom".')
    print (top)
    print (middle)
    print (bottom)
    get_score(top,middle,bottom,True)
    
def play_game():
    top=[]
    middle=[]
    bottom=[]
    hand=create_hand()
    display= (display_hand(hand, 1))
    while len(display)>0:
        print (top)
        print (middle)
        print (bottom)
        print ('Your hand is: ',display)
        choice=input('Select a card: ')
        if choice not in display:
            print ('Card not in hand. Please try again. ')
        else:
            position=input('Select a position to place the card: ')
            if 'bottom' in position:
                bottom.append(choice)
                display.remove(choice)
            elif 'middle' in position:
                middle.append(choice)
                display.remove(choice)
            elif 'top' in position:
                top.append(choice)
                display.remove(choice)
            else: 
                print ('Not a valid position. Please choose from "top", "middle", or "bottom".')
    for i in range(2,6):
        display= (display_hand(hand,i))
        while len(display)>1:
            print (top)
            print (middle)
            print (bottom)
            print ('Your hand is: ',display)
            choice=input('Select a card: ')
            if choice not in display:
                print ('Card not in hand. Please try again. ')
            else:
                position=input('Select a position to place the card: ')
                if 'bottom' in position and len(bottom)==5:
                    print ('Bottom full. Please try again and select a different position')
                elif 'middle' in position and len(middle)==5:
                    print ('Middle full. Please try again and select a different position')
                elif 'top' in position and len(top)==3:
                    print ('Top full. Please try again and select a different position')
                elif 'bottom' in position:
                    bottom.append(choice)
                    display.remove(choice)
                elif 'middle' in position:
                    middle.append(choice)
                    display.remove(choice)
                elif 'top' in position:
                    top.append(choice)
                    display.remove(choice)
                else: 
                    print ('Not a valid position. Please choose from "top", "middle", or "bottom".')
    print (top)
    print (middle)
    print (bottom)
    game_score=get_score(top,middle,bottom,False)
    return game_score
    
def full_game():
    again=True
    score=0
    while again:
        game_score=play_game()
        score+=game_score
        print ('Total score is: ',score)
        play_again=input ('Play game again?')
        if play_again!= 'Yes' or 'yes':
            again=False
    
#get_score(['2 of Diamonds','Q of Spades','Q of Diamonds'],['J of Clovers','10 of Clovers','2 of Clovers','3 of Clovers','4 of Clovers'],['4 of Spades','4 of Clovers','4 of Hearts','4 of Diamonds','K of Hearts'],False)
full_game()
