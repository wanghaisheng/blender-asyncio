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

bl_info = {
    "name" : "ls_test_addon",
    "author" : "ls",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from .test_op import *
from .test_panel import *
from .async_loop import *

def register():
    async_loop.setup_asyncio_executor()
    bpy.utils.register_class(AsyncLoopModalOperator)
    
    bpy.utils.register_class(Test_OT_Operator)
    bpy.utils.register_class(Test_OT_Mixin)
    bpy.utils.register_class(Test_OT_Block)
    bpy.utils.register_class(Test_OT_NoBlock)
    
    bpy.utils.register_class(Test_PT_Panel)

def unregister():
    bpy.utils.unregister_class(AsyncLoopModalOperator)
    
    bpy.utils.unregister_class(Test_OT_Operator)
    bpy.utils.unregister_class(Test_OT_Mixin)
    bpy.utils.unregister_class(Test_OT_Block)
    bpy.utils.unregister_class(Test_OT_NoBlock)

    bpy.utils.unregister_class(Test_PT_Panel)