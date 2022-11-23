Lumak | 2017-01-02 01:05:31 UTC | #1

Why does Sprite created using ui->GetRoot()->CreateChild<Sprite>() renders on top of a Sprite created by new Sprite( context_ ) even though the new Sprite has higher priority?

My code sniplet:
[code]
    m_pSplashScreen = new Sprite( context_ );
    m_pSplashScreen->SetTexture( cache->GetResource<Texture2D>("Textures/black128.png") );
    m_pSplashScreen->SetSize( graphics->GetWidth(), graphics->GetHeight() );
    m_pSplashScreen->SetAlignment( HA_LEFT, VA_TOP );
    m_pSplashScreen->SetPriority( 100 );

    m_uiSplashTimerId = SDL_AddTimer( 3000, &Splash_TimerCallback, this );

    Sprite *pSpriteBackground = ui->GetRoot()->CreateChild<Sprite>();
    pSpriteBackground->SetTexture( cache->GetResource<Texture2D>("Textures/free-wallpaper-19.jpg") );
    pSpriteBackground->SetSize( graphics->GetWidth(), graphics->GetHeight() );
    pSpriteBackground->SetAlignment( HA_LEFT, VA_TOP );
    pSpriteBackground->SetPriority( -200 );

[/code]

And m_pSplashScreen is never seen, however, if I construct the m_pSplashScreen using the ui->GetRoot()->CreateChild<Sprite>() method, it becomes visible.

Not sure what's going on.  Any help would be appreciated.

-------------------------

thebluefish | 2017-01-02 01:05:31 UTC | #2

Not sure what you mean by the priority bit. Calling

[code]
new Sprite( context_ );
[/code]

Will create a new Sprite object, but you do nothing to draw it. It needs to be added to the UI subsystem root (or another UIElement) so that the UI subsystem can handle drawing the sprite.

What happens when you create both sprites with ui->GetRoot()->CreateChild<Sprite>(); and then set their individual priority? It's working for me when I add them both to the UI root.

-------------------------

Lumak | 2017-01-02 01:05:31 UTC | #3

I figured it out but you beat me to it. 
Thank you.

-------------------------

