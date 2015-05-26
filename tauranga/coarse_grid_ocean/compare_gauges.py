

from pylab import *
from clawpack.visclaw.data import ClawPlotData
from clawpack.clawutil.data import ClawData
from clawpack.geoclaw import topotools

comparison_data_dir = '/Users/rjl/git/tsunami_benchmarks/nthmp_currents_2015/all_data/3_Tauranga_2011_Field/comparison_data/'

geodata = ClawData()
geodata.read('geoclaw.data', force=True)
sea_level = geodata.sea_level
print "GeoClaw simulation at sea_level = %g relative to MHW" % sea_level


plotdata = ClawPlotData()

#plotdata.outdir = '_output_1_3sec'
plotdata.outdir = '_output'
toffset = 0.2

port_data = loadtxt(comparison_data_dir + 'port_data.txt')
tAB = port_data[:,0] - toffset
zAB = port_data[:,1] # tsunami only
tTug = port_data[:,3] - toffset
zTug = port_data[:,4] # tsunami only

figure(1, figsize=(12,5))
clf()


g = plotdata.getgauge(1)
t = g.t / 3600.

plot(tAB,zAB,'k-o',label='Observations')
plot(t, g.q[3,:], 'r',lw=2,label='GeoClaw')
ylabel('meters')
legend(loc='upper right')
xlim(12.5, 18)
ylim(-1,1)
#title('Surface elevation at A Beacon')
show()

# ------------------------

figure(2, figsize=(12,5))
clf()

g = plotdata.getgauge(2)
t = g.t / 3600.

plot(tTug,zTug,'k-o',label='Observations')
plot(t, g.q[3,:], 'r',lw=2,label='GeoClaw')
ylabel('meters')
legend(loc='upper right')
xlim(12.5, 18)
ylim(-0.8,0.8)
title('Surface elevation at Tug')
show()

# ------------------------

tide_gauge = loadtxt(comparison_data_dir + 'tide_gauge.txt')
tTT = port_data[:,0] - toffset
zTT = port_data[:,1] # tsunami only
tMT = port_data[:,3] - toffset
zMT = port_data[:,4] # tsunami only

figure(4, figsize=(12,5))
clf()

g = plotdata.getgauge(4)
t = g.t / 3600.

plot(tMT,zMT,'k-o',label='Observations')
plot(t, g.q[3,:], 'r',lw=2,label='GeoClaw')
ylabel('meters')
legend(loc='upper right')
xlim(12.5, 18)
ylim(-0.8,0.8)
title('Surface elevation at Moturiki')
show()

#---------

currents = loadtxt(comparison_data_dir + 'currents.txt')
tADCP = currents[:,0] - toffset
utsuADCP = currents[:,1] # tsunami only
vtsuADCP = currents[:,2] # tsunami only
speedtsuADCP = currents[:,3] # tsunami only
dirtsuADCP = currents[:,4] # tsunami only
tspan = find(logical_and(tADCP>12.5, tADCP < 18))

figure(100, figsize=(12,12))
clf()
Cgrid = topotools.Topography()
Cgrid.read('../topo/TAU_C_10m_c.tt5', -3)

figure(200, figsize=(8,8))
clf()
#contour(Cgrid.X, Cgrid.Y, Cgrid.Z, linspace(-50,0,6), linestyles='-', \
#            colors='k')
contourf(Cgrid.X, Cgrid.Y, Cgrid.Z, [0,500], colors=['g'])
ticklabel_format(format='plain',useOffset=False)
axis([-183.85, -183.82, -37.65, -37.62])
xticks(rotation=20)
gca().set_aspect(1./cos(pi*37.6/180.))

# From ADCP.kmz file:
# ADCP - Official: 176.16535,-37.63435
# ADCP - Actual:
x_ADCP = 176.1656739914625 - 360
y_ADCP = -37.63462262944208
u = x_ADCP + 0.001*utsuADCP[tspan]
v = y_ADCP + 0.001*vtsuADCP[tspan]
plot([x_ADCP],[y_ADCP],'bo')
plot(u,v,'b')

gaugenos = [g[0] for g in plotdata.gaugesoln_dict.keys() if g[0] >= 10]
print "Found harbour entrance gauges: ",gaugenos

#gaugenos = [25]

