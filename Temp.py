text = ' qwertyабвqwerty'
replace_text = "абв"

result_text = list(filter(lambda x: replace_text !=x, text.split('абв')))

result_text = "".join(result_text)
print(result_text)

# final_text = list(filter(lambda x: question not in x, initial_text.split("aбв")))