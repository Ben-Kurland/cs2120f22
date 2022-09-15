theorem -- make theorem
and_commutes:   --name of theorem
∀ (P Q : Prop), P ∧ Q -> Q ∧ P --proposition to be proved
:=    --symbol for binding a name to a proof value
begin   --between begin and end building the proof
    intros P Q,
    assume h : P ∧ Q,
    let p : P := and.elim_left h,
    let q : Q := and.elim_right h,
    apply and.intro q p,
end

/-
Theorem: Logical and is commutative.

Proof: assume P and Q are arbitrary but specific propositions,
and that we have a proof of P ∧ Q.
From this prof we can derive proofs of P and of Q separately.
Then we can combine these proofs in the opposite order to construc a proof of Q ∧ P.
-/