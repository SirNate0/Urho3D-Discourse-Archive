graveman | 2017-01-02 01:05:51 UTC | #1

Hi, I have a question a license about.
If I modified some source code file of Urho and wanted to add some other expanded license to my changes what I must do then: 
to leave last Urho license and add my license or something else?

-------------------------

cadaver | 2017-01-02 01:05:53 UTC | #2

Welcome to the forums.

There are no requirements in the MIT license concerning the ordering of license texts. Practically the only requirement is that the original Urho3D license is included (somewhere) and it will continue to govern all included Urho3D source code. For a somewhat related discussion, see e.g. [url]http://stackoverflow.com/questions/4035702/can-i-relicense-someones-mit-code-under-gpl[/url]

-------------------------

friesencr | 2017-01-02 01:05:53 UTC | #3

Don't forget the part where you can't sue the urho authors :slight_smile:

-------------------------

graveman | 2017-01-02 01:05:55 UTC | #4

[b]cadaver[/b].
It is still not very clear.
If I would take some Urho3D source  file and changed some original text there in (not only  added my own text),can I write something like that in the beginning of that modified version:
[i]"Original code license:
//
// Copyright (c) 2008-2014 the Urho3D project.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.
//

Modification code is under next licence:
"
My some expanded MIT-based lisence saying that:
It is allowed to do what somebody want with my code. Some punct that forbid to deny (to forbid) you this rights. Shortly speaking, I don't need some "dick" to close my code.
"[/i]

-------------------------

graveman | 2017-01-02 01:05:56 UTC | #5

[quote="friesencr"]Don't forget the part where you can't sue the urho authors :slight_smile:[/quote]
Yes, of course

-------------------------

cadaver | 2017-01-02 01:05:56 UTC | #6

As far as I understand, you cannot change the existing Urho license, and you shouldn't make it to appear as if the whole code in the file is under your new, stricter license. (But I'm not a lawyer so this does not constitute legal advice, I'm just stating what would look clearest to me.) Rather, add your own license for example below the Urho license, and mark clearly the places of code which it governs. 

Do note that adding a license with any "viral" clauses can make your code unattractive to others, particularly if they're working on closed platforms (iOS etc.) where it's hard to avoid "closing" the published application. That's the reason Urho accepts only libraries with permissive MIT/BSD style licenses in the official repo.

In my honest opinion, if you're seriously afraid that people will take your modifications and make them part of a for-profit closed application, the best option (considering the Urho project itself is not afraid of that scenario, hence the MIT license) is to not publish the source to your modifications at all, rather than go to the hassle of an added license.

-------------------------

graveman | 2017-01-02 01:06:05 UTC | #7

[b]cadaver[/b], thanks.

-------------------------

