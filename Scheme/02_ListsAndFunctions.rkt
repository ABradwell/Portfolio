#lang racket
;Use cons to build the following lists:
;
;		'(3 4)
;		'(1 2 3)
;		'(a (b c))
;		'(1)
;		'(2 (3 (4)))
(cons 3 4)
(cons 1 (list 2 3))
(cons "a" (list "b" "c"))
(list 1)
(list 2 (list 3 (list 4)))



;  	Example:
;       (define L '(1 2 3 4 5))    
;
; 	(car L)
; 	=> 1
;
; 	(cdr L)
;       => '(2 3 4 5)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Combine calls car and cdr to get the element 2 and 5 from the list LL (2 solutions).

;       (define LL '(1 (2 3 4) (5)))    
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(define L '(1 2 3 4 5))
(car (cdr L))
(car (cdr (cdr L)))
(car (cdr (cdr (cdr L))))
(car (cdr (cdr (cdr (cdr L)))))


;       Give a function that creates a list with integers in the specified range.
;       The function takes two indices, i and k, and produces the integers
;       between i and k including i and k.
;
; 	Example:
; 	(range 4 9)
; 	=> (4 5 6 7 8 9)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(define (range start end) ( begin
                             (let ([X (+ end 1)])
                               (for/list (
                                          [i (in-range start X)]
                                          )
                                 i)
                               )
                             )
  )

(range 4 9)

; Consider the digits d_k,d_(k-1),…,d_1,d_0 of a positive integer number. The squares of the digits are then s = d_k^2 + d_(k-1)^2 + … + d_1^2 + d_0^2.
; Create a function sosd that calculates the sum of square digits.
;
;   The function calculates the sum of square digits. 
;
; 	Example:
;  (sosd 130)
; 	=> 10
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (isValid num rages)
  (define valid #f)
  (define curCount 0)
  (define endRange (+ num 1))
  (for([i endRange])
    (set! curCount (+ curCount (* i i))))
  (set! valid (<= curCount rages))
  valid
  )

(define (sosd rages)
  (define count 1)
  (define endRange (+ rages 1))
  (for([i endRange]
       #:when (isValid i rages))
    (set! count (+ count 1)))
  count
  )

(sosd 130)


;      The function takes a list and a number selecting every kth
;      element. Start counting at 1.
;
; 	Example:
; 	(drop '(a b c d e f g h i k) 3)
; 	=> (a b d e g h k)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(define (drop lst k)
  (define index 0)
  (define outlist list)
  (for ([i lst])
    (cond
      [(= (modulo index k) 0)
       (set! index (+ index 1))
       (list outlist i)]
      [else (set! index (+ index 1))]
      )
    )
  outlist
  )

(drop '(a b c d e f g h i k) 3)


;Define a function addSubList that processes a list of lists of numbers and adds up all sub-lists. The output of your function is a flat list of numbers.
;(You can assume that your function only receives valid input).

(define Q '(1 2 (3 4) 1 5 (7 8)))
;;;;;;;;;;;;;;;;;;;;;
; (addSubList Q)      
; => '(1 2 7 1 5 15)
;;;;;;;;;;;;;;;;;;;

(define (addSubList L)
  (define X 0)
  (define L1 empty)
  (cond
    [(list? (car L))
     (set! X (foldr + 0 (car L)))]
    [else (set! X (car L))]
    )
  (cond
    [(not (null? (cdr L)))
     (set! L1 (addSubList (cdr L)))])
  (cons X L1)
  )

(addSubList Q)    