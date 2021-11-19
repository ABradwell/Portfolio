% Aiden Stevenson Bradwell
% 300064655
% abrad060@uottawa.ca


% Task Given: Generate a list of values such that no elements within this list are divisible by the user-given D

divisible([],_):- fail. % Always fail to allow for the recursive or to work, Otherwise it would always be true.
divisible([H|T], C) :- divisible(T,C); C mod H =:= 0. % Either another item in the list divides C or this one does.

generateList(_, 0, []) :- !. % Base case. Create an empty list to be filled.
generateList(D, N, [X|L]) :- N1 is N-1, % Until base case reached
                             generateList(D,N1, L), % Until base case reached
                             length(D, Len), % where Len is the rank of D
                             between(1,Len, X), % Some integer X less than this rank
                             \+ divisible(D, X). % Such that it is not divisible by any item in D
