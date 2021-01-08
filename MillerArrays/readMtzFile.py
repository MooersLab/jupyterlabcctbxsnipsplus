"""
from iotbx.file_reader import any_file
mtz_in = any_file("$1:data}.mtz", force_type="mtz")
miller_arrays = mtz_in.file_server.miller_arrays
"""

from iotbx.file_reader import any_file
mtz_in = any_file("$1:data.mtz", force_type="mtz")
miller_arrays = mtz_in.file_server.miller_arrays

# Description:  Read in a mtz file into a Miller array with iotbx.file_reader.
# Source:  NA

