#lang scheme
;; Aiden Stevenson Bradwell
;; 300064655
;; abrad060@uottawa.ca
;; March 28th, 2020

;;Use the built-in filter and map to change a list as follows
;;Drop each number between -1 and +1 inclusive
;;For each number greater than 1 replace the number with 10 times the number
;;For each number smaller than -1 replace the number with the absolute value of the reciprocal.



(define (changeList l)
  (define l1 (filter (lambda (x) (or (> x 1)(< x -1)))
                     l))
  (define l2 (map (lambda (x) (* 10 x))
                  (filter (lambda (y) (> y 1)) l1)
                  ))
  (define l3 (map (lambda (x) (/ 1 (sqrt (* x x)))) l1))
  (append l2 l3)
  )
  
  
(changeList '(0 -2 3 -4 1))


;;QUESTION TWO
;;Find the longest sub-list of numbers which are identical and return this sub-list.
;;In case of a tie, return the sub-list occurring last.
(define (sameNum lst)
  (sameNumhelper '() '() lst)
  )

(define (sameNumhelper curLongest curCheck lst)
  (cond
    [(list? lst) ;; if there are more items remaining
     (cond
       [(not (pair? curCheck)) ;; and we arent currently in a run (for first call)
        (cond
          [(not (pair? (cdr lst))) (list (car lst))] ;; If the tail is empty, Then it must only be the head
          [else ;; Otherwise
           (sameNumhelper curLongest (list (car lst)) (cdr lst))]) ;; Recursive call with the head as the start of the first run
        ]
       [(= (car lst) (car curCheck)) ;; Is the current head a continuation of the run?
        (cond
          [(>= (length (append curCheck (list (car curCheck)))) ;; if so, see if this run is longest yet
               (length curLongest)) ;; replace if so
           (cond
             [(not (pair? (cdr lst))) (append  curCheck (list (car curCheck)))] ;; if last element, return the extended run as the largest
             [else (sameNumhelper (append  curCheck (list (car curCheck))) ;; otherwise recursive call with this extended run as the new longest
                                  (append  curCheck (list (car curCheck)))
                                  (cdr lst))])
           ]
          [else ;; If it is a continuation but not the longest
           (cond
             [(not (pair? (cdr lst))) curLongest] ;; and the list ends then return the current longest
             [else (sameNumhelper curLongest (append curCheck  (list (car curCheck))) (cdr lst))])] ;; otherwise recursive call with the current run continued
          )]
       [else ;; if it is not a continuation
        (sameNumhelper curLongest (list (car lst)) (cdr lst))] ;; start a new run and send it into a recursive call
       )]
    [else ;; Otherwise there are no more items remaining
     (curLongest) ;; thus return the current longest run
     ])
  )

(sameNum '( 0 1 5 3 3 3 2 1 1))
(sameNum '( 0 1 5 3 3 3 2 1 1 1 ))
(sameNum '( 0 1 5 3 3 3 3 2 1 1 1 ))
(sameNum '( 1 ))

;;QUESTION THREE
;;Implement a function destination that tallies the vote for where a group of friends want to travel to.
;;Each friend votes for three destinations. The result needs to be a list containing all destinations that
;;received the most votes (ties are possible).
;;





;;This runs on a system which takes each placement of vote (IE peru 1st choide) and places it in a
;; List that many times (1 time for peru), and then counts the least amount of occurances. Thus, the most popular overall.

(define (destination coupledList)
  (define overallList (expandFromStart coupledList)) ;; Fully expanded rating system list
  (define votedFor (car (cdr (car coupledList)))) ;; which places were options
  ;; Counts the number of occurances and puts them into pairs of (PLACE, RATING)
  (define votedScores (map (lambda(i)(cons i (length (filter (lambda (y) (equal? i y)) overallList)))) votedFor))
  ;; Finds the lowest rating, and therefore the most popular
  (findLowestScore votedScores 100 '())
  )

;; Function which determines which place occurs the least in the overall list
(define (findLowestScore votedScores curLow curWinners)
  (define curPair (car votedScores)) ;; The place currently being looked at
  (define curScore (cdr curPair)) ;; The number of occurances it has
  (cond [(and (list? (cdr votedScores)) (pair? (cdr votedScores))) ;; if a list and not empty
         (cond [(< curScore curLow)(findLowestScore (cdr votedScores) curScore (list curPair))] ;; and it is a lower score then set as new lowest
               [(= curScore curLow)(findLowestScore (cdr votedScores) curScore (append (list curPair) curWinners))] ;; if equal than add to list of winners
               [else (findLowestScore (cdr votedScores) curLow curWinners)])] ;; Otherwise disregard
        [else (cond
                [(< curScore curLow)(list curPair)] ;; Return current place if lowest
                [(= curScore curLow)(append (list curPair) curWinners)] ;; Return winners and this place if tied
                [else curWinners])] ;; Return the winning places
        ))
;; Function which takse votes and converts them into one massive list
(define (expandFromStart coupledList)
  (define curPer (car coupledList)) ;; The current person being tallied
  (define curperchoices  (car (cdr curPer))) ;; Take their choices
  ;; recursivly combine all extended lists  
  (cond [(pair? (cdr coupledList)) (append (expandFrompersonsChoice curperchoices) (expandFromStart (cdr coupledList)))]
        [else (expandFrompersonsChoice curperchoices)])
  )

(define (expandFrompersonsChoice chosen)
  (define str1 (list-ref chosen 0)) ;; first choice
  (define str2 (list-ref chosen 1)) ;; second choice
  (define str3 (list-ref chosen 2)) ;;  thid choice
  (append (append (repList str1 1) (repList str2 2)) (repList str3 3)) ;; make a list that represents tat
  )

(define (repList str num) ;; The creation of the list per choice
  (cond[(> num 0) (append (list str) (repList str (- num 1)))]
       [else (list str)]))

(define (translate lst) ;; Designed algorithm with list instead of ' so this converts
  (map (lambda(i)(list (car (car (cdr i))) (car(cdr (car (cdr (car (cdr i)))))))) lst))
  

(define choices '('("marie" '("peru" "greece" "vietnam"))
 '("jean" '("greece" "peru" "vietnam"))
 '("sasha" '("vietnam" "peru" "greece"))
 '("helena" '("peru" "vietnam" "greece"))
 '("emma" '("greece" "peru" "vietnam"))))

(define choices2 '('("marie" '("peru" "greece" "vietnam"))
 '("jean" '("greece" "peru" "vietnam"))
 '("sasha" '("vietnam" "peru" "greece"))
 '("helena" '("peru" "vietnam" "greece"))
 '("emma" '("greece" "peru" "vietnam"))
 '("jane" '("greece" "vietnam" "peru"))))

