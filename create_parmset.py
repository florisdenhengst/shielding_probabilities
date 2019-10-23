import numpy as np

dial_lens = np.arange(1, 31, step=1)
step = 500
n_dials = np.arange(1, 10000+step, step=step)

for i in n_dials:
    for j in dial_lens:
        print("{} {} {} True".format(i, j, i+j))
        print("{} {} {} False".format(i, j, i+j))

