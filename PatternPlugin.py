#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns
import pandas as pd
sns.set(color_codes=True)

from scipy import stats
import matplotlib.pyplot as plt
import os.path as path
plt.rcParams.update({'font.size': 50})
sns.set(rc={"lines.linewidth": 8})
from itertools import cycle


# In[3]:


from matplotlib.ticker import (MultipleLocator, MaxNLocator, 
                                FuncFormatter, ScalarFormatter)

class PatternPlugin:
 def input(self, inputfile):
  self.webmail_16_workload = pd.read_csv(inputfile, header=None, index_col=None)
 def run(self):
     pass
 def output(self, outputfile):
  self.webmail_16_workload.columns = ['request', 'time', 'block']

  fig = plt.figure(figsize=(10, 8))

  ax = sns.scatterplot(x="request", y="block", data=self.webmail_16_workload, 
                     s=5, edgecolor=None, linewidth=0.1, alpha=0.9, color='k')

  #print(ax.xaxis.get_ticklocs()

  ax.xaxis.set_major_locator(plt.MaxNLocator(np.max(self.webmail_16_workload['time']) + 2))
  #print(ax.xaxis.get_ticklocs())
  #print(np.max(webmail_16_workload['time']) + 1)

  ticks=sorted(list(set(self.webmail_16_workload['time'])))
  ticks.insert(0, 0)
  tick_labels = [str(i) for i in ticks]
  print(tick_labels)
  ax.set_xticklabels(tick_labels)

  ax.set_xlabel("Time",fontsize=20)
  ax.tick_params(labelsize=20)
  ax.set_ylabel("Requested item",fontsize=20)

  plt.savefig(outputfile, bbox_inches="tight", dpi=300)


  # In[ ]:




