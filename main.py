#Variables, lists and dictionries
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack = {"player_money_amount" : 2500, "player_bet" : 0, "player_hand" : [0, 0], "player_hand_value" : 0,"player_2split_hand" : [0, 0], "player_2split_value" : 0, "dealer_hand" : [0, 0], "dealer_hand_value" : 0}

#Functions

def deal_card() :
  """This function deals a card from the cards list"""
  card = random.choice(cards)
  return card
#

def hit(score) :
  """This function deals a card to the player"""
  score += deal_card()
  print(f"Your score is: {score}")
  if score > 21 :
    return "Bust"
  else :
    return score
  #
#

def play_hand() :
  """This function plays a hand of blackjack"""
  global blackjack
  if blackjack["player_hand_value"] == 21 :
    while blackjack["dealer_hand_value"] < 17 :
      blackjack["dealer_hand_value"] = blackjack["dealer_hand_value"] + deal_card()
    #
    print(blackjack["dealer_hand_value"])
    if blackjack["dealer_hand_value"] == blackjack["player_hand_value"] :
      return "It's a push."
    else :
      return "You win."
  option = input("Hit or Stand? ").lower()
  while option != 'stand' :
    blackjack["player_hand_value"] = hit(score = blackjack["player_hand_value"])
    if blackjack["player_hand_value"] == 'Bust':
      option = 'stand'
    else :
      option = input("Hit or Stand? ").lower()
    #
  #
  if blackjack["player_hand_value"] == 'Bust' :
    outcome = "Bust"
    blackjack["player_money_amount"] -= blackjack["player_bet"]
    return outcome
  #
  while blackjack["dealer_hand_value"] < 17 :
    blackjack["dealer_hand_value"] = blackjack["dealer_hand_value"] + deal_card()
  #
  print(f"Dealer's hand value is: {blackjack['dealer_hand_value']}")
  if blackjack["dealer_hand_value"] > 21 :
    blackjack["player_money_amount"] +=  blackjack["player_bet"]
    return "Win"
  elif blackjack["dealer_hand_value"] > blackjack["player_hand_value"] :
    blackjack["player_money_amount"] -= blackjack["player_bet"]
    return "Lose"
  elif blackjack["dealer_hand_value"] < blackjack["player_hand_value"] :
    blackjack["player_money_amount"] += blackjack["player_bet"]
    return "Win"
  elif blackjack["dealer_hand_value"] == blackjack["player_hand_value"] :
    return "It's a push"
  #
#

