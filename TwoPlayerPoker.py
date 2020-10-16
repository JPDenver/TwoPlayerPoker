
import random



class cards:
    def __init__(self,value,suit,face):
        self.value = value   
        self.suit = suit
        self.face = face

card1 = cards(1,'Hearts','1')
card2 = cards(2,'Hearts','2')
card3 = cards(3,'Hearts','3')
card4 = cards(4,'Hearts','4')
card5 = cards(5,'Hearts','5')
card6 = cards(6,'Hearts','6')
card7 = cards(7,"Hearts",'7')
card8 = cards(8,'Hearts','8')
card9 = cards(9,'Hearts','9')
card10 = cards(10,'Hearts','Jack')
card11 = cards(11,'Hearts','Queen')
card12 = cards(12,'Hearts','King')
card13 = cards(13,'Hearts','Ace')

card14 = cards(1,'Diamonds','1')
card15 = cards(2,'Diamonds','2')
card16 = cards(3,'Diamonds','3')
card17 = cards(4,'Diamonds','4')
card18 = cards(5,'Diamonds','5')
card19 = cards(6,'Diamonds','6')
card20 = cards(7,"Diamonds",'7')
card21 = cards(8,'Diamonds','8')
card22 = cards(9,'Diamonds','9')
card23 = cards(10,'Diamonds','Jack')
card24 = cards(11,'Diamonds','Queen')
card25 = cards(12,'Diamonds','King')
card26 = cards(13,'Diamonds','Ace')

card27 = cards(1,'Clubs','1')
card28 = cards(2,'Clubs','2')
card29 = cards(3,'Clubs','3')
card30 = cards(4,'Clubs','4')
card31 = cards(5,'Clubs','5')
card32 = cards(6,'Clubs','6')
card33 = cards(7,'Clubs','7')
card34 = cards(8,'Clubs','8')
card35 = cards(9,'Clubs','9')
card36 = cards(10,'Clubs','Jack')
card37 = cards(11,'Clubs','Queen')
card38 = cards(12,'Clubs','King')
card39 = cards(13,'Clubs','Ace')

card40 = cards(1,'Spades','1')
card41 = cards(2,'Spades','2')
card42 = cards(3,'Spades','3')
card43 = cards(4,'Spades','4')
card44 = cards(5,'Spades','5')
card45 = cards(6,'Spades','6')
card46 = cards(7,'Spades','7')
card47 = cards(8,'Spades','8')
card48 = cards(9,'Spades','9')
card49 = cards(10,'Spades','Jack')
card50 = cards(11,'Spades','Queen')
card51 = cards(12,'Spades','King')
card52 = cards(13,'Spades','Ace')


def deal():
    objectlist = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15,card16,card17,
    card18,card19,card20,card21,card22,card23,card24,card25,card26,card27,card28,card29,card30,card31,card32,card33,card34,
    card35,card36,card37,card38,card39,card40,card41,card42,card43,card44,card45,card46,card47,card48,card49,card50,card51,card52]
    # objectlist = card(1,52)
    
    global p1c1
    cardindex1 = random.randint(0,len(objectlist)-1)
    p1c1 = objectlist[cardindex1]
    # print(p1c1.face,p1c1.suit)
    objectlist.pop(cardindex1)
    
    global p1c2
    cardindex2 = random.randint(0,len(objectlist)-1)
    p1c2 = objectlist[cardindex2]
    # print(p1c2.face,p1c2.suit)   
    objectlist.pop(cardindex2)

    global p1c3
    cardindex3 = random.randint(0,len(objectlist)-1)
    p1c3 = objectlist[cardindex3]
    # print(p1c3.face,p1c3.suit)
    objectlist.pop(cardindex3)
    
    global p1c4
    cardindex4 = random.randint(0,len(objectlist)-1)
    p1c4 = objectlist[cardindex4]
    # print(p1c4.face,p1c4.suit)
    objectlist.pop(cardindex4)

    global p1c5
    cardindex5 = random.randint(0,len(objectlist)-1)
    p1c5 = objectlist[cardindex5]
    # print(p1c5.face,p1c5.suit)
    objectlist.pop(cardindex5)
    global p1hand
    p1hand = (p1c1.face +' of ' + p1c1.suit,p1c2.face +' of ' + p1c2.suit,p1c3.face +' of ' + p1c3.suit,p1c4.face +' of ' + p1c4.suit,p1c5.face +' of ' + p1c5.suit)
    
    

deal()


print(p1hand)
print(p1c1.value,p1c2.value,p1c3.value,p1c4.value,p1c5.value)

