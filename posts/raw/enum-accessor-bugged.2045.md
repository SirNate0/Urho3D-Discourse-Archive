TheComet | 2017-01-02 01:12:32 UTC | #1

Hey!

I'm trying to use URHO3D_ENUM_ACCESSOR_ATTRIBUTE but it's adding an extra item into the dropdown menu that shouldn't be there. I have the following code:

[code]void IKRoot::RegisterObject(Context* context)
{
    context->RegisterFactory<IKRoot>(IK_CATEGORY);

    static const char* algorithmNames[] = {
        "None",
        "Jacobian Inverse",
        "Jacobian Transpose",
        "FABRIK"
    };
    URHO3D_ENUM_ACCESSOR_ATTRIBUTE("Algorithm", GetSolverType, SetSolverType, IKSolver::SolverAlgorithm, algorithmNames, IKSolver::FABRIK, AM_DEFAULT);
}[/code]

Where my enum is defined as:
[code]    enum SolverAlgorithm
    {
        NONE = 0,
        JACOBIAN_INVERSE,
        JACOBIAN_TRANSPOSE,
        FABRIK
    };[/code]

The result is a dropdown menu with 5 items instead of 4:

[img]http://i.imgur.com/BiKTkBL.png[/img]

If I add another string to the array of strings:

[code]    static const char* algorithmNames[] = {
        "None",
        "Jacobian Inverse",
        "Jacobian Transpose",
        "FABRIK",
        "This shouldn't be here"
    };[/code]

Then the dropdown menu also gains another item, but it's still one too many:

[img]http://i.imgur.com/O29AZLV.png[/img]

Is this a bug or am I doing something wrong?

-------------------------

cadaver | 2017-01-02 01:12:33 UTC | #2

You need a terminator null ptr. See e.g. BillboardSet.cpp.

-------------------------

TheComet | 2017-01-02 01:12:33 UTC | #3

Aaah, that makes sense. Thanks a lot!

-------------------------

