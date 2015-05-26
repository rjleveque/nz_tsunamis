
"""
Currently requires rjleveque/tauranga branch of geoclaw.
"""

from clawpack.geoclaw import ngdc_tools
from clawpack.geoclaw import topotools
from clawpack.geoclaw import util

import os
from matplotlib.pyplot import savefig

xlimits = (-240,-180)
ylimits = (-77,65)
dx = 4./60.  # 4-minute
file_name = 'etopo4_-240_-180_-77_65.tt3'
ngdc_tools.etopo1_download(xlimits,ylimits,dx,file_name=file_name)

topo = topotools.Topography()
topo.read(file_name,3)
topo.plot()
fname_png = '%s.png' % os.path.splitext(file_name)[0]
savefig(fname_png)
print "Created ",fname_png


xlimits = (-180,-60)
file_name = 'etopo4_-180_-60_-77_65.tt3'
ngdc_tools.etopo1_download(xlimits,ylimits,dx,file_name=file_name)

topo = topotools.Topography()
topo.read(file_name,3)
topo.plot()
fname_png = '%s.png' % os.path.splitext(file_name)[0]
savefig(fname_png)
print "Created ",fname_png


if 0:
    # The files below are not for public distribution 
    private_file_url = '??'

    file_name = 'TAU_A_750m_c.ttm3'
    url = private_file_url + file_name
    util.get_remote_file(url, file_name=file_name, output_dir='.', verbose=True)

    file_name = 'TAU_Whole_Harbour_10_m_srf6.ttm3'
    url = private_file_url + file_name
    util.get_remote_file(url, file_name=file_name, output_dir='.', verbose=True)

