# program 10:
print('\nprogram 10:')
# sentence with repeated words
input_sentence = "Python is my favourite programming language, and this programming program is done in python."
print(f'The sentence is: {input_sentence}')
input_sentence = input_sentence.replace(",", "").replace(
    ".", '')  # removing comma and fullstop for easier processing
list_of_words = input_sentence.split(' ')  # splits sentence into words
print(f'List of words in the sentence: {list_of_words}')
# converts list into set to remove duplicates
set_of_words = set(list_of_words)
print(f'Set of the words in the sentence, without repetition: {set_of_words}')
# converts set back to list to be accessible for the dictionary
list_out_of_set_of_words = list(set_of_words)
dictionary_with_length = {
    list_out_of_set_of_words[0]: len(list_out_of_set_of_words[0]),
    list_out_of_set_of_words[1]: len(list_out_of_set_of_words[1]),
    list_out_of_set_of_words[2]: len(list_out_of_set_of_words[2]),
    list_out_of_set_of_words[3]: len(list_out_of_set_of_words[3]),
    list_out_of_set_of_words[4]: len(list_out_of_set_of_words[4]),
    list_out_of_set_of_words[5]: len(list_out_of_set_of_words[5]),
    list_out_of_set_of_words[6]: len(list_out_of_set_of_words[6]),
    list_out_of_set_of_words[7]: len(list_out_of_set_of_words[7]),
    list_out_of_set_of_words[8]: len(list_out_of_set_of_words[8]),
    list_out_of_set_of_words[9]: len(list_out_of_set_of_words[9]),
    list_out_of_set_of_words[10]: len(list_out_of_set_of_words[10]),
    list_out_of_set_of_words[11]: len(list_out_of_set_of_words[11]),
}
print(f'Dictionary with words and their length: {dictionary_with_length}')
