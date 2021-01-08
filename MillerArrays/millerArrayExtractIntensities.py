"""
Iobs = miller_arrays[${1:0}]
iobsdata = Iobs.data()
list(iobsdata[${1:100:110}])
"""

Iobs = miller_arrays[0]
iobsdata = Iobs.data()
list(iobsdata[100:110])

# Description:  Extract just the intensities for a give Miller array and print ten rows of them.
# Source:  NA

