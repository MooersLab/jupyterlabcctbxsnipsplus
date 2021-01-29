# Description:  Read in the mtz file and print its column labels as a sanity check.
# Source:  NA

"""
mtz_filename2 = "${1:3hz7intensities}.mtz"
mtz_file2 = mtz.object(mtz_filename2)
mtz_file2.column_labels()
"""

mtz_filename2 = "3hz7intensities.mtz"
mtz_file2 = mtz.object(mtz_filename2)
mtz_file2.column_labels()
