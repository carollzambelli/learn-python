'''
Dado dois conjuntos A e B, dizer se o conjunto A está contido em B, ou seja, se é subconjunto.
Se A for subconjunto de B, retorne True, caso contrário, retorne False.

Input
- Quantidade de elementos de A
- Conjunto A em lista
- Quantidade de elementos de B
- Conjunto B em lista

###########
# Testing #
###########

# Test 1
Input:
[
5,
[1, 2, 3, 5, 6],
9,
[9, 8, 5, 6, 3, 2, 1, 4, 7]
]
Output: True

# Test 2
Input:
[
1,
[2],
5,
[3, 6, 5, 4, 1]
]
Output: False

# Test 3
Input:
[
7,
[1, 2, 3, 5, 6, 8, 9],
3,
[9, 8, 2]
]
Output: False
'''