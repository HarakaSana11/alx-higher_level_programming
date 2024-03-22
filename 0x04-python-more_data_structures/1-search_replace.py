#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return (list(map(lambda xyz: replace if xyz is search else xyz, my_list)))
