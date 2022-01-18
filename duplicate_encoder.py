def duplicate_encode(word):
    word_array = ['(' if word.lower().count(symbol) == 1 else ')' for symbol in word]
    return "".join(word_array)


# print(duplicate_encode("Success"))
# print(duplicate_encode("(( @"))
print(duplicate_encode('VURU oRVpSLtvQWtivi'))  # '))))(())((())(())))'
# VURU oRVpSLtvQWtivi
# ))))(())((())(())))
# ))))(())())))))))))
