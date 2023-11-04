from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is a knight or a knave but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # If A is a knight, A is telling the truth
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a knave, A is lying
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A and B are one of a knight or a knave
    And(Or(AKnight, AKnave), Or(BKnight, BKnave)),
    # If A is a knight, A and B are both knaves
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a knave, A and B are not both knaves
    Implication(AKnave, Not(And(AKnave, BKnave)))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # If A is a knight,
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a knave,
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # If B is a knight,
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    # If B is a knave,
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))),
    # A and B are one of a knight or a knave
    And(Or(AKnight, AKnave), Or(BKnight, BKnave))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A, B, and C are one of a knight or a knave
    And(Or(AKnight, AKnave), Or(BKnight, BKnave), Or(CKnight, CKnave)),
    # If A is a knight, A is telling the truth and is a knave or a knight
    Implication(AKnight, Or(AKnight, AKnave)),
    # If A is a knave, A is lying, and is not a knave or a knight
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    # If B is a knight, B is telling the truth, C is a knave, and A said 'A is a knave'
        # If A is a Knight (who tells the truth) -> A is a Knave
        # If A is a Knave (who lies) -> A is a Knight
    Implication(BKnight, And(CKnave, Or(Implication(AKnight, AKnave), Implication(AKnave, AKnight)))),
    # If B is a knave, B is lying, C is not a knave, and A did not say 'A is a knave'
        # If B is a knave, and is lying about what A said, A said 'A is a knight'
    Implication(BKnave, And(Not(CKnave), Implication(AKnight, AKnight))),
    # If C is a knight, C is telling the truth, and A is a knight
    Implication(CKnight, AKnight),
    # If C is a knave, C is lying, and A is not a knight
    Implication(CKnave, Not(AKnight))

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
