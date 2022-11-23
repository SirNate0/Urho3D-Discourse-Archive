practicing01 | 2017-01-02 01:07:38 UTC | #1

Edit #2:  The following works but I lose fading. [pastebin.com/34FqtWhQ](http://pastebin.com/34FqtWhQ)
[code]
    void ModelController::RecursiveSetAnimation(Node* noed, String ani, bool loop, unsigned char layer)
    {
            if (noed->HasComponent<AnimationController>())
            {
                    String fileName = noed->GetVar("fileName").GetString();
     
                    String aniPath = "Models/" + fileName + "/" + ani + ".ani";
     
                    if (main_->cache_->Exists(aniPath))
                    {
                            if (( (noed->GetComponent<AnimationController>()->IsPlaying(aniPath) == false)
                                            && (noed->GetComponent<AnimationController>()->IsFadingIn(aniPath) == false) )
                                            || (noed->GetComponent<AnimationController>()->IsFadingOut(aniPath) == true) )
                            {
                                    noed->GetComponent<AnimationController>()->StopLayer(0, 0.0f);
                                    noed->GetComponent<AnimationController>()->PlayExclusive(aniPath, layer, loop, 0.0f);
     
                                    if (!loop)
                                    {
                                            noed->GetComponent<AnimationController>()->SetAutoFade(aniPath, 0.25f);
                                    }
                            }
                            else
                            {
                                    return;
                            }
                    }
            }
     
            for (int x = 0; x < noed->GetNumChildren(); x++)
            {
                    RecursiveSetAnimation(noed->GetChild(x), ani, loop, layer);
            }
    }
[/code]

[img]http://img.ctrlv.in/img/15/10/13/561d8bbe8dc0c.gif[/img]

Edit #1:  I made some progress.  It seems something doesn't like the long path after the first usage.  Using String aniPath = "Models/" + fileName + "/" + ani + ".ani"; along with noed->GetComponent<AnimationController>()->FadeOthers(aniPath, 0.0f, 0.25f); works but it seems that each time PlayExclusive() is called, a new animation is added.  After too many calls, the app hangs.

Hello, I'm loading a prefab and its idle animation is showing.  Then I tell it to play a run animation and it does.  Afterwards I tell it to play the idle animation again but the run animation plays faster.  Thanks for any help.

[code]
    void ModelController::RecursiveSetAnimation(Node* noed, String ani, bool loop, unsigned char layer)
    {
            if (noed->HasComponent<AnimationController>())
            {
                    String fileName = noed->GetVar("fileName").GetString();
     
                    String aniPath = main_->filesystem_->GetProgramDir() + "Data/Models/" + fileName + "/" + ani + ".ani";
     
                    if (main_->cache_->Exists(aniPath))
                    {
                            if (( (noed->GetComponent<AnimationController>()->IsPlaying(aniPath) == false)
                                            && (noed->GetComponent<AnimationController>()->IsFadingIn(aniPath) == false) )
                                            || (noed->GetComponent<AnimationController>()->IsFadingOut(aniPath) == true) )
                            //if (noed->GetComponent<AnimationController>()->IsPlaying(aniPath) == false)
                            {
                                    LOGERRORF("playing %s @ %d",ani.CString(), layer);
                                    noed->GetComponent<AnimationController>()->PlayExclusive(aniPath, layer, loop, 0.25f);
     
                                    if (!loop)
                                    {
                                            noed->GetComponent<AnimationController>()->SetAutoFade(aniPath, 0.25f);
                                    }
                            }
                            else
                            {
                                    return;
                            }
                    }
            }
     
            for (int x = 0; x < noed->GetNumChildren(); x++)
            {
                    RecursiveSetAnimation(noed->GetChild(x), ani, loop, layer);
            }
    }
[/code]

Model in question: [dropbox.com/s/mmgkj3r3mchojye/urho.7z?dl=0](https://www.dropbox.com/s/mmgkj3r3mchojye/urho.7z?dl=0)

-------------------------

cadaver | 2017-01-02 01:07:39 UTC | #2

Using absolute paths (including programdir + "Data") in resource and animation requests shouldn't ever be used, just use names within the resource dirs.

Looks like AnimationController logic of detecting existing animations can get broken, will check it. However it shouldn't be that different to NinjaSnowWar animation switching, which uses PlayExclusive() quite similarly.

-------------------------

cadaver | 2017-01-02 01:07:39 UTC | #3

Pushed a potential fix to master. Duplicate animation states could have been created if you managed to request the animation using a non-canonical (unsanitated) resource name.

-------------------------

