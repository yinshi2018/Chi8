#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sphinx_gallery_thumbnail_number = 3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
from matplotlib.ticker import FuncFormatter  # scientific numbers
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
chi2mub200cen=np.loadtxt(r'./mub200/cmucen/final/buffer/chi2.dat')
chi4mub200cen=np.loadtxt(r'./mub200/cmucen/final/buffer/chi4.dat')
chi6mub200cen=np.loadtxt(r'./mub200/cmucen/final/buffer/chi6.dat')
chi8mub200cen=np.loadtxt(r'./mub200/cmucen/final/buffer/chi8.dat')
r42mub200cen=chi4mub200cen/chi2mub200cen
r62mub200cen=chi6mub200cen/chi2mub200cen
r82mub200cen=chi8mub200cen/chi2mub200cen
chi2mub200up=np.loadtxt(r'./mub200/cmuup/final/buffer/chi2.dat')
chi4mub200up=np.loadtxt(r'./mub200/cmuup/final/buffer/chi4.dat')
chi6mub200up=np.loadtxt(r'./mub200/cmuup/final/buffer/chi6.dat')
chi8mub200up=np.loadtxt(r'./mub200/cmuup/final/buffer/chi8.dat')
r42mub200up=chi4mub200up/chi2mub200up
r62mub200up=chi6mub200up/chi2mub200up
r82mub200up=chi8mub200up/chi2mub200up
chi2mub200up1=np.loadtxt(r'./mub200/cmuup1/final/buffer/chi2.dat')
chi4mub200up1=np.loadtxt(r'./mub200/cmuup1/final/buffer/chi4.dat')
chi6mub200up1=np.loadtxt(r'./mub200/cmuup1/final/buffer/chi6.dat')
chi8mub200up1=np.loadtxt(r'./mub200/cmuup1/final/buffer/chi8.dat')
r42mub200up1=chi4mub200up1/chi2mub200up1
r62mub200up1=chi6mub200up1/chi2mub200up1
r82mub200up1=chi8mub200up1/chi2mub200up1
chi2mub200up2=np.loadtxt(r'./mub200/cmuup2/final/buffer/chi2.dat')
chi4mub200up2=np.loadtxt(r'./mub200/cmuup2/final/buffer/chi4.dat')
chi6mub200up2=np.loadtxt(r'./mub200/cmuup2/final/buffer/chi6.dat')
chi8mub200up2=np.loadtxt(r'./mub200/cmuup2/final/buffer/chi8.dat')
r42mub200up2=chi4mub200up2/chi2mub200up2
r62mub200up2=chi6mub200up2/chi2mub200up2
r82mub200up2=chi8mub200up2/chi2mub200up2
chi2mub200up3=np.loadtxt(r'./mub200/cmuup3/final/buffer/chi2.dat')
chi4mub200up3=np.loadtxt(r'./mub200/cmuup3/final/buffer/chi4.dat')
chi6mub200up3=np.loadtxt(r'./mub200/cmuup3/final/buffer/chi6.dat')
chi8mub200up3=np.loadtxt(r'./mub200/cmuup3/final/buffer/chi8.dat')
r42mub200up3=chi4mub200up3/chi2mub200up3
r62mub200up3=chi6mub200up3/chi2mub200up3
r82mub200up3=chi8mub200up3/chi2mub200up3
chi2mub200up4=np.loadtxt(r'./mub200/cmuup4/final/buffer/chi2.dat')
chi4mub200up4=np.loadtxt(r'./mub200/cmuup4/final/buffer/chi4.dat')
chi6mub200up4=np.loadtxt(r'./mub200/cmuup4/final/buffer/chi6.dat')
chi8mub200up4=np.loadtxt(r'./mub200/cmuup4/final/buffer/chi8.dat')
r42mub200up4=chi4mub200up4/chi2mub200up4
r62mub200up4=chi6mub200up4/chi2mub200up4
r82mub200up4=chi8mub200up4/chi2mub200up4
chi2mub200down=np.loadtxt(r'./mub200/cmudown/final/buffer/chi2.dat')
chi4mub200down=np.loadtxt(r'./mub200/cmudown/final/buffer/chi4.dat')
chi6mub200down=np.loadtxt(r'./mub200/cmudown/final/buffer/chi6.dat')
chi8mub200down=np.loadtxt(r'./mub200/cmudown/final/buffer/chi8.dat')
r42mub200down=chi4mub200down/chi2mub200down
r62mub200down=chi6mub200down/chi2mub200down
r82mub200down=chi8mub200down/chi2mub200down
chi2mub200down1=np.loadtxt(r'./mub200/cmudown1/final/buffer/chi2.dat')
chi4mub200down1=np.loadtxt(r'./mub200/cmudown1/final/buffer/chi4.dat')
chi6mub200down1=np.loadtxt(r'./mub200/cmudown1/final/buffer/chi6.dat')
chi8mub200down1=np.loadtxt(r'./mub200/cmudown1/final/buffer/chi8.dat')
r42mub200down1=chi4mub200down1/chi2mub200down1
r62mub200down1=chi6mub200down1/chi2mub200down1
r82mub200down1=chi8mub200down1/chi2mub200down1
chi2mub200down2=np.loadtxt(r'./mub200/cmudown2/final/buffer/chi2.dat')
chi4mub200down2=np.loadtxt(r'./mub200/cmudown2/final/buffer/chi4.dat')
chi6mub200down2=np.loadtxt(r'./mub200/cmudown2/final/buffer/chi6.dat')
chi8mub200down2=np.loadtxt(r'./mub200/cmudown2/final/buffer/chi8.dat')
r42mub200down2=chi4mub200down2/chi2mub200down2
r62mub200down2=chi6mub200down2/chi2mub200down2
r82mub200down2=chi8mub200down2/chi2mub200down2
chi2mub200down3=np.loadtxt(r'./mub200/cmudown3/final/buffer/chi2.dat')
chi4mub200down3=np.loadtxt(r'./mub200/cmudown3/final/buffer/chi4.dat')
chi6mub200down3=np.loadtxt(r'./mub200/cmudown3/final/buffer/chi6.dat')
chi8mub200down3=np.loadtxt(r'./mub200/cmudown3/final/buffer/chi8.dat')
r42mub200down3=chi4mub200down3/chi2mub200down3
r62mub200down3=chi6mub200down3/chi2mub200down3
r82mub200down3=chi8mub200down3/chi2mub200down3
chi2mub200down4=np.loadtxt(r'./mub200/cmudown4/final/buffer/chi2.dat')
chi4mub200down4=np.loadtxt(r'./mub200/cmudown4/final/buffer/chi4.dat')
chi6mub200down4=np.loadtxt(r'./mub200/cmudown4/final/buffer/chi6.dat')
chi8mub200down4=np.loadtxt(r'./mub200/cmudown4/final/buffer/chi8.dat')
r42mub200down4=chi4mub200down4/chi2mub200down4
r62mub200down4=chi6mub200down4/chi2mub200down4
r82mub200down4=chi8mub200down4/chi2mub200down4
r42200=np.zeros((300,100))
r62200=np.zeros((300,100))
r82200=np.zeros((300,100))
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
#####################################################################################
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
for t in range(0,20):
    if t<10:
       r42100[:,t]=spline(T/ct[t],r42mub100up,xsame)
    else:
       r42100[:,t]=spline(T/ct[t-10],r42mub100down,xsame)


