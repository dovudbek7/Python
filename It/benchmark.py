def banchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args,**kwargs)
        end = time.time()
        print(f'[*] vaqt {round(end-start,2)}')
    return wrapper