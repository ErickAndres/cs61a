;;;  Name:Erick Andres
;;;  Email:eandres1@berkeley.edu

;;; Q1.
#(fact (add-to-all a ((b)) (a b)))
#(fact (add-to-all a (c d) a c d))
(query (add-to-all a ((b) (c d)) ((a b) (a c d))))
; expect Success!
(query (add-to-all a ((b c) (b) (foo)) ?what))
; expect Success! ; what: ((a b c) (a b) (a foo))
(query (add-to-all ?what ((c) (d e) ()) ((b c) (b d e) (b))))
; expect Success! ; what: b
(query (add-to-all ?what ?list ((b c) (d e) (b))))
; expect Failed.

;;; Q2.

(fact (append () ?a ?a))
(fact (append (?x . ?r) ?b (?x . ?c))
      (append ?r ?b ?c))


(query (sublists (1 2 3) ?subs))
; expect Success! ; subs: (() (3) (2) (2 3) (1) (1 3) (1 2) (1 2 3))

;;; Q3.

(fact (fruits apple banana cherry date elderberry fig guava))


(query (fruits-tail date elderberry fig guava))
; expect Success!
(query (fruits-tail banana . ?after-banana))
; expect Success! ; after-banana: (cherry date elderberry fig guava)
(query (fruits-tail ?e fig guava))
; expect Success! ; e: elderberry

;;; Q4.

(fact (prefix () ?s))
(fact (prefix (?first . ?p) (?first . ?s))
      (prefix ?p ?s))


(query (fruit-range cherry guava (date elderberry fig)))
; expect Success!
(query (fruit-range cherry elderberry date))
; expect Failed.
(query (fruit-range cherry elderberry ?between))
; expect Success! ; between: (date)
(query (fruit-range cherry date ()))
; expect Failed.
(query (fruit-range banana fig ?between))
; expect Success! ; between: (cherry date elderberry)

;;; Q5.

(fact (increment 1 2))
(fact (increment 2 3))
(fact (increment 3 4))
(fact (increment 4 5))
(fact (increment 5 6))
(fact (increment 6 7))
(fact (increment 7 8))
(fact (increment 8 9))


(query (max 2 4 4) (max 4 2 4) (max 4 4 4))
; expect Success!
(query (max 3 ?x ?x) (max ?x 5 5))
; expect Success! ; x: 3 ; x: 4 ; x: 5
(query (max 1 2 3))
; expect Failed.

;;; Q6.

(fact (add       1 ?x ?x+1)
      (increment ?x ?x+1))
(fact (add       ?x+1 ?y ?z+1)
      (increment ?x ?x+1)
      (increment ?z ?z+1)
      (add       ?x ?y ?z))


(query (reduce-to ?value add 1 1 2 3))
; expect Success! ; value: 7
(query (reduce-to ?value max 1 2 4 1 3 1))
; expect Success! ; value: 4
(query (reduce-to 4 add . ?addends))
; expect Success! ; addends: (1 3) ; addends: (2 2) ; addends: (3 1) ; addends: (1 1 2) ; addends: (1 2 1) ; addends: (1 1 1 1) ; addends: (2 1 1)
