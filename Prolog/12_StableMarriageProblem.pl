:- dynamic happiness/3.
:- dynamic matched/2.
:- dynamic offered/2.
:- dynamic student/1.
:- dynamic company/1.
:- use_module(library(lists)).



%		Aiden Stevenson Bradwell
%		University of Ottawa
%		abrad060@uottawa.ca
%		300064655
%
%		Programmed on April 1st, 2020
%		Submitted to Programming Paradigms for final
%		comprehensive

%		Task Given: Implement the recursive solution to the Stable Marriage problem in prolog.


matched('', '').
offered('', '').


%Main algorithm's offer function given a company list
offer([Company|_]):-
		findall((S1,C),matched(S1,C),M1), %find all currently matched companies
		\+ member((_,Company), M1), % assure this company was not found
		happiness(Company,PotentialStudent,_), % Find the company's first happiest choice
		findall((S2,Company),offered(S2,Company),M2), % Find all students which have been matched
		\+ member((PotentialStudent,Company), M2), % assure this student is not matched
		assert(offered(PotentialStudent, Company)), % this student has now been offered
		evaluate([PotentialStudent, Company]), !. % evaluate the pair

% Main algorithm's offer function given the final company on the list,
% runs exact same as the one above
offer(Company):-
		findall((S1,C),matched(S1,C),M1),
		\+ member((_,Company), M1),
		happiness(Company,PotentialStudent,_),
		findall((S2,Company),offered(S2,Company),M2),
		\+ member((PotentialStudent,Company), M2),
		assert(offered(PotentialStudent, Company)),
		evaluate([PotentialStudent, Company]).

% Main aglorithm's evaluate function given a student and a company pair
evaluate([Student,Company]) :-
	findall((S,C),matched(S,C),M), % Find all matched students
	\+ member((Student,_), M), % If the student is unmatched
	assert(matched(Student, Company)), !. % Then match the two of them


%Otherwise if the student is currently matched
evaluate([Student, Company]) :-
		       matched(Student, Y), %Find the currently matched company
		       happiness(Student, Y, X), % And how happy the student it
			happiness(Student, Company, Z), % and how happy the company is
			\+ Company = Y, % and assure the two companies arent the same
			(X < Z, %If the student would be happier with the new company
			retract(matched(Student, Y)), % then unmatch with current and rematch with new
			assert(matched(Student, Company)),
			offer(Y)); (offer(Company)). %OTHERWISE continue offering current company

% Given the employee data and the student data, run the offer loop and
% execute the algorithm
%
stableMatching(L_employer_preferences, L_student_preferences, M) :-
		                convertCompanyCSV(L_employer_preferences), % Convert given csv information into data & facts
				convertStudentCSV(L_student_preferences), % Convert given csv information into data & facts
				retractall(matched(_,_)), % In case algorithm run twice in same compiler
				retractall(offered(_,_)), % In case algorithm run twice in same compiler
				% Run offer loop for all companies
				offerLoop(L_employer_preferences),										        findall((S,C),matched(S,C),M). % returns a set of all matches at the end

findStableMatch(EmpFileName, StuFileName, M) :-
				retractall(student(_)), % In case algorithm run twice in same compiler
				retractall(company(_)), % In case algorithm run twice in same compiler
				retractall(happiness(_,_,_)), % In case algorithm run twice in same compiler

				get_data(EmpFileName, Empdata), % returns the string representation of the csv file
				get_data(StuFileName, Studata), % returns the string representation of the csv file
				stableMatching(Empdata,Studata, M). % Execute the algorithm
%Offers for each company
offerLoop([]) :- !.
offerLoop([CurCompanySet|Rem]) :-  offerLoop(Rem), % Continue till last company on the list is read
				   offer(CurCompanySet). % Then begin offer proccess

% Runs through the string file, establishing facts for students
convertStudentCSV([]) :- !. % No more students found
convertStudentCSV([Head|Tail]) :- convertStudentCSV(Tail), declare_Student(Head). % send to teh fact declaring function

% Runs through the string file, establishing facts for companies
convertCompanyCSV([]) :- !.
convertCompanyCSV([Head|Tail]) :- convertCompanyCSV(Tail), declare_Company(Head). % send to the fact declaring function

%Student declaring method
declare_Student([]) :- !.
declare_Student([Stu|Pref]) :- student(Stu) ; (assert(student(Stu)), % if this is not already a student then establish it is
			        reverse(Pref, PrefRev), % invert its preferences
				setup_Happiness([Stu|PrefRev])). % begin to give them a hapiness scale
%Company declaring method
declare_Company([]) :- !.
declare_Company([Co|Pref]) :-   company(Co) ; (assert(company(Co)), % if this is not already a company establish that it is
								assert(offered(nil, Co)), % Then assert it has not offered anyone its position yet
								reverse(Pref, PrefRev), % and rever preferences
								setup_Happiness([Co|PrefRev])). % giving them a hapiness rating

% Based on their position in the list, it initializes the happiness of
% the two placed together, increasing the further from 1st they are
setup_Happiness([X|A]) :- length(A,I), setup_Happiness(X, A, _, I).
setup_Happiness(_, [], 1, _) :- !.
setup_Happiness(X,[A|B], N, I) :- setup_Happiness(X,B,N1,I),
								C is I - N1 + 1,
								assert(happiness(X,A,C)),
								N is N1 + 1.

% Runs through a file, and uses the sub functions beneath it to read it
% as a string, and then split it up at the line breaks, followed by
% splitting it up at the commas within
get_data(FileName, FileData) :- open(FileName, read, Stream), % Open file to read data
			        readFile(Stream, Content), % Read the file into a string
				split_string(Content,"\n", " ", LinesSplit), % Split that string at each row
				split_lines(LinesSplit, FileData), % Split those rows into objects
				close(Stream). % Close stream
%Return the string representation of a file
readFile(InStream,Content) :-
		get0(InStream,Char), % Find first character
		checkCharAndReadRest(Char,Chars,InStream), % get full string using this character
		atom_chars(Content,Chars). % convert these into proper letters

checkCharAndReadRest(-1,[],_) :- !. % End of Stream
checkCharAndReadRest(end_of_file,[],_) :- !. % End of file

checkCharAndReadRest(Char,[Char|Chars],InStream) :- % Otherwise keep scanning until one of those is reached
		get0(InStream,NextChar), % next character
		checkCharAndReadRest(NextChar,Chars,InStream). % continue searching

split_lines([], []) :-	!. % no more lines to split
split_lines([H|T], [CurL|OthLines]) :- (split_string(H, ",", " ", CurL)), %recursive call until last line
						 split_lines(T, OthLines). % Then combine all lines post split












