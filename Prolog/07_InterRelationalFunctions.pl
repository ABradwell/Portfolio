% Aiden Stevenson Bradwell
% 300064655
% abrad060@uottawa.ca


% Task Given: Create a relation of functions which will apply cosN N number of times


% Factorial from class
 fact(0, 1).
 fact(N, F) :- N > 0,
		  N1 is N-1,
		  fact(N1, F1),
		  F is F1 * N.

 % Calculate -1 ^ K
 signCnt(0,1).
 signCnt(K,S) :- K > 0,
		  K1 is K - 1,
		  signCnt(K1,S1),
		  S is 0-S1.

% Base case
 cosN(N,N,_,1).

% Recursive case
 cosN(K,N,X,Y) :- K < N,
		  signCnt(K,S),
		  K2 is 2 * K,
		  fact(K2,F),
		  Yk is (S * X**K2)/F,
		  K1 is K + 1,
		  cosN(K1,N,X,Y3),
		  Y is Yk + Y3.

cosN(N,X,Y) :- N>0, cosN(0,N,X,Y).