(destination (translate choices))
(destination (translate choices2))


;; QUESTION FOUR
;;
;; Write a program that simulates a Neural Network in Scheme. We use what is called a multilayer
;; perceptron with 1 hidden layer with an input and output layer. Each neuron calculates the weighted sum
;; of its input (including an offset) and applies an activation function. Consider the figure below. for the
;; example of a slice of size 2.


(define (sigmond v) (/ 1 (+ 1 (expt (exp 1) (- 0 v ))))) ;; signma function
(define ((neuralNode weightLst func) inLst) ;; The neural node function
  (define v1 (car weightLst))
  (define v2 (car (cdr weightLst)))
  (define v3 (car (cdr (cdr weightLst))))
  (define x1 (car inLst))
  (define x2 (car ( cdr inLst)))
  (func (+ v1 (+ (* v2 x1) (* v3 x2)))))

(define ((neuralLayer weightLists) inputList)
  (define x1 (car inputList))
  (define x2 (car ( cdr inputList)))
  (define w1 (car weightLists))
  (define w2 (car (cdr weightLists)))
  (define w3 (car (cdr (cdr weightLists))))
  (define node1 ((neuralNode w1 sigmond) (list x1 x2)))
  (define node2 ((neuralNode w2 sigmond) (list x1 x2)))
  (define node3 ((neuralNode w3 sigmond) (list x1 x2)))
  (append (list node1) (list node2 node3)))

(define (neuralNet inputList)
  (define x1 (car inputList))
  (define x2 (car ( cdr inputList)))
  (define w1 (list 0.1 0.3 0.4))
  (define w2 (list 0.5 0.8 0.3))
  (define w3 (list 0.7 0.6 0.6))
  
  (define layer1 ((neuralLayer (list w1 w2 w3)) (list x1 x2)))
  
  (define z1 (car layer1))
  (define z2 (car (cdr layer1)))
  (define z3 (car (cdr (cdr layer1))))
  
  (list (sigmond (+ 0.5 (+ (* z1 0.3) (+ (* 0.7 z2) (* 0.1 z3)))))))

(define (applyNetHelper k n)
  (define in1 (sin (/ (* 2 (* 3.14159 (- n 1))) n)))
  (define in2 (cos (/ (* 2 (* 3.14159 (- n 1))) n)))
  (cond [(< n k)(append (neuralNet (list in1 in2)) (applyNetHelper k (+ n 1)) )]
        [else  (neuralNet (list in1 in2))]))

(define (applyNet k)
  (applyNetHelper k 1))
(neuralNode (list 0.1 0.3 0.4) sigmond)
((neuralNode (list 0.1 0.3 0.4) sigmond) (list 0.5 0.5))
(neuralLayer '((0.1 0.3 0.4)(0.5 0.8 0.3)(0.7 0.6 0.6)))
((neuralLayer '((0.1 0.3 0.4)(0.5 0.8 0.3)(0.7 0.6 0.6))) '(0.5 0.5))
(neuralNet '(0.5 0.5))
(applyNet 16)





