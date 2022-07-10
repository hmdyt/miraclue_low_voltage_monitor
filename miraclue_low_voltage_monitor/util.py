import datetime
import sys

from loguru import logger

def parse_to_float(x: any) -> any: # None | float
    try:
        x = float(x)
    except:
        logger.error('ERROR: failed to parse {x} into float')
        x = None
    return x

def parse_to_str(x: any) -> any: # None | str
    try:
        x = str(x)
    except:
        logger.error('ERROR: failed to parse {x} into str')
        x = None
    return x

def parse_to_int(x: any) -> any: # None | int
    try:
        x = int(x)
    except:
        logger.error('ERROR: failed to parse {x} into int')
        x = None
    return x