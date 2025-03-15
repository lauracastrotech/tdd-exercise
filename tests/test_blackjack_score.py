from main import blackjack_score
import pytest

# @pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
    # Arrange
    hand = [3, 4]

    # Act
    score = blackjack_score(hand)

    # Assert <-- Write assert statement here
    assert score == 7

# @pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
    hand_1 = ['King', 5]
    hand_2 = ['Queen', 'Jack']

    score_1 = blackjack_score(hand_1)
    score_2 = blackjack_score(hand_2)

    assert score_1 == 15
    assert score_2 == 20

# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
    hand_1 = ['Jack', 'Ace']
    hand_2 = [6,'Ace']
    hand_3 = [3,2,'Ace']

    score_1 = blackjack_score(hand_1)
    score_2 = blackjack_score(hand_2)
    score_3 = blackjack_score(hand_3)

    assert score_1 == 21
    assert score_2 == 17
    assert score_3 == 16


# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
    hand =[10, 2, 'Ace']
    score = blackjack_score(hand)
    assert score == 13

# @pytest.mark.skip(reason="no way of currently testing this")
# def test_returns_invalid_for_invalid_cards():
#     hand_1 = ['@', 4, 'Jack']
#     hand_2 = [11, 6]
#     hand_3 = [True, 2.3]

#     with pytest.raises(AttributeError):
#         blackjack_score(hand_1)
#         blackjack_score(hand_2)
#         blackjack_score(hand_3)

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
    hand_1 = [1,2,3,4,5,6]
    hand_2 = [1,2]
    

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
    hand = ['Jack', 5, 7]
    score = blackjack_score(hand)
    assert score == 'Bust'

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
    hand = ['Ace','Ace','King']
    score = blackjack_score(hand)
    assert score == 12

# @pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
    pass