# A | B = > {x | x in A OR x in B}
def union(A, B):
    s = set()
    for a in A:
        s.add(a)
    for b in B:
        s.add(b)
    return s

# A & B
def intersection(A, B):
    s = set()
    for a in A:
        if a in B:
            s.add(a)
    return s

# A ^ B
def symmetric_difference(A, B):

    s = set()
    for a in A:
        if a not in B:
            s.add(a)
    for b in B:
        if b not in A:
            s.add(b)
    return s

# A - B {x | x in A and x not in B }
def minus(A, B):

    s = set()
    for a in A:
        if a not in B:
            s.add(a)
    return s


# A x B {(a, b) | a in A and b in B} # notice cross is a verb
def cross(A, B):
    return set( (a, b) for a in A  for b in B )


# A <= B True if forall a in A a also in B 
def is_subset(A, B):

    for a in A:
        if a not in B:
            return False
    return True


# A >= B
def is_superset(A, B):
    return is_subset(B, A)


# A < B
def is_proper_subset(A, B):
    return is_subset(A, B) and A != B


# A > B
def is_proper_superset(A, B):
    return is_superset(A, B) and A != B


# set S is a relation if it is a subset of A X B
def is_relation(S, A, B):
    return is_subset(S, cross(A, B))




