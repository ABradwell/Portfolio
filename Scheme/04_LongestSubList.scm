#lang scheme
;; Aiden Stevenson Bradwell
;; 300064655
;; abrad060@uottawa.ca
;; March 28th, 2020


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