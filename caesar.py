alphabet = "abcdefghijklmnopqrstuvwxyz"

message = "ittgwczjiamizmjmtwvobwca"

for shift in range(1, 26):
    print(shift, "".join([alphabet[alphabet.index(letter) - shift] for letter in message]))