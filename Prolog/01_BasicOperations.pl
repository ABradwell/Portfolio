% Aiden Stevenson Bradwell
% 300064655
% abrad060@uottawa.ca


% Task Given: Experiment with the syntax of Prolog

%Comment
%Variable are capitalized
%functions are not

% X < Y
% X =< Y
% X =:= Y
% X =\= Y
% X >= Y
% X > Y

% \+ not

% [H| []] only head remaining


numOccur(_,[],0).
numOccur(X, [H|T], R):- H=:=X, numOccur(X, T, R1), R is R1 + 1, !.
numOccur(X, [H|T], R):- H =\= X, numOccur(X, T, R), !.


flip([], []).

flip([ (A,B) | T ], L ) :- flip(T, L1), append(L1, [(B,A)], L).
