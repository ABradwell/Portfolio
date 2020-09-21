% Aiden Stevenson bradwell
% 300064655
% abrad060@uottawa.ca

%A nice month is defined as a month which is higher or equal to its expected temperature, as defined in the inital statemnt of weekends

weekends(march, 2020,
		[-4, 1, 6, 4,-2,-4, 0, 7, 8],
		[-1, 0, 0, 2, 2, 4, 4, 6 ,6]).

difference([],[],[]). %base case : no more comparisons exist, so initalize return list as empty

difference([H1|T1], [H2|T2],[Dif|L1]):- difference(T1,T2,L1), % Given two lists, return the difference between their heads, and the rest of the already generated differences as the tail
                                Dif is  H1-H2. % Find difference. This is teh new head of the return list

positive([], 0):- !. % Base case reached, start counter at 0
positive([H|T], N) :- H >= 0, % If head is greater than zero
                      positive(T, N1), % Call counter on tail
                      N is N1 + 1. % and add 1 to the result

positive([H|T], N) :- H < 0, % Otherwise head is less than 0
                      positive(T, N). % So simply call counter on tail, and relay count back

niceMonth(Month, Year) :-  weekends(Month,Year, WeekEndTemperature, Normals), % Get infomration for a given month and year
                             difference(WeekEndTemperature, Normals, D), % Find the differences for the expected and actual for that dataset
                             positive(D, N), % Count how many of those differences were better than expected
                             length(WeekEndTemperature, L), % # of days
                             Goal is L/2, % Goal (is # of days)/2
                             N >= Goal. % True false if this was in fact a good month (did it pass the goal of half better days)



