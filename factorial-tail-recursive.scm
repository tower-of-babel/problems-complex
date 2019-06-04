(define factorial
  (lambda (n)
    (factorial-aux n 1)))

(define factorial-aux
  (lambda (n acc)
    (cond
     ((zero? n) acc)
     (else (factorial-aux (- n 1) (* n acc))))))
