Sir_Nate | 2017-01-02 01:11:47 UTC | #1

Using (evile black magic) preprocessor programming (sorcery) and the autowrapper addon to AngelScript, I believe I have successfully made AngelScript work on an Emscripten build. I'm not certain it fully works, as my project has other problems that cause the Emscripten build to crash (that I'm pretty sure are unrelated), but I was at least able to Print a message from AngelScript.

Code and such (i.e. modified CMake module), and possibly a pull request, will be forth coming, but for those who are impatient, these are the important parts:
* there were 2 or 3 macros that needed to be changed in the Urho Library dealing with message handling and exception handling -- they can use the original AngelScript macros, which have been duplicated prefixed with an underscore in my file (i.e. _asFUNCTION(fn))
* Requires c++11 support (one of the things that had to be changed in the CMake
* Uses BOOST Preprocessor for some macro stuff, but in theory it should be completely replaceable

[code]
//angelscript.h
//at top
#ifdef EMSCRIPTEN
#define AS_MAX_PORTABILITY
#endif
...
//at bottom of file, to overwrite the macros defined above
END_AS_NAMESPACE
#ifndef URHO_PROJECT_BUILD // you need to define this for building the Angelscript library within the Urho build, but not when building Urho itself
#include "mine.h"
#endif
[/code]

[code]
//mine.hpp -- where the evil sorcery happens. Not all of these macros work, I'm pretty sure (especially some of the behavior ones), but there are no compilation errors when building Urho, and any fixes should be trivial
#ifdef EMSCRIPTEN
#include "wrap16.h"
//can help solve potential ... problems if we need it at the start: http://stackoverflow.com/questions/3046889/optional-parameters-with-c-macros
#define asFUNCTION(f) F, f

#define _asFUNCTION(f) asFunctionPtr(f)
//#define asMETHOD(cls, f) cls, M, f
#define asMETHOD(cls, f) M, (cls,f) //package class and function for UNWRAPping later
#define UNWRAP(x,y) x,y// try -fmacro-backtrace-limit=0 on compile
#define _asMETHOD(c,m) asSMethodPtr<sizeof(void (c::*)())>::Convert((void (c::*)())(&c::m))
#define RegisterGlobalFunction(...) RegGlobalIndirect(__VA_ARGS__)
#define RegGlobalIndirect(decl, F, func, kind) RegisterGlobalFunction##F##kind (decl,func) // ... = decl or it = decl, cls for asCall_ThisCall
#define RegisterGlobalFunctionFasCALL_CDECL(decl,fun) RegisterGlobalFunction(decl, WRAP_FN(fun), asCALL_GENERIC); //assert(r >= 0);
#define RegisterGlobalFunctionFasCALL_STDCALL(decl,fun) RegisterGlobalFunction(decl, WRAP_FN(fun), asCALL_GENERIC); //assert(r >= 0);
#define RegisterGlobalFunctionMasCALL_THISCALL_ASGLOBAL(decl,fun) RegisterGlobalFunctionMasCALL_THISCALL_ASGLOBAL_2(decl,UNWRAP fun)
#define RegisterGlobalFunctionMasCALL_THISCALL_ASGLOBAL_2(decl, ...) RegisterGlobalFunction(decl, WRAP_MFN(__VA_ARGS__), asCALL_GENERIC); //assert(r >= 0);
#define RegisterGlobalFunctionFasCALL_GENERIC(decl,fun) RegisterGlobalFunction(decl, asFunctionPtr(fun), asCALL_GENERIC); //assert(r >= 0);

//object indirects
#define RegisterObjectMethod(...) RegObjectMethodIndirect(__VA_ARGS__)
//#define RegObjectIndirect(clsdcl,decl, F, func, kind) RegObjectIndirect_2(clsdcl,decl, F, UNWRAP func, kind)
#define RegObjectMethodIndirect(clsdcl,decl, F, clsfunc, kind) RegisterObjectMethod##F##kind (clsdcl,decl,clsfunc) // ... = decl or it = decl, cls for asCall_ThisCall
#define RegisterObjectMethodMasCALL_THISCALL(clsdcl,decl,clsfunc) RegisterObjectMethodMasCALL_THISCALL_2(clsdcl,decl,UNWRAP clsfunc)
#define RegisterObjectMethodMasCALL_THISCALL_2(clsdcl,decl,...) RegisterObjectMethodMasCALL_THISCALL_3(clsdcl,decl, WRAP_MFN(__VA_ARGS__));
#define RegisterObjectMethodMasCALL_THISCALL_3(clsdcl,decl,fn) RegisterObjectMethod(clsdcl,decl, fn, asCALL_GENERIC); //assert(r >= 0);
#define RegisterObjectMethodFasCALL_CDECL_OBJLAST(clsdcl,decl,fun) RegisterObjectMethod(clsdcl,decl, WRAP_OBJ_LAST(fun), asCALL_GENERIC); //assert(r >= 0);
#define RegisterObjectMethodFasCALL_CDECL_OBJFIRST(clsdcl,decl,fun) RegisterObjectMethod(clsdcl,decl, WRAP_OBJ_FIRST(fun), asCALL_GENERIC); //assert(r >= 0);
//#define RegisterObjectMethodMasCALL_CDECL_OBJECTFIRST(decl,cls,fun) RegisterObjectMethodMasCALL_THISCALL_ASGLOBAL_2(decl,UNWRAP fun)
//#define RegisterObjectMethodMasCALL_THISCALL_ASGLOBAL_2(decl, ...) RegisterObjectMethod(decl, WRAP_MFN(__VA_ARGS__), asCALL_GENERIC); //assert(r >= 0);
#define RegisterObjectMethodFasCALL_GENERIC(clsdcl,decl,fun) RegisterObjectMethod(clsdcl,decl, asMethodPtr(fun), asCALL_GENERIC); //assert(r >= 0);

////note:unfortunately, the WrapCon methods are for creating the constructor wrapper, which typically seems to be done anyways, so we should just handle it like Register Object Method with 1 extra parameter
//#define RegisterObjectBehaviour(...) RegObjectBehaviorIndirect(__VA__ARGS__)
//#define RegObjectBehaviorIndirect(clsdcl,behavior,decl,fn,kind) RegisterObjectBehavior##behavior(clsdcl,behavior,decl,fn,kind)
//#define RegisterObjectBehaviorasBEHAVE_CONSTRUCT(clsdcl,behavior,decl,fn,kind) RegisterObjectConstructor##F##kind (clsdcl,behavior,decl,fn)
//#define RegisterObjectConstructorFasCALL_CDECL_OBJECTLAST(clsdcl,behavior,decl,fn) RegisterObjectBehavior(clsdcl,behavior,decl,WRAP_OBJ_LAST(fn),asCALL_GENERIC)
////RegisterObjectConstructorF##kind (clsdcl,decl,clsfunc)

//NOTE: Angelscript uses the British English spelling __iour!
#define RegisterObjectBehaviour(...) RegObjectBehaviorIndirect(__VA_ARGS__)
//#define RegObjectIndirect(clsdcl,behavior,decl, F, func, kind) RegObjectIndirect_2(clsdcl,behavior,decl, F, UNWRAP func, kind)
#define RegObjectBehaviorIndirect(clsdcl,behavior,decl, F, clsfunc, kind) RegisterObjectBehavior##F##kind (clsdcl,behavior,decl,clsfunc) // ... = decl or it = decl, cls for asCall_ThisCall
#define RegisterObjectBehaviorMasCALL_THISCALL(clsdcl,behavior,decl,clsfunc) RegisterObjectBehaviorMasCALL_THISCALL_2(clsdcl,behavior,decl,UNWRAP clsfunc)
#define RegisterObjectBehaviorMasCALL_THISCALL_2(clsdcl,behavior,decl,...) RegisterObjectBehaviour(clsdcl,behavior,decl, WRAP_MFN(__VA_ARGS__), asCALL_GENERIC); //assert(r >= 0);
#define RegisterObjectBehaviorFasCALL_CDECL_OBJLAST(clsdcl,behavior,decl,...) RegisterObjectBehaviour(clsdcl,behavior,decl, WRAP_OBJ_LAST(__VA_ARGS__), asCALL_GENERIC); //assert(r >= 0);
#define RegisterObjectBehaviorFasCALL_CDECL_OBJFIRST(clsdcl,behavior,decl,...) RegisterObjectBehaviour(clsdcl,behavior,decl, WRAP_OBJ_FIRST(__VA_ARGS__), asCALL_GENERIC); //assert(r >= 0);
//#define RegisterObjectBehaviorMasCALL_CDECL_OBJECTFIRST(decl,cls,fun) RegisterObjectBehaviorMasCALL_THISCALL_ASGLOBAL_2(decl,UNWRAP fun)
//#define RegisterObjectBehaviorMasCALL_THISCALL_ASGLOBAL_2(decl, ...) RegisterObjectBehavior(decl, WRAP_MFN(__VA_ARGS__), asCALL_GENERIC); //assert(r >= 0);
#define RegisterObjectBehaviorFasCALL_CDECL(clsdcl,behavior,decl,...) RegisterObjectBehaviour(clsdcl,behavior,decl, WRAP_FN(__VA_ARGS__),asCALL_GENERIC);
#define RegisterObjectBehaviorFasCALL_GENERIC(clsdcl,behavior,decl,fun) RegisterObjectBehaviour(clsdcl,behavior,decl, asFunctionPtr(fun), asCALL_GENERIC); //assert(r >= 0);

//Parameter-Return versions:

#define asFUNCTIONPR(f,p,r) FPR, (f,p,r)
#define UNWRAP3(x,y,z) x,y,z
#define UNWRAP4(x,y,z,w) x,y,z,w
#define asMETHODPR(cls,f,p,r) MPR, (cls,f,p,r)
#if (defined(_MSC_VER) && _MSC_VER <= 1200) || (defined(__BORLANDC__) && __BORLANDC__ < 0x590)
// MSVC 6 has a bug that prevents it from properly compiling using the correct asFUNCTIONPR with operator >
// so we need to use ordinary C style cast instead of static_cast. The drawback is that the compiler can't
// check that the cast is really valid.
// BCC v5.8 (C++Builder 2006) and earlier have a similar bug which forces us to fall back to a C-style cast.
#define _asFUNCTIONPR(f,p,r) asFunctionPtr((void (*)())((r (*)p)(f)))
#elif (defined(_MSC_VER) && _MSC_VER >= 1900)
// Urho3D: VS2015 does not compile the C-style cast of the function pointer
#define _asFUNCTIONPR(f,p,r) asFunctionPtr(reinterpret_cast<void (*)()>(static_cast<r (*)p>(f)))
#else
#define _asFUNCTIONPR(f,p,r) asFunctionPtr((void (*)())(static_cast<r (*)p>(f)))
#endif
#define _asMETHODPR(c,m,p,r) asSMethodPtr<sizeof(void (c::*)())>::Convert(AS_METHOD_AMBIGUITY_CAST(r (c::*)p)(&c::m))


#define RegisterGlobalFunctionFPRasCALL_CDECL(decl,fun) RegisterGlobalFunctionFPRasCALL_CDECL_2(decl, UNWRAP3 fun);
#define RegisterGlobalFunctionFPRasCALL_CDECL_2(decl,...) RegisterGlobalFunction(decl, WRAP_FN_PR(__VA_ARGS__), asCALL_GENERIC);
#define RegisterGlobalFunctionFPRasCALL_STDCALL(decl,fun) RegisterGlobalFunctionFPRasCALL_STDCALL_2(decl, UNWRAP3 fun);
#define RegisterGlobalFunctionFPRasCALL_STDCALL_2(decl,...) RegisterGlobalFunction(decl, WRAP_FN_PR(__VA_ARGS__), asCALL_GENERIC);
#define RegisterGlobalFunctionMPRasCALL_THISCALL_ASGLOBAL(decl,fun) RegisterGlobalFunctionMasCALL_THISCALL_ASGLOBAL_2(decl,UNWRAP4 fun)
#define RegisterGlobalFunctionMPRasCALL_THISCALL_ASGLOBAL_2(decl, ...) RegisterGlobalFunction(decl, WRAP_MFN_PR(__VA_ARGS__), asCALL_GENERIC);
#define RegisterGlobalFunctionFPRasCALL_GENERIC(decl,fun) RegisterGlobalFunctionFPRasCALL_GENERIC_2(decl, UNWRAP3 fun);
#define RegisterGlobalFunctionFPRasCALL_GENERIC_2(decl,...) RegisterGlobalFunction(decl, _asFUNCTIONPR(__VA_ARGS__), asCALL_GENERIC);

#define RegisterObjectMethodMPRasCALL_THISCALL(clsdcl,decl,clsfunc) RegisterObjectMethodMPRasCALL_THISCALL_2(clsdcl,decl,UNWRAP4 clsfunc)
#define RegisterObjectMethodMPRasCALL_THISCALL_2(clsdcl,decl,...) RegisterObjectMethod(clsdcl,decl, WRAP_MFN_PR(__VA_ARGS__), asCALL_GENERIC);
#define RegisterObjectMethodFPRasCALL_CDECL_OBJLAST(clsdcl,decl,fun) RegisterObjectMethodFPRasCALL_CDECL_OBJLAST_2(clsdcl,decl, UNWRAP3 fun);
#define RegisterObjectMethodFPRasCALL_CDECL_OBJLAST_2(clsdcl,decl,...) RegisterObjectMethod(clsdcl,decl, WRAP_OBJ_LAST_PR(__VA_ARGS__), asCALL_GENERIC);
#define RegisterObjectMethodFPRasCALL_CDECL_OBJFIRST(clsdcl,decl,fun) RegisterObjectMethodFPRasCALL_CDECL_OBJFIRST_2(clsdcl,decl, UNWRAP3 fun);
#define RegisterObjectMethodFPRasCALL_CDECL_OBJFIRST_2(clsdcl,decl,...) RegisterObjectMethod(clsdcl,decl, WRAP_OBJ_FIRST_PR(__VA_ARGS__), asCALL_GENERIC);
#define RegisterObjectMethodFPRasCALL_GENERIC(clsdcl,decl,fun) RegisterObjectMethodFPRasCALL_GENERIC_2(clsdcl,decl, UNWRAP3 fun);
#define RegisterObjectMethodFPRasCALL_GENERIC_2(clsdcl,decl,...) RegisterObjectMethod(clsdcl,decl, _asFUNCTIONPR(__VA_ARGS__), asCALL_GENERIC);

#define RegisterObjectBehaviorMPRasCALL_THISCALL(clsdcl,behavior,decl,clsfunc) RegisterObjectBehaviorMPRasCALL_THISCALL_2(clsdcl,behavior,decl,UNWRAP4 clsfunc)
#define RegisterObjectBehaviorMPRasCALL_THISCALL_2(clsdcl,behavior,decl,...) RegisterObjectBehaviour(clsdcl,behavior,decl, WRAP_MFN_PR(__VA_ARGS__), asCALL_GENERIC);
#define RegisterObjectBehaviorFPRasCALL_CDECL_OBJLAST(clsdcl,behavior,decl,clsfunc) RegisterObjectBehaviour(clsdcl,behavior,decl, WRAP_OBJ_LAST_PR clsfunc, asCALL_GENERIC);
#define RegisterObjectBehaviorFPRasCALL_CDECL_OBJFIRST(clsdcl,behavior,decl,...) RegisterObjectBehaviour(clsdcl,behavior,decl, WRAP_OBJ_FIRST_PR(__VA_ARGS__), asCALL_GENERIC);
#define RegisterObjectBehaviorFPRasCALL_GENERIC(clsdcl,behavior,decl,...) RegisterObjectBehaviour(clsdcl,behavior,decl, _asFUNCTIONPR(__VA_ARGS__), asCALL_GENERIC);
#define RegisterObjectBehaviorFPRasCALL_CDECL(clsdcl,behavior,decl,clsfunc) RegisterObjectBehaviour(clsdcl,behavior,decl, WRAP_FN_PR clsfunc, asCALL_GENERIC);

#define RegisterStringFactory(...) EV(RegisterStringFactory_2(__VA_ARGS__))
#define RegisterStringFactory_2(str,F,params,kind) RegisterStringFactory(str, WRAP_FN (params), asCALL_GENERIC);

/*#define SetExceptionCallback(...) SetExceptionCallback_2(__VA_ARGS__)
#define SetExceptionCallback_2(M,params,obj,kind) SetExceptionCallback(WRAP_MFN params, obj, asCALL_GENERIC);

#define SetMessageCallback(...) SetMessageCallback_2(__VA_ARGS__)
#define SetMessageCallback_2(M,params,obj,kind) SetMessageCallback(WRAP_MFN params, obj, asCALL_GENERIC);
*/

#endif
[/code]

[code]
//wrap16.h -- the file generated by the angelscript autowrapper addon that supports 16 parameter arguments (because of Matrix4x4)
//I believe the only changes to the generate file were adding the "wrap.h" include and commenting out the WRAP_MFN_PR macro
...
} // end namespace gw

