def safe_input(inputstr):
    try:
        f = raw_input(inputstr)
    except (EOFError,KeyboardInterrupt):
        f = None
    return f
    
if __name__ == '__main__':
    print safe_input('Please input something:\n')