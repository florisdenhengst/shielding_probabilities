import numpy as np

dial_lens = np.arange(1, 51, step=1)

for i in dial_lens:
    print("{} {} True".format(i, i))
    print("{} {} False".format(i, i))