pair1 = []


def pairing():
    if p1c1.value == p1c2.value:
        pair1.append(p1c1.value)
        pair1.append(p1c2.value)
    if p1c1.value == p1c3.value:
        pair1.append(p1c1.value)
        pair1.append(p1c3.value)
    if p1c1.value == p1c4.value:
        pair1.append(p1c1.value)
        pair1.append(p1c4.value)
    if p1c1.value == p1c5.value:
        pair1.append(p1c1.value)
        pair1.append(p1c5.value)
    if p1c2.value == p1c3.value:
        pair1.append(p1c2.value)
        pair1.append(p1c3.value)
    if p1c2.value == p1c4.value:
        pair1.append(p1c2.value)
        pair1.append(p1c4.value)
    if p1c2.value == p1c5.value:
        pair1.append(p1c2.value)
        pair1.append(p1c5.value)
    if p1c3.value == p1c4.value:
        pair1.append(p1c3.value)
        pair1.append(p1c4.value)
    if p1c3.value == p1c5.value:
        pair1.append(p1c3.value)
        pair1.append(p1c5.value)
    if p1c4.value == p1c5.value:
        pair1.append(p1c4.value)
        pair1.append(p1c5.value)

pairing()
print(pair1)


def score():
    #High Card
    global p1score
    p1score = 0
    if len(pair1) == 0:
        print("High Card")
        p1score = max(p1c1.value,p1c2.value,p1c3.value,p1c4.value,p1c5.value)
    #1 Pair
    if len(pair1) == 2:
        print("1 Pair")
        p1score = sum(pair1)+15
    #2 Pairs
    if len(pair1) == 4:
        print('2 Pairs')
        p1score = sum(pair1)+100
    # 3 of a kind
    if len(pair1) == 6:
        print('3 of a kind')
        p1score = (pair1[0]*3)+200
    #if Straight
    p1sort = (p1c1.value,p1c2.value,p1c3.value,p1c4.value,p1c5.value)
    sorted_hand = sorted(p1sort)
    if sorted_hand[0] == sorted_hand[1]-1 and sorted_hand[0] == sorted_hand[2]-2 and \
        sorted_hand[0] == sorted_hand[3]-3 and sorted_hand[0] == sorted_hand[4]-4:
        print("Straight")
        p1score = p1c1.value + p1c2.value + p1c3.value + p1c4.value + p1c5.value + 300
    if sorted_hand[0] == 2 and sorted_hand[1] == 3 and \
        sorted_hand[2] == 4 and sorted_hand[3] == 5 and sorted_hand[4] == 13:
        print("Straight")
        p1score = p1c1.value + p1c2.value + p1c3.value + p1c4.value + p1c5.value + 300
    #Flush
    if p1c1.suit == p1c2.suit and p1c1.suit == p1c3.suit and\
    p1c1.suit == p1c4.suit and p1c1.suit == p1c5.suit:
        print('Flush')
        p1score += p1c1.value + p1c2.value + p1c3.value + p1c4.value + p1c5.value + 400
    #Fullhouse
    if len(pair1) == 8:
        print('fullhouse')
        p1score = pair1[0]+pair1[1]+pair1[7]+pair1[6]+500
    #4 of a kind
    if len(pair1) == 12:
        print('4 of a kind')
        p1score = (pair1[0]*4)+600
    p1score = int(p1score)
    if int(p1score) > 700:
        print("Royal Flush")
        p1score = sum(p1hand) + 700

score()

print(p1score)




def deal2():
    objectlist = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15,card16,card17,
    card18,card19,card20,card21,card22,card23,card24,card25,card26,card27,card28,card29,card30,card31,card32,card33,card34,
    card35,card36,card37,card38,card39,card40,card41,card42,card43,card44,card45,card46,card47,card48,card49,card50,card51,card52]
    # objectlist = card(1,52)
    
    global p2c1
    cardindex1 = random.randint(0,len(objectlist)-1)
    p2c1 = objectlist[cardindex1]
    # print(p1c1.face,p1c1.suit)
    objectlist.pop(cardindex1)
    
    global p2c2
    cardindex2 = random.randint(0,len(objectlist)-1)
    p2c2 = objectlist[cardindex2]
    # print(p1c2.face,p1c2.suit)   
    objectlist.pop(cardindex2)

    global p2c3
    cardindex3 = random.randint(0,len(objectlist)-1)
    p2c3 = objectlist[cardindex3]
    # print(p1c3.face,p1c3.suit)
    objectlist.pop(cardindex3)
    
    global p2c4
    cardindex4 = random.randint(0,len(objectlist)-1)
    p2c4 = objectlist[cardindex4]
    # print(p1c4.face,p1c4.suit)
    objectlist.pop(cardindex4)

    global p2c5
    cardindex5 = random.randint(0,len(objectlist)-1)
    p2c5 = objectlist[cardindex5]
    # print(p1c5.face,p1c5.suit)
    objectlist.pop(cardindex5)
    global p2hand
    p2hand = (p2c1.face +' of ' + p2c1.suit,p2c2.face +' of ' + p2c2.suit,p2c3.face +' of ' + p2c3.suit,p2c4.face +' of ' + p2c4.suit,p2c5.face +' of ' + p2c5.suit)
    
    

