:- dynamic happiness/3.
:- dynamic matched/2.
:- dynamic offered/2.
:- dynamic isMatched/2.
:- dynamic student/1.
:- dynamic company/1.
:- use_module(library(apply)).
:- use_module(library(lists)).


get_data(FileName, FileData) :- open(FileName, read, Stream),
								atom_chars(M, [10]),
								print(M),
								readFile(Stream, Content),
								split_string(Content,"\n", " ", LinesSplit),
								split_lines(LinesSplit, FileData).	

readFile(InStream,Content) :-
		get0(InStream,Char),
		checkCharAndReadRest(Char,Chars,InStream),
		atom_chars(Content,Chars).

checkCharAndReadRest(-1,[],_) :- !. % End of Stream
checkCharAndReadRest(end_of_file,[],_) :- !.

checkCharAndReadRest(Char,[Char|Chars],InStream) :-
		get0(InStream,NextChar),
		print(NextChar),
		checkCharAndReadRest(NextChar,Chars,InStream).

split_lines([], []) :-	!.
split_lines([H|T], [CurL|OthLines]) :- (split_string(H, ",", " ", CurL)),
						 split_lines(T, OthLines).