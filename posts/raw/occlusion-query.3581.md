caseymcc | 2017-09-20 15:07:43 UTC | #1

I want to add hardware occlusion query into Urho3D, not specifically as part of the rendering but mainly to be used to determine when to load chunks of terrain (rather than just render distance). The terrain (voxel chunks) will be added as a very low level representation of the chunk (cube) to see if it gets rendered at all. If it does get rendered then the lod of the voxels (based on distance to camera) is loaded.

I have limited experience with Urho3D so I am hoping to get some feedback from someone with more insight. From my quick look through some of the code for Urho3D I assume I should setup the occlusion queries as a render pass some time after the base pass and before the postalpha pass. I haven't found where the fog is rendered yet (assuming postalpha). The plan is not to use the query in the current frame only when available (frame or 2 delayed) so there should not be any detriment to the rendering pass. Like noted before I want to set it up to add items to the query and get some delay response on the result. I am not sure the correct notification system to use in Urho3D and was hoping on some insight here is well. Outside of Urho3D I would just set up a thread protected queue to add items to the query pass and a second thread protected queue with the result information, however with Urho3D seems like it would be better to provide this information in the update pass.

-------------------------

