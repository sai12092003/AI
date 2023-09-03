
american(robert).
enemy(america, country_a).
has_missiles(country_a).
sells(robert, X) :- american(X).


criminal(X) :-
    sells(X, y),
    enemy(america, Z),
    has_missiles(Z).


%?- criminal(robert).
