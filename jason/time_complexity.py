from __future__ import print_function, division

import sys
sys.path.append('../code')
import thinkdsp
import thinkplot

import numpy as np

N = 100
n = np.arange(1, N)

thinkplot.preplot(rows=1, cols=3)
thinkplot.subplot(1)
thinkplot.plot(n, n**3, label='n**3', linewidth=1, color='r')
thinkplot.plot(n, n**2, label='n**2', linewidth=1, color='b')
thinkplot.plot(n, n*np.log(n), label='n*log(n)', linewidth=1, color='g')
thinkplot.config(xlabel='n')

thinkplot.subplot(2)
thinkplot.plot(n, n**2, label='n**2', linewidth=1, color='b')
thinkplot.plot(n, n*np.log(n), label='n*log(n)', linewidth=1, color='g')
thinkplot.config(xlabel='n')

thinkplot.subplot(3)
thinkplot.plot(n, n, label='n', linewidth=1, color='r')
thinkplot.plot(n, np.log(n), label='log(n)', linewidth=1, color='b')
thinkplot.config(xlabel='n')
thinkplot.show()
