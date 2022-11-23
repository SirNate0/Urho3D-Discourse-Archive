Askhento | 2019-10-28 01:31:55 UTC | #1

I have some functions to be called with delay. I can do it with Update event and take timestep from it, but I've read some posts here and found DelayedExecution method. So, it works! However I need to run a method inside a class, but I could not set the third parameter "declaration of function" right( 
I am stuck, again.

UPD : docs says that class should be ScriptObject, so my question should be more about the correct method to use for this task.

-------------------------

orefkov | 2019-10-28 06:41:53 UTC | #2

In order for the DelayedExecution to look for a method inside the class, its call must also be made inside the method of this class.
For declaration of fuction you must use name of class method without class name, and use parametrs convertable to Variant.

    class SceneSwitcher : ScriptObject {
        void on_SceneSwitch(StringHash, VariantMap& data) {
            String path = data["ScenePath"].GetString();
            DelayedExecute(0.1, false, "void switchScene(const String&)", Array<Variant> = {Variant(path)});
        }
        void switchScene(const String& path) {
    ...

-------------------------

Askhento | 2019-10-28 07:24:50 UTC | #3

I've managed this one, but what if my class already inherit from some other class, not a ScriptObject?

-------------------------

orefkov | 2019-10-29 06:58:39 UTC | #4

You always can create proxy ScriptObject class for it. For example

    funcdef void PVV();

    class PvvWrapper : ScriptObject {
    	PVV@ ptr;
    	void shedulle(float time, bool repeat, PVV@ callback) {
    		@ptr = callback;
    		DelayedExecute(time, repeat, "tick");
    	}
    	void tick() {
    	    ptr();
            node.RemoveComponent(self);
    	}
    };
    void setTimeout(float time, bool repeat, PVV&& callback) {
    	PvvWrapper&& wrapper = cast<PvvWrapper>(scene_.CreateScriptObject(scriptFile, "PvvWrapper"));
    	wrapper.shedulle(time, repeat, callback);
    }

-------------------------

Askhento | 2019-10-28 07:46:11 UTC | #5

[quote="orefkov, post:2, topic:5691"]
String path = data["ScenePath"].GetString(); DelayedExecute(0.1, false, "void switchScene(const String&)", Array<Variant> = {Variant(path)});
[/quote]

This one looks really difficult for me! Thnx;

-------------------------

