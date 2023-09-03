firstn(swethanair,swetha).
lastn(swethanair,nair).

findfirstlastname(Name,Firstname,Lastname):-
    firstn(Name,Firstname),
    lastn(Name,Lastname).


