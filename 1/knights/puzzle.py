from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# A is Knight xor A is KNave (encapsulates 1->0, 0->1 ) (opposite of AKnight<=>AKnave) (means if AisKnight then AisNotKnave)
basicA = Or(And(AKnight, Not(AKnave)), And(Not(AKnight), AKnave))
basicB = Or(And(BKnight, Not(BKnave)), And(Not(BKnight), BKnave))
basicC = Or(And(CKnight, Not(CKnave)), And(Not(CKnight), CKnave))

 

# Puzzle 0
# A says "I am both a knight and a knave."
statementA = And(AKnight, AKnave)

elementalA = And(Biconditional(AKnight, statementA), Biconditional(AKnave, Not(statementA)))
elementalA.add(basicA)
knowledge0 = elementalA

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
statementA = And(AKnave, BKnave)
elementalA = And(Biconditional(AKnight, statementA), Biconditional(AKnave, Not(statementA)))
elementalA.add(basicA)
elementalA.add(basicB)

knowledge1 = elementalA

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
statementA = And(Biconditional(AKnave, BKnave), Biconditional(AKnight, BKnight))
statementB = And(Biconditional(AKnave, BKnight), Biconditional(AKnight, BKnave))
elementalA = And(Biconditional(AKnight, statementA), Biconditional(AKnave, Not(statementA)))
elementalA.add(basicA)
elementalB = And(Biconditional(BKnight, statementB), Biconditional(BKnave, Not(statementB)))
elementalB.add(basicB)
knowledge2 = And(
    elementalA, elementalB
)
# Soln
# A is a Knave
# B is a Knight




# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.  ## NOT FIGUREOUTABLE HOW TO CONVERT INTO PROPOSITIONAL
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."

statementA = basicA
elementalA = And(Biconditional(AKnight, statementA), Biconditional(AKnave, Not(statementA)))
elementalA.add(basicA)

statementB = And(CKnave, Biconditional(BKnave, statementA))
elementalB = And(Biconditional(BKnight, statementB), Biconditional(BKnave, Not(statementB)))
elementalB.add(basicB)


statementC = AKnight
elementalC = And(Biconditional(CKnight, statementC), Biconditional(CKnave, Not(statementC)))
elementalC.add(basicC)

knowledge3 = And(
    elementalA,
    elementalB,
    elementalC
    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
