#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) Joseph Areeda (2015)
#
# This file is part of GWpy.
#
# GWpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GWpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GWpy.  If not, see <http://www.gnu.org/licenses/>.
#

""" Spectrum plots
"""
from CliProduct import CliProduct

class Spectrum(CliProduct):

    def get_action(self):
        """Return the string used as "action" on command line."""
        return 'Spectrum'

    def init_cli(self, parser):
        """Set up the argument list for this product"""
        self.arg_chan1(parser)
        self.arg_freq(parser)
        self.arg_plot(parser)
        return

    def get_ylabel(self, args):
        """Text for y-axis label"""
        return r'$\mathrm{log_{10}  ASD}$ $\left( \frac{\mathrm{Counts}}{\sqrt{\mathrm{Hz}}}\right)$'


    def gen_plot(self, args):
        """Generate the plot from time series and arguments"""
        return
