#lang scheme

;; Aiden Stevenson Bradwell
;; March 31st, 2020
;; 
;; The structure of this program includes MatchedOffered, which is a 2 item list, including
;;            1) All current matches
;;            2) All offers that have been made
;; This tuple is passed throughout the program, being added to on each iteration of the offerloop, as the last variable

;;Function used to take two file names and execute the main matching alorithm
(define (findStableMatch EmpFileName StuFileName)
  (define StudentsFileDataList (parseCSV StuFileName)) ;; Read file and create corresponding list of data
  (define CompanyFileDataList (parseCSV EmpFileName)) ;; Read file and create corresponding list of data
  (stableMatching CompanyFileDataList StudentsFileDataList)) ;; Run main algorithm

;;Function which executes the main matching alorithm
(define (stableMatching L_employer_preferences L_student_preferences) 
  (define CompanyList (getSideList L_employer_preferences)) ;; Create a list of all companies to be matched
  (car (OfferLoop CompanyList L_employer_preferences L_student_preferences)) ;; Start the loop of offering these companies to students
  )

;;Function used to loop over all companies and goes through their offering procccess
(define (OfferLoop Companies L_employer_preferences L_student_preferences)  
  (cond
    [(pair? Companies) ;;If there are more companies in the list
     ;;Call offer, combining the MatchedOffered tuple on each cycle
     (offer (car Companies) L_employer_preferences L_student_preferences (OfferLoop (cdr Companies) L_employer_preferences L_student_preferences))]
    [else ;;Otherwise Start the MatchedOffered tuple as empty
     (list empty empty)
     ])
  )

;  || MAIN ALGORITHM ||
;;Function which runs through the offer section of the algorithm
(define (offer Company L_employer_preferences L_student_preferences MatchedOffered) 
  (define StudentList (getCompanyPreferences L_employer_preferences Company)) ;; A list of the students this company would prefer
  (cond
    [(or (empty? MatchedOffered) (not (isCompanyMatched Company (car MatchedOffered)))) ;; Either theres nothing in the MatchedOffered tuple, or the company isnt matched
     (define BestStu (firstStudentUnoffered StudentList Company (cadr MatchedOffered))) ;; Find the first student who has not been offered this position
     (cond [(not (equal? BestStu "")) ;;If this student is found then
            (evaluate (list Company BestStu) L_employer_preferences L_student_preferences MatchedOffered)]) ;; evaluate the possible match 
     ]
    [else MatchedOffered])) ;; Otherwise no more possibilities found

;;Function which evaluates the proposed pair based on the current preference files
(define (evaluate ProposedPair L_employer_preferences L_student_preferences MatchedOffered)
  (define CurStudent (cadr ProposedPair)) ;; Define the current student of the pair
  (define CurCompany (car ProposedPair)) ;; Define the current company of the file
  (cond
    [(not (isStudentMatched CurStudent (car MatchedOffered))) ;; If the student isnt matched
     (addOffered (addMatched MatchedOffered ProposedPair) ProposedPair) ;; Then offer and match the company and student
     ]
    [(isHappier ProposedPair L_employer_preferences L_student_preferences (car MatchedOffered)) ;; Otherwise if the student would be happier with this company
     (define OtherCompany (findCurrentlyMatched CurStudent (car MatchedOffered))) ;; Find the company the student is currently matched to
     (offer OtherCompany L_employer_preferences L_student_preferences  ;; Offer the replaced company sending w/ it the tuple after you sub it out
            (list (subMatch ProposedPair OtherCompany (car MatchedOffered)) (cadr MatchedOffered)))
     ]
    [else ;;Otherwise the student would be happier with its current pair
     (offer CurCompany L_employer_preferences L_student_preferences (addOffered  MatchedOffered ProposedPair)) ;; Offer this company again
     ]
    ))

;; SECTION TWO: HELPER METHODS FOR ADDING OFFERS AND MATCHES TO THE TUPLE
;;Function which adds another offer to the tuple, given the current list of offers
(define (addOffered MatchedOffered NewOffer)
  (cond
    [(empty? (cadr MatchedOffered)) ;; If the current list of offers is empty
     (list (car MatchedOffered) (list NewOffer))] ;; Then return a tuple of the matches and only the current offer on the right side
    [else ;; Otherwise
     (list (car MatchedOffered) (append (list NewOffer) (cadr MatchedOffered)))])) ;; Return a tuple of the current matches and the combiantion of this offer and the previous offers

;;Function which adds a new match to the (Match, Offered) tuple
(define (addMatched MatchedOffered NewMatch)  
  (cond
    [(empty?(car MatchedOffered)) ;; If there are no current matches
     (list (list NewMatch) (cadr MatchedOffered))] ;; Return current match on left side, and the offers on the right
    [else ;; Otherwise append this match to the left side of the tuple
     (list (append (list NewMatch) (car MatchedOffered)) (cadr MatchedOffered))]))

;;Function which replaces one match with another in the list
(define (subMatch NewMatch OldCompany Matched)
  (cond
    [(empty? Matched) ;; If this is the only match
     (list NewMatch)] ;; Then just return the new match
    [(equal? OldCompany (caar Matched)) ;; if the current head of matches is the one to be replaced
     (append  (list NewMatch) (cdr Matched))] ;; Then swap out
    [else ;; Otherwise continue searching
     (append (subMatch NewMatch OldCompany (cdr Matched)) (list (car Matched)))] ;; Send back the matches with the new one added
    ))

