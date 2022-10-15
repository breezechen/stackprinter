import stackprinter
stackprinter.set_excepthook()


def bomb(msg):
    try:
        raise Exception(msg)
    except Exception as e:
        raise Exception(f'{msg}_b') from e

try:
    bomb('1')
except Exception as e:
    try:
        raise Exception('2') from e
    except:
        bomb('3')

