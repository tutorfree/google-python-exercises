#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.


# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

# Dada uma lista de strings, retorne a contagem do numero de
# strings em que o comprimento e 2 ou mais e o primeiro
# e os ultimos caracteres da string sao os mesmos.
# Nota: python nao possui um operador ++, mas + = funciona.
def match_ends(words):
	
	counter = 0 # definindo o contador como inicial zero
	for i in words: # percorrendo o indice
		if len(i) > 1 and i[0] == i[-1]: #  se for >=2 e letras inicial e final forem iguais
			counter += 1 # adiciona 1 ao contador
	return counter 


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

# Dada uma lista de strings, retorne uma lista com as strings na ordem classificada, 
# exceto agrupando todas as sequencias que comecam com 'x' primeiro.
# por exemplo. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] produz ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Dica: isso pode ser feito fazendo duas listas e classificando cada uma delas antes de combina-las.
def front_x(words):
	
	# utilizando aqui a dica do enunciado
	l1 = []
	l2 = []
	
	for i in words: # percorrendo o indice
		if i[0] == 'x': # se a posicao inicial for a letra 'x'
		  l1.append(i)  # adicione a lista 1
		else:
		  l2.append(i)
	
	# colocando em ordem e concatenando
	return sorted(l1) + sorted(l2)


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

# Dada uma lista de tuplas nao vazias, retorne uma lista classificada
# em ordem crescente ordenada pelo ultimo elemento em cada tupla.
# por exemplo. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] produz
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Dica: use uma tecla personalizada = funcao para extrair o ultimo elemento de cada tupla.

def last(tupla):
	return tupla[-1]


def sort_last(tuples):
    # +++your code here+++
    return sorted(tuples, key=last)


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print()
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print()
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
