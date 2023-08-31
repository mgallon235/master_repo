import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb, factorial

p= 1/2

n = np.arange(0,10)
X = np.power(p,n)

plt.bar(n,X)
plt.show()

### compute N choose K (n k) and k! --- this basically  help us calculate the  number of possible combinations

n2 = 10 # 10 coins
k = 2 # 2 successes

comb(n2,k) ## Final Result
factorial(k)
factorial(8)

(3628800.0)/(2* 40320.0)