;; SECTION THREE: FINDING LOGISTICS FROM THE OFFEREDMATCHED TUPLE
;Function to find the first student which a given company hasn't offered its position too
(define (firstStudentUnoffered StudentList Company Offered)
  (car
   (filter (lambda (Student) (not (isOffered Student Company Offered))) StudentList))) ;find first instance of student who is not offered by the company

;Function to check if this student has been offered by this company given the set of offered already
(define (isOffered Student Company Offered)
  (cond
    [(empty? Offered) ; If noones been offered yet than this student cannot have been offered
     #f]
    [else ; Otherwise if there are currently offers
     (pair? (filter (lambda (X) (equal? (list Company Student) X)) Offered))])) ; Check if there are any matched for this company student combination

;Function which checks if the student is currently matched
(define (isStudentMatched Student Matched)
  (cond
    [(empty? Matched) ;; If noone has been offered yet then this student could not have been
     #f]
    [else ;; Otherwise scan matches
     (pair? (filter (lambda (Pair) (equal? (cadr Pair) Student)) Matched))])) ; If this finds a pair than then it is matched

;Function to find if the company is currently matched given current matches 
(define (isCompanyMatched Company Matched)
  (cond
    [(empty? Matched) ; If there are no matches than it couldnt have been
     #f]
    [else ;; Otherwise scan through current matches
     (pair? (filter (lambda (Pair) (equal? (car Pair) Company)) Matched))])) ; If this isnt empty then it has found it as matched


; SECTION FOUR: FUNCTIONS FOR FINDING HAPPINESS FOR DIFFERENT COMBINATIONS
;Function to find if the proposed pair would be happier than the students current match
(define (isHappier ProposedPair L_employer_preferences L_student_preferences Matched)
  (define CurStudent (cadr ProposedPair)) ; current student being considered
  (define CurCompany (car ProposedPair)) ; Current potential company
  (define OtherCompany (findCurrentlyMatched CurStudent Matched)) ; Company student is currently paired with
  (> (getHappinessForStudent CurStudent OtherCompany L_employer_preferences L_student_preferences) ; Compare their happiness
     (getHappinessForStudent CurStudent CurCompany L_employer_preferences L_student_preferences))
  )

;Function to find the happiness fropm the students perspective
(define (getHappinessForStudent Student Company L_employer_preferences L_student_preferences)
  (getHappinessHelper Company (getPreferences Student L_student_preferences)) ; Use helper to find the happiness
  )

;Helper function to find the potential happiness
; The lower the happiness, the happier it is
(define (getHappinessHelper SearchingFor Preferences)
  (cond
    [(equal? (car Preferences) SearchingFor) 1] ; If current choice start count
    [else (+ 1 (getHappinessHelper SearchingFor (cdr Preferences)))]) ;; Add 1 for each futher from start
  )


; SECTION FIVE; FUNCTIONS TO SCAN THROUGH GIVEN LIST CONTENT TO FIND SUBLISTS
;Function to find the name of all students or all companies
(define (getSideList FileContent)
  (map(lambda (x) (car x))FileContent) ; Find the first item of each row
  )

;Function to find the preferences for a given company
(define (getCompanyPreferences Company_data Company)
  (cdr(car(filter (lambda (x) (equal? (car x) Company)) Company_data))) ; Finds the preferences for the given company
 )

;Function to get the preferences for  the given Prefers object
(define (getPreferences Prefers Lines)
  (define curLine (car Lines))
  (cond
    [(equal? (car curLine) Prefers) (cdr curLine)] ; If this lines start is prefers, return rest of list
    [else (getPreferences Prefers (cdr Lines))]) ; Otherwise continue searching
  )

;Function to find which company the student is currently matched to
(define (findCurrentlyMatched Student Matched)
  (define CurMatch (car Matched)) ; The first match on the list 
  (cond
    [(pair? Matched) (cond ; If there are any more matches 
                       [(equal? (cadr CurMatch) Student) (car CurMatch)] ; And the current match is w/ the student then return current company
                       [else (findCurrentlyMatched Student (cdr Matched))])] ; Otherwise continue searching
    [else (cond ; Otherwise 
            [(equal? (cadr CurMatch) Student) (car CurMatch)] ; If current match is only match left & contains student then return company
            [else ""])]) ; Otherwise current company is null
  )

; SECTION SIX: READING FILES & PARSING THEM
;Function which call csv reading and break it into lists
(define (parseCSV fileName)
  (define inputStream (open-input-file fileName)) ; open the file stream
  (define fileContent (fileToString inputStream)) ; convert it into a string
  (define brokenLines (string-split fileContent "\r\n")) ; break this string into row lists
  (map (lambda (line) (string-split line ",")) brokenLines) ; break these rows into their components
  )

;Function which converts the file to a string
(define (fileToString inputStream)
  (fileToStringHelper inputStream (read-char inputStream)) ; Call helper
  )

;Function which converts the file into string helper
(define (fileToStringHelper inputStream nextChar)
  (cond
    [(eof-object? nextChar) ""] ; Base case of character search
    [(char? nextChar)
     (define curString (make-string 1 nextChar)) ; Next character is the following string
     (string-append curString (fileToStringHelper inputStream (read-char inputStream)))] ; Recursive call combining next with base
    [else ""]) ; Otherwise empty file
  )

(findStableMatch "e10.csv" "s10.csv")