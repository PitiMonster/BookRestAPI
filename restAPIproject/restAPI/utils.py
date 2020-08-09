def find_values(dictionary : dict, book_data: dict):
    for k,v in dictionary.items():
        if k in book_data.keys:
            book_data[k] = v
        elif isinstance(k, dict):
            book_data = find_values(k, book_data)

    return book_data