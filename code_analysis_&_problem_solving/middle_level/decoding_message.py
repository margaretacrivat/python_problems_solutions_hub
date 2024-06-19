# Task: Decoding a Message from a Text File
# In this exercise, you will develop a function named decode(message_file). This function should read an encoded
# message from a .txt file and return its decoded version as a string.

# Your function must be able to process an input file with the following format:
# 3 love
# 6 computers
# 2 dogs
# 4 cats
# 1 I
# 5 you

# In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the
# arrangement of these numbers into a "pyramid" structure. The numbers are placed into the pyramid in ascending order,
# with each line of the pyramid having one more number than the line above it. The smallest number is 1, and the
# numbers increase consecutively, like so:
#   1
#  2 3
# 4 5 6

# The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line
# (in this example, 1, 3, and 6). You should ignore all the other words. So for the example input file above, the
# message words are:
# 1: I
# 3: love
# 6: computers
# and your function should return the string "I love computers".

# This function first reads the lines from the input file, then iterates over each line to extract the word
# corresponding to the number at the end of the line according to the pyramid structure. Finally, it returns the
# decoded message as a string by joining the extracted words with spaces. You can uncomment the example usage line
# to test the function with the provided file encoded_message.txt.
# To verify that your code works, please download this text input file (direct download link) or copy this list into
# a text editor of your choosing and use your function to decode the message (this file was recently updated;
# your file should begin with 193 land).

def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    decoded_words = []
    position = 0

    for line in lines:
        words = line.split()
        if position < len(words):  # Check if position is within bounds
            decoded_words.append(words[position])
            position += 1

    return ' '.join(decoded_words)


# Test usage:
print(decode('coding_input.txt'))















