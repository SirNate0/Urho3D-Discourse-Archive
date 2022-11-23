CE184 | 2020-12-09 05:58:04 UTC | #1

I have some complicated game logic components. I have been keeping refactoring them for a while and I found it's really hard to iterate without some unit test coverage. 
I do have unit test coverage for my some standalone classes that do not include any Urho3D class. But this one has some dependency on Urho3D (given input of a character's state, test current animation, blending, etc). And simply use something like
```
add_executable(MyCustomTest my_unittest.cc ${urho3d_src_cc} ${urho3d_src_h})
target_link_libraries(MyCustomTest gtest gtest_main)
```
does not work since Urho3D CMake has specific macro like ```define_source_files``` and ```setup_main_executable``` to add all the dependencies.

I was wondering if anyone is using any unit test and could provide a sample CMakeList?

-------------------------

vmost | 2020-12-09 13:11:43 UTC | #2

You might find [this PR](https://github.com/urho3d/Urho3D/pull/2665) or [this PR](https://github.com/urho3d/Urho3D/pull/2683) helpful. I have not written any tests myself, but plan to at some point once I learn how to use CMake properly.

-------------------------

CE184 | 2020-12-10 02:35:22 UTC | #3

Thanks. 
I managed to setup my separate test target using [this](https://discourse.urho3d.io/t/have-multiple-executable-targets-in-cmake-setting/6611/4?u=ce184). It works only for simple test cases but not for Urho3D node/components stuff. For example, if I have
```
auto *cache = GetSubsystem<ResourceCache>();
```
in some functions I test, the cache will always be ```null```. I suspect it's due to Urho3D specific mechanism to initialize everything when create components (e.g. like when we create component, the ```node_``` in that component is not set yet).

Other things simple as creating component will fail too.
```
TEST(GoogleTestOne, MyTest) {
  Urho3D::SharedPtr<Urho3D::Context> context(new Urho3D::Context());
  Urho3D::SharedPtr<Node> animation_node(new Node(context));
  ASSERT_NE(animation_node, nullptr);
  auto* model = animation_node->CreateComponent<AnimatedModel>();
  ASSERT_NE(model, nullptr);   // Fail here, model will be nullptr.
}
```

I could not see an easy way to mock those things out. I think it needs Urho3D official support for those thing like your PRs. I am not expert on that.

-------------------------

vmost | 2020-12-10 02:53:04 UTC | #4

Yes afiact Urho3D was not designed with unit testing in mind...

-------------------------

SirNate0 | 2020-12-10 04:45:56 UTC | #5

A lot of the initialization is handled by the Application and Engine. I'm not surprised that you were unable to create the model successfully, it's very possible that the AnimatedModel had not been added as a factory to the Context because of that missing initialization. You might want to create a separate application class for each of your test runs, and/or just copy all of the initialization code from it.

-------------------------

CE184 | 2020-12-10 05:53:26 UTC | #6

Yes, you are right.
I did registered factory for my custom component, but did not do it for native urho3d ones. I had the false impression that they are done automatically. So when I manually registered all the components I use in the test, everything works fine.
So at least it looks like to work for most of unit test settings. The only thing is just to do correct initialization and set context.
Thanks.

-------------------------

CE184 | 2020-12-10 06:05:23 UTC | #7

Yes, I read some of the posts earlier by cadaver and I agree unit test is not necessary/flexible for most part of engine code. I think it makes more sense for developer to do their own unit test since game logic is defined by developer. Unit test is not very popular in general game industry afaik. I am doing this only because I benefit from some large projects I did for work.
Now I've had the successful setup, I can try something here.

-------------------------

