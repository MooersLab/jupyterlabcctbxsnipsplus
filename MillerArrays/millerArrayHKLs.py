# Description:  Print all of the miller indices for a given Miller array.
# Source:  NA

"""
[print(hkl) for hkl in miller_arrays[${1:0}].indices()]
"""

[print(hkl) for hkl in miller_arrays[0].indices()]
