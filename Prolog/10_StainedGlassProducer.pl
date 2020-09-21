% Aiden Stevenson Bradwell
% 300064655
% abrad060@uottawa.ca


% Task Given: Create a program which can produce color comibinations for a given stained glass window, such that no two touching panes have the same color

%Prepare the database
adj(a,b).
adj(a,g).
adj(b,c).
adj(b,i).
adj(c,d).
adj(d,e).
adj(d,j).
adj(e,l).
adj(f,g).
adj(g,h).
adj(h,i).
adj(i,j).
adj(j,k).
adj(k,l). 

color(red).
color(yellow).
color(blue).

colorset([_|[]],[X|[]]):- color(X).  % Choose any color to begin with
colorset([_|T], [X|C1]) :- colorset(T,C1), color(X). % Choose all next possible colors

diffadjcolor(_,_,[],[]). % End of list found
diffadjcolor(X,C,[H|T], [CH|CT]):-  X1 = X, % Currently looking at plane H w/ color CH
									C1 = C, % Unbalanced Operator error fixed by assigneing to clone variables.
									T1 = T, 
									CT1 = CT,
									diffadjcolor(X1,C1,T1,CT1), %Call method until end of list reached
									(\+ adj(H,X), \+ adj(X,H)); \+ C = CH . % Confirm that allplanes are either not touching, or are not the same as this pane

generate(Gs,Cs):-colorset(Gs,Cs),valid(Gs,Cs).

valid([],[]). % End of list reached.
valid([GH|GT],[CH|CT]) :- diffadjcolor(GH,CH, GT, CT), %Confirm no same-colored panes are touching this pane
						  valid(GT,CT). % Check this for each pane in the set