#include "wrap.h"

#endif
[/code]

[code]
/*
 * wrap.h -- this file contains my replacement of the WRAP_MFN_PR macro, which failed to compile due to complaints about template argument deduction or some such
 * It requires c++11 for the lambdas, and it requires no-argument functions to be given as () and not (void) (I believe there was a single case of this in the Urho library)
 *
 *  Created on: Apr 6, 2016
 *      Author: SirNate0
 */

#pragma once
#include <type_traits>
//#include "AngelScript/angelscript.h"
#include "angelscript.h"
#include <boost/preprocessor.hpp>



//Return void enable if: http://stackoverflow.com/questions/12002447/template-method-enable-if-specialization
//# do with // http://stackoverflow.com/questions/5588855/standard-alternative-to-gccs-va-args-trick


#define EV(...) __VA_ARGS__

//inline asSFuncPtr asFunctionPtr<asGENFUNC_t>(asGENFUNC_t func)
//{
//	// Mark this as a generic function
//	asSFuncPtr p(1);
//	p.ptr.f.func = reinterpret_cast<asFUNCTION_t>(func);
//	return p;
//}
typedef void (*asGENFUNC_t)(asIScriptGeneric *);


//#define DO_2(_,a,b) GET(a,0), GET(b,1)//Proxy<a>::cast(gen->arguments[0])
//#define DO_4(_,a,b,c,d) GET(a,0), GET(b,1),GET(c,2), GET(d,3)//(a*)(gen->arguments[0]),(b*)(gen->arguments[1]),(a*)(gen->arguments[2]),(b*)(gen->arguments[3])
//#define DO_6(_,a,b,c,d,e,f) GET(a,0), GET(b,1),GET(c,2), GET(d,3),GET(e,4), GET(f,5)//(a*)(gen->arguments[0]),(b*)(gen->arguments[1]),(a*)(gen->arguments[2]),(b*)(gen->arguments[3]),(a*)(gen->arguments[4]),(b*)(gen->arguments[5])
//
////#define DO_1(_,a) static_cast<Proxy <a> *>(gen->arguments[0])->value
//#define DO_1(_,a) Proxy<a>::cast(gen->arguments[0])
//#define DO_3(_,a,b,c) GET(a,0), GET(b,1),GET(c,2)
//#define DO_5(_,a,b,c,d,e) GET(a,0), GET(b,1),GET(c,2), GET(d,3),GET(e,4)
//
//#define DO_0(_)
//
//#define GET7TH(_,arg1, arg2, arg3, arg4, arg5, arg6, arg7,...) arg7
//#define DO_CHOOSER(...) GET7TH(__VA_ARGS__,DO_6,DO_5,DO_4,DO_3,DO_2,DO_1,DO_0)
//
//#define DO(...) DO_CHOOSER(_,##__VA_ARGS__)(_,##__VA_ARGS__)
//
//#define CHOOSE(...)


