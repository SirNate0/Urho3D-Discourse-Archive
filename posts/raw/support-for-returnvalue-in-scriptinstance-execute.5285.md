Leith | 2019-07-07 05:50:27 UTC | #1


Today I was prompted to make a minor change to the Urho3D sourcecode.
Generally speaking, I prefer to work around such issues, rather than mess with the engine source, however in this case I made an exception.

ScriptFile::Execute supports an optional pointer to receive a return value when executing a script function or method.
ScriptInstance::Execute internally calls ScriptFile::Execute, but does not pass on, or provide for, the optional returnvalue container.

I made the following (harmless?) changes to ScriptInstance.h:
[code]
    /// Query for a method by declaration and execute. Log an error if not found.
    bool Execute(const String& declaration, const VariantVector& parameters = Variant::emptyVariantVector, Variant* rv=nullptr);
    /// Execute a method.
    bool Execute(asIScriptFunction* method, const VariantVector& parameters = Variant::emptyVariantVector, Variant* rv=nullptr);
[/code]

And these changes to ScriptInstance.cpp:
[code]
bool ScriptInstance::Execute(const String& declaration, const VariantVector& parameters, Variant* rv)
{
    if (!scriptObject_)
        return false;

    asIScriptFunction* method = scriptFile_->GetMethod(scriptObject_, declaration);
    if (!method)
    {
        URHO3D_LOGERROR("Method " + declaration + " not found in class " + className_);
        return false;
    }

    return scriptFile_->Execute(scriptObject_, method, parameters, rv);
}

bool ScriptInstance::Execute(asIScriptFunction* method, const VariantVector& parameters, Variant* rv)
{
    if (!method || !scriptObject_)
        return false;

    return scriptFile_->Execute(scriptObject_, method, parameters, rv);
}
[/code]

Noting that support for returnvalues was NOT extended to "delayed calls", the C++ caller (such as my behavior tree nodes) can now receive return values when executing script methods.
This is the first and only change I've made in a fresh copy of the engine source I pulled down last week.
If anyone can think of a reason why this change is a bad idea, please let me know!

-------------------------

Leith | 2019-07-07 08:41:52 UTC | #2

To justify this change, I offer the following (rather convoluted) use-case.
Here I have a situation where C++ will execute some AngelScript class method, and return something to the caller.

Here is the logic for a behavior tree node which can execute a named method of a scriptinstance, passing in zero, one or two variant arguments, and store a return argument, with storage context hints. Storage can be Global, Local (Caller Attribute/Property) or Local (Caller Node Variable)

[code]
    BTNodeState ServiceNode::HandleStep()  {

            /// Method Arguments
            VariantVector parameters;
            /// Return Value
            Variant rv;

            /// Assume we have two arguments: if theres no first arg, then there will be no second arg!
            bool checkArg2=true;

            switch(Arg1Source_){
                case RVT_AgentVariable:
                    parameters.Push(tree_->callingAgent->GetNode()->GetVar(Arg1Name_));
                    break;
                case RVT_AgentState:
                    parameters.Push(tree_->callingAgent->GetAttribute(Arg1Name_));
                    break;
                case RVT_World:
                      parameters.Push(GetGlobalVar(Arg1Name_));
                    break;
                case RVT_NONE:
                    checkArg2=false;
                    break;
                default:
                    URHO3D_LOGERROR("ServiceNode: Unhandled Arg1 Source");
            }

            if(checkArg2){
                switch(Arg2Source_){
                    case RVT_AgentVariable:
                        parameters.Push(tree_->callingAgent->GetNode()->GetVar(Arg2Name_));
                        break;
                    case RVT_AgentState:
                        parameters.Push(tree_->callingAgent->GetAttribute(Arg2Name_));
                        break;
                    case RVT_World:
                          parameters.Push(GetGlobalVar(Arg2Name_));
                        break;
                    case RVT_NONE:
                        break;
                    default:
                        URHO3D_LOGERROR("ServiceNode: Unhandled Arg2 Source");
                }
            }

            /// Execute script method, and note the return value from the script
            bool result = tree_->callingAgent->Execute(decl_, parameters, &rv);

            if(result)
            {
                state_=NS_SUCCESS;
                
                switch(RVTarget_){
                    case RVT_AgentVariable:
                        tree_->callingAgent->GetNode()->SetVar(RVName_,rv);
                    case RVT_AgentState:
                        tree_->callingAgent->SetAttribute(RVName_,rv);
                        break;
                    case RVT_World:
                        context_->SetGlobalVar(RVName_, rv);
                        break;
                    case RVT_NONE:
                        break;
                    default:
                        URHO3D_LOGERROR("Unhandled RVType in ServiceNode");
                }
            }else{
                URHO3D_LOGERROR("Failed to execute method with decl="+decl_);
                state=NS_ERROR;
            }

            return state_;

        }