def play_hand_split() :
  """This function plays a hand of blackjack with splitting"""
  global blackjack
  outcome_first_split = 0
  outcome_second_split = 0
  print(f"This is for the firs split hand {blackjack['player_hand']}.")
  option = input("Hit or Stand? ").lower()
  while option != 'stand' :
    blackjack["player_hand_value"] = hit(score = blackjack["player_hand_value"])
    if blackjack["player_hand_value"] == 'Bust':
      option = 'stand'
    else :
      option = input("Hit or Stand? ").lower()
    #
  #
  if blackjack["player_hand_value"] == 'Bust' :
    outcome_first_split = "Bust"
  #
  print(f"This is for the second split hand {blackjack['player_2split_hand']}.")
  option = input("Hit or Stand? ").lower()
  while option != 'stand' :
    blackjack['player_2split_hand_value'] = hit(score = blackjack['player_2split_hand_value'])
    if blackjack['player_2split_hand_value'] == 'Bust':
      option = 'stand'
    else :
      option = input("Hit or Stand? ").lower()
    #
  #
  if blackjack['player_2split_hand_value'] == 'Bust' :
    outcome_second_split = "Bust"
  #
  if outcome_first_split == "Bust" and outcome_second_split == "Bust" :
    blackjack["player_money_amount"] -=  2 * blackjack["player_bet"]
    return "Both hands are a bust."
  #
  while blackjack["dealer_hand_value"] < 17 :
    blackjack["dealer_hand_value"] = blackjack["dealer_hand_value"] + deal_card()
  #
  print(f"Dealer's hand value is: {blackjack['dealer_hand_value']}")
  if blackjack["dealer_hand_value"] > 21 :
    if outcome_first_split == 'Bust':
      return "The second hand is a winner, the first one is a bust."
    elif outcome_second_split == 'Bust' :
      return "The first hand is a winner, the second one is a bust."
    blackjack["player_money_amount"] +=  2 * blackjack["player_bet"]
    return "You win both hands."
  elif outcome_first_split == "Bust" and blackjack['player_2split_hand_value'] < blackjack["dealer_hand_value"]:
    blackjack["player_money_amount"] -=  2 * blackjack["player_bet"]
    return "The first hand is a bust and you lose the second one."
  elif outcome_first_split == "Bust" and blackjack['player_2split_hand_value'] > blackjack["dealer_hand_value"]:
    return "The first hand is a bust and you win the second one."
  elif outcome_first_split == "Bust" and blackjack['player_2split_hand_value'] == blackjack["dealer_hand_value"]:
    blackjack["player_money_amount"] -=  blackjack["player_bet"]
    return "The first hand is a bust and the second one has the same hand value for the cards."
  elif blackjack["dealer_hand_value"] > blackjack["player_hand_value"] and outcome_second_split == "Bust":
    blackjack["player_money_amount"] -=  2 * blackjack["player_bet"]
    return "You lost the first hand and the second one is a bust."
  elif blackjack["dealer_hand_value"] < blackjack["player_hand_value"] and outcome_second_split == "Bust":
    return "You win the first hand and the second one is a bust."
  elif blackjack["dealer_hand_value"] == blackjack["player_hand_value"] and outcome_second_split == "Bust":
    blackjack["player_money_amount"] -=  blackjack["player_bet"]
    return "You and the dealer have the same hand value for the firs split and the second one is a bust."
  elif blackjack["dealer_hand_value"] < blackjack["player_hand_value"] and blackjack['player_2split_hand_value'] > blackjack["dealer_hand_value"]:
    blackjack["player_money_amount"] +=  2 * blackjack["player_bet"]
    return "You win both hands."
  elif blackjack["dealer_hand_value"] > blackjack["player_hand_value"] and blackjack['player_2split_hand_value'] < blackjack["dealer_hand_value"]:
    blackjack["player_money_amount"] -=  2 * blackjack["player_bet"]
    return "You lost both hands."
  elif blackjack["dealer_hand_value"] < blackjack["player_hand_value"] and blackjack['player_2split_hand_value'] < blackjack["dealer_hand_value"]:
    return "You win the first hand but lost the second one."
  elif blackjack["dealer_hand_value"] > blackjack["player_hand_value"] and blackjack['player_2split_hand_value'] > blackjack["dealer_hand_value"]:
    return "You lost the first hand but win the second one."
  elif blackjack["dealer_hand_value"] == blackjack["player_hand_value"] and blackjack['player_2split_hand_value'] == blackjack["dealer_hand_value"]:
    return "You and the dealer have the same hand value for the cards.It's a push."
  elif blackjack["dealer_hand_value"] == blackjack["player_hand_value"] and blackjack['player_2split_hand_value'] > blackjack["dealer_hand_value"]:
    blackjack["player_money_amount"] +=  blackjack["player_bet"]
    return "You and the dealer have the same hand value for the first split and you win the second one."
  elif blackjack["dealer_hand_value"] == blackjack["player_hand_value"] and blackjack['player_2split_hand_value'] < blackjack["dealer_hand_value"]:
    blackjack["player_money_amount"] -=  blackjack["player_bet"]
    return "You and the dealer have the same hand value for the first split and you lose the second one."
  elif blackjack["dealer_hand_value"] > blackjack["player_hand_value"] and blackjack['player_2split_hand_value'] == blackjack["dealer_hand_value"]:
    blackjack["player_money_amount"] -=  blackjack["player_bet"]
    return "You lose the first hand and you have the same hand value as the dealer for the second split."
  elif blackjack["dealer_hand_value"] < blackjack["player_hand_value"] and blackjack['player_2split_hand_value'] == blackjack["dealer_hand_value"]:
    blackjack["player_money_amount"] +=  blackjack["player_bet"]
    return "You win the first hand and you have the same hand value as the dealer for the second split."
  #
#

def check_insurance() :
  """This function checks if the dealer has a 11 as the face card , if the player wants to take insurance and plaies from there."""""
  global blackjack
  if blackjack["dealer_hand"][0] == 11 :
    insurance = input("Do you want to take insurance? Type 'yes' if you want , 'no' if you don't: ").lower()
    if insurance == 'yes' :
      second_bet = int(input("How much do you want to bet?\n$ "))
      while second_bet > blackjack["player_bet"] / 2 :
        second_bet = int(input(f"You can bet up to half the original bet, which is {blackjack['player_bet'] / 2 } . Try again:  "))
      #
      if blackjack["dealer_hand"][1] == 10 :
        if blackjack["player_hand_value"] < 21 :
          blackjack["player_money_amount"] -= (blackjack["player_bet"] - second_bet)
          return "Yuo win the insurance but lost the original bet."
        #
      else :
        print("You lost the insurance.")
        blackjack["player_money_amount"] -= second_bet
        outcome = play_hand()
        return outcome
      #
    else :
      outcome = play_hand()
      return outcome
    #
  else :
    outcome = "No insurance."
    return outcome
  #
#