#define UNWRAP(...) __VA_ARGS__
#define EXTRACT_CONST(...) (__VA_ARGS__),
// from http://stackoverflow.com/questions/18851889/boost-preprocessor-skip-if-variadic-is-empty


// based on the: http://gustedt.wordpress.com/2010/06/08/detect-empty-macro-arguments
#define __ARG16(_0, _1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11, _12, _13, _14, _15, ...) _15
#define __HAS_COMMA(...) __ARG16(__VA_ARGS__, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0)
#define __TRIGGER_PARENTHESIS_(...) ,
#define __PASTE5(_0, _1, _2, _3, _4) _0 ## _1 ## _2 ## _3 ## _4
#define __IS_EMPTY_CASE_0001 ,
#define __IS_EMPTY(_0, _1, _2, _3) __HAS_COMMA(__PASTE5(__IS_EMPTY_CASE_, _0, _1, _2, _3))

#define TUPLE_IS_EMPTY(...) \
    __IS_EMPTY( \
        /* test if there is just one argument, eventually an empty one */ \
        __HAS_COMMA(__VA_ARGS__), \
        /* test if _TRIGGER_PARENTHESIS_ together with the argument adds a comma */ \
        __HAS_COMMA(__TRIGGER_PARENTHESIS_ __VA_ARGS__),                 \
        /* test if the argument together with a parenthesis adds a comma */ \
        __HAS_COMMA(__VA_ARGS__ (/*empty*/)), \
        /* test if placing it between _TRIGGER_PARENTHESIS_ and the parenthesis adds a comma */ \
        __HAS_COMMA(__TRIGGER_PARENTHESIS_ __VA_ARGS__ (/*empty*/)) \
    )

