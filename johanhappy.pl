happy(X):-win(X),exampassed(X).

passedexam(X):-studeies(X),lucky(X).
lucky(happy).

goal(X):-
    lucky(X).
