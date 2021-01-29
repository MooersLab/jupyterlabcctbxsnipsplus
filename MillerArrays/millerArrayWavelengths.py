# Description:  Print wavelengths of each miller array.
# Source:  NA

"""
[print("Miller Array %s: %s" % (i, miller_array.info().wavelength)) for i, miller_array in list(enumerate(miller_arrays))]
"""

[print("Miller Array %s: %s" % (i, miller_array.info().wavelength)) for i, miller_array in list(enumerate(miller_arrays))]
