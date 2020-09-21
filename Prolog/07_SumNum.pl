sum_int(1,A) :- A is 1.
sum_int(X,A) :- X>1,
                X1 is X-1,
                sum_int(X1,A1),
		A is A1+ X.
