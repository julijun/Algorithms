"""
Function decode can read an encoded message from a message file. File contains words associated with numbers.
To find an encoded message order numberd from smallet to biggest and arrange them into a pyramid.
Each line of the pyramid includes one more number than the line before it. Example
1
2 3
4 5 6
The numbers at the end of each line (1, 3 and 6) correspond to the words that are part of the message.
You should ignore all the other words.
"""


def decode(message_file):
    # Read the contents of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Parse the lines into a dictionary of {number: word}
    number_word_map = {}
    for line in lines:
        number, word = line.split()
        number_word_map[int(number)] = word

    # Generate the pyramid and select the words at the end of each line
    decoded_message = []
    row_end = 1
    for number in sorted(number_word_map.keys()):
        if number == row_end:
            decoded_message.append(number_word_map[number])
            row_end += len(decoded_message) + 1

    return ' '.join(decoded_message)


# Example usage
message = decode('test.txt')
print(message)