#define __GEN_EMPTY_ARGS(...)

#define __GEN_NONEMPTY_ARGS_CB(unused, data, idx, elem) \
	, static_cast<gw::Proxy <elem> *>(gen->GetAddressOfArg(idx))->value
//	, Proxy<elem>::cast(gen->arguments[idx])

#define __GEN_NONEMPTY_ARGS(seq) \
    BOOST_PP_SEQ_FOR_EACH_I( \
         __GEN_NONEMPTY_ARGS_CB \
        ,~ \
        ,seq \
    )



#define CreateGenericFromMethod_2(...) EV(CreateGenericFromMethod_3(__VA_ARGS__))
#define CreateGenericFromMethod_3(class_t,method,parameters,const,return_t) \
asFunctionPtr<asGENFUNC_t>([] (asIScriptGeneric* gen) {\
		BOOST_PP_CAT(wrap::call,const) <return_t,class_t BOOST_PP_COMMA_IF(BOOST_PP_IF(TUPLE_IS_EMPTY parameters ,0,1)) EV parameters>\
				(gen,/*&(Proxy<class_t>::cast(gen->GetObject()))*/((class_t*)gen->GetObject()), static_cast<return_t (class_t::*) parameters const>(&class_t::method)\
					BOOST_PP_IF( \
						 TUPLE_IS_EMPTY parameters \
						,__GEN_EMPTY_ARGS \
						,__GEN_NONEMPTY_ARGS \
					)(BOOST_PP_TUPLE_TO_SEQ( parameters )) \
				);\
})

