import datetime
import sys

def tprint(msg: any) -> None:
    # blue
    pre = '\033[34m'
    post = '\033[0m'
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'{pre}[{t}]{post} {msg}')

def tprint_error(msg: any) -> None:
    # red
    pre = '\033[31m'
    post = '\033[0m'
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'{pre}[{t}]{post} {msg}', file=sys.stderr)

def parse_to_float(x: any) -> any: # None | float
    try:
        x = float(x)
    except:
        tprint_error('ERROR: failed to parse {x} into float')
        x = None
    return x

def parse_to_str(x: any) -> any: # None | str
    try:
        x = str(x)
    except:
        tprint_error('ERROR: failed to parse {x} into str')
        x = None
    return x

def parse_to_int(x: any) -> any: # None | int
    try:
        x = int(x)
    except:
        tprint_error('ERROR: failed to parse {x} into int')
        x = None
    return x