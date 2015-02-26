#!/usr/bin/python3

"""
Contains the PlotSettings-class that controls the appearance of the plot.

The PlotSettings-class initializes the default values for the plot. The class
can return those values to the main window and the plot-settings dialog. The
plot-settings dialog will call the instance of this class to change the
different settings. This class also stores the figure and can return different
subplot-layouts. This class also stores the normal and inverse transformations
of the stereonet, and will return the correct one for either the Schmidt- or
Wulff-Net.
"""

from gi.repository import Gtk, Gdk
from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec
import mplstereonet


class PlotSettings(object):

    """
    The PlotSettings-class initializes the default values for the plot.

    The class can return those values to the main window and the plot-settings
    dialog. The plot-settings dialog will call the instance of this class to
    change the different settings. This class also stores the figure and can
    return different subplot-layouts. This class also stores the normal and
    inverse transformations of the stereonet, and will return the correct
    one for either the Schmidt- or Wulff-Net.
    """

    def __init__(self):
        """
        Initalizes the default values, colors and the matplotlib-figure.

        Initializes and stores the default settings. Initializes the
        matplotlib-figure, a folder-icon for the group-layers of the layer-view.
        """
        self.folder_icon = Gtk.IconTheme.get_default().load_icon(
            "folder", 16, 0)
        self.draw_grid = True
        self.equal_area_projection = True
        self.minor_grid_spacing = 2
        self.major_grid_spacing = 10
        self.grid_cutoff_lat = 80
        self.show_north = False
        self.show_center_cross = False
        self.pixel_density = 75
        self.grid_linestyle = "--"
        self.grid_color = "#787878"
        self.grid_width = 0.4
        self.fig = Figure(dpi=self.pixel_density)
        self.draw_legend = True
        self.canvas_color = "#bfbfbf"

    def get_fig(self):
        """
        Returns the Matplotlib-Figure.

        Returns the figure that is stored by this class. The MainWindow class
        calls this function once during initialization to add the figure to
        the FigureCanvas.
        """
        return self.fig

    def get_inverse_transform(self):
        """
        Returns the inverse transform for the current stereonet projection.

        If the projection is equal are (True) the function returns the
        InvertedLambertTransform- or else the
        InvertedSterreographicTransform-class.
        """
        if self.equal_area_projection is True:
            return mplstereonet.stereonet_transforms.\
                        InvertedLambertTransform(0, 0, self.pixel_density)
        else:
            return mplstereonet.stereonet_transforms.\
                        InvertedStereographicTransform(0, 0, self.pixel_density)

    def get_transform(self):
        """
        Returns the normal transform for the current stereonet projection.

        If the projection is equal are (True) the function returns the
        LambertTransform- or else the SterreographicTransform-class.
        """
        if self.equal_area_projection is True:
            return mplstereonet.stereonet_transforms.\
                        LambertTransform(0, 0, self.pixel_density)
        else:
            return mplstereonet.stereonet_transforms.\
                        StereographicTransform(0, 0, self.pixel_density)

    def get_draw_grid_state(self):
        """
        Returns if the grid should be drawn for the stereonet.

        Returns a boolean. True mean that a grid should be drawn. False means
        that no grid should be drawn. This method is called by the MainWindow-
        redraw_plot-method.
        """
        return self.draw_grid

    def set_draw_grid_state(self, new_state):
        """
        Sets if the grid should be drawn for the stereonet.

        Expects a boolean. True mean that a grid should be drawn. False means
        that no grid should be drawn. This method is called by the
        LayerProperties-dialog when the setting is changed.
        """
        self.draw_grid = new_state

    def get_folder_icon(self):
        """
        Returns the folder icon used for the group-layer pixbuf.

        Always returns the "folder" icon from the Gtk.IconTheme. The folder
        will therefore match the desktop-theme set by the user. This method is
        called by the MainWindow "on_toolbutton_create_group_layer_clicked"-
        method.
        """
        return self.folder_icon

    def get_pixel_density(self):
        """
        Returns the pixel density the plot is using.

        The pixel density is an int and the default value is 75. This method
        is called by the LayerProperties-dialog so it can display the current
        value.
        """
        return self.pixel_density

    def set_pixel_density(self, new_pixel_density):
        """
        Sets a new pixel density for the plot.

        Expects an int. This method is called by the LayerProperties-dialog.
        The new value will be used when the plot redraws when the settings
        in the dialog are applied.
        """
        self.pixel_density = new_pixel_density

    def get_projection(self):
        """
        Returns the projection currently used by the stereonet.

        Returns one of two strings that MPLStereonet uses to distinguish
        between the equal-area and equal-angle projection. This method is only
        called from this class when the view is switched.
        """
        if self.equal_area_projection is True:
            return "equal_area_stereonet"
        else:
            return "equal_angle_stereonet"

    def get_projection_state(self):
        """
        Returns the projection state for the stereonet.

        Returns a boolean. True means that the stereonet should be drawn
        with equal-area. False mean equal-angle. This method is called by the
        StereonetProperties-dialog to load the current setting.
        """
        return self.equal_area_projection

    def set_projection_state(self, new_state):
        """
        Sets a new projection state.

        Expects a boolean. True means that the projection will be equal-area,
        False means equal-angle. This method is called by the
        StereonetProperties-dialog when a new setting for the projection is
        applied.
        """
        self.equal_area_projection = new_state

    def get_grid_linestyle(self):
        """
        Returns the linestyle of the grid.

        The linestyle is returned as a string. Default is "--" (dashed). This
        method is called by the MainWindow "redraw_plot"-method.
        """
        return self.grid_linestyle

    def get_grid_color(self):
        """
        Returns the color of the grid.

        Returns the color as a hex-triplet. The default is "#787878". This
        method is called by the MainWindow "redraw_plot"-method.
        """
        return self.grid_color

    def get_grid_width(self):
        """
        Returns the width of the grid lines.

        The width of the grid lines is returned as a float or int. The default
        is "0.4". This method is called by the MainWindow "redraw_plot"-method.
        """
        return self.grid_width

    def get_draw_legend(self):
        """
        Returns if the legend should be drawn as a boolean.

        The returned value is either True if a legend should be drawn, or False
        if no legend should be drawn. This method is called by the MainWindow
        "redraw_plot"-method and the StereonetProperties-dialog.
        """
        return self.draw_legend

    def set_draw_legend(self, new_state):
        """
        Sets a new state for whether the legend should be drawn.

        Expects a boolean. True means that the legend should be drawn. False
        means that no legend should be drawn. This method is called by the
        StereonetProperties-dialog when a new setting is applied.
        """
        self.draw_legend = new_state

    def get_canvas_rgba(self):
        """
        Returns the canvas color as a Gdk.RGBA.

        This method is called by the StereonetProperties-dialog to apply the
        current canvas color to the ColorButton.
        """
        rgba = Gdk.RGBA()
        rgba.parse(self.canvas_color)
        return rgba.to_color()

    def set_canvas_color(self, new_color):
        """
        Sets a new canvas color.

        Expects a hex-triplet string (e.g. "#bfbfbf"). This method is called
        by the StereonetProperties-dialog when a new color is applied to the
        canvas.
        """
        self.canvas_color = new_color

    def get_stereonet(self):
        """
        Resets the figure and returns the stereonet axis.

        When the view in the main window is changed to only stereoent. The
        figure is reset. Then the current settings are applied and one subplot
        for the stereonet is created. This method is called when the
        MainWindow "__init__"-method and the "redraw_plot"-method. 
        """
        self.fig.clf()
        self.fig.patch.set_facecolor(self.canvas_color)
        self.fig.set_dpi(self.pixel_density)
        gridspec = GridSpec(1, 1)
        sp_stereo = gridspec.new_subplotspec((0, 0))
        ax_stereo = self.fig.add_subplot(sp_stereo,
                                         projection=self.get_projection())
        return ax_stereo

    def get_stereo_rose(self):
        """
        Resets the figure and returns a stereonet and rose diagram axis.

        When the view in the main window is changed to stereonet and rose
        diagram, the figure is reset. The current settings are applied and
        two subplots for the stereonet and rose diagram are created. The
        axis of the stereonet and rose diagram are returned. This method is
        called by the MainWindow "redraw_plot"-method.
        """
        self.fig.clf()
        self.fig.patch.set_facecolor(self.canvas_color)
        self.fig.set_dpi(self.pixel_density)
        gridspec = GridSpec(1, 2)
        sp_stereo = gridspec.new_subplotspec((0, 0),
                                             rowspan=1, colspan=1)
        sp_rose = gridspec.new_subplotspec((0, 1),
                                           rowspan=1, colspan=1)
        ax_stereo = self.fig.add_subplot(sp_stereo,
                                         projection=self.get_projection())
        ax_rose = self.fig.add_subplot(sp_rose, projection="northpolar")
        return ax_stereo, ax_rose

    def get_rose_diagram(self):
        """
        Resets the figure and returns the rose diagram axis.

        When the view in the main window is changed to rose-diagram-only the
        figure is reset. The current settings are applied and one subplot
        for the rose diagram is created. The axis of the rose-diagram is
        returned. This method is called by the MainWindow "redraw_plot"-method.
        """
        self.fig.clf()
        self.fig.patch.set_facecolor(self.canvas_color)
        self.fig.set_dpi(self.pixel_density)
        gridspec = GridSpec(1, 1)
        sp_rose = gridspec.new_subplotspec((0, 0))
        ax_rose = self.fig.add_subplot(sp_rose, projection="northpolar")
        return ax_rose

    def get_pt_view(self):
        """
        Resets the canvas and returns the 3 axis of the paleostress view.

        When the view in the main window is changed to paleostress the figure
        is reset. The current settings are applied and 3 subplots are created.
        The 3 axis of the subplots are returned. This method is called by the
        MainWindow "redraw_plot"-method when the view has been changed.
        """
        self.fig.clf()
        self.fig.patch.set_facecolor(self.canvas_color)
        self.fig.set_dpi(self.pixel_density)
        gridspec = GridSpec(2, 5)
        sp_stereo = gridspec.new_subplotspec((0, 0), colspan=3, rowspan=2)
        sp_fluc = gridspec.new_subplotspec((0, 3), colspan=2)
        sp_mohr = gridspec.new_subplotspec((1, 3), colspan=2)
        ax_stereo = self.fig.add_subplot(sp_stereo,
                                         projection=self.get_projection())
        ax_fluc = self.fig.add_subplot(sp_fluc, aspect="equal")
        ax_mohr = self.fig.add_subplot(sp_mohr, aspect="equal")
        return ax_stereo, ax_fluc, ax_mohr