#define WRAP_MFN_PR(class_t,method,parameters,return_t) EV(EV(EV(CreateGenericFromMethod_2(class_t,method,EXTRACT_CONST parameters,return_t))))

//typedef asIScriptGeneric Gen;

namespace wrap
{
template<class R, class C, typename ...P>
void call_helper(::std::false_type, asIScriptGeneric*g, C*obj, R (C::*fn)(P...), P... args)
{
//	cout << "do non-void";
//	g->return_value = new R ((obj->*fn)(args...));
	new (g->GetAddressOfReturnLocation()) gw::Proxy<R> ((obj->*fn)(args...));
}

template<class R, class C, typename ...P>
void call_helper(::std::true_type,asIScriptGeneric*g, C*obj, R (C::*fn)(P...), P... args)
{
//	cout << "do void";
	(obj->*fn)(args...);
//	g->return_value = nullptr;

}
template<class R, class C, typename ...P>
void call_helper(::std::false_type, asIScriptGeneric*g, C*obj, R (C::*fn)(P...)const, P... args)
{
//	cout << "do non-void const";
//	g->return_value = new R ((obj->*fn)(args...));
	new (g->GetAddressOfReturnLocation()) gw::Proxy<R> ((obj->*fn)(args...));
}

template<class R, class C, typename ...P>
void call_helper(::std::true_type,asIScriptGeneric*g, C*obj, R (C::*fn)(P...)const, P... args)
{
//	cout << "do void const";
	(obj->*fn)(args...);
//	g->return_value = nullptr;

}
template<class R, class C, typename ...P>
void call(asIScriptGeneric*g, C*obj, R (C::*fn)(P...), P... args)
{
	call_helper<R,C,P...>(::std::is_void<R>(),
			g,
			obj,
			fn,
			args...);
}
template<class R, class C, typename ...P>
void callconst(asIScriptGeneric*g, C*obj, R (C::*fn)(P...)const, P... args)
{
	call_helper<R,C,P...>(std::is_void<R>(),
			g,
			obj,
			fn,
			args...);
}
}


