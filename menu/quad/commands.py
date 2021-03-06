############################################################################
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <https://www.gnu.org/licenses/>.
############################################################################

c0000="bpy.ops.object.select_instance('INVOKE_DEFAULT')"
c0001="bpy.ops.object.smart_convert(target='MESH')"
c0002="bpy.ops.object.smart_convert(target='CURVE')"
c0003="bpy.ops.wm.tool_set_by_id(name='builtin.move')"
c0004="bpy.ops.object.transform_type_in(switch='move')"
c0005="bpy.ops.wm.tool_set_by_id(name='builtin.rotate')"
c0006="bpy.ops.object.transform_type_in(switch='rotate')"
c0007="bpy.ops.wm.tool_set_by_id(name='builtin.scale')"
c0008="bpy.ops.object.transform_type_in(switch='scale')"
c0009="bpy.ops.wm.tool_set_by_id(name='builtin.select_box')"
c0010="bpy.ops.bsmax.selectsimilar('INVOKE_DEFAULT')"
c0011="bpy.ops.object.clone('INVOKE_DEFAULT')"
c0012="bpy.ops.object.hide(mode='selection')"
c0013="bpy.ops.object.hide(mode='unselected')"
c0014="bpy.ops.object.hide(mode='clear',collection=True)"
c0015="bpy.ops.object.freeze(mode='selection')"
c0016="bpy.ops.object.freeze(mode='clear')"
c0017="bpy.ops.view3d.localview('INVOKE_DEFAULT')"
c0018="bpy.ops.object.subobject_level(level=6)"
c0019="bpy.ops.object.subobject_level(level=1)"
c0020="bpy.ops.object.subobject_level(level=2)"
c0021="bpy.ops.object.subobject_level(level=3)"
c0022="bpy.ops.object.subobject_level(level=4)"
c0023="bpy.ops.object.subobject_level(level=5)"
c0024="bpy.ops.screen.repeat_last('INVOKE_DEFAULT')"
c0025="bpy.ops.wm.tool_set_by_id(name='builtin.bisect')"
c0026="bpy.ops.mesh.knife_tool('INVOKE_DEFAULT')"
c0027="bpy.ops.mesh.edge_collapse('INVOKE_DEFAULT')"
c0028="bpy.ops.mesh.hide(unselected=True)"
c0029="bpy.ops.view3d.toggle_xray('INVOKE_DEFAULT')"
c0030="bpy.ops.curve.handle_type_set(type='AUTOMATIC')"
c0031="bpy.ops.curve.handle_type_set(type='VECTOR')"
c0032="bpy.ops.curve.handle_type_set(type='ALIGNED')"
c0033="bpy.ops.curve.handle_type_set(type='FREE_ALIGN')"
c0034="bpy.ops.curve.subdivide('INVOKE_DEFAULT')"
c0035="bpy.ops.wm.tool_set_by_id(name='builtin.poly_build')"
c0036="bpy.ops.mesh.dissolve_verts('INVOKE_DEFAULT')"
c0037="bpy.ops.mesh.separate('INVOKE_DEFAULT')"
c0038="bpy.ops.mesh.connect('INVOKE_DEFAULT')"
c0039="bpy.ops.wm.tool_set_by_id(name='builtin.extrude_region')"
c0040="bpy.ops.wm.tool_set_by_id(name='builtin.bevel')"
c0041="bpy.ops.mesh.remove_doubles(threshold=1.0,use_unselected=False)"
c0042="bpy.ops.mesh.remove_doubles('INVOKE_DEFAULT')"
c0043="bpy.ops.mesh.dissolve_edges('INVOKE_DEFAULT')"
c0044="bpy.ops.mesh.separate('INVOKE_DEFAULT')"
c0045="bpy.ops.mesh.connect('INVOKE_DEFAULT')"
c0046="bpy.ops.wm.tool_set_by_id(name='builtin.extrude_region')"
c0047="bpy.ops.wm.tool_set_by_id(name='builtin.bevel')"
c0048="bpy.ops.mesh.remove_doubles(threshold=1.0,use_unselected=False)"
c0049="bpy.ops.mesh.create_curve_from_edge('INVOKE_DEFAULT')"
c0050="bpy.ops.mesh.dissolve_faces('INVOKE_DEFAULT')"
c0051="bpy.ops.object.detach('INVOKE_DEFAULT')"
c0052="bpy.ops.wm.tool_set_by_id(name='builtin.extrude_region')"
c0053="bpy.ops.wm.tool_set_by_id(name='builtin.inset_faces')"
c0054="bpy.ops.mesh.flip_normals('INVOKE_DEFAULT')"
c0055="bpy.ops.curve.chamfer('INVOKE_DEFAULT')"
c0056="bpy.ops.curve.chamfer('INVOKE_DEFAULT',fillet=True)"
c0057="bpy.context.object.data.type='POINT'"
c0058="bpy.context.object.data.type='SUN'"
c0059="bpy.context.object.data.type='SPOT'"
c0060="bpy.context.object.data.type='AREA'"
c0061="bpy.context.object.data.use_shadow="
c0062="bpy.ops.create.sphere('INVOKE_DEFAULT')"
c0063="bpy.ops.create.box('INVOKE_DEFAULT')"
c0064="bpy.ops.create.cylinder('INVOKE_DEFAULT')"
c0065="bpy.ops.create.plane('INVOKE_DEFAULT')"
c0066="bpy.ops.create.line('INVOKE_DEFAULT')"
c0067="bpy.ops.create.circle('INVOKE_DEFAULT')"
c0068="bpy.ops.create.rectangle('INVOKE_DEFAULT')"
c0069="bpy.ops.create.arc('INVOKE_DEFAULT')"
c0070="bpy.ops.view3d.view_axis(type='FRONT')"
c0071="bpy.ops.view3d.view_axis(type='BACK')"
c0072="bpy.ops.view3d.view_axis(type='TOP')"
c0073="bpy.ops.view3d.view_axis(type='BOTTOM')"
c0074="bpy.ops.view3d.view_axis(type='LEFT')"
c0075="bpy.ops.view3d.view_axis(type='RIGHT')"
c0076="bpy.ops.view3d.view_persportho('INVOKE_DEFAULT')"
c0077="bpy.ops.camera.set_active('INVOKE_DEFAULT')"
c0078="bpy.ops.camera.create_from_view('INVOKE_DEFAULT')"
c0079="bpy.ops.anim.set_key('INVOKE_DEFAULT')"
c0080="bpy.ops.anim.set_key_filters('INVOKE_DEFAULT')"
c0081="bpy.ops.anim.delete_selected_animation('INVOKE_DEFAULT')"
c0082="bpy.ops.object.coordinate_system(coordsys='CURSOR')"
c0083="bpy.ops.object.coordinate_system(coordsys='LOCAL')"
c0084="bpy.ops.object.coordinate_system(coordsys='NORMAL')"
c0085="bpy.ops.object.coordinate_system(coordsys='GIMBAL')"
c0086="bpy.ops.object.coordinate_system(coordsys='VIEW')"
c0087="bpy.ops.object.coordinate_system(coordsys='GLOBAL')"
c0088="bpy.context.scene.tool_settings.snap_elements={'INCREMENT'}"
c0089="bpy.context.scene.tool_settings.snap_elements={'VERTEX'}"
c0090="bpy.context.scene.tool_settings.snap_elements={'VOLUME'}"
c0091="bpy.context.scene.tool_settings.snap_elements={'EDGE'}"
c0092="bpy.context.scene.tool_settings.snap_elements={'FACE'}"
c0093="bpy.context.scene.tool_settings.snap_target='CLOSEST'"
c0094="bpy.context.scene.tool_settings.snap_target='CENTER'"
c0095="bpy.context.scene.tool_settings.snap_target='MEDIAN'"
c0096="bpy.context.scene.tool_settings.snap_target='ACTIVE'"
c0097="bpy.ops.render.render('INVOKE_DEFAULT')"
c0098="bpy.ops.mesh.attach('INVOKE_DEFAULT')"
c0099="bpy.ops.mesh.attach_list('INVOKE_DEFAULT')"
c0100="bpy.ops.object.quick_smoke('INVOKE_DEFAULT')"
c0101="bpy.ops.object.quick_fur('INVOKE_DEFAULT')"
c0102="bpy.ops.object.quick_explode('INVOKE_DEFAULT')"
c0103="bpy.ops.object.quick_fluid('INVOKE_DEFAULT')"
c0104="bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN',center='MEDIAN')"
c0105="bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY',center='MEDIAN')"
c0106="bpy.ops.object.origin_set(type='ORIGIN_CURSOR',center='MEDIAN')"
c0107="bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME',center='MEDIAN')"
c0108="bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS',center='MEDIAN')"
c0109="bpy.ops.wm.tool_set_by_id(name='builtin.cursor')"
c0110="bpy.context.scene.tool_settings.use_snap_translate="
c0111="bpy.context.scene.tool_settings.use_snap_rotate="
c0112="bpy.context.scene.tool_settings.use_snap_scale="
c0113="bpy.context.scene.render.engine='BLENDER_EEVEE'"
c0114="bpy.context.scene.render.engine='BLENDER_WORKBENCH'"
c0115="bpy.context.scene.render.engine='CYCLES'"
c0116="bpy.context.scene.eevee.use_gtao=not bpy.context.scene.eevee.use_gtao"
c0117="bpy.context.scene.eevee.use_bloom=not bpy.context.scene.eevee.use_bloom "
c0118="bpy.context.scene.eevee.use_ssr=not bpy.context.scene.eevee.use_ssr"
c0119="bpy.context.scene.eevee.use_motion_blur=not bpy.context.scene.eevee.use_motion_blur"
c0120="bpy.context.scene.render.use_simplify=not bpy.context.scene.render.use_simplify"
c0121="bpy.context.scene.render.use_freestyle=not bpy.context.scene.render.use_freestyle"
c0122="bpy.context.scene.cycles_curves.use_curves=not bpy.context.scene.cycles_curves.use_curves"
c0123="bpy.context.scene.shading.show_backface_culling=not bpy.context.scene.shading.show_backface_culling"
c0124="bpy.context.scene.render.use_motion_blur=not bpy.context.scene.render.use_motion_blur"
c0125="bpy.context.scene.shading.show_xray=not bpy.context.scene.shading.show_xray"
c0126="bpy.context.scene.shading.show_shadows=not bpy.context.scene.shading.show_shadows"
c0127="bpy.context.scene.shading.show_cavity=not bpy.context.scene.shading.show_cavity"
c0128="bpy.context.scene.shading.use_dof=not bpy.context.scene.shading.use_dof"
c0129="bpy.context.scene.shading.show_object_outline=not bpy.context.scene.shading.show_object_outline"
c0130="bpy.ops.mesh.target_weld('INVOKE_DEFAULT')"
c0131="bpy.ops.camera.create_target('INVOKE_DEFAULT')"
c0132="bpy.ops.camera.clear_targte('INVOKE_DEFAULT')"
c0133="bpy.ops.camera.search('INVOKE_DEFAULT')"
c0134="bpy.ops.create.extrudeshape('INVOKE_DEFAULT')"
c0135="bpy.ops.mesh.remove_isolated_geometry('INVOKE_DEFAULT')"
c0136="bpy.ops.object.set_local_coord_in_pose_mode('INVOKE_DEFAULT')"
c0137="bpy.ops.camera.lock_to_view_toggle('INVOKE_DEFAULT')"
c0138="bpy.ops.camera.select_active_camera('INVOKE_DEFAULT',selcam=True,seltrg=False)"
c0139="bpy.ops.camera.select_active_camera('INVOKE_DEFAULT',selcam=False,seltrg=True)"
c0140="bpy.ops.camera.select_active_camera('INVOKE_DEFAULT',selcam=True,seltrg=True)"
c0141="bpy.ops.light.create_target('INVOKE_DEFAULT')"
c0142="bpy.ops.light.clear_target('INVOKE_DEFAULT')"
c0143="bpy.ops.mesh.bridge_edge_loops('INVOKE_DEFAULT',twist_offset=0)"
c0144="bpy.ops.object.align_selected_to_target('INVOKE_DEFAULT')"
c0145="bpy.ops.curve.chamfer('INVOKE_DEFAULT',typein=True)"
c0146="bpy.ops.curve.chamfer('INVOKE_DEFAULT',fillet=True,typein=True)"
c0147="bpy.ops.camera.select_target('INVOKE_DEFAULT')"
c0148="bpy.ops.armature.bone_devide('INVOKE_DEFAULT')"
c0149="bpy.ops.armature.bone_devide('INVOKE_DEFAULT',typein=True)"
c0150="bpy.ops.armature.bone_type('INVOKE_DEFAULT',mode='OCTAHEDRAL')"
c0151="bpy.ops.armature.bone_type('INVOKE_DEFAULT',mode='STICK')"
c0152="bpy.ops.armature.bone_type('INVOKE_DEFAULT',mode='BBONE')"
c0153="bpy.ops.armature.bone_type('INVOKE_DEFAULT',mode='ENVELOPE')"
c0154="bpy.ops.armature.bone_type('INVOKE_DEFAULT',mode='WIRE')"
c0155="bpy.ops.object.freeze_transform('INVOKE_DEFAULT')"
c0156="bpy.ops.object.freeze_rotation('INVOKE_DEFAULT')"
c0157="bpy.ops.object.transform_to_zero('INVOKE_DEFAULT')"
c0158="bpy.ops.object.rotation_to_zero('INVOKE_DEFAULT')"
c0159="bpy.ops.curve.dividplus('INVOKE_DEFAULT',typein=True)"
c0160="bpy.ops.curve.switch_direction('INVOKE_DEFAULT')"
c0161="bpy.ops.curve.make_first('INVOKE_DEFAULT')"
c0162="bpy.context.space_data.lock_camera = not bpy.context.space_data.lock_camera"
c0163="bpy.context.space_data.lock_cursor = not bpy.context.space_data.lock_cursor"
c0164="bpy.ops.camera.lock_transform('INVOKE_DEFAULT')"
c0165="bpy.ops.mesh.edge_split('INVOKE_DEFAULT')"
c0166="bpy.ops.object.properties('INVOKE_DEFAULT')"
c0167="bpy.ops.editor.float(ui_type='FCURVES')"
c0168="bpy.ops.editor.float(ui_type='DOPESHEET')"
c0169="bpy.ops.editor.float(ui_type='NLA_EDITOR')"
c0170="bpy.ops.editor.float(ui_type='DRIVERS')"
c0171="bpy.ops.editor.float(ui_type='TEXT_EDITOR')"
c0172="bpy.ops.object.placment('INVOKE_DEFAULT')"
c0173="bpy.ops.object.link_to('INVOKE_DEFAULT')"
c0174="bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')"
c0175="bpy.context.scene.tool_settings.use_transform_skip_children = not bpy.context.scene.tool_settings.use_transform_skip_children"
c0176="bpy.context.space_data.shading.type = 'WIREFRAME'"
c0177="bpy.context.space_data.shading.type = 'SOLID'"
c0178="bpy.context.space_data.shading.type = 'MATERIAL'"
c0179="bpy.context.space_data.shading.type = 'RENDERED'"
c0180="bpy.context.space_data.shading.render_pass = 'COMBINED'"
c0181="bpy.context.space_data.shading.render_pass = 'EMISSION'"
c0182="bpy.context.space_data.shading.render_pass = 'ENVIRONMENT'"
c0183="bpy.context.space_data.shading.render_pass = 'SHADOW'"
c0184="bpy.context.space_data.shading.render_pass = 'DIFFUSE_LIGHT'"
c0185="bpy.context.space_data.shading.render_pass = 'DIFFUSE_COLOR'"
c0186="bpy.context.space_data.shading.render_pass = 'SPECULAR_LIGHT'"
c0187="bpy.context.space_data.shading.render_pass = 'SPECULAR_COLOR'"
c0188="bpy.context.space_data.shading.render_pass = 'VOLUME_TRANSMITTANCE'"
c0189="bpy.context.space_data.shading.render_pass = 'VOLUME_SCATTER'"
c0190="bpy.context.space_data.shading.render_pass = 'NORMAL'"
c0191="bpy.context.space_data.shading.render_pass = 'MIST'"
c0192="bpy.context.space_data.shading.use_scene_lights_render = not bpy.context.space_data.shading.use_scene_lights_render"
c0193="bpy.context.space_data.shading.use_scene_world_render = not bpy.context.space_data.shading.use_scene_world_render"
c0194="bpy.ops.mesh.select_element_toggle('INVOKE_DEFAULT')"
c0195="bpy.ops.anim.keyframe_insert_menu('INVOKE_DEFAULT')"
c0196="bpy.ops.pose.copy('INVOKE_DEFAULT')"
c0197="bpy.ops.pose.paste(flipped=False, selected_mask=False)"
c0198="bpy.ops.pose.paste(flipped=True, selected_mask=False)"
c0199="bpy.ops.pose.push('INVOKE_DEFAULT')"
c0200="bpy.ops.pose.relax('INVOKE_DEFAULT')"
c0201="bpy.ops.pose.breakdown('INVOKE_DEFAULT')"
c0202="bpy.ops.pose.paths_calculate('INVOKE_DEFAULT')"
c0203="bpy.ops.pose.paths_clear('INVOKE_DEFAULT')"
c0204="bpy.ops.pose.hide('INVOKE_DEFAULT',unselected=False)"
c0205="bpy.ops.pose.hide('INVOKE_DEFAULT',unselected=True)"
c0206="bpy.ops.pose.reveal('INVOKE_DEFAULT')"
c0207="bpy.ops.pose.user_transforms_clear('INVOKE_DEFAULT')"
c0208="bpy.ops.curve.attach('INVOKE_DEFAULT')"
c0209="bpy.ops.armature.attach('INVOKE_DEFAULT')"
c0210="bpy.ops.object.attach('INVOKE_DEFAULT')"
c0211=''
c0212=''
c0213=''
c0214=''
c0215=''
c0216=''
c0217=''
c0218=''
c0219=''
c0220=''