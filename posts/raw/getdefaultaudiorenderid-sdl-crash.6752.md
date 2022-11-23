glebedev | 2021-03-10 07:04:10 UTC | #1

When waking up from hibernation sometimes application crashes:

| |Urho3D.dll!__abi_WinRTraiseException(long __hrArg) Line 1132|C++|
|---|---|---|
| |[Inline Frame] Urho3D.dll!__abi_ThrowIfFailed(long) Line 100|C++|
|>|Urho3D.dll!WASAPI_ActivateDevice(SDL_AudioDevice * _this, const SDL_bool isrecovery) Line 207|C++|
| |Urho3D.dll!RecoverWasapiDevice(SDL_AudioDevice * this) Line 252|C|
| |Urho3D.dll!WASAPI_WaitDevice(SDL_AudioDevice * this) Line 314|C|
| |Urho3D.dll!SDL_RunAudio(void * devicep) Line 758|C|
| |Urho3D.dll!SDL_RunThread(void * data) Line 283|C|
| |Urho3D.dll!RunThread(void * data) Line 91|C|

At Source\ThirdParty\SDL\src\audio\wasapi\SDL_wasapi_winrt.cpp:

	int
	WASAPI_ActivateDevice(_THIS, const SDL_bool isrecovery)
	{
		LPCWSTR devid = _this->hidden->devid;
		Platform::String^ defdevid;

		if (devid == nullptr) {
			defdevid = _this->iscapture ? MediaDevice::GetDefaultAudioCaptureId(AudioDeviceRole::Default) : MediaDevice::GetDefaultAudioRenderId(AudioDeviceRole::Default);

It looks like the error is RO_E_CLOSED

	case 0x80000013L: // RO_E_CLOSED
		__abi_WinRTraiseObjectDisposedException();

-------------------------

