1vanK | 2017-09-15 18:00:12 UTC | #1

Looking through the source code [github.com/id-Software/DOOM-3-B ... master/neo](https://github.com/id-Software/DOOM-3-BFG/tree/master/neo) I noticed that they use a strange method for rendering weapons that it does not permeate through the wall. I do not fully understand how it works, but it modifies the projection matrix. DepthHack also used for particles.
```
renderEntity_s
{
    ...
    float					modelDepthHack;			// squash depth range so particle effects don't clip into walls 
    bool					weaponDepthHack;		// squash depth range so view weapons don't poke into walls
													// this automatically implies noShadow 
}
```

```
ID_INLINE void idRenderMatrix::ApplyDepthHack( idRenderMatrix & src ) {
	// scale projected z by 25%
	src.m[2*4+0] *= 0.25f;
	src.m[2*4+1] *= 0.25f;
	src.m[2*4+2] *= 0.25f;
	src.m[2*4+3] *= 0.25f;
}


ID_INLINE void idRenderMatrix::ApplyModelDepthHack( idRenderMatrix & src, float value ) {
	// offset projected z
	src.m[2*4+3] -= value;
}
````

```
static void RB_EnterWeaponDepthHack() {
	float	matrix[16];

	memcpy( matrix, backEnd.viewDef->projectionMatrix, sizeof( matrix ) );

	const float modelDepthHack = 0.25f;
	matrix[2] *= modelDepthHack;
	matrix[6] *= modelDepthHack;
	matrix[10] *= modelDepthHack;
	matrix[14] *= modelDepthHack;

	qglMatrixMode( GL_PROJECTION );
	qglLoadMatrixf( matrix );
	qglMatrixMode( GL_MODELVIEW );
} 

static void RB_EnterModelDepthHack( float depth ) {
	float matrix[16];

	memcpy( matrix, backEnd.viewDef->projectionMatrix, sizeof( matrix ) );

	matrix[14] -= depth;

	qglMatrixMode( GL_PROJECTION );
	qglLoadMatrixf( matrix );
	qglMatrixMode( GL_MODELVIEW );
} 

static void RB_LeaveDepthHack() {
	qglMatrixMode( GL_PROJECTION );
	qglLoadMatrixf( backEnd.viewDef->projectionMatrix );
	qglMatrixMode( GL_MODELVIEW );
} 

````

```
static void RB_RenderDrawSurfListWithFunction( drawSurf_t **drawSurfs, int numDrawSurfs, void (*triFunc_)( const drawSurf_t *) ) {
	backEnd.currentSpace = NULL;

	for ( int i = 0 ; i < numDrawSurfs ; i++ ) {
		const drawSurf_t * drawSurf = drawSurfs[i];
		if ( drawSurf == NULL ) {
			continue;
		}
		assert( drawSurf->space != NULL );
		if ( drawSurf->space != NULL ) {	// is it ever NULL?  Do we need to check?
			// Set these values ahead of time so we don't have to reconstruct the matrices on the consoles
			if ( drawSurf->space->weaponDepthHack ) {
				RB_SetWeaponDepthHack();
			}

			if ( drawSurf->space->modelDepthHack != 0.0f ) {
				RB_SetModelDepthHack( drawSurf->space->modelDepthHack );
			}

			// change the matrix if needed
			if ( drawSurf->space != backEnd.currentSpace ) {
				RB_LoadMatrixWithBypass( drawSurf->space->modelViewMatrix );
			}

			if ( drawSurf->space->weaponDepthHack ) {
				RB_EnterWeaponDepthHack();
			}

			if ( drawSurf->space->modelDepthHack != 0.0f ) {
				RB_EnterModelDepthHack( drawSurf->space->modelDepthHack );
			}
		}

		// change the scissor if needed
		if ( r_useScissor.GetBool() && !backEnd.currentScissor.Equals( drawSurf->scissorRect ) ) {
			backEnd.currentScissor = drawSurf->scissorRect;
			GL_Scissor( backEnd.viewDef->viewport.x1 + backEnd.currentScissor.x1, 
				backEnd.viewDef->viewport.y1 + backEnd.currentScissor.y1,
				backEnd.currentScissor.x2 + 1 - backEnd.currentScissor.x1,
				backEnd.currentScissor.y2 + 1 - backEnd.currentScissor.y1 );
		}

		// render it
		triFunc_( drawSurf );

		if ( drawSurf->space != NULL && ( drawSurf->space->weaponDepthHack || drawSurf->space->modelDepthHack != 0.0f ) ) {
			RB_LeaveDepthHack();
		}

		backEnd.currentSpace = drawSurf->space;
	}
}
```

Also in Doom I do not see any problems with rendering shadows over weapon, so it seems it is good method. Any ideas about possibility to integrate of something like this to Urho3D?

-------------------------

cadaver | 2017-01-02 01:13:53 UTC | #2

Camera custom projection matrix should go in to master shortly, however this would require a per-object custom projection matrix (if we want to use shadows from the existing scene render) which can be somewhat unclean to get in. Ideas / PRs are welcome.

-------------------------

1vanK | 2017-03-20 01:21:48 UTC | #3

 https://forum.unity3d.com/threads/first-person-rendering-in-unity-5-writeup.401513/

-------------------------

1vanK | 2017-09-15 17:45:19 UTC | #4

https://youtu.be/WHaaFU6UfkI

Creating custum material for weapon:
1) Copy and rename LitSolid.glsl
2) Create technique used this shader
3) Modify VS():

Fix shadows when weapon drawn over wall:
```
        ...
        // Squeeze model along view Z coord to fix shadows, falling on model
        vec3 farRay = GetFarRay(gl_Position);
        vec3 shadowWorldPos = farRay * GetDepth(gl_Position) * 0.25 + cCameraPos;
        vec4 shadowProjWorldPos = vec4(shadowWorldPos, 1.0);

        #ifdef SHADOW
            // Shadow projection: transform from world space to shadow space
            for (int i = 0; i < NUMCASCADES; i++)
                vShadowPos[i] = GetShadowPos(i, vNormal, shadowProjWorldPos);
        #endif
        ...
```

Draw weapon over wall:
```
    ....
    gl_Position.z *= 0.25;
}
```

-------------------------

Eugene | 2017-09-15 18:07:28 UTC | #5

What about shadows from/on the weapon?

-------------------------

1vanK | 2017-09-15 18:14:43 UTC | #6

> shadows on the weapon?

first code block doing it as you can see on video

> shadows from the weapon?

shadows from flying weapon without players model looks not cool so it not used in games, but no any noticeable probles here (only the outer part of weapon casts shadow on the wall, but it does not strike the eye)

-------------------------

Eugene | 2017-09-15 18:42:42 UTC | #7

[quote="1vanK, post:6, topic:2202"]
first code block doing it as you can see on video
[/quote]

Sorry, I missed this part of video.

-------------------------

