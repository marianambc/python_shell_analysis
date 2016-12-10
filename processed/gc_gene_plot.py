
# coding: utf-8

# In[2]:

# Write sudo code:

# import libraries: pandas matlibplot.pyplot

# import data using pandas

# calculate proportions
# save them as new columns in existing dataframe

# make a nice plot of GC content vs. Gene content
# save figure to an appropriate file


import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import sys
# sys is for the arguments that if can take and so on?
# Usage:
# python gc_genee_plot.py myfile
# filename = "myfile"

filename = sys.argv[1]
print("You are analyzing file:")
print(filename)

human_chr21 = pd.read_csv(filename, sep = '\t') # \t -> to explain that is tab delimited data

human_chr21['gc_content'] = human_chr21['gc_bases']/ (human_chr21['win_end'] - human_chr21['win_start'])

human_chr21['gene_content'] = human_chr21['exon_bases'] / (human_chr21['win_end'] - human_chr21['win_start'])


plt.plot(human_chr21['gene_content'], human_chr21['gc_content'], 'o')
# plt.show()
plot_file_name = filename + '.plot.png'
plt.savefig(plot_file_name)


