import numpy as np

def frange(start, stop, step):
    while start < stop:
        yield start
        start += step

def format_key(val: float, decimals: int = 6) -> str:
    return f"{val:.{decimals}f}"
