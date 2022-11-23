Lys0gen | 2020-12-16 12:48:22 UTC | #1

Hey,

I have some Buttons that have multiple children (icons/text values). When hovering over those children I want more detailed information displayed in tooltips. So far, so good.

As I need to set the

    IsEnabled(true)

attribute for the tooltips to show that is sadly also blocking the click event inputs on the parent (button) element.

Is there a good way to solve this *(have child elements show tooltips without interfering with the parent)*?

**If possible I want to avoid subscribing the children to the same events as the parent and repeating whatever it does.**

Thanks!

-------------------------

