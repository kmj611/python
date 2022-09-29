import Travel.ThailandPackage
from Travel.VietnamPackage import VietnamPackage

trip_to = Travel.ThailandPackage.ThailandPackage()
trip_to.detail()

import Travel.VietnamPackage
trip_to2 = Travel.VietnamPackage.VietnamPackage()
trip_to2.detail()

from Travel import *
trip_to = VietnamPackage.VietnamPackage()
trip_to.detail()