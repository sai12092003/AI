colour(cherry,red).
colour(banana,yellow).
colour(apple,green).
colour(apple,red).
colour(orange,orange).
colour(x,unknown).

findfruit(Fruitname,Colour):-
    colour(Fruitname,Colour).
