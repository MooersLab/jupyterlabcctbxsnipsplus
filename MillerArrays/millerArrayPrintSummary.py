# Description:  Read mtz file into a miller array and print summary.
# Source:  NA

"""
from iotbx.reflection_file_reader import any_reflection_file
hkl_in = any_reflection_file(file_name="${1:3nd4}.mtz")
miller_arrays = hkl_in.as_miller_arrays()
f_obs = miller_arrays[0]
f_obs.show_summary()
"""

from iotbx.reflection_file_reader import any_reflection_file
hkl_in = any_reflection_file(file_name="3nd4.mtz")
miller_arrays = hkl_in.as_miller_arrays()
f_obs = miller_arrays[0]
f_obs.show_summary()
