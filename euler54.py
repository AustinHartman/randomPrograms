import time
values = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7,
          '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}

"""
first check if the hand is a flush, if not, straight flush and royal flush 
conditions need not be checked

check two pair condition before three, four, and full house because if the hand 
does not have a pair it can't have any of the other hands
"""
#Flush condition will be able to be removed
# NOT DONE
def flush(ls):
    suit = ls[0][1]
    for card in ls:
        if suit != card[1]:
            return False
    return True


# if flush is true and straight is true, straight flush and check royal flush
def straight(ls):
    straight_ls = []
    for card in ls:
        straight_ls.append(values[card[0]])
    straight_ls = sorted(straight_ls)
    for a in range(len(straight_ls) - 1):
        if straight_ls[a] != straight_ls[a + 1] - 1:
            return False
    return True


# if flush and straight flush are true
def royal_flush(ls):
    suit = ls[0][1]
    for card in ls:
        if suit != card[1]:
            return False
    return True


def pair(ls):
    pair_ls = []
    for card in ls:
        pair_ls.append(card[0])
    if len(pair_ls) != len(set(pair_ls)):
        return True
    return False


# if pair is true check three of a kind
def three_of_a_kind(ls):
    pair_ls = []
    for card in ls:
        pair_ls.append(card[0])
    for card in pair_ls:
        if pair_ls.count(card) > 2:
            return True
    return False


def two_pair(ls):
    pair_ls = []
    for card in ls:
        pair_ls.append(card[0])
    if len(pair_ls) == len(set(pair_ls))+2 and not three_of_a_kind(ls):
        return True
    return False


def rm_repeats(ls):
    pair_ls = []
    for card in ls:
        pair_ls.append(card[0])
    rm_dups = set(pair_ls)
    for card in pair_ls:
        if card in rm_dups:
            rm_dups.pop(card)
            pair_ls.pop(card)
    return pair_ls

# if three of a kind is true check full house
def full_house(ls):
    two = False
    three = False
    pair_ls = []
    for card in ls:
        pair_ls.append(card[0])
    for card in pair_ls:
        if pair_ls.count(card) == 2:
            two = True
        if pair_ls.count(card) == 3:
            three = True
    if two and three:
        return True
    return False


# two pair and three pair ust be true but full house must be false
def four_of_a_kind(ls):
    pair_ls = []
    for card in ls:
        pair_ls.append(card[0])
    for card in pair_ls:
        if pair_ls.count(card) > 3:
            return True
    return False


# if all previous conditions are false or if both players
# hands are the same check for higher card
def high_card(ls):
    high_card_value = values[ls[0][0]]
    hc = ls[0][0]
    for card in ls:
        if values[card[0]] > high_card_value:
            hc = card[0]
            high_card_value = values[card[0]]
    return values[hc]


def hand_score(hand):
    score = 0
    if flush(hand):
        score = 6
        if straight(hand):
            if royal_flush(hand):
                return 10
            return 9
    if three_of_a_kind(hand):
        if four_of_a_kind(hand):
            return 8
        if full_house(hand):
            return 7
        if score == 0:
            return 4
    if score == 6:
        return 6
    if straight(hand):
        return 5
    if two_pair(hand):
        return 3
    if pair(hand):
        return 2
    return 1



start = time.time()
player_1 = []
player_2 = []

p1_hand = []
p2_hand = []

poker = open('poker.txt', 'r')
for line in poker:
    player_1.append(line[:14])
    player_2.append(line[15:29])

score = 0
score_tie = 0
for i in range(len(player_1)):
    p1_hand = []
    p2_hand = []
    for n in range(0, 14, 3):
        p1_hand.append(player_1[i][n: n+2])
        p2_hand.append(player_2[i][n: n+2])
    p1 = hand_score(p1_hand)
    p2 = hand_score(p2_hand)
    if p1 > p2:
        score += 1
    if hand_score(p1_hand) == hand_score(p2_hand):
        if p1 == 1 or p1 == 5 or p1_hand == 6 or p1_hand == 7 or p1_hand == 8 or p1_hand == 9 or p1_hand == 10:
            if high_card(p1_hand) > high_card(p2_hand):
                score += 1


print(score)
print(p1_hand, p2_hand)
print(high_card(p1_hand), high_card(p2_hand))
print(rm_repeats(p1_hand))

print(time.time() - start)