
first_name(tonyblair, tony).
first_name(georgebush, georgedubya).
second_name(tonyblair, blair).
second_name(georgebush, bush).


full_name(Person, FirstName, SecondName) :-
    first_name(Person, FirstName),
    second_name(Person, SecondName).

% ?- full_name(tonyblair, FirstName, SecondName).


% ?- full_name(georgebush, FirstName, SecondName).
