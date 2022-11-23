jmiller | 2020-07-02 07:50:49 UTC | #1

## Procedural Sky Component

[![images](https://thumbs2.imgbox.com/45/e0/HozslxmO_b.jpg)](https://imgbox.com/g/Prw0gYcpNK) [![images](https://thumbs2.imgbox.com/09/41/AyYXCWIU_b.jpg)](https://imgbox.com/g/Prw0gYcpNK) [![images](https://thumbs2.imgbox.com/06/b9/CyWLcclF_b.jpg)](https://imgbox.com/g/Prw0gYcpNK)

repo: https://gitlab.com/100espressos/ProcSky

The component procedurally renders a sky with rayleigh and mie atmospheric scattering from a solar light source, with over a dozen attributes in addition to the control/light node, all [animatable](https://urho3d.github.io/documentation/HEAD/_attribute_animation.html) with Urho.

Some modern C++ features are used but backporting should be straightforward.
Advice/PRs are welcome. Design is not final and there may be bugs lurking.

The component runs on E_SCENEUPDATE. By default it uses the first Viewport RenderPath. `AddToRenderPath()` and `RemoveFromRenderPath()` may facilitate a different approach.


The GLSL draws from a webgl series by Florian Bösch, which explains the rendering technique:
http://codeflow.org/entries/2011/apr/13/advanced-webgl-part-2-sky-rendering/
(NI) http://codeflow.org/entries/2011/apr/18/advanced-webgl-part-3-irradiance-environment-map/

There are nice contributions to this thread by others, so have a look.

-------------------------

vivienneanthony | 2017-01-02 01:05:50 UTC | #2

Awesome indeed.

-------------------------

weitjong | 2017-01-02 01:05:50 UTC | #3

I like the last screenshot. Cool stuff.

-------------------------

codingmonkey | 2017-01-02 01:05:52 UTC | #4

i like the first one  :slight_smile: 
and i guess that this needs to be an std sky-component in editor )

-------------------------

namic | 2017-01-02 01:08:34 UTC | #5

AMAZING! Just what i was looking for. Thanks a lot! 

Looks even better than Unigine: [developer.unigine.com/devlog/20 ... mposed.jpg](https://developer.unigine.com/devlog/20151120-unigine-2.1/scattering_2_composed.jpg)

ps.: How can we buy you a beer?

-------------------------

jmiller | 2017-01-02 01:08:52 UTC | #6

[quote="namic"]AMAZING! Just what i was looking for. Thanks a lot! [/quote]

May your skies be... however you want your skies. :wink:

[quote="namic"]ps.: How can we buy you a beer?[/quote]

It's just a small contribution, and I would defer gratuities to charity. But I do like beer -- maybe we share some day.  :slight_smile:

-------------------------

Sir_Nate | 2017-01-02 01:09:10 UTC | #7

If you don't like the near-black coloring the sky away from the sun gets (especially during the day), adding + vec3(0.1,0.2,0.3) to the final color in the shader gives a decent appearance to the sky (though the night will no longer be black). It should probably be an animated color, or perhaps a blend between a day sky texture and a night sky texture as the base color, but I am pretty satisfied with just that change (using the default parameters for everything else).

Also, at the beginning of the PixelShader, the clamp call needs to be changed to 
[code]float alpha = clamp(dot(eyeDir, lightDir), 0.0, 1.0);[/code]
for OpenGLES, as it doesn't like the integers used in it (at least on my phone).

-------------------------

STeeL | 2017-01-02 01:10:16 UTC | #8

HLSL is here(tested on DX11):
[code]
#include "Uniforms.hlsl"
#include "ScreenPos.hlsl"
#include "Transform.hlsl"

void VS(float4 iPos : POSITION,
    out float2 oTexCoord : TEXCOORD0,
    out float4 oPos : OUTPOSITION) {	
  float4x3 modelMatrix = iModelMatrix;
  float3 worldPos = GetWorldPos(modelMatrix);
  oPos = GetClipPos(worldPos);
  oPos.z = oPos.w;
  oTexCoord = GetQuadTexCoord(oPos);
  oTexCoord.y = 1.0 - oTexCoord.y;
}


#if defined(COMPILEPS)

uniform float4x3 cInvProj;
uniform float3x3 cInvViewRot;
uniform float3 cLightDir;
uniform float3 cKr;
uniform float cRayleighBrightness, cMieBrightness, cSpotBrightness, cScatterStrength, cRayleighStrength, cMieStrength, cRayleighCollectionPower, cMieCollectionPower, cMieDistribution;

static const float surfaceHeight = 0.99; // < 1
static const float intensity = 1.8;
static const int stepCount = 16;

float3 GetWorldNormal(float2 texCoord) {
  float2 fragCoord = texCoord;
  fragCoord = (fragCoord - 0.5) * 2.0;
  float4 deviceNormal = float4(fragCoord, 0.0, 1.0);
  float4 eyeUN = float4(
	cInvProj._m00 * deviceNormal.x + cInvProj._m10 * deviceNormal.y + cInvProj._m20 * deviceNormal.z + cInvProj._m30,
	cInvProj._m01 * deviceNormal.x + cInvProj._m11 * deviceNormal.y + cInvProj._m21 * deviceNormal.z + cInvProj._m31,
	cInvProj._m02 * deviceNormal.x + cInvProj._m12 * deviceNormal.y + cInvProj._m22 * deviceNormal.z + cInvProj._m32,
	deviceNormal.w);
  float3 eyeNormal = normalize(eyeUN.xyz);
  
  float3 worldUN = float3(
	cInvViewRot._m00 * eyeNormal.x + cInvViewRot._m01 * eyeNormal.y + cInvViewRot._m20 * eyeNormal.z,
	cInvViewRot._m01 * eyeNormal.x + cInvViewRot._m11 * eyeNormal.y + cInvViewRot._m21 * eyeNormal.z,
	cInvViewRot._m02 * eyeNormal.x + cInvViewRot._m12 * eyeNormal.y + cInvViewRot._m22 * eyeNormal.z
  );
  
  float3 worldNormal = normalize(worldUN);
  
  return worldNormal;
}

float AtmosphericDepth(float3 pos, float3 dir) {
  float a = dot(dir, dir);
  float b = 2.0 * dot(dir, pos);
  float c = dot(pos, pos) - 1.0;
  float det = b * b - 4.0 * a * c;
  float detSqrt = sqrt(det);
  float q = (-b - detSqrt) / 2.0;
  float t1 = c / q;
  return t1;
}

float Phase(float alpha, float g) {
  float a = 3.0 * (1.0 - g * g);
  float b = 2.0 * (2.0 + g * g);
  float c = 1.0 + alpha * alpha;
  float d = pow(1.0 + g * g - 2.0 * g * alpha, 1.5);
  return (a / b) * (c / d);
}

float HorizonExtinction(float3 pos, float3 dir, float radius) {
  float u = dot(dir, -pos);
  if(u < 0.0) {
    return 1.0;
  }
  float3 near = pos + u * dir;
  if(length(near) < radius) {
    return 0.0;
  } else {
    float3 v2 = normalize(near) * radius - pos;
    float diff = acos(dot(normalize(v2), dir));
    return smoothstep(0.0, 1.0, pow(diff * 2.0, 3.0));
  }
}

float3 Absorb(float dist, float3 color, float factor) {
  return color - color * pow(cKr, float3(factor / dist, factor / dist, factor / dist));
}

#endif // defined(COMPILEPS)

void PS(float2 iPos: TEXCOORD0, out float4 oColor : OUTCOLOR0) {
  float3 lightDir = cLightDir;
  lightDir.z *= -1.0; // Invert world Z for Urho.
  float3 eyeDir = GetWorldNormal(iPos);
  float alpha = clamp(dot(eyeDir, lightDir), 0, 1);
  float rayleighFactor = Phase(alpha, -0.01) * cRayleighBrightness;
  float mieFactor = Phase(alpha, cMieDistribution) * cMieBrightness;
  float spot = smoothstep(0.0, 15.0, Phase(alpha, 0.9995)) * cSpotBrightness;
  float3 eyePos = float3(0.0, surfaceHeight, 0.0);
  float eyeDepth = AtmosphericDepth(eyePos, eyeDir);
  float stepLength = eyeDepth / float(stepCount);
  float eyeExtinction = HorizonExtinction(eyePos, eyeDir, surfaceHeight - 0.15);

  float3 rayleighCollected = float3(0.0, 0.0, 0.0);
  float3 mieCollected = float3(0.0, 0.0, 0.0);

  for(int i = 0; i < stepCount; ++i) {
    float sampleDistance = stepLength * float(i);
    float3 pos = eyePos + eyeDir * sampleDistance;
    float extinction = HorizonExtinction(pos, lightDir, surfaceHeight - 0.35);
    float sampleDepth = AtmosphericDepth(pos, lightDir);
    float3 influx = Absorb(sampleDepth, float3(intensity,intensity ,intensity), cScatterStrength) * extinction;
    rayleighCollected += Absorb(sampleDistance, cKr * influx, cRayleighStrength);
    mieCollected += Absorb(sampleDistance, influx, cMieStrength);
  }

  rayleighCollected = (rayleighCollected * eyeExtinction * pow(eyeDepth, cRayleighCollectionPower)) / float(stepCount);
  mieCollected = (mieCollected * eyeExtinction * pow(eyeDepth, cMieCollectionPower)) / float(stepCount);

  float3 color = float3(spot*mieCollected + mieFactor*mieCollected + rayleighFactor*rayleighCollected);
  oColor = float4(color, 1.0);
}

[/code]

-------------------------

codingmonkey | 2017-01-02 01:10:16 UTC | #9

>HLSL is here(tested on DX11):
cool, thanks!)

-------------------------

horvatha4 | 2017-01-02 01:11:26 UTC | #10

Nice code! Thanks the share a lot!
I will it extend with real sun position calculations like this: [url]http://stackoverflow.com/questions/8708048/position-of-the-sun-given-time-of-day-latitude-and-longitude[/url]
or this: [url]http://www.esrl.noaa.gov/gmd/grad/solcalc/solareqns.PDF[/url]

-------------------------

horvatha4 | 2017-01-02 01:11:29 UTC | #11

[img]http://www.esrl.noaa.gov/gmd/grad/solcalc/azelzen.gif[/img]
Here is the first raw code. The original R-codelines are commented out.
[code]
	void CalculateSunPosition(float* azimuth, float *elevation, float latitude, float longitude, 
		unsigned year, unsigned month, unsigned day, float hour = 12, float minute = 0, float sec = 0)
	{
/* 
Original R-code at: http://stackoverflow.com/questions/8708048/position-of-the-sun-given-time-of-day-latitude-and-longitude?rq=1
*/
	year = Clamp(year, -4713, 5000);
	month = Clamp(month, 1, 12);
	day = Clamp(day, 1, 31);
	hour = Clamp(hour, 0.0f, 23.0f);
	minute = Clamp(minute, 0.0f, 59.0f);
	sec = Clamp(sec, 0.0f, 59.0f);
	latitude = Clamp(latitude, -90.0f, 90.0f);
	longitude = Clamp(longitude, -180.0f, 180.0f);

	//twopi <-2 * pi
	//deg2rad <-pi / 180
	//# Get day of the year, e.g.Feb 1 = 32, Mar 1 = 61 on leap years
	unsigned month_days[] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 };
	//day <-day + cumsum(month.days)[month]
	for (unsigned z = 1; z < month;z++) day += month_days[z];
	//leapdays <-year %% 4 == 0 & (year %% 400 == 0 | year %% 100 != 0) &  day >= 60 & !(month == 2 & day == 60)
	//	day[leapdays] <-day[leapdays] + 1;
	if(year % 4 == 0 && (year % 400 == 0 || year % 100 != 0) &&  day >= 60 && !(month == 2 && day == 60))
		day++;
	//# Get Julian date - 2400000
	//hour <-hour + min / 60 + sec / 3600 # hour plus fraction
	//delta <-year - 1949
	//leap <-trunc(delta / 4) # former leapyears
	//jd <-32916.5 + delta * 365 + leap + day + hour / 24
	hour = hour + minute / 60.0f + sec / 3600.0f;
	unsigned delta = year - 1949;
	unsigned leap = delta / 4;
	double jd = 32916.5f + (double)delta * 365.0 + (double)leap + day + hour / 24.0;

	//# The input to the Astronomer's almanach is the difference between
	//# the Julian date and JD 2451545.0 (noon, 1 January 2000)
	//time <- jd - 51545.
	double time = jd - 51545.0;

	//# Ecliptic coordinates

	//# Mean longitude
	//mnlong <-280.460 + .9856474 * time
	//mnlong <-mnlong %% 360
	//mnlong[mnlong < 0] <-mnlong[mnlong < 0] + 360
	double mnlong = 280.460 + .9856474 * time;
	mnlong = fmod(mnlong, 360.0);
	if (mnlong < 0) mnlong += 360.0;
	//mnlong = mnlong * M_DEGTORAD;// mnlong turn to radian

	//# Mean anomaly
	//mnanom <-357.528 + .9856003 * time
	//mnanom <-mnanom %% 360
	//mnanom[mnanom < 0] <-mnanom[mnanom < 0] + 360
	//mnanom <-mnanom * deg2rad
	double mnanom = 357.528 + .9856003 * time;
	mnanom = fmod(mnanom, 360.0);
	if (mnanom < 0) mnanom += 360.0;
	mnanom = mnanom * M_DEGTORAD;

	//# Ecliptic longitude and obliquity of ecliptic
	//eclong <-mnlong + 1.915 * sin(mnanom) + 0.020 * sin(2 * mnanom)
	//eclong <-eclong %% 360
	//eclong[eclong < 0] <-eclong[eclong < 0] + 360
	//oblqec <-23.439 - 0.0000004 * time
	//eclong <-eclong * deg2rad
	//oblqec <-oblqec * deg2rad
	double eclong = mnlong + 1.915 * sin(mnanom) + 0.020 * sin(2 * mnanom);
	eclong = fmod(eclong, 360.0);
	if (eclong < 0) eclong += 360.0;
	eclong = eclong * M_DEGTORAD;
	double oblqec = 23.439 - 0.0000004 * time;
	oblqec = oblqec * M_DEGTORAD;

	//# Celestial coordinates
	//# Right ascension and declination
	//num <-cos(oblqec) * sin(eclong)
	//den <-cos(eclong)
	//ra <-atan(num / den)
	//ra[den < 0] <-ra[den < 0] + pi
	//ra[den >= 0 & num < 0] <-ra[den >= 0 & num < 0] + twopi
	//dec <-asin(sin(oblqec) * sin(eclong))
	double num = cos(oblqec) * sin(eclong);
	double den = cos(eclong);
	double ra = atan(num / den);
	if (den < 0) ra += M_PI;
	if (den >= 0 && num < 0) ra += 2 * M_PI;
	double dec = asin(sin(oblqec) * sin(eclong));

	//# Local coordinates
	//# Greenwich mean sidereal time
	//gmst <-6.697375 + .0657098242 * time + hour
	//gmst <-gmst %% 24
	//gmst[gmst < 0] <-gmst[gmst < 0] + 24.
	double gmst = 6.697375 + .0657098242 * time + hour;
	gmst = fmod(gmst, 24.0);
	if (gmst < 0) gmst += 24.0;

	//# Local mean sidereal time
	//lmst <-gmst + long / 15.
	//lmst <-lmst %% 24.
	//lmst[lmst < 0] <-lmst[lmst < 0] + 24.
	//lmst <-lmst * 15. * deg2rad
	double lmst = gmst + longitude / 15.0;
	lmst = fmod(lmst, 24.0);
	if (lmst < 0) lmst += 24.0;
	lmst = lmst * 15.0 * M_DEGTORAD;

	//# Hour angle
	//ha <-lmst - ra
	//ha[ha < -pi] <-ha[ha < -pi] + twopi
	//ha[ha > pi] <-ha[ha > pi] - twopi
	double ha = lmst - ra;
	if (ha < -M_PI) ha += (2 * M_PI);
	if (ha > M_PI) ha -= (2 * M_PI);

	//# Latitude to radians
	//lat <-lat * deg2rad
	double latitude_R = latitude * M_DEGTORAD;

	//# Azimuth and elevation
	*elevation = asin(sin(dec) * sin(latitude_R) + cos(dec) * cos(latitude_R) * cos(ha));// <- solar zenith angle!
	*azimuth = asin(-cos(dec) * sin(ha) / cos(*elevation));

	//# For logic and names, see Spencer, J.W. 1989. Solar Energy. 42(4) : 353
	//cosAzPos <-(0 <= sin(dec) - sin(el) * sin(lat))
	//sinAzNeg <-(sin(az) < 0)
	//az[cosAzPos & sinAzNeg] <-az[cosAzPos & sinAzNeg] + twopi
	//az[!cosAzPos] <-pi - az[!cosAzPos]
	bool cosAzPos = (0 <= sin(dec) - sin(*elevation) * sin(latitude));
	bool sinAzNeg = (sin(*azimuth) < 0);
	if (cosAzPos && sinAzNeg) *azimuth += (2 * M_PI);
	if (!cosAzPos) *azimuth = M_PI - *azimuth;

//# if (0 < sin(dec) - sin(el) * sin(lat)) {
//#     if(sin(az) < 0) az <- az + twopi
//# } else {
//			#     az <-pi - az
//# }
	//el <-el / deg2rad
	//az <-az / deg2rad
	//lat <-lat / deg2rad
	*elevation = *elevation / M_DEGTORAD;
	*azimuth = *azimuth / M_DEGTORAD;

	//return(list(elevation = el, azimuth = az))
}
[/code]

And here is the second code  "General Solar Position Calculations".
[code]
	void GeneralSolarPositionCalc(float* azimuth, float *elevation, float latitude, float longitude, float timezone,
		bool daylightsaving, unsigned year, unsigned month, unsigned day, 
		float hour,	float minute = 0, float sec = 0)
	{
		year = Clamp(year, 2000, 2050);
		month = Clamp(month, 1, 12);
		day = Clamp(day, 1, 31);
		hour = Clamp(hour, 0.0f, 23.0f);
		minute = Clamp(minute, 0.0f, 59.0f);
		sec = Clamp(sec, 0.0f, 59.0f);
		latitude = Clamp(latitude, -90.0f, 90.0f);
		longitude = Clamp(longitude, -180.0f, 180.0f);

		unsigned month_days[] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 };
		for (unsigned z = 1; z < month; z++) day += month_days[z];
		//leapday
		if (year % 4 == 0 && (year % 400 == 0 || year % 100 != 0) && day >= 60 && !(month == 2 && day == 60))
			day++;
		// latitude (radian)
		float lat_rad = latitude * M_DEGTORAD;
		//fract of year (radian)
		float gamma = (day - 1.0f + (hour - 12.0f) / 24.0f) * 2.0f * M_PI / 365.0f;
		// equation of time (minutes)
		float eqtime = 229.18f * (0.000075f + 0.001868f * cos(gamma) - 0.032077f * sin(gamma)
			- 0.014615f * cos(2.0f*gamma) - 0.040849f  *sin(2.0f * gamma));
		// solar declination angle (radian)
		float decl = 0.006918f - 0.399912f * cos(gamma) + 0.070257f * sin(gamma) - 0.006758f * cos(2.0f * gamma)
			+ 0.000907f * sin(2.0f * gamma) - 0.002697f * cos(3.0f * gamma) + 0.00148f * sin(3.0f * gamma);
		if (daylightsaving) timezone++;
		float time_offset = eqtime - 4.0f * longitude + 60.0f * timezone;
		// true solar time
		float tst = hour * 60.0f + minute + sec / 60.0f + time_offset;
		//solar hour angle (degrees)
		float ha_deg = (tst / 4.0f) - 180.0f;
		//solar hour angle (radian)
		float ha_rad = ha_deg * M_DEGTORAD;
		// solar zenith angle (radian) https://en.wikipedia.org/wiki/Solar_zenith_angle
		float za_rad = acos(sin(lat_rad) * sin(decl) + cos(lat_rad) * cos(decl) * cos(ha_rad));
		*elevation = 90.0f - za_rad / M_DEGTORAD;
		// solar azimuth, clockwise from north
		float az_rad = acos( (sin(lat_rad) * cos(za_rad) - sin(decl) ) / ( cos(lat_rad) * sin(za_rad) ) );
		*azimuth = 180.0f - az_rad / M_DEGTORAD;
	}
