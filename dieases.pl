
 symptom(amit, fever).
symptom(amit, rash).



hypothesis(Name, Disease) :-
    symptom(Name, Symptom).




%?- hypothesis(amit, Disease).
