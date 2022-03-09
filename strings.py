phrase = 'one interesanting phrase on python: '

print(phrase + ' anyplace always is good for all of us')

# simple uppercase method
print(phrase.upper())

print(phrase)

# to know if a string is in uppercase
print(phrase.isupper())
print(phrase.upper().isupper())


# indexes character in string

print(phrase[0])


# index function tell us where espesific caracter is if not exist on string the function trow an error

print(phrase.index('o'))

# replace simple function

print(phrase.replace('o', 'A'))

# if a want to know the lenght of srtring we have de len function

print(len(phrase))
