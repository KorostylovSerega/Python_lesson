def word_amount(text):
    text_list = text.split()
    text_all = list(map((lambda w: ''.join(filter(str.isalnum, w))), text_list))
    text_uniq = list(set(text_all))
    word_amount = list(map(lambda w: (w, text_all.count(w)), text_uniq))
    return word_amount

text = open('word_text.txt').read()

list(map(lambda val: print('{:16} ===> {}'.format(val[0], val[1])), word_amount(text)))



