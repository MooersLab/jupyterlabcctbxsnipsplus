# Description:  Read mtz file into a Miller array.
# Source:  NA

"""
from iotbx import mtz
mtz_obj = mtz.object(file_name="${1:3nd4}.mtz")
miller_arrays = mtz_obj.as_miller_arrays()
"""

from iotbx import mtz
mtz_obj = mtz.object(file_name="3nd4.mtz")
miller_arrays = mtz_obj.as_miller_arrays()
