beldiv | 2018-02-15 11:30:12 UTC | #1

I register 2 custom components in category “MY-COMPONENTS”, they have as predecessor class “Urho3D::LogicComponent”, as in tutorial:http://urho3d.wikia.com/wiki/Creating_your_own_C%2B%2B_components, but in editor they have name LogicComponent, when I expected my names (MySecondComponent,MyFirstComponent).
[spoiler]![image|620x320](upload://qHggFJYhcZCT06fF4QVfLzOkq6U.png)[/spoiler]
My sources:

[spoiler]
[i]MyCxxComponents.hh[/i] :
[code=c++]
#pragma once
#include <functional>
#include <Urho3D/Urho3D.h>
#include <Urho3D/Scene/LogicComponent.h>
#include <Urho3D/AngelScript/APITemplates.h> 

extern  const char *  CATEGORY_MY_COMPONENTS;

typedef  std::function<void(Urho3D::Context*context)>  reg_t;
Urho3D::Vector<reg_t>   &  get_autoregistators();

#define CXX_COMPONENT(T) \
        struct T; \
        static char const  autoreg_character_name=[](){   get_autoregistators().Push( [](Urho3D::Context*context){  context->RegisterFactory<T>(CATEGORY_MY_COMPONENTS);  } );  return 'Y'; }(); \
        struct T : Urho3D::LogicComponent \
        {   OBJECT(T); \
            T( Urho3D::Context* context ) : Urho3D::LogicComponent(context)
[/code]

[i]MyCxxComponents.cc[/i] :
[code]
#include "MyCxxComponents.hh"

const char *  CATEGORY_MY_COMPONENTS = "MY-COMPONENTS";

Urho3D::Vector<reg_t>   &  get_autoregistators()
{   static  Urho3D::Vector<reg_t>   singleton;
    return  singleton;
}

extern "C"
{   extern void cxx_components_loader_entry_point( Urho3D::Context* context )
    {   for( reg_t const & reg : get_autoregistators() )
             reg( context );
    }
}
[/code]

[i]MyFirstComponent.cc[/i] :
[code]
#include "MyCxxComponents.hh"
CXX_COMPONENT( MyFirstComponent )
    {} // ctor
    void Start() override
    {}
};
[/code]

[i]MySecondComponent.cc[/i] :
[code]
#include "MyCxxComponents.hh"
CXX_COMPONENT( MySecondComponent)
    {} // ctor
    void Start() override
    {}
};
[/code]

[/spoiler]

-------------------------

Eugene | 2018-02-15 12:49:25 UTC | #2

Every object should be registered via `URHO3D_OBJECT` macro, at least in latest versions of Urho.

[quote="beldiv, post:1, topic:4020"]
as in tutorial
[/quote]

This Wiki is quite dead, I think.

-------------------------

Modanung | 2018-02-15 19:09:06 UTC | #4

Official wiki is located mjer:
https://github.com/urho3d/Urho3D/wiki

And welcome to the forums! :confetti_ball:

-------------------------