[/code]

Yes, this example is incomplete logically, I just got RV from AS, so its early days with this route to getting work done.
I just wanted to show that yes, I actually do have a use-case that wants to know the return value, not just the result, of attempting script execution.

-------------------------

Leith | 2019-07-09 13:30:35 UTC | #3

There was one further change I needed to make (to ScriptFile.cpp) in order to receive returnvalues from script methods back to c++ caller..
Basically I needed to copy some existing sourcecode from the "function execute" to the "method execute", in order to get my return values handed back from script methods...

[code]
bool ScriptFile::Execute(asIScriptObject* object, asIScriptFunction* method, const VariantVector& parameters, Variant* functionReturn,
    bool unprepare)
{
    URHO3D_PROFILE(ExecuteMethod);

    if (!compiled_ || !object || !method)
        return false;

    // It is possible that executing the method causes us to unload. Therefore do not rely on member variables
    // However, we are not prepared for the whole script system getting destroyed during execution (should never happen)
    Script* scriptSystem = script_;

    asIScriptContext* context = scriptSystem->GetScriptFileContext();
    if (context->Prepare(method) < 0)
        return false;

    context->SetObject(object);
    SetParameters(context, method, parameters);

    scriptSystem->IncScriptNestingLevel();
    bool success = context->Execute() >= 0;

    if (success && (functionReturn != nullptr))
    {
        const int typeId = method->GetReturnTypeId();

        asIScriptEngine* engine = script_->GetScriptEngine();
        asITypeInfo* typeInfo = engine->GetTypeInfoById(typeId);

        // Built-in type
        if (typeInfo == nullptr)
        {
            switch (typeId)
            {
            case asTYPEID_VOID:
                *functionReturn = Variant::EMPTY;
                break;

            case asTYPEID_BOOL:
                *functionReturn = Variant(context->GetReturnByte() > 0);
                break;

            case asTYPEID_INT8:
            case asTYPEID_UINT8:
            case asTYPEID_INT16:
            case asTYPEID_UINT16:
            case asTYPEID_INT32:
            case asTYPEID_UINT32:
                *functionReturn = Variant(static_cast<int>(context->GetReturnDWord()));
                break;

            case asTYPEID_INT64:
            case asTYPEID_UINT64:
                *functionReturn = Variant(static_cast<long long>(context->GetReturnQWord()));
                break;

            case asTYPEID_FLOAT:
                *functionReturn = Variant(context->GetReturnFloat());
                break;

            case asTYPEID_DOUBLE:
                *functionReturn = Variant(context->GetReturnDouble());
                break;
            }
        }
        else if (typeInfo->GetFlags() & asOBJ_REF)
        {
            *functionReturn = Variant(static_cast<RefCounted*>(context->GetReturnObject()));
        }
        else if (typeInfo->GetFlags() & asOBJ_VALUE)
        {
            void* returnedObject = context->GetReturnObject();

            const VariantType variantType = Variant::GetTypeFromName(typeInfo->GetName());
            switch (variantType)
            {
            case VAR_STRING:
                *functionReturn = *static_cast<String*>(returnedObject);
                break;

            case VAR_VECTOR2:
                *functionReturn = *static_cast<Vector2*>(returnedObject);
                break;

            case VAR_VECTOR3:
                *functionReturn = *static_cast<Vector3*>(returnedObject);
                break;

            case VAR_VECTOR4:
                *functionReturn = *static_cast<Vector4*>(returnedObject);
                break;

            case VAR_QUATERNION:
                *functionReturn = *static_cast<Quaternion*>(returnedObject);
                break;

            case VAR_COLOR:
                *functionReturn = *static_cast<Color*>(returnedObject);
                break;

            case VAR_INTRECT:
                *functionReturn = *static_cast<IntRect*>(returnedObject);
                break;

            case VAR_INTVECTOR2:
                *functionReturn = *static_cast<IntVector2*>(returnedObject);
                break;

            case VAR_MATRIX3:
                *functionReturn = *static_cast<Matrix3*>(returnedObject);
                break;

            case VAR_MATRIX3X4:
                *functionReturn = *static_cast<Matrix3x4*>(returnedObject);
                break;

            case VAR_MATRIX4:
                *functionReturn = *static_cast<Matrix4*>(returnedObject);
                break;

            case VAR_RECT:
                *functionReturn = *static_cast<Rect*>(returnedObject);
                break;

            case VAR_INTVECTOR3:
                *functionReturn = *static_cast<IntVector3*>(returnedObject);
                break;

            default:
                URHO3D_LOGERRORF("Return type (%c) is not supported", typeInfo->GetName());
                break;
            }
        }
        else
        {
            URHO3D_LOGERRORF("Return type (%c)is not supported", typeInfo->GetName());
        }
    }

    if (unprepare)
        context->Unprepare();
    scriptSystem->DecScriptNestingLevel();

    return success;
}
[/code]

