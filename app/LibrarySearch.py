def library_search(media_list, search) -> list:
    ret = []
    for i in media_list:
        if i.title.lower().find(search.lower()) != -1:
            ret.append(i)
    return ret