for gaugeno in gaugenos:
    g = plotdata.getgauge(gaugeno)

    t = g.t / 3600.
    
    #figure(gaugeno, figsize=(12,12))
    figure(100)
    clf()
    subplot(311)
    plot(tADCP,utsuADCP,'k-o',label='E-W velocity')
    plot(t, g.q[1,:]/g.q[0,:], 'r',lw=2,label='GeoClaw')
    ylabel('meters/sec')
    legend(loc='upper right')
    xlim(12.5, 18)
    ylim(-0.8,0.8)
    title('Velocities at ADCP and Gauge %s' % gaugeno)
    
    subplot(312)
    plot(tADCP,vtsuADCP,'k-o',label='N-S velocity')
    plot(t, g.q[2,:]/g.q[0,:], 'r',lw=2,label='GeoClaw')
    ylabel('meters/sec')
    legend(loc='upper right')
    xlim(12.5, 18)
    ylim(-0.8,0.8)
    
    subplot(313)
    plot(tADCP,speedtsuADCP,'k-o',label='Speed')
    s = sqrt(g.q[1,:]**2 + g.q[2,:]**2) / g.q[0,:]
    plot(t, s, 'r',lw=2,label='GeoClaw')
    ylabel('meters/sec')
    legend(loc='upper right')
    xlim(12.5, 18)
    ylim(-0.2,1.5)
    show()
    
    figure(200)
    xg,yg = g.location
    plot([xg],[yg],'ro')
    u = xg + 0.001*g.q[1,:]/g.q[0,:] 
    v = yg + 0.001*g.q[2,:]/g.q[0,:]
    plot(u,v,'r')

    #u = xg + 0.001*utsuADCP[tspan]
    #v = yg + 0.001*vtsuADCP[tspan]
    #plot(u,v,'k')

    #ans = raw_input('hit return for next gauge... ')
    #if ans=='q': break

figure(20)
clf()
plot(utsuADCP[tspan],vtsuADCP[tspan],'k')
u = g.q[1,:]/g.q[0,:]; v = g.q[2,:]/g.q[0,:]
plot(u,v,'r',lw=2)
xlabel('E-W u-velocity')
ylabel('N-S v-velocity')
title('Velocity at ADCP in u-v plane')
legend(['Observations','GeoClaw'])
show()


if 0:
    figure(1)
    savefig('ABeacon.png')
    figure(2)
    savefig('Tug.png')
    figure(12)
    savefig('ADCP12.png')
    figure(20)
    savefig('ADCPuvPlane.png')


# -- combined figure -----

figure(66,figsize=(12,12))
g = plotdata.getgauge(1)
t = g.t / 3600.
a = subplot(511)
plot(tAB,zAB,'k-o',label='Surface at A-Beacon',markersize=3)
plot(t, g.q[3,:], 'r',lw=2)
ylabel('meters')
legend(loc='upper left')
xlim(12.5, 18)
ylim(-0.6,0.6)
#title('Surface elevation at A Beacon')

gaugeno = 2
g = plotdata.getgauge(gaugeno)
t = g.t / 3600.
a = subplot(512)
plot(tTug,zTug,'k-o',label='Suface at TUG',markersize=3)
plot(t, g.q[3,:], 'r',lw=2)
ylabel('meters')
legend(loc='upper left')
xlim(12.5, 18)
ylim(-0.6,0.6)
#title('Surface elevation at Tug')

gaugeno = 14
g = plotdata.getgauge(gaugeno)
t = g.t / 3600.

subplot(513)
plot(tADCP,utsuADCP,'k-o',label='E-W velocity at ADCP',markersize=3)
plot(t, g.q[1,:]/g.q[0,:], 'r',lw=2)
ylabel('meters/sec')
legend(loc='upper left')
xlim(12.5, 18)
ylim(-1,1)
#title('Velocities at ADCP')

subplot(514)
plot(tADCP,vtsuADCP,'k-o',label='N-S velocity at ADCP',markersize=3)
plot(t, g.q[2,:]/g.q[0,:], 'r',lw=2)
ylabel('meters/sec')
legend(loc='upper left')
xlim(12.5, 18)
ylim(-1,1)

subplot(515)
plot(tADCP,speedtsuADCP,'k-o',label='Speed at ADCP',markersize=3)
s = sqrt(g.q[1,:]**2 + g.q[2,:]**2) / g.q[0,:]
plot(t, s, 'r',lw=2)
ylabel('meters/sec')
legend(loc='upper left')
xlim(12.5, 18)
ylim(-0.5,1.5)
xlabel('time (hours)')

fname = 'combined_gauges.png'
savefig(fname)
print "Created ",fname
