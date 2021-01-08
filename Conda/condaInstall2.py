"""
# These commands need to be run on the command line.
conda remove --name cctbx${1:37}
conda create -n ${2:cctbx38} -c conda-forge cctbx-base python=${4:3.8}
conda activate ${2:cctbx38}
conda install -c conda-forge cctbx-base
conda install -c anaconda ipykernel
python -m ipykernel install --user --name ${2:cctbx38} --display-name "${2:cctbx38}"
"""

# These commands need to be run on the command line.
conda remove --name cctbx37
conda create -n cctbx38 -c conda-forge cctbx-base python=3.8
conda activate cctbx38
conda install -c conda-forge cctbx-base
conda install -c anaconda ipykernel
python -m ipykernel install --user --name cctbx38 --display-name "cctbx38"

# Description:  The conda commands to remove old env and create a new one for  cctbx.
# Source:  NA

