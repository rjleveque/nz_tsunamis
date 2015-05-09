
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

from clawpack.geoclaw import topotools
import numpy as np


#--------------------------
def setplot(plotdata):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of pyclaw.plotters.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 


    from clawpack.visclaw import colormaps, geoplot
    from numpy import linspace

    plotdata.clearfigures()  # clear any old figures,axes,items data
    plotdata.format = 'binary'


    # To plot gauge locations on pcolor or contour plot, use this as
    # an afteraxis function:

    def addgauges(current_data):
        from clawpack.visclaw import gaugetools
        gaugetools.plot_gauge_locations(current_data.plotdata, \
             gaugenos='all', format_string='ko', add_labels=False)
    
    def fixup(current_data):
        import pylab
        #addgauges(current_data)
        t = current_data.t
        t = t / 3600.  # hours
        pylab.title('Surface at %4.2f hours' % t, fontsize=20)
        pylab.ticklabel_format(format='plain',useOffset=False)
        pylab.xticks(rotation=20)
        mean_lat = 19.7
        pylab.gca().set_aspect(1.0 / pylab.cos(pylab.pi / 180.0 * mean_lat))
        #pylab.xticks(fontsize=15)
        #pylab.yticks(fontsize=15)

    #-----------------------------------------
    # Figure for pcolor plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='pcolor', figno=0)
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.title = 'Surface'
    #plotaxes.scaled = True

    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    #plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface_or_depth
    plotitem.pcolor_cmap = geoplot.tsunami_colormap
    plotitem.pcolor_cmin = -0.05
    plotitem.pcolor_cmax = 0.05
    plotitem.add_colorbar = True
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 1

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.land
    plotitem.pcolor_cmap = geoplot.land_colors
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [1,1,0]
    plotitem.patchedges_show = 1
    #plotaxes.xlimits = [202., 206.]
    #plotaxes.ylimits = [19., 21.]

    # add contour lines of bathy if desired:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.show = False
    plotitem.plot_var = geoplot.topo
    plotitem.contour_levels = linspace(-2000,0,5)
    plotitem.amr_contour_colors = ['y']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':2}
    plotitem.amr_contour_show = [1,0,0]  
    plotitem.celledges_show = 0
    plotitem.patchedges_show = 0


    #-----------------------------------------
    # Figure for imshow plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Pacific', figno=1)
    #plotfigure.show = False
    #plotfigure.kwargs = {'figsize': (15,6)}

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('imshow')
    #plotaxes.axescmd = 'subplot(131)'
    plotaxes.title = 'Surface'
    #plotaxes.scaled = True

    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    # plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface_or_depth
    plotitem.imshow_cmap = geoplot.tsunami_colormap
    plotitem.imshow_cmin = -0.05
    plotitem.imshow_cmax = 0.05
    plotitem.add_colorbar = True
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.amr_patchedges_show = [0,0,0]

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0
    plotaxes.xlimits = [-240,-60]
    plotaxes.ylimits = [-65,65]

    # add contour lines of bathy if desired:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.show = False
    plotitem.plot_var = geoplot.topo
    plotitem.contour_levels = linspace(-2000,0,5)
    plotitem.amr_contour_colors = ['y']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':2}
    plotitem.amr_contour_show = [1,0,0]  
    plotitem.celledges_show = 0
    plotitem.patchedges_show = 0


    #-----------------------------------------
    # Figure for zoom plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='NZ', figno=2)
    #plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('NZ')
    #plotaxes.axescmd = 'subplot(132)'
    plotaxes.title = 'Surface'
    #plotaxes.scaled = True

    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    # plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface_or_depth
    plotitem.imshow_cmap = geoplot.tsunami_colormap
    plotitem.imshow_cmin = -0.2
    plotitem.imshow_cmax = 0.2
    plotitem.add_colorbar = True
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0
    plotaxes.xlimits = [-190,-180]
    plotaxes.ylimits = [-42,-33]


    #-----------------------------------------
    # Figure for zoom plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Tauranga', figno=3)
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('Tauranga')
    #plotaxes.axescmd = 'subplot(133)'
    plotaxes.title = 'Surface'
    #plotaxes.scaled = True

    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    # plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface_or_depth
    plotitem.imshow_cmap = geoplot.tsunami_colormap
    plotitem.imshow_cmin = -0.2
    plotitem.imshow_cmax = 0.2
    plotitem.add_colorbar = True
    plotitem.colorbar_shrink = 0.5
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0
    plotaxes.xlimits = [-184.2,-183.6]
    plotaxes.ylimits = [-37.8,-37.2]


    #-----------------------------------------
    # Figure for speed
    #-----------------------------------------

    plotfigure = plotdata.new_plotfigure(name='speed', figno=4)
    plotfigure.show = False

    def speed(current_data):
        from numpy import ma, where, sqrt
        drytol = 1e-3
        q = current_data.q
        h = q[0,:,:]
        hu = q[1,:,:]
        hv = q[2,:,:]
        speed = where(h > drytol, sqrt(hu**2 + hv**2)/h**2, 0.)
        speed = ma.masked_where(h<=drytol, speed)
        return speed

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Speed'
    #plotaxes.scaled = True

    def fixup(current_data):
        import pylab
        #addgauges(current_data)
        t = current_data.t
        t = t / 3600.  # hours
        pylab.title('Speed at %4.2f hours' % t, fontsize=20)
        pylab.ticklabel_format(format='plain',useOffset=False)
        mean_lat = 19.7
        pylab.gca().set_aspect(1.0 / pylab.cos(pylab.pi / 180.0 * mean_lat))

    plotaxes.afteraxes = fixup

    # Water (contourf not working)
    plotitem = plotaxes.new_plotitem(plot_type='2d_contourf')
    plotitem.show = False
    plotitem.plot_var = speed
    clines = [0, 0.01, 0.02, 0.04, 0.06, 0.08, 0.1, 0.2]
    plotitem.contour_levels = clines
    from clawpack.geoclaw.geoplot import discrete_cmap_1
    plotitem.fill_colors = discrete_cmap_1(clines)
    plotitem.kwargs = {'extend':'max'}
    plotitem.add_colorbar = True
    plotitem.amr_celledges_show = 0
    plotitem.patchedges_show = 0

    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = speed
    plotitem.imshow_cmap = geoplot.tsunami_colormap
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 0.3
    plotitem.add_colorbar = True
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    #plotitem.show = False
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_celledges_show = [0,0,0]
    plotitem.patchedges_show = 0
    plotaxes.xlimits = [204.9, 204.96]
    plotaxes.ylimits = [19.72, 19.76]


    # add contour lines of bathy if desired:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.show = False
    plotitem.plot_var = geoplot.topo
    plotitem.contour_levels = linspace(-2000,0,5)
    plotitem.amr_contour_colors = ['y']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':2}
    plotitem.amr_contour_show = [1,0,0]  
    plotitem.celledges_show = 0
    plotitem.patchedges_show = 0


    #-----------------------------------------
    # Figures for gauges
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Surface', figno=300, \
                    type='each_gauge')
    plotfigure.clf_each_gauge = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    #plotaxes.axescmd = 'subplot(2,1,1)'
    plotaxes.title = 'Surface'

    # Plot surface as blue curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 3
    plotitem.plotstyle = 'b-'
    plotitem.kwargs = {'linewidth':2}

    # Plot topo as green curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.show = False

    def gaugetopo(current_data):
        q = current_data.q
        h = q[0,:]
        eta = q[3,:]
        topo = eta - h
        return topo
        
    plotitem.plot_var = gaugetopo
    plotitem.plotstyle = 'g-'

    def add_zeroline(current_data):
        from pylab import plot, legend, xticks, floor, xlim,ylim
        t = current_data.t
        #legend(('surface','topography'),loc='lower left')
        plot(t, 0*t, 'k')
        n = int(floor(t.max()/1800.)) + 2
        xticks([1800*i for i in range(n)],[str(0.5*i) for i in range(n)])
        xlim(25000,t.max())
        #ylim(-0.5,0.5)
        print "+++ gaugeno = ",current_data.gaugeno

    plotaxes.ylimits = [-0.5, 0.5]
    plotaxes.xlimits = [12.25*3600,20*3600]
    plotaxes.afteraxes = add_zeroline


    plotfigure = plotdata.new_plotfigure(name='Velocities', figno=301, \
                    type='each_gauge')
    plotfigure.clf_each_gauge = True

    plotaxes = plotfigure.new_plotaxes()
    #plotaxes.axescmd = 'subplot(2,1,2)'
    plotaxes.title = 'Velocities'
    #plotaxes.afteraxes = add_zeroline
    #plotaxes.xlimits = [12,15]

    # Plot velocity as red curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    #plotitem.show = False
    def speed(current_data):
        from numpy import where, sqrt
        h = current_data.q[0,:]
        h = where(h>0.01, h, 1.e6)
        u = current_data.q[1,:] / h
        v = current_data.q[2,:] / h
        s = sqrt(u**2 + v**2)
        return s
    plotitem.plot_var = speed
    plotitem.plotstyle = 'k-'

    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    def uvel(current_data):
        from numpy import where, sqrt
        h = current_data.q[0,:]
        h = where(h>0.01, h, 1.e6)
        u = current_data.q[1,:] / h
        return u
    plotitem.plot_var = uvel
    plotitem.plotstyle = 'r-'
    plotitem.kwargs = {'linewidth':2}

    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    def vvel(current_data):
        from numpy import where, sqrt
        h = current_data.q[0,:]
        h = where(h>0.01, h, 1.e6)
        v = current_data.q[2,:] / h
        return v
    plotitem.plot_var = vvel
    plotitem.plotstyle = 'g-'
    plotitem.kwargs = {'linewidth':2}

    def add_legend(current_data):
        from pylab import legend
        #legend(['u','v'],'upper left')
        legend(['Speed','u','v'],'upper left')
        add_zeroline(current_data)
    plotaxes.ylimits = [-1.5,1.5]
    plotaxes.xlimits = [12.25*3600,20*3600]
    plotaxes.afteraxes = add_legend



    #-----------------------------------------
    
    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_gaugenos = 'all'          # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

