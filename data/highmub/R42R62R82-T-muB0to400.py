#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib.ticker as ticker
import matplotlib as mpl
from scipy.interpolate import spline

mpl.style.use('classic')


# Data for plotting
T1=np.zeros((300,10))
chi2mub0=np.loadtxt(r'./mub0/final/buffer/chi2.dat')
chi4mub0=np.loadtxt(r'./mub0/final/buffer/chi4.dat')
chi6mub0=np.loadtxt(r'./mub0/final/buffer/chi6.dat')
chi8mub0=np.loadtxt(r'./mub0/final/buffer/chi8.dat')
r42mub0=chi4mub0/chi2mub0
r62mub0=chi6mub0/chi2mub0
r82mub0=chi8mub0/chi2mub0
#############################################################################
chi2mub20cen=np.loadtxt(r'./mub20/cmucen/final/buffer/chi2.dat')
chi4mub20cen=np.loadtxt(r'./mub20/cmucen/final/buffer/chi4.dat')
chi6mub20cen=np.loadtxt(r'./mub20/cmucen/final/buffer/chi6.dat')
chi8mub20cen=np.loadtxt(r'./mub20/cmucen/final/buffer/chi8.dat')
r42mub20cen=chi4mub20cen/chi2mub20cen
r62mub20cen=chi6mub20cen/chi2mub20cen
r82mub20cen=chi8mub20cen/chi2mub20cen
chi2mub20up=np.loadtxt(r'./mub20/cmuup/final/buffer/chi2.dat')
chi4mub20up=np.loadtxt(r'./mub20/cmuup/final/buffer/chi4.dat')
chi6mub20up=np.loadtxt(r'./mub20/cmuup/final/buffer/chi6.dat')
chi8mub20up=np.loadtxt(r'./mub20/cmuup/final/buffer/chi8.dat')
r42mub20up=chi4mub20up/chi2mub20up
r62mub20up=chi6mub20up/chi2mub20up
r82mub20up=chi8mub20up/chi2mub20up
chi2mub20down=np.loadtxt(r'./mub20/cmudown/final/buffer/chi2.dat')
chi4mub20down=np.loadtxt(r'./mub20/cmudown/final/buffer/chi4.dat')
chi6mub20down=np.loadtxt(r'./mub20/cmudown/final/buffer/chi6.dat')
chi8mub20down=np.loadtxt(r'./mub20/cmudown/final/buffer/chi8.dat')
r42mub20down=chi4mub20down/chi2mub20down
r62mub20down=chi6mub20down/chi2mub20down
r82mub20down=chi8mub20down/chi2mub20down
############################################################################
chi2mub100cen=np.loadtxt(r'./mub100/cmucen/final/buffer/chi2.dat')
chi4mub100cen=np.loadtxt(r'./mub100/cmucen/final/buffer/chi4.dat')
chi6mub100cen=np.loadtxt(r'./mub100/cmucen/final/buffer/chi6.dat')
chi8mub100cen=np.loadtxt(r'./mub100/cmucen/final/buffer/chi8.dat')
r42mub100cen=chi4mub100cen/chi2mub100cen
r62mub100cen=chi6mub100cen/chi2mub100cen
r82mub100cen=chi8mub100cen/chi2mub100cen
chi2mub100up=np.loadtxt(r'./mub100/cmuup/final/buffer/chi2.dat')
chi4mub100up=np.loadtxt(r'./mub100/cmuup/final/buffer/chi4.dat')
chi6mub100up=np.loadtxt(r'./mub100/cmuup/final/buffer/chi6.dat')
chi8mub100up=np.loadtxt(r'./mub100/cmuup/final/buffer/chi8.dat')
r42mub100up=chi4mub100up/chi2mub100up
r62mub100up=chi6mub100up/chi2mub100up
r82mub100up=chi8mub100up/chi2mub100up
chi2mub100down=np.loadtxt(r'./mub100/cmudown/final/buffer/chi2.dat')
chi4mub100down=np.loadtxt(r'./mub100/cmudown/final/buffer/chi4.dat')
chi6mub100down=np.loadtxt(r'./mub100/cmudown/final/buffer/chi6.dat')
chi8mub100down=np.loadtxt(r'./mub100/cmudown/final/buffer/chi8.dat')
r42mub100down=chi4mub100down/chi2mub100down
r62mub100down=chi6mub100down/chi2mub100down
r82mub100down=chi8mub100down/chi2mub100down
r42100=np.zeros((300,20))
r62100=np.zeros((300,20))
r82100=np.zeros((300,20))
#################################################################################
chi2mub160cen=np.loadtxt(r'./mub160/cmucen/final/buffer/chi2.dat')
chi4mub160cen=np.loadtxt(r'./mub160/cmucen/final/buffer/chi4.dat')
chi6mub160cen=np.loadtxt(r'./mub160/cmucen/final/buffer/chi6.dat')
chi8mub160cen=np.loadtxt(r'./mub160/cmucen/final/buffer/chi8.dat')
r42mub160cen=chi4mub160cen/chi2mub160cen
r62mub160cen=chi6mub160cen/chi2mub160cen
r82mub160cen=chi8mub160cen/chi2mub160cen
chi2mub160up=np.loadtxt(r'./mub160/cmuup/final/buffer/chi2.dat')
chi4mub160up=np.loadtxt(r'./mub160/cmuup/final/buffer/chi4.dat')
chi6mub160up=np.loadtxt(r'./mub160/cmuup/final/buffer/chi6.dat')
chi8mub160up=np.loadtxt(r'./mub160/cmuup/final/buffer/chi8.dat')
r42mub160up=chi4mub160up/chi2mub160up
r62mub160up=chi6mub160up/chi2mub160up
r82mub160up=chi8mub160up/chi2mub160up
chi2mub160down=np.loadtxt(r'./mub160/cmudown/final/buffer/chi2.dat')
chi4mub160down=np.loadtxt(r'./mub160/cmudown/final/buffer/chi4.dat')
chi6mub160down=np.loadtxt(r'./mub160/cmudown/final/buffer/chi6.dat')
chi8mub160down=np.loadtxt(r'./mub160/cmudown/final/buffer/chi8.dat')
r42mub160down=chi4mub160down/chi2mub160down
r62mub160down=chi6mub160down/chi2mub160down
r82mub160down=chi8mub160down/chi2mub160down
r42160=np.zeros((300,20))
r62160=np.zeros((300,20))
r82160=np.zeros((300,20))
#####################################################################################
chi2mub240cen=np.loadtxt(r'./mub240/cmucen/final/buffer/chi2.dat')
chi4mub240cen=np.loadtxt(r'./mub240/cmucen/final/buffer/chi4.dat')
chi6mub240cen=np.loadtxt(r'./mub240/cmucen/final/buffer/chi6.dat')
chi8mub240cen=np.loadtxt(r'./mub240/cmucen/final/buffer/chi8.dat')
r42mub240cen=chi4mub240cen/chi2mub240cen
r62mub240cen=chi6mub240cen/chi2mub240cen
r82mub240cen=chi8mub240cen/chi2mub240cen
chi2mub240up=np.loadtxt(r'./mub240/cmuup/final/buffer/chi2.dat')
chi4mub240up=np.loadtxt(r'./mub240/cmuup/final/buffer/chi4.dat')
chi6mub240up=np.loadtxt(r'./mub240/cmuup/final/buffer/chi6.dat')
chi8mub240up=np.loadtxt(r'./mub240/cmuup/final/buffer/chi8.dat')
r42mub240up=chi4mub240up/chi2mub240up
r62mub240up=chi6mub240up/chi2mub240up
r82mub240up=chi8mub240up/chi2mub240up
chi2mub240down=np.loadtxt(r'./mub240/cmudown/final/buffer/chi2.dat')
chi4mub240down=np.loadtxt(r'./mub240/cmudown/final/buffer/chi4.dat')
chi6mub240down=np.loadtxt(r'./mub240/cmudown/final/buffer/chi6.dat')
chi8mub240down=np.loadtxt(r'./mub240/cmudown/final/buffer/chi8.dat')
r42mub240down=chi4mub240down/chi2mub240down
r62mub240down=chi6mub240down/chi2mub240down
r82mub240down=chi8mub240down/chi2mub240down
r42240=np.zeros((300,20))
r62240=np.zeros((300,20))
r82240=np.zeros((300,20))
#####################################################################################
chi2mub300cen=np.loadtxt(r'./mub300/cmucen/final/buffer/chi2.dat')
chi4mub300cen=np.loadtxt(r'./mub300/cmucen/final/buffer/chi4.dat')
chi6mub300cen=np.loadtxt(r'./mub300/cmucen/final/buffer/chi6.dat')
chi8mub300cen=np.loadtxt(r'./mub300/cmucen/final/buffer/chi8.dat')
r42mub300cen=chi4mub300cen/chi2mub300cen
r62mub300cen=chi6mub300cen/chi2mub300cen
r82mub300cen=chi8mub300cen/chi2mub300cen
chi2mub300up=np.loadtxt(r'./mub300/cmuup/final/buffer/chi2.dat')
chi4mub300up=np.loadtxt(r'./mub300/cmuup/final/buffer/chi4.dat')
chi6mub300up=np.loadtxt(r'./mub300/cmuup/final/buffer/chi6.dat')
chi8mub300up=np.loadtxt(r'./mub300/cmuup/final/buffer/chi8.dat')
r42mub300up=chi4mub300up/chi2mub300up
r62mub300up=chi6mub300up/chi2mub300up
r82mub300up=chi8mub300up/chi2mub300up
chi2mub300up1=np.loadtxt(r'./mub300/cmuup1/final/buffer/chi2.dat')
chi4mub300up1=np.loadtxt(r'./mub300/cmuup1/final/buffer/chi4.dat')
chi6mub300up1=np.loadtxt(r'./mub300/cmuup1/final/buffer/chi6.dat')
chi8mub300up1=np.loadtxt(r'./mub300/cmuup1/final/buffer/chi8.dat')
r42mub300up1=chi4mub300up1/chi2mub300up1
r62mub300up1=chi6mub300up1/chi2mub300up1
r82mub300up1=chi8mub300up1/chi2mub300up1
chi2mub300up2=np.loadtxt(r'./mub300/cmuup2/final/buffer/chi2.dat')
chi4mub300up2=np.loadtxt(r'./mub300/cmuup2/final/buffer/chi4.dat')
chi6mub300up2=np.loadtxt(r'./mub300/cmuup2/final/buffer/chi6.dat')
chi8mub300up2=np.loadtxt(r'./mub300/cmuup2/final/buffer/chi8.dat')
r42mub300up2=chi4mub300up2/chi2mub300up2
r62mub300up2=chi6mub300up2/chi2mub300up2
r82mub300up2=chi8mub300up2/chi2mub300up2
chi2mub300up3=np.loadtxt(r'./mub300/cmuup3/final/buffer/chi2.dat')
chi4mub300up3=np.loadtxt(r'./mub300/cmuup3/final/buffer/chi4.dat')
chi6mub300up3=np.loadtxt(r'./mub300/cmuup3/final/buffer/chi6.dat')
chi8mub300up3=np.loadtxt(r'./mub300/cmuup3/final/buffer/chi8.dat')
r42mub300up3=chi4mub300up3/chi2mub300up3
r62mub300up3=chi6mub300up3/chi2mub300up3
r82mub300up3=chi8mub300up3/chi2mub300up3
chi2mub300up4=np.loadtxt(r'./mub300/cmuup4/final/buffer/chi2.dat')
chi4mub300up4=np.loadtxt(r'./mub300/cmuup4/final/buffer/chi4.dat')
chi6mub300up4=np.loadtxt(r'./mub300/cmuup4/final/buffer/chi6.dat')
chi8mub300up4=np.loadtxt(r'./mub300/cmuup4/final/buffer/chi8.dat')
r42mub300up4=chi4mub300up4/chi2mub300up4
r62mub300up4=chi6mub300up4/chi2mub300up4
r82mub300up4=chi8mub300up4/chi2mub300up4
chi2mub300down=np.loadtxt(r'./mub300/cmudown/final/buffer/chi2.dat')
chi4mub300down=np.loadtxt(r'./mub300/cmudown/final/buffer/chi4.dat')
chi6mub300down=np.loadtxt(r'./mub300/cmudown/final/buffer/chi6.dat')
chi8mub300down=np.loadtxt(r'./mub300/cmudown/final/buffer/chi8.dat')
r42mub300down=chi4mub300down/chi2mub300down
r62mub300down=chi6mub300down/chi2mub300down
r82mub300down=chi8mub300down/chi2mub300down
chi2mub300down1=np.loadtxt(r'./mub300/cmudown1/final/buffer/chi2.dat')
chi4mub300down1=np.loadtxt(r'./mub300/cmudown1/final/buffer/chi4.dat')
chi6mub300down1=np.loadtxt(r'./mub300/cmudown1/final/buffer/chi6.dat')
chi8mub300down1=np.loadtxt(r'./mub300/cmudown1/final/buffer/chi8.dat')
r42mub300down1=chi4mub300down1/chi2mub300down1
r62mub300down1=chi6mub300down1/chi2mub300down1
r82mub300down1=chi8mub300down1/chi2mub300down1
chi2mub300down2=np.loadtxt(r'./mub300/cmudown2/final/buffer/chi2.dat')
chi4mub300down2=np.loadtxt(r'./mub300/cmudown2/final/buffer/chi4.dat')
chi6mub300down2=np.loadtxt(r'./mub300/cmudown2/final/buffer/chi6.dat')
chi8mub300down2=np.loadtxt(r'./mub300/cmudown2/final/buffer/chi8.dat')
r42mub300down2=chi4mub300down2/chi2mub300down2
r62mub300down2=chi6mub300down2/chi2mub300down2
r82mub300down2=chi8mub300down2/chi2mub300down2
chi2mub300down3=np.loadtxt(r'./mub300/cmudown3/final/buffer/chi2.dat')
chi4mub300down3=np.loadtxt(r'./mub300/cmudown3/final/buffer/chi4.dat')
chi6mub300down3=np.loadtxt(r'./mub300/cmudown3/final/buffer/chi6.dat')
chi8mub300down3=np.loadtxt(r'./mub300/cmudown3/final/buffer/chi8.dat')
r42mub300down3=chi4mub300down3/chi2mub300down3
r62mub300down3=chi6mub300down3/chi2mub300down3
r82mub300down3=chi8mub300down3/chi2mub300down3
chi2mub300down4=np.loadtxt(r'./mub300/cmudown4/final/buffer/chi2.dat')
chi4mub300down4=np.loadtxt(r'./mub300/cmudown4/final/buffer/chi4.dat')
chi6mub300down4=np.loadtxt(r'./mub300/cmudown4/final/buffer/chi6.dat')
chi8mub300down4=np.loadtxt(r'./mub300/cmudown4/final/buffer/chi8.dat')
r42mub300down4=chi4mub300down4/chi2mub300down4
r62mub300down4=chi6mub300down4/chi2mub300down4
r82mub300down4=chi8mub300down4/chi2mub300down4
r42300=np.zeros((300,100))
r62300=np.zeros((300,100))
r82300=np.zeros((300,100))
#####################################################################################
chi2mub320cen=np.loadtxt(r'./mub320/cmucen/final/buffer/chi2.dat')
chi4mub320cen=np.loadtxt(r'./mub320/cmucen/final/buffer/chi4.dat')
chi6mub320cen=np.loadtxt(r'./mub320/cmucen/final/buffer/chi6.dat')
chi8mub320cen=np.loadtxt(r'./mub320/cmucen/final/buffer/chi8.dat')
r42mub320cen=chi4mub320cen/chi2mub320cen
r62mub320cen=chi6mub320cen/chi2mub320cen
r82mub320cen=chi8mub320cen/chi2mub320cen
chi2mub320up=np.loadtxt(r'./mub320/cmuup/final/buffer/chi2.dat')
chi4mub320up=np.loadtxt(r'./mub320/cmuup/final/buffer/chi4.dat')
chi6mub320up=np.loadtxt(r'./mub320/cmuup/final/buffer/chi6.dat')
chi8mub320up=np.loadtxt(r'./mub320/cmuup/final/buffer/chi8.dat')
r42mub320up=chi4mub320up/chi2mub320up
r62mub320up=chi6mub320up/chi2mub320up
r82mub320up=chi8mub320up/chi2mub320up
chi2mub320down=np.loadtxt(r'./mub320/cmudown/final/buffer/chi2.dat')
chi4mub320down=np.loadtxt(r'./mub320/cmudown/final/buffer/chi4.dat')
chi6mub320down=np.loadtxt(r'./mub320/cmudown/final/buffer/chi6.dat')
chi8mub320down=np.loadtxt(r'./mub320/cmudown/final/buffer/chi8.dat')
r42mub320down=chi4mub320down/chi2mub320down
r62mub320down=chi6mub320down/chi2mub320down
r82mub320down=chi8mub320down/chi2mub320down
r42320=np.zeros((300,20))
r62320=np.zeros((300,20))
r82320=np.zeros((300,20))
#####################################################################################
chi2mub340cen=np.loadtxt(r'./mub340/cmucen/final/buffer/chi2.dat')
chi4mub340cen=np.loadtxt(r'./mub340/cmucen/final/buffer/chi4.dat')
chi6mub340cen=np.loadtxt(r'./mub340/cmucen/final/buffer/chi6.dat')
chi8mub340cen=np.loadtxt(r'./mub340/cmucen/final/buffer/chi8.dat')
r42mub340cen=chi4mub340cen/chi2mub340cen
r62mub340cen=chi6mub340cen/chi2mub340cen
r82mub340cen=chi8mub340cen/chi2mub340cen
chi2mub340up=np.loadtxt(r'./mub340/cmuup/final/buffer/chi2.dat')
chi4mub340up=np.loadtxt(r'./mub340/cmuup/final/buffer/chi4.dat')
chi6mub340up=np.loadtxt(r'./mub340/cmuup/final/buffer/chi6.dat')
chi8mub340up=np.loadtxt(r'./mub340/cmuup/final/buffer/chi8.dat')
r42mub340up=chi4mub340up/chi2mub340up
r62mub340up=chi6mub340up/chi2mub340up
r82mub340up=chi8mub340up/chi2mub340up
chi2mub340down=np.loadtxt(r'./mub340/cmudown/final/buffer/chi2.dat')
chi4mub340down=np.loadtxt(r'./mub340/cmudown/final/buffer/chi4.dat')
chi6mub340down=np.loadtxt(r'./mub340/cmudown/final/buffer/chi6.dat')
chi8mub340down=np.loadtxt(r'./mub340/cmudown/final/buffer/chi8.dat')
r42mub340down=chi4mub340down/chi2mub340down
r62mub340down=chi6mub340down/chi2mub340down
r82mub340down=chi8mub340down/chi2mub340down
r42340=np.zeros((300,20))
r62340=np.zeros((300,20))
r82340=np.zeros((300,20))
#########################################################################################
chi2mub360cen=np.loadtxt(r'./mub360/cmucen/final/buffer/chi2.dat')
chi4mub360cen=np.loadtxt(r'./mub360/cmucen/final/buffer/chi4.dat')
chi6mub360cen=np.loadtxt(r'./mub360/cmucen/final/buffer/chi6.dat')
chi8mub360cen=np.loadtxt(r'./mub360/cmucen/final/buffer/chi8.dat')
r42mub360cen=chi4mub360cen/chi2mub360cen
r62mub360cen=chi6mub360cen/chi2mub360cen
r82mub360cen=chi8mub360cen/chi2mub360cen
chi2mub360up=np.loadtxt(r'./mub360/cmuup/final/buffer/chi2.dat')
chi4mub360up=np.loadtxt(r'./mub360/cmuup/final/buffer/chi4.dat')
chi6mub360up=np.loadtxt(r'./mub360/cmuup/final/buffer/chi6.dat')
chi8mub360up=np.loadtxt(r'./mub360/cmuup/final/buffer/chi8.dat')
r42mub360up=chi4mub360up/chi2mub360up
r62mub360up=chi6mub360up/chi2mub360up
r82mub360up=chi8mub360up/chi2mub360up
chi2mub360down=np.loadtxt(r'./mub360/cmudown/final/buffer/chi2.dat')
chi4mub360down=np.loadtxt(r'./mub360/cmudown/final/buffer/chi4.dat')
chi6mub360down=np.loadtxt(r'./mub360/cmudown/final/buffer/chi6.dat')
chi8mub360down=np.loadtxt(r'./mub360/cmudown/final/buffer/chi8.dat')
r42mub360down=chi4mub360down/chi2mub360down
r62mub360down=chi6mub360down/chi2mub360down
r82mub360down=chi8mub360down/chi2mub360down
r42360=np.zeros((300,20))
r62360=np.zeros((300,20))
r82360=np.zeros((300,20))
#########################################################################################
chi2mub380cen=np.loadtxt(r'./mub380/cmucen/final/buffer/chi2.dat')
chi4mub380cen=np.loadtxt(r'./mub380/cmucen/final/buffer/chi4.dat')
chi6mub380cen=np.loadtxt(r'./mub380/cmucen/final/buffer/chi6.dat')
chi8mub380cen=np.loadtxt(r'./mub380/cmucen/final/buffer/chi8.dat')
r42mub380cen=chi4mub380cen/chi2mub380cen
r62mub380cen=chi6mub380cen/chi2mub380cen
r82mub380cen=chi8mub380cen/chi2mub380cen
chi2mub380up=np.loadtxt(r'./mub380/cmuup/final/buffer/chi2.dat')
chi4mub380up=np.loadtxt(r'./mub380/cmuup/final/buffer/chi4.dat')
chi6mub380up=np.loadtxt(r'./mub380/cmuup/final/buffer/chi6.dat')
chi8mub380up=np.loadtxt(r'./mub380/cmuup/final/buffer/chi8.dat')
r42mub380up=chi4mub380up/chi2mub380up
r62mub380up=chi6mub380up/chi2mub380up
r82mub380up=chi8mub380up/chi2mub380up
chi2mub380down=np.loadtxt(r'./mub380/cmudown/final/buffer/chi2.dat')
chi4mub380down=np.loadtxt(r'./mub380/cmudown/final/buffer/chi4.dat')
chi6mub380down=np.loadtxt(r'./mub380/cmudown/final/buffer/chi6.dat')
chi8mub380down=np.loadtxt(r'./mub380/cmudown/final/buffer/chi8.dat')
r42mub380down=chi4mub380down/chi2mub380down
r62mub380down=chi6mub380down/chi2mub380down
r82mub380down=chi8mub380down/chi2mub380down
r42380=np.zeros((300,20))
r62380=np.zeros((300,20))
r82380=np.zeros((300,20))
#########################################################################################
chi2mub400cen=np.loadtxt(r'./mub400/cmucen/final/buffer/chi2.dat')
chi4mub400cen=np.loadtxt(r'./mub400/cmucen/final/buffer/chi4.dat')
chi6mub400cen=np.loadtxt(r'./mub400/cmucen/final/buffer/chi6.dat')
chi8mub400cen=np.loadtxt(r'./mub400/cmucen/final/buffer/chi8.dat')
r42mub400cen=chi4mub400cen/chi2mub400cen
r62mub400cen=chi6mub400cen/chi2mub400cen
r82mub400cen=chi8mub400cen/chi2mub400cen
chi2mub400up=np.loadtxt(r'./mub400/cmuup/final/buffer/chi2.dat')
chi4mub400up=np.loadtxt(r'./mub400/cmuup/final/buffer/chi4.dat')
chi6mub400up=np.loadtxt(r'./mub400/cmuup/final/buffer/chi6.dat')
chi8mub400up=np.loadtxt(r'./mub400/cmuup/final/buffer/chi8.dat')
r42mub400up=chi4mub400up/chi2mub400up
r62mub400up=chi6mub400up/chi2mub400up
r82mub400up=chi8mub400up/chi2mub400up
chi2mub400up1=np.loadtxt(r'./mub400/cmuup1/final/buffer/chi2.dat')
chi4mub400up1=np.loadtxt(r'./mub400/cmuup1/final/buffer/chi4.dat')
chi6mub400up1=np.loadtxt(r'./mub400/cmuup1/final/buffer/chi6.dat')
chi8mub400up1=np.loadtxt(r'./mub400/cmuup1/final/buffer/chi8.dat')
r42mub400up1=chi4mub400up1/chi2mub400up1
r62mub400up1=chi6mub400up1/chi2mub400up1
r82mub400up1=chi8mub400up1/chi2mub400up1
chi2mub400up2=np.loadtxt(r'./mub400/cmuup2/final/buffer/chi2.dat')
chi4mub400up2=np.loadtxt(r'./mub400/cmuup2/final/buffer/chi4.dat')
chi6mub400up2=np.loadtxt(r'./mub400/cmuup2/final/buffer/chi6.dat')
chi8mub400up2=np.loadtxt(r'./mub400/cmuup2/final/buffer/chi8.dat')
r42mub400up2=chi4mub400up2/chi2mub400up2
r62mub400up2=chi6mub400up2/chi2mub400up2
r82mub400up2=chi8mub400up2/chi2mub400up2
chi2mub400up3=np.loadtxt(r'./mub400/cmuup3/final/buffer/chi2.dat')
chi4mub400up3=np.loadtxt(r'./mub400/cmuup3/final/buffer/chi4.dat')
chi6mub400up3=np.loadtxt(r'./mub400/cmuup3/final/buffer/chi6.dat')
chi8mub400up3=np.loadtxt(r'./mub400/cmuup3/final/buffer/chi8.dat')
r42mub400up3=chi4mub400up3/chi2mub400up3
r62mub400up3=chi6mub400up3/chi2mub400up3
r82mub400up3=chi8mub400up3/chi2mub400up3
chi2mub400up4=np.loadtxt(r'./mub400/cmuup4/final/buffer/chi2.dat')
chi4mub400up4=np.loadtxt(r'./mub400/cmuup4/final/buffer/chi4.dat')
chi6mub400up4=np.loadtxt(r'./mub400/cmuup4/final/buffer/chi6.dat')
chi8mub400up4=np.loadtxt(r'./mub400/cmuup4/final/buffer/chi8.dat')
r42mub400up4=chi4mub400up4/chi2mub400up4
r62mub400up4=chi6mub400up4/chi2mub400up4
r82mub400up4=chi8mub400up4/chi2mub400up4
chi2mub400down=np.loadtxt(r'./mub400/cmudown/final/buffer/chi2.dat')
chi4mub400down=np.loadtxt(r'./mub400/cmudown/final/buffer/chi4.dat')
chi6mub400down=np.loadtxt(r'./mub400/cmudown/final/buffer/chi6.dat')
chi8mub400down=np.loadtxt(r'./mub400/cmudown/final/buffer/chi8.dat')
r42mub400down=chi4mub400down/chi2mub400down
r62mub400down=chi6mub400down/chi2mub400down
r82mub400down=chi8mub400down/chi2mub400down
chi2mub400down1=np.loadtxt(r'./mub400/cmudown1/final/buffer/chi2.dat')
chi4mub400down1=np.loadtxt(r'./mub400/cmudown1/final/buffer/chi4.dat')
chi6mub400down1=np.loadtxt(r'./mub400/cmudown1/final/buffer/chi6.dat')
chi8mub400down1=np.loadtxt(r'./mub400/cmudown1/final/buffer/chi8.dat')
r42mub400down1=chi4mub400down1/chi2mub400down1
r62mub400down1=chi6mub400down1/chi2mub400down1
r82mub400down1=chi8mub400down1/chi2mub400down1
chi2mub400down2=np.loadtxt(r'./mub400/cmudown2/final/buffer/chi2.dat')
chi4mub400down2=np.loadtxt(r'./mub400/cmudown2/final/buffer/chi4.dat')
chi6mub400down2=np.loadtxt(r'./mub400/cmudown2/final/buffer/chi6.dat')
chi8mub400down2=np.loadtxt(r'./mub400/cmudown2/final/buffer/chi8.dat')
r42mub400down2=chi4mub400down2/chi2mub400down2
r62mub400down2=chi6mub400down2/chi2mub400down2
r82mub400down2=chi8mub400down2/chi2mub400down2
chi2mub400down3=np.loadtxt(r'./mub400/cmudown3/final/buffer/chi2.dat')
chi4mub400down3=np.loadtxt(r'./mub400/cmudown3/final/buffer/chi4.dat')
chi6mub400down3=np.loadtxt(r'./mub400/cmudown3/final/buffer/chi6.dat')
chi8mub400down3=np.loadtxt(r'./mub400/cmudown3/final/buffer/chi8.dat')
r42mub400down3=chi4mub400down3/chi2mub400down3
r62mub400down3=chi6mub400down3/chi2mub400down3
r82mub400down3=chi8mub400down3/chi2mub400down3
chi2mub400down4=np.loadtxt(r'./mub400/cmudown4/final/buffer/chi2.dat')
chi4mub400down4=np.loadtxt(r'./mub400/cmudown4/final/buffer/chi4.dat')
chi6mub400down4=np.loadtxt(r'./mub400/cmudown4/final/buffer/chi6.dat')
chi8mub400down4=np.loadtxt(r'./mub400/cmudown4/final/buffer/chi8.dat')
r42mub400down4=chi4mub400down4/chi2mub400down4
r62mub400down4=chi6mub400down4/chi2mub400down4
r82mub400down4=chi8mub400down4/chi2mub400down4
r42400=np.zeros((300,100))
r62400=np.zeros((300,100))
r82400=np.zeros((300,100))
#########################################################################################
T=np.loadtxt(r'./TMeV.dat')
Tcen=T/1.247
Tup=T/1.259
Tdown=T/1.235
ctup=1.259
ctdown=1.235
ct=np.linspace(ctdown,ctup,10)
xsame=np.linspace(0.,300.,300)
# Create figure
fig=plt.figure(figsize=(13.5, 3.5))
#fig=plt.figure()
ax1=fig.add_subplot(131)
band_mub0=ax1.fill_betweenx(r42mub0,Tup,Tdown,alpha=0.25,facecolor='r',edgecolor='')
line_mub0,=ax1.plot(Tcen,r42mub0,'r',linewidth=1,alpha=0.5)
#########################################################################################
for t in range(0,100):
    if t<10:
       r42300[:,t]=spline(T/ct[t],r42mub300up,xsame)
    else:
       if t>=10 and t<20:
          r42300[:,t]=spline(T/ct[t-10],r42mub300up1,xsame)
       else:
          if t>=20 and t<30:
             r42300[:,t]=spline(T/ct[t-20],r42mub300up2,xsame)
          else: 
             if t>=30 and t<40:
                r42300[:,t]=spline(T/ct[t-30],r42mub300up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42300[:,t]=spline(T/ct[t-40],r42mub300up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42300[:,t]=spline(T/ct[t-50],r42mub300down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42300[:,t]=spline(T/ct[t-60],r42mub300down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42300[:,t]=spline(T/ct[t-70],r42mub300down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42300[:,t]=spline(T/ct[t-80],r42mub300down3,xsame)
                            else:
                                r42300[:,t]=spline(T/ct[t-90],r42mub300down4,xsame)


for num in range(1,100):
    if num==1:
       max300=np.maximum(r42300[:,num-1],r42300[:,num])
       min300=np.minimum(r42300[:,num-1],r42300[:,num])
    else:
       max300=np.maximum(max300,r42300[:,num])
       min300=np.minimum(min300,r42300[:,num])

band_mub300=ax1.fill_between(xsame,max300,min300,alpha=0.25,facecolor='b',edgecolor='')
line_mub300,=ax1.plot(Tcen,r42mub300cen,'b',linewidth=1,alpha=0.5)
#line_mub300,=ax1.plot(Tup,r42mub300up,'k',linewidth=1,alpha=0.5)
#line_mub300,=ax1.plot(Tup,r42mub300down,'b',linewidth=1,alpha=0.5)
#line_mub300,=ax1.plot(Tdown,r42mub300up,'r',linewidth=1,alpha=0.5)
#line_mub300,=ax1.plot(Tdown,r42mub300down,'m',linewidth=1,alpha=0.5)
############################################################################################
for t in range(0,100):
    if t<10:
       r42400[:,t]=spline(T/ct[t],r42mub400up,xsame)
    else:
       if t>=10 and t<20:
          r42400[:,t]=spline(T/ct[t-10],r42mub400up1,xsame)
       else:
          if t>=20 and t<30:
             r42400[:,t]=spline(T/ct[t-20],r42mub400up2,xsame)
          else: 
             if t>=30 and t<40:
                r42400[:,t]=spline(T/ct[t-30],r42mub400up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42400[:,t]=spline(T/ct[t-40],r42mub400up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42400[:,t]=spline(T/ct[t-50],r42mub400down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42400[:,t]=spline(T/ct[t-60],r42mub400down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42400[:,t]=spline(T/ct[t-70],r42mub400down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42400[:,t]=spline(T/ct[t-80],r42mub400down3,xsame)
                            else:
                                r42400[:,t]=spline(T/ct[t-90],r42mub400down4,xsame)
                                 


for num in range(1,99):
    if num==1:
       max400=np.maximum(r42400[:,num-1],r42400[:,num])
       min400=np.minimum(r42400[:,num-1],r42400[:,num])
    else:
       max400=np.maximum(max400,r42400[:,num])
       min400=np.minimum(min400,r42400[:,num])

band_mub400=ax1.fill_between(xsame,max400,min400,alpha=0.25,facecolor='k',edgecolor='')
line_mub400,=ax1.plot(Tcen,r42mub400cen,'k',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tup,r42mub400up,'k',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tup,r42mub400up1,'k',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tup,r42mub400up2,'k',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tup,r42mub400up3,'k',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tup,r42mub400up4,'k',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tup,r42mub400down,'b',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tup,r42mub400down1,'b',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tup,r42mub400down2,'b',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tup,r42mub400down3,'b',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tup,r42mub400down4,'b',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tdown,r42mub400up,'r',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tdown,r42mub400up1,'r',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tdown,r42mub400up2,'r',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tdown,r42mub400up3,'r',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tdown,r42mub400up4,'r',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tdown,r42mub400down,'m',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tdown,r42mub400down1,'m',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tdown,r42mub400down2,'m',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tdown,r42mub400down3,'m',linewidth=1,alpha=0.5)
#line_mub400,=ax1.plot(Tdown,r42mub400down4,'m',linewidth=1,alpha=0.5)
################################################################################################
ax1.axis([80,230,-1.5,2.])
#ax1.set_xscale('log')

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$\chi^B_4/\chi^B_2$', fontsize=14, color='black')

ax1.legend([(band_mub0,line_mub0),(band_mub300,line_mub300),(band_mub400,line_mub400)],[r'$\mu_B=0$ MeV',r'$\mu_B=300$ MeV',r'$\mu_B=400$ MeV'],loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

ax2=fig.add_subplot(132)

band_mub0=ax2.fill_betweenx(r62mub0,Tup,Tdown,alpha=0.25,facecolor='r',edgecolor='')
line_mub0,=ax2.plot(Tcen,r62mub0,'r',linewidth=1,alpha=0.5)
#####################################################################################################################
for t in range(0,100):
    if t<10:
       r62400[:,t]=spline(T/ct[t],r62mub400up,xsame)
    else:
       if t>=10 and t<20:
          r62400[:,t]=spline(T/ct[t-10],r62mub400up1,xsame)
       else:
          if t>=20 and t<30:
             r62400[:,t]=spline(T/ct[t-20],r62mub400up2,xsame)
          else: 
             if t>=30 and t<40:
                r62400[:,t]=spline(T/ct[t-30],r62mub400up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62400[:,t]=spline(T/ct[t-40],r62mub400up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62400[:,t]=spline(T/ct[t-50],r62mub400down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62400[:,t]=spline(T/ct[t-60],r62mub400down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62400[:,t]=spline(T/ct[t-70],r62mub400down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62400[:,t]=spline(T/ct[t-80],r62mub400down3,xsame)
                            else:
                                r62400[:,t]=spline(T/ct[t-90],r62mub400down4,xsame)


for num in range(1,100):
    if num==1:
       max400=np.maximum(r62400[:,num-1],r62400[:,num])
       min400=np.minimum(r62400[:,num-1],r62400[:,num])
    else:
       max400=np.maximum(max400,r62400[:,num])
       min400=np.minimum(min400,r62400[:,num])

band_mub400=ax2.fill_between(xsame,max400,min400,alpha=0.25,facecolor='k',edgecolor='')
line_mub400,=ax2.plot(Tcen,r62mub400cen,'k',linewidth=1,alpha=0.5)
#line_mub400,=ax2.plot(Tup,r62mub400up,'k',linewidth=1,alpha=0.5)
#line_mub400,=ax2.plot(Tup,r62mub400down,'b',linewidth=1,alpha=0.5)
#line_mub400,=ax2.plot(Tdown,r62mub400up,'r',linewidth=1,alpha=0.5)
#line_mub400,=ax2.plot(Tdown,r62mub400down,'m',linewidth=1,alpha=0.5)
#####################################################################################################################
for t in range(0,100):
    if t<10:
       r62300[:,t]=spline(T/ct[t],r62mub300up,xsame)
    else:
       if t>=10 and t<20:
          r62300[:,t]=spline(T/ct[t-10],r62mub300up1,xsame)
       else:
          if t>=20 and t<30:
             r62300[:,t]=spline(T/ct[t-20],r62mub300up2,xsame)
          else: 
             if t>=30 and t<40:
                r62300[:,t]=spline(T/ct[t-30],r62mub300up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62300[:,t]=spline(T/ct[t-40],r62mub300up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62300[:,t]=spline(T/ct[t-50],r62mub300down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62300[:,t]=spline(T/ct[t-60],r62mub300down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62300[:,t]=spline(T/ct[t-70],r62mub300down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62300[:,t]=spline(T/ct[t-80],r62mub300down3,xsame)
                            else:
                                r62300[:,t]=spline(T/ct[t-90],r62mub300down4,xsame)


for num in range(1,100):
    if num==1:
       max300=np.maximum(r62300[:,num-1],r62300[:,num])
       min300=np.minimum(r62300[:,num-1],r62300[:,num])
    else:
       max300=np.maximum(max300,r62300[:,num])
       min300=np.minimum(min300,r62300[:,num])

band_mub300=ax2.fill_between(xsame,max300,min300,alpha=0.25,facecolor='b',edgecolor='')
line_mub300,=ax2.plot(Tcen,r62mub300cen,'b',linewidth=1,alpha=0.5)
#line_mub300,=ax2.plot(Tup,r62mub300up,'k',linewidth=1,alpha=0.5)
#line_mub300,=ax2.plot(Tup,r62mub300down,'b',linewidth=1,alpha=0.5)
#line_mub300,=ax2.plot(Tdown,r62mub300up,'r',linewidth=1,alpha=0.5)
#line_mub300,=ax2.plot(Tdown,r62mub300down,'m',linewidth=1,alpha=0.5)
#####################################################################################################################

ax2.axis([80,230,-50,40])
#ax2.set_xscale('log')
ax2.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$\chi^B_6/\chi^B_2$', fontsize=14, color='black')

ax2.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)

############################################################################################################################
############################################################################################################################
############################################################################################################################
ax3=fig.add_subplot(133)
band_mub0=ax3.fill_betweenx(r82mub0,Tup,Tdown,alpha=0.25,facecolor='r',edgecolor='')
line_mub0,=ax3.plot(Tcen,r82mub0,'r',linewidth=1,alpha=0.5)
######################################################################################################################
for t in range(0,100):
    if t<10:
       r82300[:,t]=spline(T/ct[t],r82mub300up,xsame)
    else:
       if t>=10 and t<20:
          r82300[:,t]=spline(T/ct[t-10],r82mub300up1,xsame)
       else:
          if t>=20 and t<30:
             r82300[:,t]=spline(T/ct[t-20],r82mub300up2,xsame)
          else: 
             if t>=30 and t<40:
                r82300[:,t]=spline(T/ct[t-30],r82mub300up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82300[:,t]=spline(T/ct[t-40],r82mub300up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82300[:,t]=spline(T/ct[t-50],r82mub300down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82300[:,t]=spline(T/ct[t-60],r82mub300down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82300[:,t]=spline(T/ct[t-70],r82mub300down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82300[:,t]=spline(T/ct[t-80],r82mub300down3,xsame)
                            else:
                                r82300[:,t]=spline(T/ct[t-90],r82mub300down4,xsame)


for num in range(1,100):
    if num==1:
       max300=np.maximum(r82300[:,num-1],r82300[:,num])
       min300=np.minimum(r82300[:,num-1],r82300[:,num])
    else:
       max300=np.maximum(max300,r82300[:,num])
       min300=np.minimum(min300,r82300[:,num])

band_mub300=ax3.fill_between(xsame,max300,min300,alpha=0.25,facecolor='b',edgecolor='')
line_mub300,=ax3.plot(Tcen,r82mub300cen,'b',linewidth=1,alpha=0.5)
#line_mub300,=ax3.plot(Tup,r82mub300up,'k',linewidth=1,alpha=0.5)
#line_mub300,=ax3.plot(Tup,r82mub300down,'b',linewidth=1,alpha=0.5)
#line_mub300,=ax3.plot(Tdown,r82mub300up,'r',linewidth=1,alpha=0.5)
#line_mub300,=ax3.plot(Tdown,r82mub300down,'m',linewidth=1,alpha=0.5)
######################################################################################################################
for t in range(0,100):
    if t<10:
       r82400[:,t]=spline(T/ct[t],r82mub400up,xsame)
    else:
       if t>=10 and t<20:
          r82400[:,t]=spline(T/ct[t-10],r82mub400up1,xsame)
       else:
          if t>=20 and t<30:
             r82400[:,t]=spline(T/ct[t-20],r82mub400up2,xsame)
          else: 
             if t>=30 and t<40:
                r82400[:,t]=spline(T/ct[t-30],r82mub400up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82400[:,t]=spline(T/ct[t-40],r82mub400up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82400[:,t]=spline(T/ct[t-50],r82mub400down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82400[:,t]=spline(T/ct[t-60],r82mub400down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82400[:,t]=spline(T/ct[t-70],r82mub400down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82400[:,t]=spline(T/ct[t-80],r82mub400down3,xsame)
                            else:
                                r82400[:,t]=spline(T/ct[t-90],r82mub400down4,xsame)


for num in range(1,100):
    if num==1:
       max400=np.maximum(r82400[:,num-1],r82400[:,num])
       min400=np.minimum(r82400[:,num-1],r82400[:,num])
    else:
       max400=np.maximum(max400,r82400[:,num])
       min400=np.minimum(min400,r82400[:,num])

band_mub400=ax3.fill_between(xsame,max400,min400,alpha=0.25,facecolor='k',edgecolor='')
line_mub400,=ax3.plot(Tcen,r82mub400cen,'k',linewidth=1,alpha=0.5)
#line_mub400,=ax3.plot(Tup,r82mub400up,'k',linewidth=1,alpha=0.5)
#line_mub400,=ax3.plot(Tup,r82mub400down,'b',linewidth=1,alpha=0.5)
#line_mub400,=ax3.plot(Tdown,r82mub400up,'r',linewidth=1,alpha=0.5)
#line_mub400,=ax3.plot(Tdown,r82mub400down,'m',linewidth=1,alpha=0.5)

ax3.axis([90,210,-1400,2300])
#ax3.set_xscale('log')

ax3.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax3.set_ylabel(r'$\chi^B_8/\chi^B_2$', fontsize=14, color='black')

ax3.legend(loc=0,fontsize='x-small',frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax3.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax3.yaxis.get_ticklabels():
    label.set_fontsize(10)

#for ax in fig.axes:
#    ax.grid(True)

# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
#plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
fig.subplots_adjust(top=0.9, bottom=0.15, left=0.06, right=0.96, hspace=0.35, wspace=0.25)


fig.savefig("R42R62R82-T-muB0to400.pdf")

#plt.show()