for num in range(1,20):
    if num==1:
       max100=np.maximum(r42100[:,num-1],r42100[:,num])
       min100=np.minimum(r42100[:,num-1],r42100[:,num])
    else:
       max100=np.maximum(max100,r42100[:,num])
       min100=np.minimum(min100,r42100[:,num])

band_mub100=ax1.fill_between(xsame,max100,min100,alpha=0.25,facecolor='b',edgecolor='')
line_mub100,=ax1.plot(Tcen,r42mub100cen,'b',linewidth=1,alpha=0.5)


#########################################################################################
for t in range(0,20):
    if t<10:
       r42160[:,t]=spline(T/ct[t],r42mub160up,xsame)
    else:
       r42160[:,t]=spline(T/ct[t-10],r42mub160down,xsame)


for num in range(1,20):
    if num==1:
       max160=np.maximum(r42160[:,num-1],r42160[:,num])
       min160=np.minimum(r42160[:,num-1],r42160[:,num])
    else:
       max160=np.maximum(max160,r42160[:,num])
       min160=np.minimum(min160,r42160[:,num])

band_mub160=ax1.fill_between(xsame,max160,min160,alpha=0.25,facecolor='darkgreen',edgecolor='')
line_mub160,=ax1.plot(Tcen,r42mub160cen,'darkgreen',linewidth=1,alpha=0.5)
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
#########################################################################################
for t in range(0,100):
    if t<10:
       r42200[:,t]=spline(T/ct[t],r42mub200up,xsame)
    else:
       if t>=10 and t<20:
          r42200[:,t]=spline(T/ct[t-10],r42mub200up1,xsame)
       else:
          if t>=20 and t<30:
             r42200[:,t]=spline(T/ct[t-20],r42mub200up2,xsame)
          else: 
             if t>=30 and t<40:
                r42200[:,t]=spline(T/ct[t-30],r42mub200up3,xsame)
             else: 
                if t>=40 and t<50:
                   r42200[:,t]=spline(T/ct[t-40],r42mub200up4,xsame)
                else:
                   if t>=50 and t<60:
                      r42200[:,t]=spline(T/ct[t-50],r42mub200down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r42200[:,t]=spline(T/ct[t-60],r42mub200down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r42200[:,t]=spline(T/ct[t-70],r42mub200down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r42200[:,t]=spline(T/ct[t-80],r42mub200down3,xsame)
                            else:
                                r42200[:,t]=spline(T/ct[t-90],r42mub200down4,xsame)


for num in range(1,100):
    if num==1:
       max200=np.maximum(r42200[:,num-1],r42200[:,num])
       min200=np.minimum(r42200[:,num-1],r42200[:,num])
    else:
       max200=np.maximum(max200,r42200[:,num])
       min200=np.minimum(min200,r42200[:,num])

band_mub200=ax1.fill_between(xsame,max200,min200,alpha=0.25,facecolor='k',edgecolor='')
line_mub200,=ax1.plot(Tcen,r42mub200cen,'k',linewidth=1,alpha=0.5)

plt.axes([0.085, 0.22, 0.095, 0.3]) #不用figure的形式则无须用set
band_mub0=plt.fill_betweenx(r42mub0,Tup,Tdown,alpha=0.25,facecolor='r',edgecolor='')
line_mub0,=plt.plot(Tcen,r42mub0,'r',linewidth=1,alpha=0.5)
band_mub100=plt.fill_between(xsame,max100,min100,alpha=0.25,facecolor='b',edgecolor='')
line_mub100,=plt.plot(Tcen,r42mub100cen,'b',linewidth=1,alpha=0.5)
band_mub160=plt.fill_between(xsame,max160,min160,alpha=0.25,facecolor='darkgreen',edgecolor='')
line_mub160,=plt.plot(Tcen,r42mub160cen,'darkgreen',linewidth=1,alpha=0.5)
band_mub200=plt.fill_between(xsame,max200,min200,alpha=0.25,facecolor='k',edgecolor='')
line_mub200,=plt.plot(Tcen,r42mub200cen,'k',linewidth=1,alpha=0.5)
band_mub300=plt.fill_between(xsame,max300,min300,alpha=0.25,facecolor='c',edgecolor='')
line_mub300,=plt.plot(Tcen,r42mub300cen,'c',linewidth=1,alpha=0.5)
band_mub400=plt.fill_between(xsame,max400,min400,alpha=0.25,facecolor='m',edgecolor='')
line_mub400,=plt.plot(Tcen,r42mub400cen,'m',linewidth=1,alpha=0.5)
x=range(80,230,40)
plt.xticks(x,fontsize=8)
plt.yticks(fontsize=8)
plt.axis([80,230,-1.5,2.])

ax1.axis([80,230,0,1.2])
#ax1.set_xscale('log')

ax1.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax1.set_ylabel(r'$R^B_{42}$', fontsize=14, color='black')

ax1.legend([(band_mub0,line_mub0),(band_mub100,line_mub100),(band_mub160,line_mub160),(band_mub200,line_mub200),(band_mub300,line_mub300),(band_mub400,line_mub400)],[r'$\mu_B=0$',r'$\mu_B=100$ MeV',r'$\mu_B=160$ MeV',r'$\mu_B=200$ MeV',r'$\mu_B=300$ MeV',r'$\mu_B=400$ MeV'],loc=0,fontsize='x-small',frameon=True,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1,numpoints=1)

for label in ax1.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax1.yaxis.get_ticklabels():
    label.set_fontsize(10)
#######################################################################################################################
ax2=fig.add_subplot(132)

band_mub0=ax2.fill_betweenx(r62mub0,Tup,Tdown,alpha=0.25,facecolor='r',edgecolor='')
line_mub0,=ax2.plot(Tcen,r62mub0,'r',linewidth=1,alpha=0.5)

###############################################################################################################
for t in range(0,20):
    if t<10:
       r62100[:,t]=spline(T/ct[t],r62mub100up,xsame)
    else:
       r62100[:,t]=spline(T/ct[t-10],r62mub100down,xsame)


for num in range(1,20):
    if num==1:
       max100=np.maximum(r62100[:,num-1],r62100[:,num])
       min100=np.minimum(r62100[:,num-1],r62100[:,num])
    else:
       max100=np.maximum(max100,r62100[:,num])
       min100=np.minimum(min100,r62100[:,num])

band_mub100=ax2.fill_between(xsame,max100,min100,alpha=0.25,facecolor='b',edgecolor='')
line_mub100,=ax2.plot(Tcen,r62mub100cen,'b',linewidth=1,alpha=0.5)

#####################################################################################################################
for t in range(0,20):
    if t<10:
       r62160[:,t]=spline(T/ct[t],r62mub160up,xsame)
    else:
       r62160[:,t]=spline(T/ct[t-10],r62mub160down,xsame)


for num in range(1,20):
    if num==1:
       max160=np.maximum(r62160[:,num-1],r62160[:,num])
       min160=np.minimum(r62160[:,num-1],r62160[:,num])
    else:
       max160=np.maximum(max160,r62160[:,num])
       min160=np.minimum(min160,r62160[:,num])

band_mub160=ax2.fill_between(xsame,max160,min160,alpha=0.25,facecolor='darkgreen',edgecolor='')
line_mub160,=ax2.plot(Tcen,r62mub160cen,'darkgreen',linewidth=1,alpha=0.5)
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
#####################################################################################################################
for t in range(0,100):
    if t<10:
       r62200[:,t]=spline(T/ct[t],r62mub200up,xsame)
    else:
       if t>=10 and t<20:
          r62200[:,t]=spline(T/ct[t-10],r62mub200up1,xsame)
       else:
          if t>=20 and t<30:
             r62200[:,t]=spline(T/ct[t-20],r62mub200up2,xsame)
          else: 
             if t>=30 and t<40:
                r62200[:,t]=spline(T/ct[t-30],r62mub200up3,xsame)
             else: 
                if t>=40 and t<50:
                   r62200[:,t]=spline(T/ct[t-40],r62mub200up4,xsame)
                else:
                   if t>=50 and t<60:
                      r62200[:,t]=spline(T/ct[t-50],r62mub200down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r62200[:,t]=spline(T/ct[t-60],r62mub200down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r62200[:,t]=spline(T/ct[t-70],r62mub200down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r62200[:,t]=spline(T/ct[t-80],r62mub200down3,xsame)
                            else:
                                r62200[:,t]=spline(T/ct[t-90],r62mub200down4,xsame)


for num in range(1,100):
    if num==1:
       max200=np.maximum(r62200[:,num-1],r62200[:,num])
       min200=np.minimum(r62200[:,num-1],r62200[:,num])
    else:
       max200=np.maximum(max200,r62200[:,num])
       min200=np.minimum(min200,r62200[:,num])
band_mub200=ax2.fill_between(xsame,max200,min200,alpha=0.25,facecolor='k',edgecolor='')
line_mub200,=ax2.plot(Tcen,r62mub200cen,'k',linewidth=1,alpha=0.5)

plt.axes([0.405, 0.22, 0.093, 0.3]) #不用figure的形式则无须用set
band_mub0=plt.fill_betweenx(r62mub0,Tup,Tdown,alpha=0.25,facecolor='r',edgecolor='')
line_mub0,=plt.plot(Tcen,r62mub0,'r',linewidth=1,alpha=0.5)
band_mub100=plt.fill_between(xsame,max100,min100,alpha=0.25,facecolor='b',edgecolor='')
line_mub100,=plt.plot(Tcen,r62mub100cen,'b',linewidth=1,alpha=0.5)
band_mub160=plt.fill_between(xsame,max160,min160,alpha=0.25,facecolor='darkgreen',edgecolor='')
line_mub160,=plt.plot(Tcen,r62mub160cen,'darkgreen',linewidth=1,alpha=0.5)
band_mub200=plt.fill_between(xsame,max200,min200,alpha=0.25,facecolor='k',edgecolor='')
line_mub200,=plt.plot(Tcen,r62mub200cen,'k',linewidth=1,alpha=0.5)
band_mub300=plt.fill_between(xsame,max300,min300,alpha=0.25,facecolor='c',edgecolor='')
line_mub300,=plt.plot(Tcen,r62mub300cen,'c',linewidth=1,alpha=0.5)
band_mub400=plt.fill_between(xsame,max400,min400,alpha=0.25,facecolor='m',edgecolor='')
line_mub400,=plt.plot(Tcen,r62mub400cen,'m',linewidth=1,alpha=0.5)
x=range(80,230,40)
y=range(-40,40,20)
plt.xticks(x,fontsize=8)
plt.yticks(y,fontsize=8)
plt.axis([80,200,-50,40])

ax2.axis([80,220,-2.3,1.7])
#ax2.set_xscale('log')
ax2.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax2.set_ylabel(r'$R^B_{62}$', fontsize=14, color='black')

ax2.legend(loc=0,fontsize=7,frameon=False,shadow=True,handlelength=3.,borderpad=0.5,borderaxespad=1)

for label in ax2.xaxis.get_ticklabels():
    label.set_fontsize(10)
for label in ax2.yaxis.get_ticklabels():
    label.set_fontsize(10)

############################################################################################################################
ax3=fig.add_subplot(133)
band_mub0=ax3.fill_betweenx(r82mub0,Tup,Tdown,alpha=0.25,facecolor='r',edgecolor='')
line_mub0,=ax3.plot(Tcen,r82mub0,'r',linewidth=1,alpha=0.5)
####################################################################################################################
for t in range(0,20):
    if t<10:
       r82100[:,t]=spline(T/ct[t],r82mub100up,xsame)
    else:
       r82100[:,t]=spline(T/ct[t-10],r82mub100down,xsame)


for num in range(1,20):
    if num==1:
       max100=np.maximum(r82100[:,num-1],r82100[:,num])
       min100=np.minimum(r82100[:,num-1],r82100[:,num])
    else:
       max100=np.maximum(max100,r82100[:,num])
       min100=np.minimum(min100,r82100[:,num])

band_mub100=ax3.fill_between(xsame,max100,min100,alpha=0.25,facecolor='b',edgecolor='')
line_mub100,=ax3.plot(Tcen,r82mub100cen,'b',linewidth=1,alpha=0.5)

#######################################################################################################################33
for t in range(0,20):
    if t<10:
       r82160[:,t]=spline(T/ct[t],r82mub160up,xsame)
    else:
       r82160[:,t]=spline(T/ct[t-10],r82mub160down,xsame)


for num in range(1,20):
    if num==1:
       max160=np.maximum(r82160[:,num-1],r82160[:,num])
       min160=np.minimum(r82160[:,num-1],r82160[:,num])
    else:
       max160=np.maximum(max160,r82160[:,num])
       min160=np.minimum(min160,r82160[:,num])

band_mub160=ax3.fill_between(xsame,max160,min160,alpha=0.25,facecolor='darkgreen',edgecolor='')
line_mub160,=ax3.plot(Tcen,r82mub160cen,'darkgreen',linewidth=1,alpha=0.5)
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
######################################################################################################################
for t in range(0,100):
    if t<10:
       r82200[:,t]=spline(T/ct[t],r82mub200up,xsame)
    else:
       if t>=10 and t<20:
          r82200[:,t]=spline(T/ct[t-10],r82mub200up1,xsame)
       else:
          if t>=20 and t<30:
             r82200[:,t]=spline(T/ct[t-20],r82mub200up2,xsame)
          else: 
             if t>=30 and t<40:
                r82200[:,t]=spline(T/ct[t-30],r82mub200up3,xsame)
             else: 
                if t>=40 and t<50:
                   r82200[:,t]=spline(T/ct[t-40],r82mub200up4,xsame)
                else:
                   if t>=50 and t<60:
                      r82200[:,t]=spline(T/ct[t-50],r82mub200down,xsame)
                   else: 
                      if t>=60 and t<70:
                         r82200[:,t]=spline(T/ct[t-60],r82mub200down1,xsame)
                      else:
                         if t>=70 and t<80:
                            r82200[:,t]=spline(T/ct[t-70],r82mub200down2,xsame)
                         else: 
                            if t>=80 and t<90:
                               r82200[:,t]=spline(T/ct[t-80],r82mub200down3,xsame)
                            else:
                                r82200[:,t]=spline(T/ct[t-90],r82mub200down4,xsame)


for num in range(1,100):
    if num==1:
       max200=np.maximum(r82200[:,num-1],r82200[:,num])
       min200=np.minimum(r82200[:,num-1],r82200[:,num])
    else:
       max200=np.maximum(max200,r82200[:,num])
       min200=np.minimum(min200,r82200[:,num])

band_mub200=ax3.fill_between(xsame,max200,min200,alpha=0.25,facecolor='k',edgecolor='')
line_mub200,=ax3.plot(Tcen,r82mub200cen,'k',linewidth=1,alpha=0.5)

ax3_inset=plt.axes([0.732, 0.22, 0.095, 0.3]) #不用figure的形式则无须用set
band_mub0=plt.fill_betweenx(r82mub0,Tup,Tdown,alpha=0.25,facecolor='r',edgecolor='')
line_mub0,=plt.plot(Tcen,r82mub0,'r',linewidth=1,alpha=0.5)
band_mub100=plt.fill_between(xsame,max100,min100,alpha=0.25,facecolor='b',edgecolor='')
line_mub100,=plt.plot(Tcen,r82mub100cen,'b',linewidth=1,alpha=0.5)
band_mub160=plt.fill_between(xsame,max160,min160,alpha=0.25,facecolor='darkgreen',edgecolor='')
line_mub160,=plt.plot(Tcen,r82mub160cen,'darkgreen',linewidth=1,alpha=0.5)
band_mub200=plt.fill_between(xsame,max200,min200,alpha=0.25,facecolor='k',edgecolor='')
line_mub200,=plt.plot(Tcen,r82mub200cen,'k',linewidth=1,alpha=0.5)
band_mub300=plt.fill_between(xsame,max300,min300,alpha=0.25,facecolor='c',edgecolor='')
line_mub300,=plt.plot(Tcen,r82mub300cen,'c',linewidth=1,alpha=0.5)
band_mub400=plt.fill_between(xsame,max400,min400,alpha=0.25,facecolor='m',edgecolor='')
line_mub400,=plt.plot(Tcen,r82mub400cen,'m',linewidth=1,alpha=0.5)
x=range(80,230,40)
y=range(-1500,2500,500)
plt.xticks(x,fontsize=8)
plt.yticks(y,fontsize=8)
plt.axis([90,200,-1400,2300])

def formatnum(x, pos):
    return r'$%.1f$' % (x/10.**3)
formatter = FuncFormatter(formatnum)
ax3_inset.yaxis.set_major_formatter(formatter)



ax3.axis([80,200,-30,23])
#ax3.set_xscale('log')
ax3.text(87, -3, r'$(\times 10^3)$',fontsize=8, color='k')


ax3.set_xlabel('$T\,[\mathrm{MeV}]$', fontsize=14, color='black')
ax3.set_ylabel(r'$R^B_{82}$', fontsize=14, color='black')

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
