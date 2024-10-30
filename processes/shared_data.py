from multiprocessing import Process, Manager
import multiprocessing


def dict_and_list(d: dict, l: list):
    print(f"Enter {multiprocessing.current_process().name}")
    print(f"Process says: Got dict {d}, list {l}")
    d['foo'] = 'bar'
    d['spam'] = 'eggs'

    l.extend(['foo', 'bar', 'spam', 'eggs'])
    print(f"Process says: updated to values dict {d}, list: {l}")
    print(f"Process says: updated to id's dict {id(d)}, list {id(l)}")


with Manager() as pman:
    print(f"Main is {multiprocessing.current_process().name}")
    d = pman.dict()
    l = pman.list()
    print(f"Main says: init dict {d}, list {l}")
    p = Process(target=dict_and_list, args=(d, l))
    p.start()
    p.join()
    print(f"Main says: got values dict {d}, list {l}")
    print(f"Main says: got id's dict {id(d)}, list {id(l)}")
