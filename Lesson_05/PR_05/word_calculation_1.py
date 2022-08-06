def list_converter(text):
    text_all = text.replace(',','').replace('.','').replace('"','').replace(':','').split()
    text_uniq = list(set(text_all))
    return text_all, text_uniq


def word_calculation(word):
    text_list = list_converter(text)[0]
    word_amount = text_list.count(word)
    return word, word_amount


text = open('word_text.txt').read()
result = (list(map(word_calculation, list_converter(text)[1])))
list(map(lambda value: print('{} ==> {}'.format(value[0], value[1])), result))
