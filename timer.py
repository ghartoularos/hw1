import pickle
from algs import bubblesort, quicksort
from tqdm import tqdm
import timeit
import numpy as np

# multi large test
x = [np.random.rand(100,i) for i in [(i + 1) * 100 for i in list(range(3))]]
timebub = []
for i in tqdm(x):
    for j in i:
        tic = timeit.default_timer()
        ans = bubblesort(j)
        toc = timeit.default_timer()
        timebub.append((len(j),toc-tic))
pickle.dump(timebub,open('faketimebub.pkl','wb'))

timequi = []
for i in tqdm(x):
    for j in i:
        tic = timeit.default_timer()
        ans = quicksort(j)
        toc = timeit.default_timer()
        timequi.append((len(j),toc-tic))
pickle.dump(timequi,open('faketimequi.pkl','wb'))