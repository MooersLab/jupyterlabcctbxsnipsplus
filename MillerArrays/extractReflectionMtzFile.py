"""
from iotbx import mtz
mtz_obj = mtz.object(file_name="${1:Users/blaine/manuscripts/RETkinaseLoxo/ret_blu.mtz}")
mtz_obj.show_summary()
"""

from iotbx import mtz
mtz_obj = mtz.object(file_name="Users/blaine/manuscripts/RETkinaseLoxo/ret_blu.mtz")
mtz_obj.show_summary()

# Description:  Extract the reflections from a mtz file.
# Source:  NA

