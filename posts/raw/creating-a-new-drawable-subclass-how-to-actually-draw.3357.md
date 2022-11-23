Alan | 2017-07-15 18:21:20 UTC | #1

Hi guys, I asked this on Gitter but I think Discourse would be more appropriate:

I'm making a new Drawable subclass, and it's working rather fine, however, the way I'm drawing stuff is actually by calling IsInView in the update event and manually drawing, what's a hacky solution but I couldn't find any obvious way to properly draw something, there's no Draw() or OnDraw() or anything like that, and no way I can see to pass the data to be rendered except maybe GetLodGeometry what I don't think is what I want. How would you do that?

Thank you

-------------------------

1vanK | 2017-07-15 22:53:22 UTC | #2

Minimal template for Drawable that draws triangle: https://github.com/1vanK/Urho3DRuWiki/wiki/%D0%A8%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B3%D0%BE-%D0%BA%D0%BE%D0%BC%D0%BF%D0%BE%D0%BD%D0%B5%D0%BD%D1%82%D0%B0-(Drawable)

(sorry, comments on russian)

-------------------------

Alan | 2017-07-15 22:41:03 UTC | #3

Thank you! However, I still didn't understand something, how does the renderer access the geometry data?

At the moment I'm subscribing a method to E_POSTRENDERUPDATE and calling the drawing function in my component, what I don't think is ideal. Also, for some reason subscribing to that in the component itself didn't work, what are the requirements for that event to fire? In any case, I'm not very happy with that solution, I just need to somehow manage aabbs and also submit geometry data (vert and idx buffers) to the render pipeline along with shaders/materials, what that snippet really seems to do except the material part :P .

Thank you very much @1vanK

-------------------------

1vanK | 2017-07-15 22:53:22 UTC | #4

Engine found Drawables which fall into the field of view of the camera, take batches_ from each and render its, so the main task of Drawable is fill batches_ vector

-------------------------

Alan | 2017-07-15 22:53:13 UTC | #5

Got it! Awesome! Thank you @1vanK!

-------------------------

