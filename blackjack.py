import random

def ace_checker(user_cards, user_points):
  for card in user_cards:
    if user_points > 21:
      if card == 11:
        position = user_cards.index(11)
        print(f"ace card value is {user_cards[position]}")
        user_cards[position] = 1
        print(f"ace card value is now {user_cards[position]}")
        user_points = calculate_score(user_cards)
        half_display()
        

def add_cards(user_cards):
  card_choice = random.randint(0, 12)
  user_cards.append(cards[card_choice])

def calculate_score(user_cards):
  score = 0
  for card in user_cards:
    score += card
  return score

def half_display():
  print(f"Your Cards: {player_cards}")
  print(f"my total is {my_points}")
  print(f"Dealer shows {dealer_cards[0]}")


def initial_deal():
  for deal in range(2):
    add_cards(player_cards)
    add_cards(dealer_cards)

def full_display():
  print(f"Player Hand: {player_cards}")
  print(f"Dealer Hand: {dealer_cards}")
  print(f"Player: {my_points}")
  print(f"Dealer: {dealer_points}")
play_more = True
while play_more:
  #initial deal
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_cards = []
  dealer_cards = []
  initial_deal()
  my_points = calculate_score(player_cards)
  half_display()

  #player turn
  hit_me = True
  player_bust = False

  while hit_me:
    response = input("Would you like to add a card? ('y' or 'n')\n")
    if response == 'n' or player_bust == True:
      hit_me = False
      my_points = calculate_score(player_cards)
      dealer_points = calculate_score(dealer_cards)
    elif response == 'y':
      add_cards(player_cards)
      my_points = calculate_score(player_cards)
      dealer_points = calculate_score(dealer_cards)
      half_display()
      if my_points > 21:
        ace_checker(player_cards, my_points)
        
      if my_points > 21:
        player_bust = True
        hit_me = False

  #dealer turn
  dealer_bust = False
  if player_bust == False:
    
    dealer_points = calculate_score(dealer_cards)
    full_display()
    dealer_must_hit = True

    while dealer_must_hit:
      if dealer_points < 17:
        add_cards(dealer_cards)
        dealer_points = calculate_score(dealer_cards)
        full_display()
      elif dealer_points >= 17:
        dealer_must_hit = False
      elif dealer_points > 21:
        ace_checker(dealer_cards, dealer_points)
      if dealer_points > 21:
        dealer_bust = True
        print("dealer busted")
        dealer_must_hit = False
  else:
    print("You busted")
  print("going to determine winner now: \n")
  #determine winner
  if my_points > dealer_points and player_bust == False:
    print("You Won!")
  elif dealer_bust:
    print("You Won!")
  elif my_points == dealer_points:
    print("You Tied!")
  else:
    print("You Lose!")

  response = input("play again? 'y' or 'n'\n")
  if response == 'n':
    print("Goodbye!")
    play_more = False