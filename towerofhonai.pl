
hanoi(1, Source, _, Target) :-
    write('Move disk 1 from '),
    write(Source),
    write(' to '),
    write(Target),
    nl.

hanoi(N, Source, Auxiliary, Target) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Target, Auxiliary),
    hanoi(1, Source, _, Target),
    hanoi(M, Auxiliary, Source, Target).


% Hanoi(3, 'A', 'B', 'C').