def check_split() :
  """This function checks if the player has split and if so, splits the hand"""
  global blackjack
  if blackjack["player_bet"] > blackjack["player_money_amount"] / 2 :
    print("You don't have enough money to split.")
    outcome = check_double_down()
    print(outcome)
    if outcome == "You don't have the hand value equal to 9 or 10 or 11. You cannot double down.":
      outcome = play_hand()
    return outcome
  #
  blackjack["player_2split_hand"][0] = 0
  blackjack["player_2split_hand"][1] = 0
  if blackjack["player_hand"][0] == blackjack["player_hand"][1] :
    split = input("Do you want to split your cards? Type 'yes' if you want , 'no' if you don't: ").lower()
    if split == 'yes' :
      first_split_card = deal_card()
      second_split_card = deal_card()
      blackjack["player_hand"][1] = first_split_card
      blackjack["player_hand_value"] = blackjack["player_hand"][0] + blackjack["player_hand"][1]
      blackjack["player_2split_hand"][0] = blackjack["player_hand"][0]
      blackjack["player_2split_hand"][1] = second_split_card
      blackjack["player_2split_hand_value"] = blackjack["player_2split_hand"][0] + blackjack["player_2split_hand"][1]
      outcome = play_hand_split()
      return outcome
    else :
      outcome = play_hand()
      return outcome
    #
  else :
    return "You don't have two equal cards. You cannot split."
  #
#

def check_double_down() :
  """This function checks if the player has double down and if so, doubles the bet"""
  global blackjack
  if blackjack["player_hand_value"] == 9 or blackjack["player_hand_value"] == 10 or blackjack["player_hand_value"] == 11 :
    double_down = input("Do you want to double down? Type 'yes' if you want , 'no' if you don't: ").lower()
    if double_down == 'yes' :
      draw_card = deal_card()
      blackjack["player_hand"].append(draw_card)
      blackjack["player_hand_value"] += draw_card
      print(f"This is your hand {blackjack['player_hand']} and the value of your hand is {blackjack['player_hand_value' ]}.")
      while blackjack["dealer_hand_value"] < 17 :
        blackjack["dealer_hand_value"] = blackjack["dealer_hand_value"] + deal_card()
      #
      print(f"Dealer's hand value is: {blackjack['dealer_hand_value']}")
      if blackjack["dealer_hand_value"] > 21 :
        blackjack["player_hand"].remove(draw_card)
        blackjack["player_money_amount"] += 2 * blackjack["player_bet"]
        return "Win"
      elif blackjack["dealer_hand_value"] > blackjack["player_hand_value"] :
        blackjack["player_hand"].remove(draw_card)
        blackjack["player_money_amount"] -= 2 * blackjack["player_bet"]
        return "Lose"
      elif blackjack["dealer_hand_value"] < blackjack["player_hand_value"] :
        blackjack["player_hand"].remove(draw_card)
        blackjack["player_money_amount"] += 2 * blackjack["player_bet"]
        return "Win"
      elif blackjack["dealer_hand_value"] == blackjack["player_hand_value"] :
        blackjack["player_hand"].remove(draw_card)
        return "It's a push"
      #
    else :
      outcome = play_hand()
      return outcome
    #
  else :
    return "You don't have the hand value equal to 9 or 10 or 11. You cannot double down."
  #
#
     
  
      
def play_balckjack() :
  global blackjack
  if blackjack["player_money_amount"] == 0 :
    print("You don't have any money to play.The game is over.")
    return "You don't have any money to play."
  #
  blackjack["player_bet"] = int(input("How much do you want to bet?\n$"))
  while blackjack["player_bet"] > blackjack["player_money_amount"] :
    blackjack["player_bet"] = int(input("This is more than you have in your bank. Choose a lesser sum?\n$"))
  blackjack["player_hand"][0] = deal_card()
  blackjack["player_hand"][1] = deal_card()
  print(f"Your hand is: {blackjack['player_hand']}")
  blackjack["player_hand_value"] = blackjack["player_hand"][0] + blackjack["player_hand"][1]
  print(f"Your hand value is: {blackjack['player_hand_value']}")
  blackjack["dealer_hand"][0] = deal_card()
  blackjack["dealer_hand"][1] = deal_card()
  print(f"Dealers firs card is: {blackjack['dealer_hand'][0]}")
  blackjack["dealer_hand_value"] = blackjack["dealer_hand"][0] + blackjack["dealer_hand"][1]
  result = check_insurance()
  print(result)
  if result == "No insurance.":
    result = check_split()
    print(result)
    if result == "You don't have two equal cards. You cannot split." :
      result = check_double_down()
      print(result)
      if result == "You don't have the hand value equal to 9 or 10 or 11. You cannot double down." :
        result = play_hand()
        print(result)
      #
    #
  #
  print(f"You have {blackjack['player_money_amount']}$ in the bank.")
  play_balckjack() 
#

############################## MAIN CODE ################################


print(art.logo)
print("Welcome to Blackjack!")
print(f"You have {blackjack['player_money_amount']}$ in the bank.")
# cash = int(input("How much mone"))
play_balckjack()
