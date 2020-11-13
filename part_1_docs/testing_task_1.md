### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # should be double equals ==
      return True
    else # needs colon
      return False
   

  dif highest_card(self, card1 card2): # should be def and missing comma between card 1 and 2
  if card1.value > card2.value: # indentation
    return card # should be card 1
  else:
    return card2
  


def cards_total(self, cards): # indentation didnt notice til last test!
  total # variable total not defined. Should be total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total # needs to be wrapped in formatted print statement also need indentation fixed to allow for loop to work correctly
  
```
