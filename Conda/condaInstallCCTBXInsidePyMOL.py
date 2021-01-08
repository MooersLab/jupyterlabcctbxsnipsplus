"""
# At the PyMOL prompt in the PyMOL GUI paste the following:
conda install conda-forge::cctbx-base conda-forge::jupyter 
conda install conda-forge::jupyterlab=2.2.0
conda install conda-forge::cctbx-base
# In a terminal
/Applications/PyMOL.app/Contents/bin/jupyter serverextension enable --py jupyterlab --user
/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol --user
/Applications/PyMOL.app/Contents/bin/pip install jupyterlab-snippets-multimenus
/Applications/PyMOL.app/Contents/bin/jupyter lab build
/Applications/PyMOL.app/Contents/bin/jupyter lab clean
/Applications/PyMOL.app/Contents/bin/jupyter --path # select the top option under Data for storing the libraries
cd ~.local/share/jupyter # change as per output from prior line
mkdir multimenus_snippets
cd multimenus_snippets
git clone https://github.com/MooersLab/juptyerlabpymolcctbx.git cctbx
git clone https://github.com/MooersLab/juptyerlabpymolcctbxplus.git cctbx+
git clone https://github.com/MooersLab/juptyerlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/juptyerlabpymolpysnipsplus.git pymol+
/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol37 --user
"""

# At the PyMOL prompt in the PyMOL GUI paste the following:
conda install conda-forge::cctbx-base conda-forge::jupyter 
conda install conda-forge::jupyterlab=2.2.0
conda install conda-forge::cctbx-base
# In a terminal
/Applications/PyMOL.app/Contents/bin/jupyter serverextension enable --py jupyterlab --user
/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol --user
/Applications/PyMOL.app/Contents/bin/pip install jupyterlab-snippets-multimenus
/Applications/PyMOL.app/Contents/bin/jupyter lab build
/Applications/PyMOL.app/Contents/bin/jupyter lab clean
/Applications/PyMOL.app/Contents/bin/jupyter --path # select the top option under Data for storing the libraries
cd ~.local/share/jupyter # change as per output from prior line
mkdir multimenus_snippets
cd multimenus_snippets
git clone https://github.com/MooersLab/juptyerlabpymolcctbx.git cctbx
git clone https://github.com/MooersLab/juptyerlabpymolcctbxplus.git cctbx+
git clone https://github.com/MooersLab/juptyerlabpymolpysnips.git pymol
git clone https://github.com/MooersLab/juptyerlabpymolpysnipsplus.git pymol+
/Applications/PyMOL.app/Contents/bin/ipython kernel install --name pymol37 --user

# Description:  Install cctbx inside PyMOL. This protocol worked on a Mac OS.
# Source:  NA

