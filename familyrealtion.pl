% Facts
female(sarah).
female(rebekah).
female(hagar_concubine).
female(milcah).
female(bashemath).
female(mahalath).
female(first_daughter).
female(rachel).
female(labans_wife).

male(terah).
male(abraham).
male(nahor).
male(haran).
male(isaac).
male(ismael).
male(uz).
male(kemuel).

% Family relations
parent(terah, abraham).
parent(terah, nahor).
parent(terah, haran).
parent(abraham, isaac).
parent(abraham, ismael).
parent(haran, lot).
parent(rebekah, isaac).
parent(hagar_concubine, ismael).
parent(labans_wife, first_daughter).
parent(labans_wife, rachel).
parent(labans_wife, milcah).
parent(labans_wife, bashemath).
parent(labans_wife, mahalath).
parent(isaac, uz).
parent(isaac, kemuel).


mother(Mother, Child) :-
    female(Mother),
    parent(Mother, Child).

father(Father, Child) :-
    male(Father),
    parent(Father, Child).





% ?- mother(Mother, isaac).
