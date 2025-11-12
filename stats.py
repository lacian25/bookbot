def get_num_words(bookString):
    words_list = bookString.split()
    return len(words_list)

def count_chars(bookString):
    dict_count = {}

    for word in bookString:
        for char in word.lower():
            if char in dict_count:
                dict_count[char] += 1
            else:
                dict_count[char] = 1
    return dict_count

def sort_on(items):
    return items["count"]

def sort_dict(dict_count):
    
    list_dict = []
    for char in dict_count:
        list_dict.append({"char": char, "count": dict_count[char]})

    list_dict.sort(key=lambda x: x["count"], reverse=True)
    return list_dict