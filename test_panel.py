# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import bpy

class Test_PT_Panel(bpy.types.Panel):
    bl_idname = "LS_SAMPLE_PT_Panel"
    bl_label = "Asyncio Examples"
    bl_category = "Asyncio Examples"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context_):
        layout = self.layout

        layout.row().operator('view3d.sample_1', text="Synchronous")
        layout.row().operator('view3d.sample_2', text="Async mixin (non-blocking)")
        layout.row().operator('view3d.sample_3', text="Async blocking")
        layout.row().operator('view3d.sample_4', text="Async non-blocking")