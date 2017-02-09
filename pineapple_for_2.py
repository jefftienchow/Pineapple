# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:33:20 2017

@author: Jeff
"""

import random

def create_hand():
    hand=[]
    list_suits=['S','H','D','C']
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

def get_score(top_one, middle_one, bottom_one,top_two,middle_two,bottom_two,fanta):
    top_score=0
    middle_score=0
    bottom_score=0
    foul_one=False
    scoop=False
    scoop_bonus=0
    fantasy=False
    top_one.append('X of Nothing_one')
    top_one.append('Y of Also_nothing_one')
    list_rows_one=[top_one,middle_one,bottom_one]
    reverse_dict={1:'A',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'J',12:'Q',13:'K',14:'A'}
    top_hand='nothing'
    middle_hand='nothing'
    bottom_hand='nothing'
    list_functions=[is_royal,is_full_house,is_of_a_kind,is_flush,is_straight,high]
    list_points=[]
    for i in list_rows_one:
        for j in list_functions:
            if j(i)[0]>=0:
                list_points.append(j(i))
                break
    top_list_one=list_points[0]
    mid_list_one=list_points[1]
    bottom_list_one=list_points[2]
    if top_list_one[0]==1 and top_list_one[1]>5:
        number=reverse_dict[top_list_one[1]]
        top_hand='pair of '+number
        top_score=top_list_one[1]-5
    if top_list_one[0]==1 and top_list_one[1]>11 and fanta==False:
        fantasy=True
    if top_list_one[0]==3:
        number=reverse_dict[top_list_one[1]]
        top_hand='three of a kind of '+number
        top_score=top_list_one[1]+8
        fantasy=True
    mid_dictionary={0:[0,'nothing'],1:[0,'nothing'],2:[0,'nothing'],3:[2,'three of a kind'],4:[4,'straight'],5:[8,'flush'],6:[12,'full house'],7:[20,'four of a kind'],8:[30,'straight flush'],9:[50,'royal flush']}
    if mid_list_one[0]>2:
        middle_score=(mid_dictionary[mid_list_one[0]])[0]
    bottom_dictionary={0:[0,'nothing'],1:[0,'nothing'],2:[0,'nothing'],3:[0,'nothing'],4:[2,'straight'],5:[4,'flush'],6:[6,'full house'],7:[10,'four of a kind'],8:[15,'straight flush'],9:[25,'royal flush']}
    if bottom_list_one[0]>3:
        bottom_score=(bottom_dictionary[bottom_list_one[0]])[0]
    if bottom_list_one[0]==mid_list_one[0] and bottom_list_one[1]<mid_list_one[1]:
        print ('Foul. Your score for this round is 0.')
        foul_one=True
    if mid_list_one[0]==top_list_one[0] and mid_list_one[1]<top_list_one[1]:
        print ('Foul. Your score for this round is 0.')
        foul_one=True
    if bottom_list_one[0]<mid_list_one[0] or mid_list_one[0]<top_list_one[0]:
        print ('Foul. Your score for this round is 0.')
        foul_one=True
    if bottom_list_one[0]>=7 and fanta==True:
        fantasy=True
    bottom_hand=(bottom_dictionary[bottom_list_one[0]])[1]
    middle_hand=(mid_dictionary[mid_list_one[0]])[1]
    
    
    top_score_two=0
    middle_score_two=0
    bottom_score_two=0
    foul_two=False
    top_two.append('X of Nothing_two')
    top_two.append('Y of Also_nothing_two')
    list_rows_two=[top_two,middle_two,bottom_two]
    list_points=[]
    for i in list_rows_two:
        for j in list_functions:
            if j(i)[0]>=0:
                list_points.append(j(i))
                break
    top_list_two=list_points[0]
    mid_list_two=list_points[1]
    bottom_list_two=list_points[2]
    
    if top_list_two[0]==1 and top_list_two[1]>5:
        top_score_two=top_list_one[1]-5
    if top_list_two[0]==3:
        top_score_two=top_list_one[1]+8
    if mid_list_two[0]>2:
        middle_score_two=(mid_dictionary[mid_list_two[0]])[0]
    if bottom_list_two[0]>3:
        bottom_score_two=(bottom_dictionary[bottom_list_two[0]])[0]
        
    if bottom_list_two[0]==mid_list_two[0] and bottom_list_two[1]<mid_list_two[1]:
        foul_two=True
    if mid_list_two[0]==top_list_two[0] and mid_list_two[1]<top_list_two[1]:
        foul_two=True
    if bottom_list_two[0]<mid_list_two[0] or mid_list_two[0]<top_list_two[0]:
        foul_two=True
    
    if foul_two:
        scoop=True
    top_win=False
    middle_win=False
    bottom_win=False
    scoring_list=[[bottom_list_one,bottom_list_two,bottom_score,bottom_win],[mid_list_one,mid_list_two,middle_score,middle_win],[top_list_one,top_list_two,top_score,top_win]]
    for i in scoring_list:
        if i[0][0]<i[1][0]:
            i[2]-=1
        elif i[0][0]==i[1][0] and i[0][1]<i[1][1]:
            i[2]-=1
        else:
            i[2]+=1
            i[3]=True
    bottom_score-=bottom_score_two
    middle_score-=middle_score_two
    top_score-=top_score_two
        
    if bottom_win and top_win and middle_win:
        scoop=True
    if scoop:
        scoop_bonus=3

    bottom_hand=(bottom_dictionary[bottom_list_one[0]])[1]
    middle_hand=(mid_dictionary[mid_list_one[0]])[1]

    if not foul_one:
        print ('Top score is: ',top_score,';',top_hand)
        print ('Middle score is: ',middle_score,';',middle_hand)
        print ('Bottom score is: ',bottom_score,';',bottom_hand)
        final_score=top_score+bottom_score+middle_score+scoop_bonus
        print ('Your score for this round is: ',final_score)
        if fantasy==True:
            print ('Congratulations!You have reached fantasy land!')
            fantasyland()
        return final_score
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
    
def play_game_for_two():
    top_one=[]
    middle_one=[]
    bottom_one=[]
    hand_one=create_hand()
    display_one=display_hand(hand_one,1)
    while len(display_one)>0:
            print ('You are player 1. Your setup is:')
            print (top_one)
            print (middle_one)
            print (bottom_one)
            print ('Your hand is: ',display_one)
            choice=input('Select a card: ')
            if choice not in display_one:
                print ('Card not in hand. Please try again. ')
            else:
                position=input('Select a position to place the card: ')
                if 'bottom' in position:
                    bottom_one.append(choice)
                    display_one.remove(choice)
                elif 'middle' in position:
                    middle_one.append(choice)
                    display_one.remove(choice)
                elif 'top' in position:
                    top_one.append(choice)
                    display_one.remove(choice)
                else: 
                    print ('Not a valid position. Please choose from "top", "middle", or "bottom".')
    top_two=[]
    middle_two=[]
    bottom_two=[]
    hand_two=create_hand()
    display_two=display_hand(hand_two,1)
    while len(display_two)>0:
            print ("Your opponent's setup is:")
            print (top_one)
            print (middle_one)
            print (bottom_one)
            print ('You are player 2. Your setup is:')
            print (top_two)
            print (middle_two)
            print (bottom_two)
            print ('Your hand is: ',display_two)
            choice=input('Select a card: ')
            if choice not in display_two:
                print ('Card not in hand. Please try again. ')
            else:
                position=input('Select a position to place the card: ')
                if 'bottom' in position:
                    bottom_two.append(choice)
                    display_two.remove(choice)
                elif 'middle' in position:
                    middle_two.append(choice)
                    display_two.remove(choice)
                elif 'top' in position:
                    top_two.append(choice)
                    display_two.remove(choice)
                else: 
                    print ('Not a valid position. Please choose from "top", "middle", or "bottom".')
    for i in range(2,6):
        display_one=display_hand(hand_one,i)
        while len(display_one)>1:
                print ("Your opponent's setup is:")
                print (top_two)
                print (middle_two)
                print (bottom_two)
                print ('You are player 1. Your setup is:')
                print (top_one)
                print (middle_one)
                print (bottom_one)
                print ('Your hand is: ',display_one)
                choice=input('Select a card: ')
                if choice not in display_one:
                    print ('Card not in hand. Please try again. ')
                else:
                    position=input('Select a position to place the card: ')
                    if 'bottom' in position and len(bottom_one)==5:
                        print ('Bottom full. Please try again and select a different position')
                    elif 'middle' in position and len(middle_one)==5:
                        print ('Middle full. Please try again and select a different position')
                    elif 'top' in position and len(top_one)==3:
                        print ('Top full. Please try again and select a different position')
                    elif 'bottom' in position:
                        bottom_one.append(choice)
                        display_one.remove(choice)
                    elif 'middle' in position:
                        middle_one.append(choice)
                        display_one.remove(choice)
                    elif 'top' in position:
                        top_one.append(choice)
                        display_one.remove(choice)
                    else: 
                        print ('Not a valid position. Please choose from "top", "middle", or "bottom".')
        display_two=display_hand(hand_two,i)
        while len(display_two)>1:
                print ("Your opponent's setup is:")
                print (top_one)
                print (middle_one)
                print (bottom_one)
                print ('You are player 2. Your setup is:')
                print (top_two)
                print (middle_two)
                print (bottom_two)
                print ('Your hand is: ',display_two)
                choice=input('Select a card: ')
                if choice not in display_two:
                    print ('Card not in hand. Please try again. ')
                else:
                    position=input('Select a position to place the card: ')
                    if 'bottom' in position and len(bottom_two)==5:
                        print ('Bottom full. Please try again and select a different position')
                    elif 'middle' in position and len(middle_two)==5:
                        print ('Middle full. Please try again and select a different position')
                    elif 'top' in position and len(top_two)==3:
                        print ('Top full. Please try again and select a different position')
                    if 'bottom' in position:
                        bottom_two.append(choice)
                        display_two.remove(choice)
                    elif 'middle' in position:
                        middle_two.append(choice)
                        display_two.remove(choice)
                    elif 'top' in position:
                        top_two.append(choice)
                        display_two.remove(choice)
                    else: 
                        print ('Not a valid position. Please choose from "top", "middle", or "bottom".')
    print ("Player 1's final setup is:")
    print (top_one)
    print (middle_one)
    print (bottom_one)
    game_score_one=get_score(top_one,middle_one,bottom_one,top_two, middle_two, bottom_two,False)
    print ("Player 2's final setup is:")
    print (top_two)
    print (middle_two)
    print (bottom_two)
    game_score_two=get_score(top_two,middle_two,bottom_two,top_one, middle_one, bottom_one,False)
    both_scores=[]
    both_scores.append(game_score_one)
    both_scores.append(game_score_two)
    return both_scores

def play_full_game_for_two():
    again=True
    while again:
        scores=play_game_for_two()
        full_scores=[]
        full_scores[0]+=scores[0]
        full_scores[1]+=scores[1]
        print ('Total score for player one is', full_scores[0])
        print ('Total score for player two is', full_scores[1])
        
        keep_going=input('Play game again?')
        if keep_going!='yes' or 'Yes':
            again=False
        
play_full_game_for_two()
#get_score(['2 of Diamonds','J of Spades','Q of Diamonds'],['J of Clovers','10 of Clovers','2 of Clovers','3 of Clovers','4 of Clovers'],['4 of Spades','4 of Clovers','4 of Hearts','4 of Diamonds','K of Hearts'],['2 of Diamonds','5 of Spades','6 of Diamonds'],['J of Clovers','10 of Clovers','2 of Clovers','3 of Clovers','4 of Clovers'],['4 of Spades','4 of Clovers','4 of Hearts','4 of Diamonds','K of Hearts'],False)