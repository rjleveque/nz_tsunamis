
import matplotlib.pyplot as plt
from clawpack.geoclaw import dtopotools

slip = {}
slip['kiszb24'] = 4.66
slip['kiszb25'] = 12.23
slip['kiszb26'] = 21.27
slip['kisza26'] = 26.31
slip['kiszb27'] = 4.98
slip['kisza27'] = 22.75

f = dtopotools.SiftFault(slip)


# create x-y arrays with 1' resolution and 1 degree buffer around bounding box
x,y = f.create_dtopo_xy(dx=1/60., buffer_size=1)  

dtopo = f.create_dtopography(x,y,times=[0,1.],verbose=True)

if 0:
    fname = 'tohoku_sift.tt3'
    dtopo.write(fname, dtopo_type=3)
    print "Created ",fname


# shift longitude to East:
dtopo.x = dtopo.x - 360.
dtopo.X = dtopo.X - 360.
if 1:
    fname = 'tohoku_sift_E.tt3'
    dtopo.write(fname, dtopo_type=3)
    print "Created ",fname


plt.figure(figsize=(10,8))
ax1 = plt.subplot(121)
f.plot_subfaults(axes=ax1,slip_color=True)
ax1.set_xlim(x.min(),x.max())
ax1.set_ylim(y.min(),y.max())

ax2 = plt.subplot(122)
dtopo.plot_dZ_colors(t=1,axes=ax2)

fname = 'tohoku_sift.png'
plt.savefig(fname)
print "Created ",fname

