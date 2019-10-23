import argparse
import math
import numpy as np
from joblib import Parallel, delayed
import ast

parser = argparse.ArgumentParser(description='Calculate expected # recommendations.')

# dial_len
parser.add_argument('dialogue_length', metavar='L', type=int, nargs=1)
# seed
parser.add_argument('seed', metavar='S', type=int, nargs=1)
# enforce
parser.add_argument('enforce_recommendation', metavar='E', type=ast.literal_eval, nargs=1)

args = parser.parse_args()

dial_len = args.dialogue_length[0]
seed = args.seed[0]
enforce_rec = args.enforce_recommendation[0]

np.random.seed(seed)

# 0: ko
# 1: dna
# 2: dec_profile
# 3: verified_profile
# 4: recommend
letters = list(np.arange(0,42))
n = int(2e2)

def generate(dial_len, letters):
    return np.random.choice(letters, dial_len, replace=True)

def check_elements(seq, enforce_rec):
    """
    Validates that `seq` contains all necessary elements
    """
    if enforce_rec:
       required_letters = np.array([0,1,2,3])
    else:
       required_letters = np.array([0,1,2,3,4])
    return np.all(np.isin(required_letters, seq))

def check_order(seq, enforce_rec):
    """
    Validates order of items in sequences
    """
    if enforce_rec:
       pass
    else:
       last_recommendation = np.argwhere(seq == 4).max()
       for i in {0, 1, 2, 3}:
          if np.argwhere(seq == i).min() > last_recommendation:
             return False
    last_verification = np.argwhere(seq == 3).max()
    if np.argwhere(seq == 2).min() > last_verification:
        return False
    return True

def check(seq, enforce_rec):
    return check_elements(seq, enforce_rec) and check_order(seq, enforce_rec)

#def simulate(n_dials, dial_len, letters, enforce_rec):
#    results_mc = np.zeros(n_dials, dtype=bool)
#    for i in range(n_dials):
#       results_mc[i] = check(generate(dial_len, letters), enforce_rec)
#    return results_mc.sum()

def simulate(dial_len, letters, enforce_rec):
    return check(generate(dial_len, letters), enforce_rec)

def monte_carlo(n, dial_len, letters, enforce_rec):
    results = Parallel(n_jobs=16)(delayed(simulate)(dial_len, letters, enforce_rec) for i in range(n))
    return np.array(results)

result = monte_carlo(n, dial_len, letters, enforce_rec)
print(",".join(map(str,[n, dial_len, seed, enforce_rec, result.mean(), result.std()])))
