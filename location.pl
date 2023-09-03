location(desk,office).
location(apple,kitchen).
location(flashlight,house).

findlocation(Item,Location):-
    location(Item,Location).

%?-findloatin(desk,Location).
