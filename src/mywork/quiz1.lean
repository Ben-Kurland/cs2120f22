/-
CS2120 Fall 2022 Sullivan. Quiz #1. Edit your answers into
this file using VSCode. Save the file to your *local* hard 
drive (File > Save As > local > ...). Submit it to the Quiz1
assignment on Collab.
-/

/-
#1: For each of the following questions give a yes/no answer 
and then a very brief explanation why that answer is correct.
To explain why your answer is correct, name the specific rule
of inference that tells you it's correct, or explain that 
there is no such valid inference rule.
-/

/-
#1A

If a ball, b, is round *and* b is also red, is b red?

A: yes/no: yes

B: Why? assuming we have a proof that b is round and b is
  also red, we can apply "and elimination right" to deduce 
  a proof that b is red


#1B

If flowers make you happy and chocolates make you happy,
and I give you flowers *or* I give you chocolates, will
you be happy?

A: yes/no: yes

B: Why? If we have a proof that flowers make me happy and
  chocolates make me happy, and if we are given a proof
  that you give me flowers or you give me chocolates, we
  can apply "or elimination" to deduce a proof that I will
  be happy


#1C: If giraffes are just zebras in disguise, then the 
moon is made of green cheese?

A. yes/: yes

B. Why? Assume we have a proof that giraffes are just zebras
  in disguise. There are zero ways in which a proof of this
  could be constructed, so this is a contradiction. A contradiction
  is essentially a proof of false, and by applying "false
  elimination" any thing follows, including a proof that the moon
  is made of cheese


#1D. If x = y implies that 0 = 1, then is it true that
x ≠ y?

A. yes/no: yes

B. Why? assume that we have a proof of x = y, and we are given
  a proof that this implies 0 = 1. Using arrow elimination we 
  can derive a proof that 0 = 1. From our knowledge of equality
  and the natural numbers we know that this is a contradiction
  and a proof of 0=1 cannot exist. Therefore there must be no
  proof of x = y so x = y implies false. Then applying the "definition
  of not" we can derive a proof of not(x = y), which is equivalent to 
  x ≠ y



#1E. If every zebra has stripes and Zoe is a Zebra then
Zoe has stripes.

A. yes/no: yes

B. Why? assume we have a proof that Zoe is a zebra, and we
  have a proof that for all zebras z, z has stripes, now we
  can use this proof by applying it to the particular zebra
  Zoe to show that zoe has stripes


#1F. If Z could be *any* Zebra and Z has stripes, then 
*every* Zebra has stripes.

A. Yes/no: yes

B: Why? Assume we havea proof that Z is an arbitrary zebra,
and a proof that z has stripes, in this context we can deduce
a proof that every zebra has stripes from the knowledge that
the proof that z has stripes is true for any zebra z.


#1G. If whenever the wind blows, the leaves move, and 
the leaves are moving, then the wind is blowing.

A. yes/no: no

B. Why? The leaves could be moving for a reason other than the
  wind, as illustrated by the fact that the law of the converse
  always being true is a fallacy


#1H: If Gina is nice *or* Gina is tall, and Gina is nice,
then Gina is not tall. (The "or" here is understood to be
the or of predicate logic.)

A. yes/no: no

B. Why? Using case analysis: to satisfy the first assertion,
  assume in one case that Gina is tall, then assume for the second assertion
  that gina is nice, from this context we know that gina is tall and therefore
  it is falses that gina is not tall
-/



/- 
#2

Consider the following formula/proposition in propositional
logic: X ∨ ¬Y.

#2A: Is is satisfiable? If so, give a model (a binding of 
the variables to values that makes the expressions true).
Yes it is satisfiable: X:True, Y:False

#2B: Is it valid? Explain your answer. 
It is not valid. Validity means it is true for all cases
and if X is False and Y is True, then it evaluates to false

-/


/-
#3: 

Express the following propositions in predicate logic, by
filling in the blank after the #check command.

If P and Q are arbitrary (any) propositions, then if (P is 
true if and only if Q is true) then if P is true then Q is 
true.
-/

#check ∀ (P Q : Prop), (Q → P) → (P → Q)



/-
#4 Translate the following expressions into English.
The #check commands are just Lean commands and can
be ignored here. 
-/


-- A
#check ∀ (n m : ℕ), n < m → m - n > 0

/-
Answer: If n and m are any natural numbers, then if n
is greater than m, then m minus n is greater than 0.
-/

-- B

#check ∃ (n : ℕ), ∀ (m : nat), m >= n

/-
Answer: If n is a natural number and m is any natural number,
then for every m there is some n such that m is greater than or equal to n.
-/


-- C

variables (isEven: ℕ → Prop) (isOdd: ℕ → Prop)
#check ∀ (n : ℕ), isEven n ∨ isOdd n

/-
Answer: If n is any natural number, then n is even or n is odd
-/


-- D

#check ∀ (P : Prop), P ∨ ¬P

/-
Answer: if P is any proposition, then P is true or not P is true
-/


-- E

#check ∀ (P : Prop), ¬(P ∧ ¬P)

/-
Answer: If P is any proposition, then (P and not P) is not true
-/


/-
#5 Extra Credit

Next we define contagion as a proof of a slightly long
proposition. Everything before the comma introduces new
terms, which are then used after the comma to state the
main content of the proposition. 

Using the names we've given to the variables to infer
real-world meanings, state what the logic means in plain
natural English. Please don't just give a verbatim reading
of the formal logic.

Answer: If an animal has a virus and a second animal is in
close contact with them, then the second animal has a virus
-/

variable contagion : 
  ∀ (Animal : Type) 
  (hasVirus : Animal → Prop) 
  (a1 a2 : Animal) 
  (hasVirus : Animal → Prop)
  (closeContact : Animal → Animal → Prop), 
  hasVirus a1 → closeContact a1 a2 → hasVirus a2


