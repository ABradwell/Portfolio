#lang scheme
;; Aiden Stevenson Bradwell
;; 300064655
;; abrad060@uottawa.ca
;; March 28th, 2020

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