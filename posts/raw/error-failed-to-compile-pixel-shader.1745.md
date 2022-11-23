vivienneanthony | 2017-01-02 01:09:50 UTC | #1

Hello

What would cause? I'm trying to isolate a weird problem that occurs in the editor. I'm making. Any clue is appreciated?

[code]Wed Feb  3 22:13:48 2016] ERROR: Failed to compile vertex shader LitSolid(DIRLIGHT INSTANCED NOUV PERPIXEL SHADOW):
Owner shader has expired
[Wed Feb  3 22:13:48 2016] ERROR: Failed to compile pixel shader LitSolid(AMBIENT DIRLIGHT PCF_SHADOW PERPIXEL SHADOW):
Owner shader has expired
[Wed Feb  3 22:13:48 2016] ERROR: Failed to compile vertex shader LitSolid(DIRLIGHT INSTANCED NOUV PERPIXEL SHADOW):
Owner shader has expired
[Wed Feb  3 22:13:48 2016] ERROR: Failed to compile pixel shader LitSolid(AMBIENT DIRLIGHT PCF_SHADOW PERPIXEL SHADOW):
Owner shader has expired
[Wed Feb  3 22:13:48 2016] ERROR: Failed to compile vertex shader LitSolid(DIRLIGHT NOUV PERPIXEL SHADOW):
Owner shader has expired
[Wed Feb  3 22:13:48 2016] ERROR: Failed to compile vertex shader LitSolid(DIRLIGHT NOUV PERPIXEL SHADOW):
Owner shader has expired
[Wed Feb  3 22:13:48 2016] ERROR: Failed to compile vertex shader LitSolid(DIRLIGHT NOUV PERPIXEL):
Owner shader has expired
[Wed Feb  3 22:13:48 2016] ERROR: Failed to compile pixel shader LitSolid(DIRLIGHT PERPIXEL):
Owner shader has expired
[Wed Feb  3 22:13:48 2016] ERROR: Failed to compile vertex shader LitSolid(DIRLIGHT NOUV PERPIXEL):
Owner shader has expired
[Wed Feb  3 22:13:48 2016] ERROR: Failed to compile pixel shader LitSolid(DIRLIGHT PERPIXEL):
Owner shader has expired
[Wed Feb  3 22:13:48 2016] ERROR: Failed to compile vertex shader LitSolid(DIRLIGHT PERPIXEL):
Owner shader has expired
[Wed Feb  3 22:13:48 2016] ERROR: Failed to compile pixel shader LitSolid(DIFFMAP DIRLIGHT PERPIXEL):
Owner shader has expired
[Wed Feb  3 22:13:48 2016] ERROR: Failed to compile vertex shader LitSolid(DIRLIGHT PERPIXEL):
Owner shader has expired
[Wed Feb  3 22:13:48 2016][/code]


Vivienne

-------------------------

thebluefish | 2017-01-02 01:09:50 UTC | #2

This happens when a ShaderVariation is created for a Shader that doesn't exist.

Not 100% sure how this would happen in practice outside of accidentally passing a null Shader when creating a ShaderVariation in code.

-------------------------

