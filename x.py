words = 'the world is mine take a look what you have started'.split()


def concat(*args):
    '''f' {delimiter} '.join(map(str, *data))'''
    return list(map(lambda x: '"' + str(x) + '"', *args))

print(*concat(words))
