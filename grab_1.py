def search_word(word, word_list):
    data=[]
    for i in word_list:
        if word in i:
            data.append(i)
    return  data