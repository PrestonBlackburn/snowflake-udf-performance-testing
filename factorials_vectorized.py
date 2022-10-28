
import pandas as pd
from scipy.special import factorial

def factorials_vectorized(df):
    df['factorial_sum'] = factorial(df[0].astype(int).values) + factorial(df[1].astype(int).values)
    return df['factorial_sum']
