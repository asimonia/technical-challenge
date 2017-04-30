LETTER_ROW = 7
from letters import A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, \
			W, X, Y, Z, _0, _1, _2, _3, _4, _5, _6, _7, _8, _9

def get_char(char):
	"""Returns a terminal character

	char: Alphanumeric character
	"""

	letters = { "A" : A,
	"B" : B,
	"C" : C,
	"D" : D,
	"E" : E,
	"F" : F,
	"G" : G,
	"H" : H,
	"I" : I,
	"J" : J,
	"K" : K,
	"L" : L,
	"M" : M,
	"N" : N,
	"O" : O,
	"P" : P,
	"Q" : Q,
	"R" : R,
	"S" : S,
	"T" : T,
	"U" : U,
	"V" : V,
	"W" : W,
	"X" : X,
	"Y" : Y,
	"Z" : Z,
	"0" : _0,
	"1" : _1,
	"2" : _2,
	"3" : _3,
	"4" : _4,
	"5" : _5,
	"6" : _6,
	"7" : _7,
	"8" : _8,
	"9" : _9,
	}

	return letters[char]


def print_lines(phrase):
	"""Given a phrase, prints out the lines of text to the screen.

	phrase: list of alphanums
	"""
	for row in range(LETTER_ROW):
		line = [char[row] for char in phrase]
		print(''.join(line))


if __name__ == '__main__':

	while True:
		# Get input from user
		parser = input("Enter an alphanumeric combination (0 - 100 characters): ").upper()

		if not parser.isalnum() or len(parser) > 100:
			print("Please enter a valid alphanumeric combination")
			continue

		# Build a phrase from each alphanumeric
		phrase = [get_char(char) for char in parser]

		# Print lines
		print_lines(phrase)

