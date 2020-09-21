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