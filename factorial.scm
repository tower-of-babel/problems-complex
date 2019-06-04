(define factorial
  (lambda (n)
    (cond
     ((zero? n) 1)
     (else (* n (factorial (- n 1)))))))
