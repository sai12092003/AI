% Facts
rainy(chennai).
rainy(coimbatore).
rainy(ooty).
cold(ooty).


rainy_city(City) :-
    rainy(City).

cold_city(City) :-
    cold(City).


happy(X) :-
    rainy_city(X),
    cold_city(X).


% ?- happy(City).