[/code]

I not tested deeply the codes, just run a few times, but here is a site for test: [url]http://sunposition.info/sunposition/spc/locations.php#1[/url]

-------------------------

horvatha4 | 2017-01-02 01:11:34 UTC | #12

Hi Forum!
I tested the above codes. So, in the first code, the Sun make a loop at near the Horizont. In the second code the Sun goes back to "East" after reach the Zenith.
Fortunatly I found a better code at here: [url]http://www.psa.es/sdg/sunpos.htm[/url]
With this code the Sun moves mutch better on the sky. (maybe perfect?)
And the here is my test code:
[code]
#include "SunPos.h"
...
	void HandleUpdate(StringHash eventType, VariantMap& eventData)
	{
		float timeStep = eventData[Update::P_TIMESTEP].GetFloat();
                MoveCamera(timeStep);
		deltaTime_sec_ += timeStep;
		cTime ct;
		cLocation cl;
		cSunCoordinates csc;
		ct.iYear = 2016;
		ct.iMonth = 3;
		ct.iDay = 21;
		ct.dSeconds = 0;
		cl.dLatitude = 48.1206126f;
		cl.dLongitude = 21.3827353f;

		if (deltaTime_sec_ > 0.01f)
		{
			deltaTime_min_++;
			deltaTime_sec_ = 0;
			if (deltaTime_min_ > 60) { deltaTime_hour_++; deltaTime_min_ = 0; }
			if (deltaTime_hour_ > 23) { deltaTime_hour_ = 0; }
			ct.dHours = deltaTime_hour_;
			ct.dMinutes = deltaTime_min_;
			sunpos(ct, cl, &csc);
			Node *procskylightnode = scene_->GetChild("ProcSkyLight");
			Node *mylightnode = scene_->GetChild("DirectionalLight");
			if (procskylightnode && mylightnode)
			{
				mylightnode->SetRotation(Quaternion(0, 0, 0));
				mylightnode->Yaw(-csc.dAzimuth);
				mylightnode->Pitch(90-csc.dZenithAngle);
				mylightnode->Roll(0);
				procskylightnode->SetRotation(mylightnode->GetRotation());
			}
		}
	}
