SirNate0 | 2021-05-26 07:21:59 UTC | #1

There is apparently an issue with how the forum's DNS entry is signed, which is preventing it from being available at my university.

See https://dnsviz.net/d/discourse.urho3d.io/dnssec/ for a description.

-------------------------

weitjong | 2021-04-15 17:09:54 UTC | #2

Thanks for reporting that. Unfortunately, I am not able to find anything wrong with the existing setup that I inherited from hd_, who started this forum initially. Looking at the result from another tool [here](https://dnssec-analyzer.verisignlabs.com/discourse.urho3d.io), it appears the domain "urho3d.io" works fine. The error seems to happen in CNAME record which links the "discourse.urho3d.io" to the hosted Discourse site (urho3d.hosted-by-discourse.com), which we actually got it for free. I won't pretend I actually know what the error is all about, but most likely it is not something I can fix from my end.

Could you test whether you can access other "hosted" discourse forums from your university?

-------------------------

SirNate0 | 2021-05-19 13:14:57 UTC | #3

It looks like the [python forum](https://discuss.python.org/) works fine. You can see the same report here that doesn't show the error messages:
https://dnsviz.net/d/discuss.python.org/dnssec/

Here's a group that had similar issues that seem to have been solved
https://groups.google.com/g/public-dns-discuss/c/HxKWcF3vm9o

and the Discourse instructions, in case they changed at some point
https://meta.discourse.org/t/configure-your-domain-name-for-hosted-discourse/21827

-------------------------

weitjong | 2021-05-22 14:08:51 UTC | #4

The link you have provided for setting up the hosted Discourse forum is the one we use. I don't see any discrepancies in our existing setup, like I said before. I may need to talk to our name registrar for additional support to get into the bottom of this. There is really not much in the settings to play around with on our side.

-------------------------

weitjong | 2021-05-23 05:08:54 UTC | #5

Our name registrar has checked the setup and confirmed that there is nothing wrong in our configuration (and on their side as well) in respect to DNSSEC. It is the hosted Discourse forum (that we got for free from Discourse) that does not support DNSSEC. I will have to loop in the support from Discourse to investigate further.

In the meantime, you may want to try to request your network admin to try to the clear DNS cache in case that is the problem why you cannot reach the forum from your university, while the rest of us can, despite the issue with DNSSEC.

> You may ask your forum user to clear cache of his browser or use another one. You can follow this guide to clear cache: [https://www.namecheap.com/support/knowledgebase/article.aspx/9209/2194/how-to-clear-cache-in-different-browsers-windows](http://mailtrackemailout1.namecheap.com/ls/click?upn=weJnGaxuvEB3idx9zQKUnTv4iTRZuMEP9lhOW9E2EIFX7nqMzH-2FJWTa-2B0NoQUZHLRHIoPGbz5UNhpIQloFbFrHhHTMh4mAJmLWmTEabL8GyXx5jghmIEcb7xU2z2i1WKib1enei0R-2F026Ln6r6C-2FuVOxlGYhnzMInshUNzlzWlBTlSVyfeYBU3u8hqitU-2BR1AMlw_LB7KWfKuU3GVdB9mtTD67dvIcXR00T1KiLksAAgP7MtMK8Zh-2Bo2UHFpQaUL262UAeyZvOFLLYP8-2FNuOtyKJ2uF3EfVm94Pyk6KZWSxg9PwYYpmOUlZ-2FU1kPE8ku-2FtQpQ5KmYd8uJXDN4RzTq3-2B81eZBPmgiXRIDOy-2FYagc6Erk62O9F9hsYQK4QLlg-2FwsRQ7UcyvQk7aAg3h6wuR94MMmQ-3D-3D) .
> 
> Also, he can clear his DNS cache as it is described in this guide: [https://www.namecheap.com/support/knowledgebase/article.aspx/397/2194/how-to-clear-local-dns-cache](http://mailtrackemailout1.namecheap.com/ls/click?upn=weJnGaxuvEB3idx9zQKUnTv4iTRZuMEP9lhOW9E2EIFX7nqMzH-2FJWTa-2B0NoQUZHLRHIoPGbz5UNhpIQloFbFrKDUdw5mU3lYVUZ2KyLXegu-2Fcpt9deT14KmO2olOUBvRuUoTnO1-2B4K0jcq4b-2Bc3Znw-3D-3D0Atg_LB7KWfKuU3GVdB9mtTD67dvIcXR00T1KiLksAAgP7MtMK8Zh-2Bo2UHFpQaUL262UAsAVjF-2ByZ3lpjK3EYqP-2BG5juqU7P5jwZ3SkK4BayeZxg2jxu0CXFnwMD4hJVb5qtmQI35i6QXJseLgq7RCVLNPMoMBz9DeaU-2Bp5-2FpgMX-2FYQN5nqchjeHS8-2FFb8MpmD0Lxp-2BVgBWmIN1OJW6zlRYaKpw-3D-3D) .

-------------------------

weitjong | 2021-05-26 04:41:39 UTC | #6

Just a brief update. I have contacted Discourse staff to get their support. The discussion is still on going in the PM. The temporary summary is, there is something wrong with the setup that causing the DNSSEC error, but there is still no conclusion who is at fault (me maintaining that one single CNAME record[?], the name registrar, or the hosted Discourse forum). The only thing that both the `namecheap` guy and `Discourse` guys agree (on separate discussion with me) is, the DNSSEC error should not cause issue to the forum users to access the forum.

-------------------------

SirNate0 | 2021-05-28 12:16:12 UTC | #7

Per the IT staff,

> The domain now appears to be working, although the DNSSEC setup is still not completely correct.

I'm traveling at present, so I can't confirm. If you made any changes, though, they seem to have worked.

-------------------------

weitjong | 2021-05-28 12:49:56 UTC | #8

I am glad to hear that. I did not specifically alter our DNS records to solve the DNSSEC error though, but the DNS records have been altered to make way for migrating gh-pages to our apex domain.

I have closed the DNSSEC error investigation on both the namecheap and Discourse. The conclusion I got so far is, it is the CNAME target itself does not have DNSSEC enabled, i.e. if you point the url to "`urho3d.github.io`" directly or point to "`urho3d.hosted-by-discourse.com`" on the analyze tool then you will see it ends up with DNSSEC errors too.

-------------------------

