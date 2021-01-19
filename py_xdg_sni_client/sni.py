#!/usr/bin/python
#
# Copyright <year> Ahmad Hasan Mubashshir <ahmubashshir@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#
#
from pydbus import SessionBus


class StatusNotifierItem:
    """
    <node name="/StatusNotifierItem">
        <interface name="org.kde.StatusNotifierItem">
            <property name="Category" type="s" access="read"/>
            <property name="Id" type="s" access="read"/>
            <property name="Title" type="s" access="read"/>
            <property name="Status" type="s" access="read"/>
            <property name="WindowId" type="i" access="read"/>
            <property name="Menu" type="o" access="read" />

            <!-- main icon -->
            <!-- names are preferred over pixmaps -->
            <property name="IconName" type="s" access="read" />
            <property name="IconThemePath" type="s" access="read" />

            <!-- struct containing width, height and image data-->
            <!-- implementation has been dropped as of now -->
            <property name="IconPixmap" type="a(iiay)" access="read" />

            <!-- not used in ayatana code, no test case so far -->
            <property name="OverlayIconName" type="s" access="read"/>
            <property name="OverlayIconPixmap" type="a(iiay)" access="read" />

            <!-- Requesting attention icon -->
            <property name="AttentionIconName" type="s" access="read"/>

            <!--same definition as image-->
            <property name="AttentionIconPixmap" type="a(iiay)" access="read" />

            <!-- tooltip data -->
            <!--(iiay) is an image-->
            <property name="ToolTip" type="(sa(iiay)ss)" access="read" />

            <method name="Activate">
                <arg name="x" type="i" direction="in"/>
                <arg name="y" type="i" direction="in"/>
            </method>
            <method name="SecondaryActivate">
                <arg name="x" type="i" direction="in"/>
                <arg name="y" type="i" direction="in"/>
            </method>
            <method name="Scroll">
                <arg name="delta" type="i" direction="in"/>
                <arg name="dir"   type="s" direction="in"/>
            </method>

            <signal name="NewTitle"></signal>
            <signal name="NewIcon"></signal>
            <signal name="NewIconThemePath"></signal>
            <signal name="NewAttentionIcon"></signal>
            <signal name="NewOverlayIcon"></signal>
            <signal name="NewToolTip"></signal>
            <signal name="NewStatus"></signal>

            <!-- ayatana labels -->
            <signal name="XAyatanaNewLabel">
                <arg type="s" name="label" direction="out" />
                <arg type="s" name="guide" direction="out" />
            </signal>
            <property name="XAyatanaLabel" type="s" access="read" />
            <property name="XAyatanaLabelGuide" type="s" access="read" />
        </interface>
    </node>
    """
    data = {
        'Category': None,
        'Id': None,
        'Title': None,
        'XAyatanaLabel': None,
        'XAyatanaLabelGuide': None
    }

    def Activate(self, x, y):
        pass

    def SecondaryActivate(self, x, y):
        pass

    def Scroll(self, delta, direction):
        pass
# vim: ft=python ts=4 et