[/code]

-------------------------

hdunderscore | 2017-01-02 01:11:47 UTC | #2

Very cool ! Great use of evile black magic in the way of great justice !

I had given in to the dark side and started a project in lua because I didn't expect to see emscripten angelscript support any time soon :O

-------------------------

cadaver | 2017-01-02 01:11:47 UTC | #3

Excellent! In general Urho should not require C++11 or Boost, but as it only affects Emscripten build it should be acceptable. Depending on the number of Boost headers needed it may be preferable to download Boost as part of the build, rather than include them directly in the repo like the other third-party libraries are included.

-------------------------

weitjong | 2017-01-02 01:11:47 UTC | #4

Interesting! Have you measured how is the performance after converting all those native calling conventions to generic calling conventions? Just for a gauge, it would be also interesting to quickly know how much work is still needed by test running all the AngelScript scripted samples, although those samples may not have used all the available calling convention conversion macros.

I don't want to steal the thunder but I once took a different approach to tackle this because I think using generic calling conventions could be slow under normal circumstances, not to mention now all these calls would be cross-compiled again to JS. I actually did not have any number to back this and hence my question above.

-------------------------

hdunderscore | 2017-01-02 01:11:57 UTC | #5

I hope you are still working on the PR for this :smiley:

-------------------------

