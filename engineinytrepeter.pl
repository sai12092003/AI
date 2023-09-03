% Define some facts and rules
happy(john).
study(john, history).
win_lottery(john).
lucky(john).
pass_exam(X) :- study(X, _), lucky(X).

% Define the inference engine predicates
interpret(true) :- !.
interpret((GoalA, GoalB)) :- !,
    interpret(GoalA),
    interpret(GoalB).
interpret(Goal) :-
    call(Goal), % Attempt to call the Goal
    write('Goal: '), write(Goal), write(' is true.'), nl.
interpret(Goal) :-
    write('Goal: '), write(Goal), write(' is false.'), nl.

% Main query to check if John is happy
check_happiness :-
    interpret(happy(john)).

% Example usage:
% Run the query to check if John is happy
% You can add more facts and queries as needed.
