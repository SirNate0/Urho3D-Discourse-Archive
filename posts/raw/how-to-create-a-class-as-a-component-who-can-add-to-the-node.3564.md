spwork | 2017-09-14 17:41:36 UTC | #1

To do that,what class do i need inherit，and what thing do i do follow,
and my component i serializable when i use Scene->SaveXML();

Or i don't create a component, just make my class can add to the Node like other component,and i serializable auto when i use Scene->SaveXML();

-------------------------

Eugene | 2017-09-14 14:49:27 UTC | #2

To add class as Component you should inherit it from `Component`. You could also use more specific `Component` derivatives like `LogicComponent` or `Drawable` or `CustomGeometry` or so on depending on your goals.

-------------------------

spwork | 2017-09-14 14:55:37 UTC | #3

thank you ，i'll try.

-------------------------

