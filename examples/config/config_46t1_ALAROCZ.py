#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import os

REP_MUSC = os.getcwd()
EMS_DIR = os.environ["EMS_DIR"]

############# Begin editing

#GROUP = '46h1'
GROUP = '46t1'
# EXPID will be taken from this file name following the convention config_EXPID.py

# Binaries
bindir = '/path/to/hm_musc/expname/lib/bin'
MASTER = os.path.join(bindir, 'MASTERODB')
PGD = os.path.join(bindir, 'PGD')
PREP = os.path.join(bindir, 'PREP')
ASCII2FA = os.path.join(bindir, 'ACADFA1D')

# Namelists
ATMNAM = os.path.join(EMS_DIR, 'share/namelist/ALARO/namarp_46t1_ALARO_CZ')
SFXNAM = os.path.join(EMS_DIR, 'share/namelist/SURFEX/nam.sfx.46t1.test')

# Model configuration
vert_grid = os.path.join(EMS_DIR, 'share/grid/L87_ALAROCZ.dta')
timestep = 50

# Postprocessing
dirpost = os.path.join(EMS_DIR,'share/post')
variablesDict = 'variables.py'
defaultConfigPost = 'config_ARMCU.py'
caseDependent = True

# EMS configuration
model = 'ALARO'

lforc_ascii = False
lsurfex = False
sfxfmt = 'FA'
loverwrite = True
lupdate_ATM = True
lupdate_SFX = True
lupdate_RUN = True

# ecoclimap data
#ecoclimap

############# End editing