[/code]
Because in my World East is Vector3::RIGHT the Azimuth is negated, and because the "sunpos" function calculating the Zenith angle it subtracted from 90 for Elevation.
Happy sunniness!
Arpi

[video]https://www.youtube.com/watch?v=0rBL2Y_SF3g[/video]

-------------------------

jmiller | 2017-01-13 00:10:44 UTC | #13

Hi, and thanks Arpi and horvatha4, those are excellent additions!

-------------------------

namic | 2017-01-02 01:12:40 UTC | #14

How would you guys add clouds? Big billboarded planes randomly distributed very far from the player?

-------------------------

jmiller | 2017-01-02 01:12:40 UTC | #15

Skyrim's clouds look good and are highly compatible with older/mobile hardware. Having looked at the models, they seem to be flat tri/quad models arranged inside the skydome corresponding to various cloud types, with everything attached to and facing the camera. Real cloud textures are applied and edges could be faded with alpha textures (possibly separate). I guess the clouds are slowly moved/rotated and have new textures faded in for night, weather events, etc.

A different simple method using raymarching: [prideout.net/blog/?p=64](http://prideout.net/blog/?p=64)
There are code and links to source documents. Note this uses geometry shader capability introduced with Direct3D 10/11 and OpenGL 3.2.
*edit: Related note: some members have done some work on geometry shader support: [topic1684-10.html](http://discourse.urho3d.io/t/geometry-shaders-gl/1621/1)

And yet more sophisticated procedural clouds, this one uses 3D textures.
[guerrilla-games.com/read/th ... -zero-dawn](https://www.guerrilla-games.com/read/the-real-time-volumetric-cloudscapes-of-horizon-zero-dawn)

-------------------------

Bananaft | 2017-01-02 01:12:40 UTC | #16

[quote="namic"]How would you guys add clouds? Big billboarded planes randomly distributed very far from the player?[/quote]
That's highly depends on the type of game you are making. Do you need camera to fly between clouds, Or you need them only as a backdrop? Will you have dynamic time of day?

[quote="carnalis"]And yet more sophisticated procedural clouds, this one uses 3D textures.
[guerrilla-games.com/read/th](https://www.guerrilla-games.com/read/th) ... -zero-dawn
[/quote]
This method is still very slow for games. They end up using 1/4 resolution and updating it not in every frame.

Here is the video of GTA V where some of their cloud solutions can be clearly spotted:
[youtube.com/watch?v=197Li1LJ6kI](https://www.youtube.com/watch?v=197Li1LJ6kI)

-------------------------

namic | 2017-01-02 01:12:41 UTC | #17

Only as a backdrop for a normal FPS/FPS point of view.

-------------------------

NiteLordz | 2017-01-09 15:47:26 UTC | #18

I have got the ProcSky component to work, however, the lighting and shadows do not work properly together.

I added ProcSky to the Terrain sample, disabled the skybox creation within CreateScene and replaced with creating a ProcSky component from "scene_".  

When the sun is animated (via the SunPos.h), the boxes are lit when the sun is not "shown" and as it the sun rises, the shadows are reversed.

Any suggestions please

-------------------------

SirNate0 | 2017-01-09 19:42:47 UTC | #19

Negate the direction of the vector from the SunPos.h calculation to fix the backwards shadows and manually change the color of the light so that it does not illuminate when the sun is below the horizon (e.g. SetColor(Color::BLACK) or disable the light then). 

If by the shadows are reversed you mean that west is east, for example, negate the corresponding vector component (e.g. direction.x_ *= -1;)

-------------------------

NiteLordz | 2017-01-09 22:52:32 UTC | #20

I am not following what you mean.  The shadows on the boxes are on the same side as the sun, instead of behind them. 

    void Landscape::HandleUpdate(StringHash eventType, VariantMap& eventData) {
	using namespace Update;

	// Take the frame time step, which is stored as a float
	float timeStep = eventData[P_TIMESTEP].GetFloat();

	// Move the camera, scale movement with time step
	MoveCamera(timeStep);

	cTime ct;
	cLocation cl;
	cSunCoordinates csc;

	ct.iYear = 2016;
	ct.iMonth = 3;
	ct.iDay = 21;
	ct.dSeconds = 0;
	cl.dLatitude = 48.1206126f;
	cl.dLongitude = 21.3827353f;

	deltaTime_sec_ += timeStep;

	if (deltaTime_sec_ > 0.01f) {
		deltaTime_min_++;
		deltaTime_sec_ = 0;
		if (deltaTime_min_ > 60) { deltaTime_hour_++; deltaTime_min_ = 0; }
		if (deltaTime_hour_ > 23) { deltaTime_hour_ = 0; }
		ct.dHours = deltaTime_hour_;
		ct.dMinutes = deltaTime_min_;
		GetSunPosition(ct, cl, &csc);

		Node* procskylightnode = scene_->GetChild("ProcSkyLight");
		Node* mylightnode = scene_->GetChild("DirectionalLight");

		if (procskylightnode && mylightnode) {
			mylightnode->SetRotation(Quaternion(0, 0, 0));
			mylightnode->Yaw(-csc.dAzimuth);
			mylightnode->Pitch(90 - csc.dZenithAngle);
			mylightnode->Roll(0);
			procskylightnode->SetRotation(mylightnode->GetRotation());
		}
	}
}

The values are already negated from the above post, however, modifying either or both of those values, does not fix the issue.  

Note: This is in Direct3D (HLSL), have not tested OpenGL yet.

Thanks much

-------------------------

SirNate0 | 2017-01-12 18:45:06 UTC | #21

Try using Yaw(180-csc.dAzimuth) and Pitch (270-csc.dZenithAngle). I use LookAt to set the direction, that's why I was saying to negate the vector.

-------------------------

vivienneanthony | 2017-01-31 19:28:06 UTC | #22

Is this a github fork with this update on it? not sure if it's in 1.6

-------------------------

dev4fun | 2018-04-20 06:21:34 UTC | #23

Someone already tried to implement clouds on this?
Something simple like this: https://www.researchgate.net/publication/220982572_Clouds_and_stars_efficient_real-time_procedural_sky_rendering_using_3D_hardware

-------------------------

