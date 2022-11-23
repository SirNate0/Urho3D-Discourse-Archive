DUNDUN-ww | 2021-09-27 02:40:18 UTC | #1

Hello, everyone~
I just begin to study urho3D and I want to ask a question.
I want to build transparent ground with objects on this ground and these objects should have its shade.
However,  when I set the ground into transparent, these objects can not have shade.
Looking for your answers~ Thanks

-------------------------

PsychoCircuitry | 2021-09-24 13:27:33 UTC | #2

Hi,

I think [this](https://discourse.urho3d.io/t/solved-render-shadow-on-transparent-ground/1327) thread might have the answers.

Summary, shadow maps are reused per light while rendering by default and thus are no longer available during the transparent pass. You can turn shadow map reuse off at the expense of larger video bandwidth (if you're using multiple shadow casting lights) but then the maps are still available on this pass. Then it's just configuring your material technique to work as expected. There's more details in the linked thread.

Hope that helps, good luck on your project!
-PsychoCircuitry

-------------------------

DUNDUN-ww | 2021-09-27 02:39:51 UTC | #3

Your answer is so helpful. The question was solved based on your answer. Thank you very much~

-------------------------