deal2() 

print(p2hand)
print(p2c1.value,p2c2.value,p2c3.value,p2c4.value,p2c5.value)

pair2 = []

def pairing2():
    if p2c1.value == p2c2.value:
        pair2.append(p2c1.value)
        pair2.append(p2c2.value)
    if p2c1.value == p2c3.value:
        pair2.append(p2c1.value)
        pair2.append(p2c3.value)
    if p2c1.value == p2c4.value:
        pair2.append(p2c1.value)
        pair2.append(p2c4.value)
    if p2c1.value == p2c5.value:
        pair2.append(p2c1.value)
        pair2.append(p2c5.value)
    if p2c2.value == p2c3.value:
        pair2.append(p2c2.value)
        pair2.append(p2c3.value)
    if p2c2.value == p2c4.value:
        pair2.append(p2c2.value)
        pair2.append(p2c4.value)
    if p2c2.value == p2c5.value:
        pair2.append(p2c2.value)
        pair2.append(p2c5.value)
    if p2c3.value == p2c4.value:
        pair2.append(p2c3.value)
        pair2.append(p2c4.value)
    if p2c3.value == p2c5.value:
        pair2.append(p2c3.value)
        pair2.append(p2c5.value)
    if p2c4.value == p2c5.value:
        pair2.append(p2c4.value)
        pair2.append(p2c5.value)

pairing2()
print(pair2)

def score2():
    #High Card
    global p2score
    p2score = 0
    if len(pair2) == 0:
        print("High Card")
        p2score = max(p2c1.value,p2c2.value,p2c3.value,p2c4.value,p2c5.value)
    #1 Pair
    if len(pair2) == 2:
        print("1 Pair")
        p2score = sum(pair2)+15
    #2 Pairs
    if len(pair2) == 4:
        print('2 Pairs')
        p2score = sum(pair2)+100
    # 3 of a kind
    if len(pair2) == 6:
        print('3 of a kind')
        p2score = (pair2[0]*3)+200
    #if Straight
    p2sort = (p2c1.value,p2c2.value,p2c3.value,p2c4.value,p2c5.value)
    sorted_hand2 = sorted(p2sort)
    if sorted_hand2[0] == sorted_hand2[1]-1 and sorted_hand2[0] == sorted_hand2[2]-2 and \
        sorted_hand2[0] == sorted_hand2[3]-3 and sorted_hand2[0] == sorted_hand2[4]-4:
        print("Straight")
        p2score = p2c1.value + p2c2.value + p2c3.value + p2c4.value + p2c5.value + 300
    if sorted_hand2[0] == 2 and sorted_hand2[1] == 3 and \
        sorted_hand2[2] == 4 and sorted_hand2[3] == 5 and sorted_hand2[4] == 13:
        print("Straight")
        p1score = p1c1.value + p1c2.value + p1c3.value + p1c4.value + p1c5.value + 300
    #Flush
    if p2c1.suit == p2c2.suit and p2c1.suit == p2c3.suit and\
    p2c1.suit == p2c4.suit and p2c1.suit == p2c5.suit:
        print('Flush')
        p2score += p2c1.value + p2c2.value + p2c3.value + p2c4.value + p2c5.value + 400
     #Fullhouse
    if len(pair2) == 8:
        print('fullhouse')
        p2score = pair2[0]+pair2[1]+pair2[7]+pair2[6]+500
    #4 of a kind
    if len(pair2) == 12:
        print('4 of a kind')
        p2score = (pair2[0]*4)+600
    p2score = int(p2score)
    if int(p2score) > 700:
        print("Royal Flush")
        p2score = sum(p2hand) + 700
    


score2()
print(p2score)

def Whowon():
    if p1score > p2score:
        print("Player 1 Wins")
    elif p1score == p2score:
        print("Tie")
    else:
        print("Player 2 Wins")

Whowon()