Sir_Nate | 2017-01-02 01:12:00 UTC | #6

I do still intend it, though it's taking longer than expected. Currently there's a strange error -- it does not seem to be adding the reference to the objects, though it does remove them. For example, in running Ninja Snow War, it fails in the Audio Init because it removes a reference to the Audio the first time the audio variable is used, and, based on breakpoints on the lambda functions that are registered with the script engine, it never called an AddRef to match, leading to the destruction of the Audio subsystem (though Angelscript thinks it still exists) and then a segfault at the next audio line. (I can catch the RemoveRef lambda with a break point, so I think it is fair to say that AddRef is never called).

Any ideas?

-------------------------

cadaver | 2017-01-02 01:12:00 UTC | #7

Could this be related to the auto handles "@+" used in the bindings? Are these supported in the generic convention?

-------------------------

Sir_Nate | 2017-01-02 01:12:01 UTC | #8

That may be it. From the AS documentation ([url]http://www.angelcode.com/angelscript/sdk/docs/manual/doc_obj_handle.html[/url]): 
[quote]The auto handles does not affect the behaviour of the handles when the generic calling convention is used. [/quote]
Any ideas about how to deal with it (aside from changing AngelScript to support them with the Generic calling convention, which should mostly just require moving some stuff from the non-generic PrepareSystemFunction to PrepareSystemFunctionGeneric dealing with the autohandles)? Do you know if there is a way to determine if a parameter or return type is an auto-handle from asIScriptGeneric?

It looks like asCScriptFunction contains the needed information, storing a pointer to the asSSystemFunctionInterface that has an array of bools for autohandles, but that would require a cast and further header includes, and it may be easier to just modify the PrepareSystemFunctionGeneric at that point, unless you can think of something better. Though it is important to see if the builder actually fills that data if it is given a generic system function...

-------------------------

cadaver | 2017-01-02 01:12:01 UTC | #9

The laborious but certain solution would be to change all of our bindings to not use auto handles. Basically incrementing and decrementing the refcounts ourselves. However that would require creating a wrapper function for almost all functions dealing with pointers, to which the generic convention wrapper would be layered on top of (= worse performance.) AngelScript modification sounds like the more attractive way to go. I'm not familiar with the implementation details so can't help you.

-------------------------

Sir_Nate | 2017-01-02 01:12:35 UTC | #10

I believe I've gotten it to work, though I've only tested it with the 12_PhysicsStressTest.as code, so there may still be (potentially very major) bugs.
It can be found at [url]https://github.com/SirNate0/Urho3D[/url] for now, and a pull request should be forthcoming, but I still need to fix some of the code so that it complies with the style (and works in the normal build case - 3 macro calls currently will not work because they have an _ prefixed).

Edit:
Pull Request: [url]https://github.com/urho3d/Urho3D/pull/1399[/url]

For any who are interested, the solution to the autohandles problem was from here: [url]http://www.gamedev.net/topic/630414-autohandles-with-generic-callconv/[/url]

-------------------------

hdunderscore | 2017-01-02 01:12:41 UTC | #11

Nice work ! This got merged into master, I tested it a little and it seems to work well ! I really appreciate you getting this working.

-------------------------

