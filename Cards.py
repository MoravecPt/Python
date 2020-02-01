deck=[]
cards = ("A",2,3,4,5,6,7,8,9,10,"J","Q","K")
suits = ('\u2660','\u2665','\u2666','\u2663')
for card in cards:
        for suit in suits:
                a={card:suit}
                deck.append(a)
print(deck,'\n\n',len(deck),"cards")

 #test
