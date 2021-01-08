"""
from iotbx import mtz
mtz_obj = mtz.object(file_name="${1:3nd4}.mtz")
# Only works with mtz.object. 
# Does not work if mtz is read in with iotbx.file_reader.
miller_arrays_dict = mtz_obj.as_miller_arrays_dict()
"""

from iotbx import mtz
mtz_obj = mtz.object(file_name="3nd4.mtz")
# Only works with mtz.object. 
# Does not work if mtz is read in with iotbx.file_reader.
miller_arrays_dict = mtz_obj.as_miller_arrays_dict()

# Description:  Set up the arrays as dictionaries
# Source:  NA

