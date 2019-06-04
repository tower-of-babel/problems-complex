(define fibonacci-nth
  (lambda (n)
    (cond
     ((zero? n) 0)
     ((eq? n 1) 1)
     (else (+ (fibonacci-nth (- n 1)) (fibonacci-nth (- n 2)))))))


(define fibonacci
  (lambda (n)
    (cond
     ((zero? n) (quote ()))
     (cons (fibonacci-nth n) (fibonacci (- n 1))))))
