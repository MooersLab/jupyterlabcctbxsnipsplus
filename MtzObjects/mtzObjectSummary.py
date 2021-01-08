"""
from iotbx import mtz
mtz_obj = mtz.object(file_name="/Users/blaine/${1:3nd4}.mtz")
mtz_obj.show_summary()
"""

from iotbx import mtz
mtz_obj = mtz.object(file_name="/Users/blaine/3nd4.mtz")
mtz_obj.show_summary()

# Description:  Read mtz file into a mtz object and print summary.
# Source:  NA

