# Description:  Map generated reflections to the asu and print.
# Source:  NA

"""
from cctbx import miller
import cctbx
from cctbx import crystal

ms = miller.build_set(
    crystal_symmetry=crystal.symmetry(
        space_group_symbol="${1:Fd-3m}",
        unit_cell=(${2:5.4307,5.4307,5.4307,90.00,90.0,90.00})),
    anomalous_flag=${3:True},
    d_min=${4:0.4})

msu = ms.map_to_asu()
[print(hkl2) for hkl2 in msu.indices()]
"""

from cctbx import miller
import cctbx
from cctbx import crystal

ms = miller.build_set(
    crystal_symmetry=crystal.symmetry(
        space_group_symbol="Fd-3m",
        unit_cell=(5.4307,5.4307,5.4307,90.00,90.0,90.00)),
    anomalous_flag=True,
    d_min=0.4)

msu = ms.map_to_asu()
[print(hkl2) for hkl2 in msu.indices()]
