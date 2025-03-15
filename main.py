VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0
    total_aces_in_hand = []
    for card in hand:
        if card not in VALID_CARDS:
            return "That's not a valid card. Try again."
        elif card == 'Ace':
            total_aces_in_hand.append(card)
            score += 11
        elif not isinstance(card, int):
            score += 10
        else:
            score += card

    if score > 21 and len(total_aces_in_hand) > 0:
        score -= (10 * len(total_aces_in_hand))
    elif score > 21:
        score = 'Bust'
    return score

#Refactor sum(hand)