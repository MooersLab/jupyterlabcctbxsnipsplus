# Description:  Print the crystal symmetry of each miller array.
# Source:  NA

"""
[print("Miller Array %s: %s" % (i, miller_array.info().crystal_symmetry_from_file)) for i, miller_array in list(enumerate(miller_arrays))]
"""

[print("Miller Array %s: %s" % (i, miller_array.info().crystal_symmetry_from_file)) for i, miller_array in list(enumerate(miller_arrays))]
