# Description:  The conda commands to install cctbx with the jupyter notebook, pandas, and xarray.
# Source:  NA

"""
conda create --name ${1:cctbx37} python=${2:3.7}
conda activate ${1:cctbx37}
conda install -c conda-forge cctbx-base jupyter pandas xarray
"""

conda create --name cctbx37 python=3.7
conda activate cctbx37
conda install -c conda-forge cctbx-base jupyter pandas xarray
