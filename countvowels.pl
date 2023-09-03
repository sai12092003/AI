% Define the vowels
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).


count_vowels([], 0).

count_vowels([Head | Tail], Count) :-
    vowel(Head),          % If the head is a vowel
    count_vowels(Tail, RestCount), % Count the vowels in the tail
    Count is RestCount + 1.       % Increment the count.

count_vowels([_ | Tail], Count) :-
    count_vowels(Tail, Count). % If the head is not a vowel, skip it.


count_vowels_in_sentence(Sentence, TotalCount) :-
    string_chars(Sentence, CharList), % Convert the sentence to a list of characters
    count_vowels(CharList, TotalCount). % Call the counting predicate

% Example usage:
sentence("This is my first Degree in Saveetha School of Engineering.", Count),
write("Total vowels: "), write(Count).
