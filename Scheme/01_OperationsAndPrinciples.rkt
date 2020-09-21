#lang racket
;; EXERCISE ONE
(* 6 (- 10 5))

(+ (* 1 1) (+ (* 2 2) (+ (* 3 3) (* 4 4))))

;;(define (f x) (= (+(* 2 (* x x)) (- (* 5 x) 3)) 0))
;;(write (f ))

(/ (+ -5 (sqrt (- (* 5 5) (* 4 2 -3)))) (* 2 2))
(/ (- -5 (sqrt (- (* 5 5) (* 4 2 -3)))) (* 2 2))

;;Calculate the result of the sin(pi/4) cos(pi/3) + cos(pi/4) sin(pi/3)

(+ ( * (sin(/ pi 4)) (cos(/ pi 3))) (* (cos(/ pi 4)) (sin(/ pi 3))))

;;EXERCISE TWO
;;Global definition use define and local definition use let bindings.

(define myFavourite 42)

(writeln myFavourite)

(let ((x 1) (y 2))
  (+ x y))
;; (writeln x y) Creates an error

;;Use a local let binding for the angles to calculate sin(pi/4) cos(pi/3) + cos(pi/4) sin(pi/3) again.
(let ((a (/ pi 4)) (b (/ pi 3))) (+ (* (sin a) (cos b)) (* (sin b) (cos a))))


;;EXERCISE THREE
;;Lambda expressions create local procedures.
((lambda (x y) (+ x y)) 1 2)
;;This code defines the lambda and then uses it with the arguments 1 and 2.
;;Use a lambda with the angles as arguments
;;to calculate sin(pi/4) cos(pi/3) + cos(pi/4) sin(pi/3) again.
(define f (lambda (a b) (+ (* (sin a) (cos b)) (* (sin b) (cos a)))))
(f (/ pi 4) (/ pi 3))
;;We can also define global procedures.
(define foo (lambda (x y) (+ x y)))

;;Call the function foo with 1 and 2 as arguments.
(foo 1 2)


;;EXERCISE FOUR
;;Define a global function that finds both roots of a quadratic equation
;;ax^2+bx+c = 0 with a,b,c as arguments.
;;Note that you can calculate two solutions and return them as a list as follows:

;;(define foog (lambda (a b c ) (list
;;(/ (+ (- 0 b) (sqrt (- (* b b) (* 4 a -c)))) (* a a))
;;(/ (- (- 0 b) (sqrt (- (* b b) (* 4 a -c)))) (* a a))
;;)))


;;EXERCISE FIVE


(define (halfTrig theta) ( let ((x (tan (/ theta 2))) (y (* (tan (/ 1.57 2)) (tan (/ 1.57 2)))))
                            (/ (* 2 x)) (+ 1 y)
                            ))
write(halfTrig 30)



