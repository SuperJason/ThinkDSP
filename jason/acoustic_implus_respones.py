from __future__ import print_function, division

import sys
sys.path.append('../code')

import thinkdsp
import thinkplot

import numpy as np
import pandas as pd

from copy import deepcopy

# acoustic implus
print(' ---------- acoustic implus ----------')
response = thinkdsp.read_wave('../code/180960__kleeb__gunshot.wav')

start = 0.12
response = response.segment(start=start)
response.shift(-start)

response.normalize()
response.plot()
thinkplot.config(title='response of gunshot', xlabel='Time (s)', ylim=[-1.05, 1.05])
thinkplot.show()
response.play()

transfer = response.make_spectrum()
transfer.plot()
thinkplot.config(title='transfer spectrum', xlabel='Frequency (Hz)', ylabel='Amplitude')
thinkplot.show()

# violin music
print(' ---------- violin music  ----------')
violin = thinkdsp.read_wave('../code/92002__jcveliz__violin-origional.wav')

start = 0.11
violin = violin.segment(start=start)
violin.shift(-start)

violin.truncate(len(response))
violin.normalize()
violin.plot()
thinkplot.config(title='violin music', xlabel='Time (s)', ylim=[-1.05, 1.05])
thinkplot.show()
violin.play()

violin_spectrum = violin.make_spectrum()
violin_spectrum.plot()
thinkplot.config(title='violin spectrum', xlabel='Frequency (Hz)', ylabel='Amplitude')
thinkplot.show()

# multiplication in the frequency domain corresponds to convolution in the
# time domain.
print(' ---------- acoustic implus effect on violin music  ----------')
output = (violin_spectrum * transfer).make_wave()
output.normalize()

output.plot()
thinkplot.config(title='response effect on violin', xlabel='Time (s)', ylim=[-1.05, 1.05])
thinkplot.show()
output.play()

output_spectrum = output.make_spectrum()
output_spectrum.plot()
thinkplot.config(title='output spectrum', xlabel='Frequency (Hz)', ylabel='Amplitude')
thinkplot.show()

violin.plot()
output.plot()
thinkplot.config(title='compare with orignal violin', xlabel='Time (s)', ylim=[-1.05, 1.05])
thinkplot.show()

print(' ---------- recover violin music  ----------')
revert_transfer = deepcopy(transfer)
revert_transfer.hs = 1 / transfer.hs

revert_transfer.plot()
thinkplot.config(title='revert transfer spectrum', xlabel='Frequency (Hz)', ylabel='Amplitude')
thinkplot.show()

revert_response = revert_transfer.make_wave()
revert_response.plot()
thinkplot.config(title='revert response wave', xlabel='Time (s)', ylim=[-1.05, 1.05])
thinkplot.show()
revert_response.play()

output_spectrum = output.make_spectrum()
output_spectrum.plot()
thinkplot.config(title='recoverred violin spectrum', xlabel='Frequency (Hz)', ylabel='Amplitude')
thinkplot.show()

recoverred_violin = (output_spectrum * revert_transfer).make_wave()
recoverred_violin.normalize()
recoverred_violin.plot()
thinkplot.config(title='recoverred violin wave', xlabel='Time (s)', ylim=[-1.05, 1.05])
thinkplot.show()
recoverred_violin.play()

recoverred_violin.plot(linewidth=1, color='r')
violin.plot(linewidth=1, color='b')
thinkplot.config(title='compare with original violin wave', xlabel='Time (s)', ylim=[-1.05, 1.05])
thinkplot.show()

print('The difference between original violin wave and recoverred violin wave:')
print(max(violin.ys - recoverred_violin.ys))