-------------------------

SirNate0 | 2019-07-09 16:27:27 UTC | #4

Provided you've tested this with, e.g. all of passing built-in types and pod types like Vector3 and pointer tires (like a Node*/Node@), I am fully in favor of this code bring moved into master. (I'd actually support it even if you broke the existing API, as I think this is functionality that the engine has been lacking for years). 

I remember I tried to do something similar before where I basically ended up having to pass "return" values by reference into the script function and then modify them in that, but it would fail for built in types like integers (so they'd have to be passed in an IntVector2 or something). This approach seems to cleanly solve the problem (unlike my hacked together approach), so I'm for it! Thanks for solving the problem well!

Regarding delayed calls, it seems to me that with the work done to handle return values already completed, it would be plausible to allow an optional `std::function<void, Variant>` to be called on the return value, or we could put the return value in the event that I assume we send when the delayed execute is finished. (I don't think the rest of the code needs to wait for this possible improvement to be merged, though)

-------------------------

Leith | 2019-07-10 07:10:46 UTC | #5

I'm currently experimenting with returning various datatypes - so far the only noticeable problem is unpacking array types, which I think I can probably sort out. At any rate, any return types that are a problem for method execution, will also be a problem for function execution, since I basically copied and pasted the code to unpack return value types...
[EDIT]
An unexpected problem return type was Variant.
The code (as posted) to wrap return values does not expect that scripts might actually be nice and return a variant already wrapped...
I'll repost my code to include any further type support once I've had a chance to test more thoroughly.

Notice that I have to wrap angelscript strings in Urho String before trying to compare them... compare will fail if I don't do that, guess String is missing some compare cases...
[code]
	    if(String(typeInfo->GetName())=="Variant")
	    {
                    *functionReturn=*static_cast<Variant*>(returnedObject);

	    }else{
		    const VariantType variantType = Variant::GetTypeFromName(typeInfo->GetName());
		    switch (variantType)
		    {
		    case VAR_STRING:
[/code]

-------------------------

Leith | 2019-07-10 08:28:59 UTC | #6

There are a few bumps ahead, as the existing code I borrowed is far from type-complete, but if a Variant can hold it, then I assume I can resolve the issues. The key thing to remember is that the return value will be held by a variant - so it has to be acceptable in terms of what a variant can hold.

-------------------------

Leith | 2019-07-12 05:47:31 UTC | #7

One major stumbling block appears to be CScriptArray!
If this is a reference type, why is it implementing its own refcount? Why does it not derive from RefCounted? 
If this is a template container type, but holds a void*, why is no solid type information retained within the class?
[EDIT]
When instantiated by AngelScript, the CScriptArray object does contain angelscript type information for the element type, including a name string. Further, we can query Variant for a corresponding Urho type by name. So it's not all bad.

-------------------------

SirNate0 | 2019-07-11 12:08:48 UTC | #8

If I had to guess, some of the shortcomings might be because it was adapted from the AngelScript add-on code. In terms of type information, is the `asITypeInfo* objType` insufficient?

-------------------------

Leith | 2019-07-12 05:33:06 UTC | #9

Here's what I've come up with so far.... It's not the most pretty code I've ever written, but it should handle all kinds of return types... primitives, variants, object refs, and arrays of these things (but not nested arrays...)
Note that arrays are always returned as a VariantVector: CScriptArray can always be "unpacked" into a variant vector, although Urho appears not to provide a utility function that can do it.

[code]
   /// Execute an object method.
    bool Execute(asIScriptObject* object, asIScriptFunction* method, const VariantVector& parameters = Variant::emptyVariantVector,
        Variant* functionReturn = nullptr, bool unprepare = true)
{
//    URHO3D_PROFILE(ExecuteMethod);

    if (!compiled_ || !object || !method)
        return false;

    // It is possible that executing the method causes us to unload. Therefore do not rely on member variables
    // However, we are not prepared for the whole script system getting destroyed during execution (should never happen)
    Script* scriptSystem = script_;

    asIScriptContext* context = scriptSystem->GetScriptFileContext();
    if (context->Prepare(method) < 0)
        return false;

    context->SetObject(object);
    SetParameters(context, method, parameters);

    scriptSystem->IncScriptNestingLevel();
    bool success = context->Execute() >= 0;

    if (success && (functionReturn != nullptr))
    {
        const int typeId = method->GetReturnTypeId();

        asIScriptEngine* engine = script_->GetScriptEngine();
        asITypeInfo* typeInfo = engine->GetTypeInfoById(typeId);

        // Built-in type
        if (typeInfo == nullptr)
        {
            switch (typeId)
            {
            case asTYPEID_VOID:
                *functionReturn = Variant::EMPTY;
                break;

            case asTYPEID_BOOL:
                *functionReturn = Variant(context->GetReturnByte() > 0);
                break;

            case asTYPEID_INT8:
            case asTYPEID_UINT8:
            case asTYPEID_INT16:
            case asTYPEID_UINT16:
            case asTYPEID_INT32:
            case asTYPEID_UINT32:
                *functionReturn = Variant(static_cast<int>(context->GetReturnDWord()));
                break;

            case asTYPEID_INT64:
            case asTYPEID_UINT64:
                *functionReturn = Variant(static_cast<long long>(context->GetReturnQWord()));
                break;

            case asTYPEID_FLOAT:
                *functionReturn = Variant(context->GetReturnFloat());
                break;

            case asTYPEID_DOUBLE:
                *functionReturn = Variant(context->GetReturnDouble());
                break;
            }
        }
        else if (typeInfo->GetFlags() & asOBJ_REF)
        {
            /// Check for special case: array type
            String name=typeInfo->GetName();
            if(name=="Array")
            {
                /// We have an array<T> on our hands...
                CScriptArray* ary = static_cast<CScriptArray*>(context->GetReturnObject());
                int cnt=ary->GetSize();
                VariantVector vary(cnt);


                /// Query the type of array elements (ie type of T)
                String subname=typeInfo->GetSubType(0)->GetName();
                int flags=typeInfo->GetSubType(0)->GetFlags();


                /// Check if we have an array of "handles"
                /// If so, we will assume that all handles are pointers to Urho3D Objects
                /// which always derive from "RefCounted"...
                if(flags&asOBJ_REF)
                {
                    for(int i=0;i<cnt;i++)
                        vary[i]=static_cast<RefCounted*>(ary->At(i));
                    *functionReturn = Variant(vary);

                /// Check if we have an array of "values"
                }else if(flags&asOBJ_VALUE){

                    /// Check for special case: value is already a Variant
                    if(subname=="Variant")
                    {
                        for(int i=0;i<cnt;i++)
                            vary[i]=*static_cast<Variant*>(ary->At(i));
                        *functionReturn = Variant(vary);


                    }else{
                        /// Handle all variant-supported types
                        const VariantType variantType = Variant::GetTypeFromName(subname);
                        switch (variantType)
                        {
                        case VAR_BOOL:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<Bool*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_FLOAT:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<float*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_DOUBLE:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<double*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_INT:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<int*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_INT64:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<int64_t*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_STRING:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<String*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_VECTOR2:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<Vector2*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_VECTOR3:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<Vector3*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_VECTOR4:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<Vector4*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_QUATERNION:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<Quaternion*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_COLOR:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<Color*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_INTRECT:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<IntRect*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_INTVECTOR2:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<IntVector2*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_MATRIX3:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<Matrix3*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_MATRIX3X4:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<Matrix3x4*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_MATRIX4:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<Matrix4*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_RECT:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<Rect*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_INTVECTOR3:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<IntVector3*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        case VAR_VARIANTVECTOR:
                            for(int i=0;i<cnt;i++)
                                vary[i]=*static_cast<VariantVector*>(ary->At(i));
                            *functionReturn = Variant(vary);
                            break;

                        default:
                            URHO3D_LOGERROR("Array value type is not supported by Variant: typeid is " +String(typeId)+" VarType="+String((int)variantType)+" "+ subname);
                        }
                    }

                }else{
                    URHO3D_LOGERROR("Unhandled type detected in Array: "+subname);
                    *functionReturn = Variant::EMPTY;
                }

            }
            else{
                /// We can generally assume that Handles are pointers to Urho3D Objects
                /// which always derive from "RefCounted"...
                RefCounted* obj = static_cast<RefCounted*>(context->GetReturnObject());
                *functionReturn = Variant(obj);
            }
        }

        else if (typeInfo->GetFlags() & asOBJ_VALUE)
        {
            void* returnedObject = context->GetReturnObject();

            if(String(typeInfo->GetName())=="Variant")
            {
                        *functionReturn=*static_cast<Variant*>(returnedObject);

            }else{
                const VariantType variantType = Variant::GetTypeFromName(typeInfo->GetName());
                switch (variantType)
                {
                case VAR_STRING:
                    *functionReturn = *static_cast<String*>(returnedObject);
                    break;

                case VAR_VECTOR2:
                    *functionReturn = *static_cast<Vector2*>(returnedObject);
                    break;

                case VAR_VECTOR3:
                    *functionReturn = *static_cast<Vector3*>(returnedObject);
                    break;

                case VAR_VECTOR4:
                    *functionReturn = *static_cast<Vector4*>(returnedObject);
                    break;

                case VAR_QUATERNION:
                    *functionReturn = *static_cast<Quaternion*>(returnedObject);
                    break;

                case VAR_COLOR:
                    *functionReturn = *static_cast<Color*>(returnedObject);
                    break;

                case VAR_INTRECT:
                    *functionReturn = *static_cast<IntRect*>(returnedObject);
                    break;

                case VAR_INTVECTOR2:
                    *functionReturn = *static_cast<IntVector2*>(returnedObject);
                    break;

                case VAR_MATRIX3:
                    *functionReturn = *static_cast<Matrix3*>(returnedObject);
                    break;

                case VAR_MATRIX3X4:
                    *functionReturn = *static_cast<Matrix3x4*>(returnedObject);
                    break;

                case VAR_MATRIX4:
                    *functionReturn = *static_cast<Matrix4*>(returnedObject);
                    break;

                case VAR_RECT:
                    *functionReturn = *static_cast<Rect*>(returnedObject);
                    break;

                case VAR_INTVECTOR3:
                    *functionReturn = *static_cast<IntVector3*>(returnedObject);
                    break;

                case VAR_VARIANTVECTOR:
                *functionReturn = *static_cast<VariantVector*>(returnedObject);
                break;

                default:
                    URHO3D_LOGERROR("Return value type is not supported: typeid is " +String(typeId)+" VarType="+String((int)variantType)+" "+ typeInfo->GetName());
                    break;
                }
            }
        }
        else
        {
            URHO3D_LOGERRORF("Return type (%c)is not supported",typeInfo->GetName());
        }
    }

    if (unprepare)
        context->Unprepare();
    scriptSystem->DecScriptNestingLevel();

    return success;
}
[/code]

Note that I moved this method temporarily from ScriptFile.cpp to ScriptFile.h just because it's easier for me to debug engine code when it's not part of the static library.

-------------------------

Leith | 2019-07-12 07:51:17 UTC | #10

That code contains some 2 or 3 small typo bugs, but otherwise compiles fine.

-------------------------

Leith | 2019-07-13 10:44:58 UTC | #11

I am still currently not understanding why our CScriptArray implementation has its own addref and release methods, instead of deriving from RefCounted.

If the object was refcounted, I could reduce the amount of code in my version of ScriptFile::Execute by half... I would not have to deal with a special case class which angelscript says is REF but urho says is not derived from RefCounted, like every other non-value class registered with angelscript.

I recognize the sourcecode from the angelscript website, I appreciate that its legacy code, but why is it *still* legacy code at this time?

-------------------------

SirNate0 | 2019-07-13 20:38:43 UTC | #12

Looking through the source, I think the reason we didn't just replace the reference counting comes down to how the existing code handles the memory management. It seems AS uses malloc and free, while RefCounted uses delete. I'm certainly not against the implementation being updated, but I imagine no one else has felt a need to do it since prior to this it probably didn't require any extra work. Another difference seems to be that RefCounted allows weak references, which I don't think the AngelScript types have any notion of.

It's probably pretty straightforward to correct this, since there seem to be only about a dozen uses of the userAlloc and userFree functions between the dictionary and the array. The only concern I'd raise is that this may require more work in updating the AngelScript library later on, since presently I think our changes are limited to disabling garbage collection.

-------------------------

Leith | 2019-07-14 04:19:12 UTC | #13

Apparently we already have support for weakptr handles:
[quote]
WeakHandle rigidBodyWeak = node.CreateComponent("RigidBody");
RigidBody@ rigidBodyShared = rigidBodyWeak.Get(); // Is null if expired
[/quote]

There is also some example addon sourcecode for angelscript weakptr which I might look into, but for the moment I have a much more simple problem...

[quote]
Additional global properties exist for accessing the script object's node, the scene and the scene-wide components: node, scene, octree, physicsWorld, debugRenderer. When an object method is not executing, these are null. "
[/quote]

My script class (Actor.Update method in my test script) calls a c++ global function which in turn leads to a nested execution of a script method on the same class... that is to say, when Urho engine calls the script update method, execution is passed from script to my c++ function, and then from c++ I call another script method on the same instance of the same script class... we're now two angelscript contexts deep (since our implementation creates a new script context per nesting depth)...

When executing script in this nested fashion, the script global properties mentioned above are null - where exactly are these "properties" being set and cleared?

-------------------------

Leith | 2019-07-15 12:50:24 UTC | #14

On this topic, why the hell are we making a new context per depth, when we have push and pop methods on the context, wholly intended to deal with nesting?

-------------------------

Leith | 2019-07-16 10:20:07 UTC | #15

if our angelscript implementation is the coal face of this engine, then we need to evaluate our implementation, the addons, all of it - in its current state, I find it unusable. I have use cases you can test.

-------------------------

Leith | 2019-08-01 09:36:51 UTC | #16

Here is a proposed patch to allow AngelScript to return rubber values to C++ callers - changes appear not to break existing code ... both functions and script class methods are supported - return values are anything we can shove into a variant, including arrays, and possibly, arrays of arrays, of any variant-containable value type.
<https://www.dropbox.com/s/d48oorgsgz6okoz/AngelScript_FullRV.zip?dl=0>

-------------------------

George1 | 2019-08-01 09:46:25 UTC | #17

while you are at this.  Maybe help to look at reloading of script or re assignment to new script.  This way it is possible to change the behaviour of agent/component in realtime.  Great for testing of new behaviour and features.

-------------------------

Leith | 2019-08-01 09:58:16 UTC | #18

I don't pretend to know everything - live updates, and monitoring files for changes, is not so far on my todo list, but I will consider adding that, because live editing is the main reason to use scripting - that we can make changes, even without closing our app... and see the changes, in realtime. Rapid application development is where it's at. I will see what I can do, but I don't really know what's been done! I am not an expert in Urho - it's a big topic, I am a fairly new user to Urho. I am not new to gamedev. I will look into it :)

-------------------------

Leith | 2019-08-02 06:43:58 UTC | #19

The reason I developed this patch was to support data-driven AI behavior trees, which need at some point to get connected to named code functions, which is something c++ is natively bad at doing - script functions / class methods offered a way to hook up c++ code to named scripted functions at runtime, but Urho's existing implementation (with respect to Return Values) was incomplete - there was indication of a return value in the ScriptFile class, but it was only partially implemented for script functions, and not at all for script class methods. I filled in the gaps.

-------------------------

