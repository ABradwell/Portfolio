#lang scheme
;; Aiden Stevenson Bradwell
;; 300064655
;; abrad060@uottawa.ca


(define names
 '("marie" "jean" "claude" "emma" "sam" "tom" "eve" "bob"))

;; Part One
(define (first N L)
  (cond
    [(not (pair? L)) '()] ;; If end of list reached, begin return call
    [(> N 0) (append (list (car L)) (first (- N 1) (cdr L)))] ;; If not at the Nth person, recurive, and add current eprson to list
    [else '()])) ;;Now at Nth person, begin list return

(define (insertAt El1 L N)
  (cond
    [(not (pair? L)) (list El1)] ;;If only item is this elemnest, list it and return
    [(> N 0) (append (list (car L)) (insertAt El1 (cdr L) (- N 1)))] ;; If not at the Nth person, recurive, and add current eprson to list
    [else (append (list El1) L)])) ;; Reached location, combine this element infront of the rest of the list

(define (shuffle lst n)
  (cond
    [(= n 0) lst] ;; If all shuffle calls have been made return shuffled
    [(> n 0) ;; If some calls remain
     (shuffle ;; New shuffle call
      (insertAt
          (car lst) ;; With start of deck
          (cdr lst) ;; Inserted into the rest of it
          (random (- (length names) 1))) ;; At this random location
      (- n 1))] ;; to inform another hsuffle has been made, lower counter by 1
    ))

(define (winner lst n)
 (first n (shuffle lst 20)))

(winner names 3)


 
