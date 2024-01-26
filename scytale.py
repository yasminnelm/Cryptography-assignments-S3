# def text_to_matrix(text, num_columns):
#     matrix = [[] for _ in range(num_columns)]

#     for i, char in enumerate(text):
#         column_index = i % num_columns
#         matrix[column_index].append(char)

#     # Fill in empty spaces in columns with spaces
#     max_length = max(len(column) for column in matrix)
#     for column in matrix:
#         while len(column) < max_length:
#             column.append(' ')

#     return matrix

# # Example usage:
# text = "lelnracsrunanatuvllerrmcnjeeaesetanctsagsgeemftqdnnentraraueneciliianeredofaesntdneenignpcdaishdcaoaeenede"
# columns = 5
# matrix = text_to_matrix(text, columns)

# # Print the matrix (you can read the text from the matrix)
# for row in matrix:
#     print(''.join(row))

def decrypt_scytale(ciphertext, key):
    columns = (len(ciphertext) // key)+1
    plaintext = [''] * len(ciphertext)

    for i in range(columns):
        for j in range(key):
            index = i + j * columns
            plaintext[index] = ciphertext[i * key + j]

    return ''.join(plaintext)

ciphertext = "lelnracsrunanatuvllerrmcnjeeaesetanctsagsgeemftqdnnentraraueneciliianeredofaesntdneenignpcdaishdcaoaeenede"
key = 10

plaintext = decrypt_scytale(ciphertext, key)
print(len(plaintext))

