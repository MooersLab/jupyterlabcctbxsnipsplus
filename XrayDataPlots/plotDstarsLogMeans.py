# Description:  Generate the list of dstars and logMeans as lists for plotting by matplotlib.
# Source:  NA

"""
'''Generate the list of dstars and logMeans as lists
for plotting by matplotlib.'''

used = list(binner.range_used())
selections = [binner.selection(i) for i in used]

# make means of the intensities by bin
means = [Iobs.select(sel).mean() for sel in selections]
from math import log
lnmeans = [log(y) for y in means]

# meansBR = [Iobs.bijvoet_ratios().select(sel).mean() for sel in selections]

# make d_centers
d_star_power = 1.618034
centers = binner.bin_centers(d_star_power)
d_centers = list(centers**(-1 / d_star_power))

%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams["savefig.dpi"] = 600
mpl.rcParams["figure.dpi"] = 600

fig, ax = plt.subplots(figsize=[3.25, 2.])
ax.scatter(d_centers,lnmeans,c="k",alpha=0.3,s=5.5)

ax.set_xlim(${1:8, 1.5}) # decreasing time
ax.set_xlabel(r"$d^*$ in $\AA$",fontsize=12)
ax.set_ylabel("ln(I)",fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
ax.grid(False)
plt.savefig("${2:3hz7}iobsvsdstar.pdf",bbox_inches="tight")
plt.show()
"""

'''Generate the list of dstars and logMeans as lists
for plotting by matplotlib.'''

used = list(binner.range_used())
selections = [binner.selection(i) for i in used]

# make means of the intensities by bin
means = [Iobs.select(sel).mean() for sel in selections]
from math import log
lnmeans = [log(y) for y in means]

# meansBR = [Iobs.bijvoet_ratios().select(sel).mean() for sel in selections]

# make d_centers
d_star_power = 1.618034
centers = binner.bin_centers(d_star_power)
d_centers = list(centers**(-1 / d_star_power))

%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams["savefig.dpi"] = 600
mpl.rcParams["figure.dpi"] = 600

fig, ax = plt.subplots(figsize=[3.25, 2.])
ax.scatter(d_centers,lnmeans,c="k",alpha=0.3,s=5.5)

ax.set_xlim(8, 1.5) # decreasing time
ax.set_xlabel(r"$d^*$ in $\AA$",fontsize=12)
ax.set_ylabel("ln(I)",fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
ax.grid(False)
plt.savefig("3hz7iobsvsdstar.pdf",bbox_inches="tight")
plt.show()
