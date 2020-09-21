% Aiden Stevenson Bradwell
% 300064655
% abrad060@uottawa.ca


% Task Given: Use in order traversal to sum all values within a tree

sumNodes(T,L) :- sumNodes( T, [], L, 0).

sumNodes(nil,L,L,_) :-!.

sumNodes(t(Root,Left,Right),T,L, Sum) :-
    Num is Root + Sum,
    sumNodes(Left,T,LL,Num),
    sumNodes(Right,T,RL,Num),
    append(LL,[Num|RL],L).

inorder(T,L) :- inorder(T,[],L).

inorder(nil,T,T) :-!.
inorder(t(Root,Left,Right),T,L) :-
	inorder(Left,T,LL),
	inorder(Right,T,LR),
	append(LL,[Root|LR],L).