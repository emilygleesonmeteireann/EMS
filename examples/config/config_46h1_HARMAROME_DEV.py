#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os
REP_MUSC = os.getcwd()

############# Begin editing

#GROUP = '46h1'
GROUP = '46t1'
# EXPID will be taken from this file name following the convention config_EXPID.py

# Binaries
bindir = '/home/ewhelan/HARMONIE_BIN/MAKEUP_46h1_DEV/bin'
MASTER = os.path.join(bindir, 'MASTERODB')
#PGD
#PREP
ASCII2FA = os.path.join(bindir, 'ACADFA1D')

# Namelists
ATMNAM = os.path.join(REP_MUSC, 'namelist/AROME/namarp_46t1_AROME_OPER')
#ATMNAM = os.path.join(REP_MUSC, 'namelist/AROME/al46t1_arome-op1.01.nam-namel_previ_dyn_prod')
#SFXNAM

# Model configuration
vert_grid = os.path.join(REP_MUSC, 'grid/L60_AROME.dta')
timestep = 50

# Postprocessing
dirpost = os.path.join(REP_MUSC,'post')
variablesDict = 'variables.py'
defaultConfigPost = 'config_default.py'
caseDependent = True

# EMS configuration
#model = 'AROME46h1'
model = 'AROME46t1'
lforc_ascii = False
lsurfex = False
#sfxfmt
loverwrite = True
lupdate_ATM = True
#lupdate_SFX
lupdate_RUN = True

# ecoclimap data
#ecoclimap

############# End editing
