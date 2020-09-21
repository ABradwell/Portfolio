#lang scheme
;; Aiden Stevenson Bradwell
;; 300064655
;; abrad060@uottawa.ca
;; March 28th, 2020

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
