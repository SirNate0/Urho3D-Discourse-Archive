INait1 | 2017-01-22 13:40:25 UTC | #1

It all compiles fine, but linker got errors

Undefined symbols for architecture x86_64:
  "_AudioQueueAllocateBuffer", referenced from:
      _prepare_audioqueue in libUrho3D.a(SDL_coreaudio.m.o)
  "_AudioQueueDispose", referenced from:
      _COREAUDIO_CloseDevice in libUrho3D.a(SDL_coreaudio.m.o)
  "_AudioQueueEnqueueBuffer", referenced from:
      _prepare_audioqueue in libUrho3D.a(SDL_coreaudio.m.o)
      _inputCallback in libUrho3D.a(SDL_coreaudio.m.o)
      _outputCallback in libUrho3D.a(SDL_coreaudio.m.o)
  "_AudioQueueFreeBuffer", referenced from:
      _COREAUDIO_CloseDevice in libUrho3D.a(SDL_coreaudio.m.o)
  "_AudioQueueNewInput", referenced from:
      _prepare_audioqueue in libUrho3D.a(SDL_coreaudio.m.o)
  "_AudioQueueNewOutput", referenced from:
      _prepare_audioqueue in libUrho3D.a(SDL_coreaudio.m.o)
  "_AudioQueueSetProperty", referenced from:
      _prepare_audioqueue in libUrho3D.a(SDL_coreaudio.m.o)
  "_AudioQueueStart", referenced from:
      _prepare_audioqueue in libUrho3D.a(SDL_coreaudio.m.o)
  "_AudioQueueStop", referenced from:
      _audioqueue_thread in libUrho3D.a(SDL_coreaudio.m.o)

What can be wrong with coreaudio? Linker text has -framework coreaudio enabled.

-------------------------

Virgo | 2018-08-22 13:20:48 UTC | #2

:sweat_smile:not a Mac user, just a guess: link framework AudioToolBox

-------------------------

