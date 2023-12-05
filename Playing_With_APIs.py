#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json

def __get_deck__id():
    response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6")
    deck_id = (response.json()['deck_id'])
    return deck_id    

def __draw_three_cards(deck_id):
    #print("https://deckofcardsapi.com/api/deck/"+__get_deck__id()+"/draw/?count=2")
    url = "https://deckofcardsapi.com/api/deck/"+__get_deck__id()+"/draw/?count=10"
    response = requests.get(url)
    return response.json()
    

    


    


# In[4]:


#__draw_three_cards(__get_deck__id())


# In[5]:


# Get deck_id
deck_id = __get_deck__id()

# Draw three cards


drawn_cards_response = __draw_three_cards(deck_id)

# Retrieve values of "value" and "suit" from each card
for card in drawn_cards_response['cards']:
    card_value = card['value']
    card_suit = card['suit']
    print(f"Card Value: {card_value}, Card Suit: {card_suit}")


# In[ ]:




