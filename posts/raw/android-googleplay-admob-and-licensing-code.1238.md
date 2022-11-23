Lumak | 2017-01-02 01:06:18 UTC | #1

This exchange covers most of Google Play Services Achievements and Leaderboard, AdMob Banner and Interstitial, and Licensing check.  It doesn't cover in-app purchases, as I haven't had any in-app products to sell.

[b]There are several parts to this exchange.[/b]
I'll start with Java code which will cover an optional part to remove the default shared library loader and replacing it with loading just a single game shared library, things that need to be changed in SDLActivity, what base function declarations are in SDLActivity, and onto a full implementation of it all in a secondary java file.
Then I'll cover JNI functions which will be an intermediary to Java and native code, and onto ServiceCmd singleton class, and wrap it up with a game side sample code.

[b]Edit: this project was built in Android SDK and linked with a library from [url]https://github.com/okamstudio/godot/tree/master/platform/android/libs/play_licensing[/url][/b]

[b][size=150]1) Removing the default shared library loader in SDLActivity (optional)[/size][/b]
This is optional, but I didn't see a point of having this shared library loader for a final product when I just needed to load MyGame.so file.  Nor did I need the screen to change from portrait to landscape when I launched the game.
In SDLActivity.java, starting at line 88.  Look for comment:  // Urho3D: auto load all the shared libraries available in the library path
[ul]
i) Remove lines 88 to line 113.
ii) grep and remove all instances of [b]mIsSharedLibraryLoaded[/b] in the file.   Leave SDLActivity.nativeQuit(); there at line 172. 
iii) replace [b]protected boolean onLoadLibrary()[/b] function with


[code]
    // load the .so
    static {
        System.loadLibrary( "MyGame" );  // actual filename has "lib" prefix and ".so" suffix, e.g. "libMyGame.so" in the jniLibs folder under Android SDK project
                                         // or in libs folder for a non Android SDK project            
    }
[/code]
iv) You no longer need SampleLauncher.java and Urho3D.java files, delete them both.  These will be replaced by MyGame.java
[/ul]

[b][size=150]2) Changes to SDLActivity[/size][/b]
[ul]
i) replace [b]import android.widget.AbsoluteLayout;[/b] with import android.widget.RelativeLayout;  // required for AdView
ii) optional - change private static final String TAG = "SDL"; to [b]protected[/b] if you want to use the TAG in MyGame.java class.
iii) changes starting from [b]onCreate()[/b]: change the layout, declare base class functions, JNI func. and changes to the onXXXX() funcs.
[b]Note:[/b] //LUMAKSOFTWARE comments were added to keep track of where I made the changes to the original code.
[code]
    // Setup
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.v("SDL", "onCreate():" + mSingleton);
        super.onCreate(savedInstanceState);

        SDLActivity.initialize();
        // So we can call stuff from static callbacks
        mSingleton = this;

        // Set up the surface
        mSurface = new SDLSurface(getApplication());

        // SDL standard layout
        //mLayout = new AbsoluteLayout(this);
        mLayout = new RelativeLayout(this);
        mLayout.addView( mSurface );
        setContentView( mLayout );

        // intialize app after mLayout is created
        InitializeApp();

        // rest of setup
        if ( Build.VERSION.SDK_INT >= 12 ) {
            mJoystickHandler = new SDLJoystickHandler_API12();
        }
        else {
            mJoystickHandler = new SDLJoystickHandler();
        }
    }

    // LUMAKSOFTWARE: declare base class funcs
    protected void InitializeApp() {
    }
    protected void PauseApp() {
    }
    protected void ResumeApp() {
    }
    protected void DestroyApp() {
    }
    protected boolean onProcessUserCommand(int command, Object param) { 
        return false; 
    }

    // LUMAKSOFTWARE: user native callback function
    public static native void nativeUserActivityCallback(int val, int istat, String file);

    // Events
    @Override
    protected void onPause() {
        Log.v("SDL", "onPause()");

        // LUMAKSOFTWARE: pause app
        PauseApp();

        super.onPause();
        SDLActivity.handlePause();
    }

    @Override
    protected void onResume() {
        Log.v("SDL", "onResume()");
        super.onResume();
        SDLActivity.handleResume();

        // LUMAKSOFTWARE: resume app
        ResumeApp();
    }

    @Override
    protected void onDestroy() {
        Log.v("SDL", "onDestroy()");

        // LUMAKSOFTWARE: destroy app
        DestroyApp();

        // Send a quit message to the application
        SDLActivity.mExitCalledFromJava = true;
        SDLActivity.nativeQuit();

        // Now wait for the SDL thread to quit
        if (SDLActivity.mSDLThread != null) {
            try {
                SDLActivity.mSDLThread.join();
            } catch(Exception e) {
                Log.v("SDL", "Problem stopping thread: " + e);
            }
            SDLActivity.mSDLThread = null;

            //Log.v("SDL", "Finished waiting for SDL thread");
        }

        super.onDestroy();
        // Reset everything in case the user re opens the app
        SDLActivity.initialize();
    }

[/code]
iv) also replace another place that had AbsoluteLayout with RelativeLayout
[code]
    static class ShowTextInputTask implements Runnable {
        /*
         * This is used to regulate the pan&scan method to have some offset from
         * the bottom edge of the input region and the top edge of an input
         * method (soft keyboard)
         */
        static final int HEIGHT_PADDING = 15;

        public int x, y, w, h;

        public ShowTextInputTask(int x, int y, int w, int h) {
            this.x = x;
            this.y = y;
            this.w = w;
            this.h = h;
        }

        @Override
        public void run() {
            // LUMAKSOFTWARE: AdView requires RelativeLayout - Add adView to the bottom of the screen.
            RelativeLayout.LayoutParams params = new RelativeLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT);
            params.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM);

            //AbsoluteLayout.LayoutParams params = new AbsoluteLayout.LayoutParams(
            //        w, h + HEIGHT_PADDING, x, y);

            if (mTextEdit == null) {
                mTextEdit = new DummyEdit(getContext());

                mLayout.addView(mTextEdit, params);
            } else {
                mTextEdit.setLayoutParams(params);
            }

            mTextEdit.setVisibility(View.VISIBLE);
            mTextEdit.requestFocus();

            InputMethodManager imm = (InputMethodManager) getContext().getSystemService(Context.INPUT_METHOD_SERVICE);
            imm.showSoftInput(mTextEdit, 0);
        }
    }

[/code]
v) changes to the SDLCommandHandler() func.
[code]
    protected static class SDLCommandHandler extends Handler {
        @Override
        public void handleMessage(Message msg) {
            Context context = getContext();
            if (context == null) {
                Log.e(TAG, "error handling message, getContext() returned null");
                return;
            }
            switch (msg.arg1) {
            case COMMAND_CHANGE_TITLE:
                if (context instanceof Activity) {
                    ((Activity) context).setTitle((String)msg.obj);
                } else {
                    Log.e(TAG, "error handling message, getContext() returned no Activity");
                }
                break;
            case COMMAND_TEXTEDIT_HIDE:
                if (mTextEdit != null) {
                    mTextEdit.setVisibility(View.GONE);

                    InputMethodManager imm = (InputMethodManager) context.getSystemService(Context.INPUT_METHOD_SERVICE);
                    imm.hideSoftInputFromWindow(mTextEdit.getWindowToken(), 0);
                }
                break;

            default:
                // LUMAKSOFTWARE: onProcessUserCommand function
                if ((context instanceof SDLActivity) && ((SDLActivity) context).onProcessUserCommand(msg.arg1, msg.obj)) {
                    // returning true means the message was intended for the game/app, 
                    // otherwise process it as a unhandled message
                }
                else if ((context instanceof SDLActivity) && !((SDLActivity) context).onUnhandledMessage(msg.arg1, msg.obj)) {
                    Log.e(TAG, "error handling message, command is " + msg.arg1);
                }
            }
        }
    }

[/code]
[/ul]

[b][size=150]3) MyGame.java code[/size][/b]
This replaces the java files mentioned in option 1).
This is the main code that drives GooglePlay, AdMob, and License functions, class extends SDLActivity overriding the base class functions that we declared in step 2).
[code]
//=============================================================================
// Copyright (c) 2015 LumakSoftware
//=============================================================================
package com.mycompany.mygame;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

import org.libsdl.app.SDLActivity;

import android.content.Intent;

import android.widget.RelativeLayout;
import android.content.*;
import android.view.*;
import android.os.*;
import android.util.Log;

//============================================
// imports for licensing, admob and googleAPI
//============================================
import com.google.android.vending.licensing.LicenseChecker;
import com.google.android.vending.licensing.LicenseCheckerCallback;
import com.google.android.vending.licensing.Policy;
import com.google.android.vending.licensing.ServerManagedPolicy;
import com.google.android.vending.licensing.AESObfuscator;

import com.google.android.gms.ads.AdRequest;
import com.google.android.gms.ads.AdSize;
import com.google.android.gms.ads.AdView;
import com.google.android.gms.ads.AdListener;
import com.google.android.gms.ads.InterstitialAd;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.GooglePlayServicesUtil;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.games.Games;
import com.google.android.gms.games.Player;
import com.google.android.gms.plus.Plus;

// game R string values
import com.mycompany.mygame.R;

//=============================================================================
// game/app class
//=============================================================================
public class MyGame extends SDLActivity implements GoogleApiClient.ConnectionCallbacks,
        GoogleApiClient.OnConnectionFailedListener {

    // google API
    private GoogleApiClient mGoogleApiClient;
    private static final int DBG_GCONNECT = 1;
    private static final int RC_SIGN_IN = 9001;
    private static final int RC_UNUSED = 5001;

    // AdMob
    private InterstitialAd mInterstitialAd;
    private AdView mAdView;
    private AdRequest mAdRequest;
    private static final boolean DBG_ADMOB_TESTMODE = true;

    private static final byte[] SALT = new byte[] {
            -46,  63, 30, -77, -153, -59,  74, -64, 51, 88,
            -95, -45, 77, -167, -33, -133, -15, 32, -64, 89
    };

    // license
    private LicenseCheckerCallback mLicenseCheckerCallback;
    private LicenseChecker mChecker;
    private int miLicenseCheckRetries;

    //=================================
    // LUMAKSOFTWARE: func overrides
    //=================================
    @Override
    protected void InitializeApp(){

        // google api
        CreateGoogleAPI();

        // licensing - uncomment for test or for in-app purchase stuff
        //CreateLicenseCheck();

        // AdMob - only create the AdRequest on init, interstitial and adview are created on command
        CreateAdRequest();
    }

    @Override
    protected void PauseApp() {
        // pause AdView
        PauseAdView();
    }

    @Override
    protected void ResumeApp() {
        // resume AdView
        ResumeAdView();
    }

    @Override
    protected void DestroyApp(){

        if ( mChecker != null )
        {
            mChecker.onDestroy();
            mChecker = null;
        }

        // AdView
        DestroyAdView();

        // disconnect
        if ( isSignedIn() ){
            mGoogleApiClient.disconnect();
        }
    }

    // LUMAKSOFTWARE: onProcessUserCommand function 
    @Override
    protected boolean onProcessUserCommand(int command, Object param) {

        boolean bresult = false;
        int iParam = (int)param;
        int iHasFocus = hasWindowFocus()?1:0;

        //if ( command != COMMAND_WINDOW_HAS_FOCUS )
        //{
        //    Log.i("SDL", "onProcessUserCommand() cmd=" + command + ", param=" + iParam);
        //}

        switch ( command ) 
        {
        case COMMAND_ADMOB_REQUEST_VIDEO:
            CreateInterstitialAd();

            if ( mInterstitialAd != null )
            {
                if ( mInterstitialAd.isLoaded() )
                {
                    nativeUserActivityCallback( COMMAND_ADMOB_STATE_VIDEO, ADMOB_STATE_VIDEO_LOADED, " ");
                }
                else
                {
                    mInterstitialAd.loadAd(mAdRequest);
                }
            }
            bresult = true;
            break;

        case COMMAND_ADMOB_SHOW_VIDEO:
            if ( mInterstitialAd != null && mInterstitialAd.isLoaded()) {
                mInterstitialAd.show();
                nativeUserActivityCallback(COMMAND_ADMOB_STATE_VIDEO, ADMOB_STATE_VIDEO_PLAYING, " ");
            }

            bresult = true;
            break;

        case COMMAND_ADMOB_HIDE_VIDEO:
            // video hides itself, and the game is minimized while the video is playing - do nothing
            bresult = true;
            break;

        case COMMAND_ADMOB_DELETE_VIDEO:
            if ( mInterstitialAd != null ) 
            {
                mInterstitialAd = null;

                nativeUserActivityCallback(COMMAND_ADMOB_STATE_VIDEO, ADMOB_STATE_VIDEO_DESTROYED, " ");
            }
            bresult = true;
            break;

        case COMMAND_ADMOB_REQUEST_BANNER:
            CreateAdView();

            if ( mAdView != null )
            {
                mAdView.loadAd( mAdRequest );
            }

            bresult = true;
            break;

        case COMMAND_ADMOB_SHOW_BANNER:
            if ( mAdView != null )
            {
                mAdView.setVisibility( View.VISIBLE );
                nativeUserActivityCallback(COMMAND_ADMOB_STATE_BANNER, ADMOB_STATE_BANNER_VISIBLE, " ");
            }
            bresult = true;
            break;

        case COMMAND_ADMOB_HIDE_BANNER:
            if ( mAdView != null )
            {
                mAdView.setVisibility( View.GONE );
                nativeUserActivityCallback(COMMAND_ADMOB_STATE_BANNER, ADMOB_STATE_BANNER_HIDDEN, " ");
            }
            bresult = true;
            break;

        case COMMAND_ADMOB_DELETE_BANNER:
            if ( mAdView != null )
            {
                mAdView.destroy();
                mAdView = null;
                nativeUserActivityCallback( COMMAND_ADMOB_STATE_BANNER, ADMOB_STATE_BANNER_DESTROYED, " " );
            }
            bresult = true;
            break;

        case COMMAND_LICENSE_QUERY:
            if ( mChecker != null )
            {
                mChecker.checkAccess(mLicenseCheckerCallback);
            }
            bresult = true;
            break;

        case COMMAND_GOOGLEAPI_CONNECT:
            if ( !isSignedIn() ){
                mGoogleApiClient.connect();
            }
            bresult = true;
            break;

        case COMMAND_GOOGLEAPI_DISCONNECT:
            if ( isSignedIn() ){
                mGoogleApiClient.disconnect();
            }
            bresult = true;
            break;

        case COMMAND_ACHIEVEMENT_QUERY:
            ShowAchievementsRequested();
            bresult = true;
            break;

        case COMMAND_ACHIEVEMENT_SUBMIT:
            UnlockAchievement(iParam);
            bresult = true;
            break;

        case COMMAND_LEADERBOARD_QUERY:
            ShowLeaderboardsRequested();
            bresult = true;
            break;

        case COMMAND_LEADERBOARD_SUBMIT:
            bresult = true;
            break;

        case COMMAND_LEADERBOARD_SETTIME_1:
        case COMMAND_LEADERBOARD_SETTIME_2:
        case COMMAND_LEADERBOARD_SETTIME_3:
        case COMMAND_LEADERBOARD_SETTIME_4:
        case COMMAND_LEADERBOARD_SETTIME_5:
        case COMMAND_LEADERBOARD_SETTIME_6:
            SubmitLeaderboardScore( command - COMMAND_LEADERBOARD_SETTIME_1, iParam  );
            bresult = true;
            break;

        case COMMAND_WINDOW_HAS_FOCUS:
            nativeUserActivityCallback(COMMAND_WINDOW_HAS_FOCUS, iHasFocus, " ");
            bresult = true;
            break;

        default:
        }

        return bresult;
    }

    //================================
    // static vars
    //================================
    // AdMob
    static final int COMMAND_ADMOB_REQUEST_VIDEO = 4;
    static final int COMMAND_ADMOB_SHOW_VIDEO    = 5;
    static final int COMMAND_ADMOB_HIDE_VIDEO    = 6;
    static final int COMMAND_ADMOB_DELETE_VIDEO  = 7;

    static final int COMMAND_ADMOB_REQUEST_BANNER = 8;
    static final int COMMAND_ADMOB_SHOW_BANNER    = 9;
    static final int COMMAND_ADMOB_HIDE_BANNER    = 10;
    static final int COMMAND_ADMOB_DELETE_BANNER  = 11;

    // Licensing
    static final int COMMAND_LICENSE_QUERY  = 12;
    static final int COMMAND_LICENSE_RETRY  = 13;
    static final int COMMAND_LICENSE_FAILED = 14;

    // GoogleApi
    static final int COMMAND_GOOGLEAPI_CONNECT    = 15;
    static final int COMMAND_GOOGLEAPI_ERROR      = 16;
    static final int COMMAND_GOOGLEAPI_DISCONNECT = 17;

    // achievement
    static final int COMMAND_ACHIEVEMENT_QUERY  = 18;
    static final int COMMAND_ACHIEVEMENT_SUBMIT = 19;

    // leaderboard
    static final int COMMAND_LEADERBOARD_QUERY  = 20;
    static final int COMMAND_LEADERBOARD_SUBMIT = 21;

    static final int COMMAND_LEADERBOARD_SETTIME_1 = 22;
    static final int COMMAND_LEADERBOARD_SETTIME_2 = 23;
    static final int COMMAND_LEADERBOARD_SETTIME_3 = 24;
    static final int COMMAND_LEADERBOARD_SETTIME_4 = 25;
    static final int COMMAND_LEADERBOARD_SETTIME_5 = 26;
    static final int COMMAND_LEADERBOARD_SETTIME_6 = 27;

    // misc
    static final int COMMAND_WINDOW_HAS_FOCUS   = 28;

    // states
    static final int COMMAND_ADMOB_STATE_APP    = 1000;
    static final int COMMAND_ADMOB_STATE_VIDEO  = 1001;
    static final int  ADMOB_STATE_VIDEO_LOADED    = 0;
    static final int  ADMOB_STATE_VIDEO_PLAYING   = 1;
    static final int  ADMOB_STATE_VIDEO_CLOSED    = 2;
    static final int  ADMOB_STATE_VIDEO_DESTROYED = 3;
    static final int  ADMOB_STATE_VIDEO_ERROR     = 4;
    static final int COMMAND_ADMOB_STATE_BANNER = 1002;
    static final int  ADMOB_STATE_BANNER_LOADED    = 0;
    static final int  ADMOB_STATE_BANNER_VISIBLE   = 1;
    static final int  ADMOB_STATE_BANNER_HIDDEN    = 2;
    static final int  ADMOB_STATE_BANNER_DESTROYED = 3;
    static final int  ADMOB_STATE_BANNER_ERROR     = 4;
    
    // size declaration
    static final int APP_SIZE_NUM_ACHIEVEMENTS  = 9;
    static final int APP_SIZE_NUM_LEADERBOARD   = 6; // should match COMMAND_LEADERBOARD_SETTIME_1 to last leaderboard settime

    //================================
    // googleAPI
    //================================
    protected void CreateGoogleAPI() {
        // instantiate
        mGoogleApiClient = new GoogleApiClient.Builder(this)
                .addConnectionCallbacks( this )
                .addOnConnectionFailedListener(this)
                .addApi(Plus.API).addScope(Plus.SCOPE_PLUS_LOGIN)
                .addApi(Games.API).addScope(Games.SCOPE_GAMES)
                .build();
    }

    //================================
    // license
    //================================
    private class MyLicenseCheckerCallback implements LicenseCheckerCallback {
        // void allow()
        public void allow(int reason) {
            Log.v("SDL", "allow()" + reason);
            nativeUserActivityCallback(COMMAND_LICENSE_QUERY, 0, "OK");
            if (isFinishing()) {
                // Don't update UI if Activity is finishing.
                return;
            }
        }

        // void dontAllow
        public void dontAllow(int reason) {
            Log.v("SDL", "dontAllow()" + reason);

            if (isFinishing()) {
                // Don't update UI if Activity is finishing.
                return;
            }

            if (reason == Policy.RETRY) {
                // If the reason received from the policy is RETRY, it was probably
                // due to a loss of connection with the service, so we should give the
                // user a chance to retry. So show a dialog to rety.
                //showDialog(DIALOG_RETRY); COMMAND_LICENSE_RETRY
                nativeUserActivityCallback(COMMAND_LICENSE_RETRY, 0, "OK");
            } else {
                // Otherwise, the user is not licensed to use this app.
                // Your response should always inform the user that the application
                // is not licensed, but your behavior at that point can vary. You might
                // provide the user a limited access version of your app or you can
                // take them to Google Play to purchase the app.
                //showDialog(DIALOG_GOTOMARKET);
                nativeUserActivityCallback(COMMAND_LICENSE_FAILED, reason, "OK");
            }
        }

        // void applicationError()
        public void applicationError(int errorCode){
            Log.v("SDL", "MyLicenseCheckerCallback() app error" + errorCode);
            // error 3 - not published in google play, just mark it as 'ok' for testing
            if ( errorCode == 3 ) {
                nativeUserActivityCallback(COMMAND_LICENSE_QUERY, 0, "OK");
            }
        }

    }

    // licensing
    protected void CreateLicenseCheck() {

        // Construct the LicenseCheckerCallback. The library calls this when done.
        mLicenseCheckerCallback = new MyLicenseCheckerCallback();

        // Construct the LicenseChecker with a Policy.
        mChecker = new LicenseChecker(
                this, new ServerManagedPolicy(this,
                new AESObfuscator(SALT, getPackageName(), getResources().getString(R.string.app_id) )),
                getResources().getString(R.string.BASE64_PUBLIC_KEY)  // Your public licensing key.
                );
    }

    //================================
    // AdRequest
    //================================
    protected void CreateAdRequest() {

        if ( mAdRequest != null )
        {
            return;
        }

        if ( !DBG_ADMOB_TESTMODE )
        {
            // live mode
            mAdRequest = new AdRequest.Builder().build();

        } else {
            // test mode
            mAdRequest = new AdRequest.Builder()
                                      // the string below is not populated at the beginning and you should comment it out the 
                                      // first time you run it then grep for addTestDevice in logcat to get it
                                      .addTestDevice( "AF9C9F5B6C6595D55D1E9A9B07011546" )  // add as many test devices as you want
                                      .addTestDevice( AdRequest.DEVICE_ID_EMULATOR )
                                      .build();
        }
    }

    //================================
    // AdView
    //================================
    protected void CreateAdView() {

        if ( mAdView != null )
        {
            return;
        }

        mAdView = new AdView(this);
        mAdView.setAdUnitId( getResources().getString(R.string.banner_ad_unit_id) );

        mAdView.setAdSize(AdSize.SMART_BANNER);

        // set the layer type as LAYER_TYPE_SOFTWARE to avoid getting the black screen of death (will avoid most of them, not all)
        mAdView.setLayerType(View.LAYER_TYPE_SOFTWARE, null);

        // Add adView to the bottom of the screen.
        RelativeLayout.LayoutParams adParams = new RelativeLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        //adParams.addRule(RelativeLayout.ALIGN_PARENT_TOP);
        adParams.addRule(RelativeLayout.ALIGN_PARENT_LEFT);

        // add it to the layout
        mLayout.addView(mAdView, adParams);

        mAdView.setAdListener( new AdListener() {
            @Override
            public void onAdLoaded() {
                // Code to be executed when an ad finishes loading.
                nativeUserActivityCallback( COMMAND_ADMOB_STATE_BANNER, ADMOB_STATE_BANNER_LOADED, " " );
                //Log.i("SDL", "ADMOB_STATE_BANNER_LOADED" );
            }

            @Override
            public void onAdFailedToLoad(int errorCode) {
                // Code to be executed when an ad request fails.
                String strError = Integer.toString( errorCode );
                nativeUserActivityCallback( COMMAND_ADMOB_STATE_BANNER, ADMOB_STATE_BANNER_ERROR, strError );
            }

            //@Override
            public void onAdClosed() {
                // Code to be executed when when the user is about to return
                // to the application after tapping on an ad.
                nativeUserActivityCallback(COMMAND_ADMOB_STATE_BANNER, ADMOB_STATE_BANNER_HIDDEN, " ");
                //Log.i("SDL", "-- mAdView -- onAdClosed() " );
            }
        });
    }

    protected void PauseAdView() {
        if ( mAdView != null ) {
            mAdView.pause();
        }
    }

    protected void ResumeAdView() {

        if ( mAdView != null ) {
            mAdView.resume();
        }
    }

    protected void DestroyAdView() {

        if ( mAdView != null ) {
            mAdView.destroy();
            mAdView = null;
        }
    }

    //================================
    // interstitial
    //================================
    protected void CreateInterstitialAd() {

        if ( mInterstitialAd != null )
        {
            return;
        }

        mInterstitialAd = new InterstitialAd(this);
        mInterstitialAd.setAdUnitId(getResources().getString(R.string.interstitial_ad_unit_id));

        mInterstitialAd.setAdListener(new AdListener() {
            @Override
            public void onAdLoaded() {
                // Code to be executed when an ad finishes loading.
                nativeUserActivityCallback(COMMAND_ADMOB_STATE_VIDEO, ADMOB_STATE_VIDEO_LOADED, " ");
                Log.i("SDL", "ADMOB_STATE_VIDEO_LOADED" );
            }

            @Override
            public void onAdFailedToLoad(int errorCode) {
                // Code to be executed when an ad request fails.
                Log.v(TAG, "Interstitial - onAdFailedToLoad() error=" + errorCode);
                String strError = Integer.toString(errorCode);
                nativeUserActivityCallback(COMMAND_ADMOB_STATE_VIDEO, ADMOB_STATE_VIDEO_ERROR, strError);
            }

            @Override
            public void onAdClosed() {
                // Code to be executed when when the user is about to return
                // to the application after tapping on an ad.
                nativeUserActivityCallback(COMMAND_ADMOB_STATE_VIDEO, ADMOB_STATE_VIDEO_CLOSED, " ");
                Log.i("SDL", "ADMOB_STATE_VIDEO_CLOSED" );
            }
        });

    }

    //================================
    // google api - connect 
    //================================
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent intent) {

        super.onActivityResult(requestCode, resultCode, intent);

        if (requestCode == RC_SIGN_IN) {
            if (resultCode == RESULT_OK) {
                mGoogleApiClient.connect();
            } else {
                nativeUserActivityCallback( COMMAND_GOOGLEAPI_ERROR, resultCode, "1" );
            }
        }
    }

    @Override
    public void onConnected(Bundle bundle) {
        //Log.d(TAG, "onConnected(): ");
        
        // uncomment below if you want to get the playa's name
        //Player p = Games.Players.getCurrentPlayer(mGoogleApiClient);
        String displayName = "playa";

        //if (p == null) {
        //    Log.w(TAG, "mGamesClient.getCurrentPlayer() is NULL!");
        //    displayName = "???";
        //} else {
        //    displayName = p.getDisplayName();
        //}

        nativeUserActivityCallback(COMMAND_GOOGLEAPI_CONNECT, 1, displayName);
    }

    @Override
    public void onConnectionSuspended(int var1) {
        mGoogleApiClient.connect();
        Log.d(TAG, "onConnectionSuspended():");
    }

    @Override
    public void onConnectionFailed(ConnectionResult connectionResult) {
        Log.d(TAG, "onConnectionFailed(): attempting to resolve");

        if ( connectionResult.hasResolution() ) {
            try {
                connectionResult.startResolutionForResult(this, RC_SIGN_IN);
            } catch (IntentSender.SendIntentException e) {
                // The intent was canceled before it was sent.  Return to the default
                // state and attempt to connect to get an updated ConnectionResult.
                mGoogleApiClient.connect();
            }
        } else {
            // not resolvable... so show an error message
            int errorCode = connectionResult.getErrorCode();
            nativeUserActivityCallback( COMMAND_GOOGLEAPI_ERROR, errorCode, " " );
        }

    }
    private boolean isSignedIn() {
        return (mGoogleApiClient != null && mGoogleApiClient.isConnected());
    }

    //================================
    // achievement and leaderboard
    //================================
    public void ShowAchievementsRequested() {
        if ( isSignedIn() ) 
        {
            startActivityForResult(Games.Achievements.getAchievementsIntent(mGoogleApiClient), RC_UNUSED );
        }
    }

    public void UnlockAchievement(int _idx) {
        if ( isSignedIn() && _idx >= 0 && _idx < APP_SIZE_NUM_ACHIEVEMENTS )
        {
            String[] astrAchievementNames = getResources().getStringArray(R.array.achievement_array);

            //Log.v("SDL", "UnlockAchievement() idx=" + _idx + ", str='" + astrAchievementNames[_idx] + "'" );
            Games.Achievements.unlock(mGoogleApiClient, astrAchievementNames[_idx]);
        }
    }

    public void ShowLeaderboardsRequested() {
        if ( isSignedIn() ) 
        {
            startActivityForResult(Games.Leaderboards.getAllLeaderboardsIntent(mGoogleApiClient), RC_UNUSED);
        }
    }

    public void SubmitLeaderboardScore(int _idx, int _iTime) {
        if ( isSignedIn() && _idx >= 0 && _idx < APP_SIZE_NUM_LEADERBOARD )
        {
            long lTime = _iTime;
            String[] astrLBNames = getResources().getStringArray(R.array.leaderboard_array);

            //Log.v("SDL", "SubmitLeaderboardScore() idx=" + _idx + ", str='" + astrLBNames[_idx] + "'" );
            Games.Leaderboards.submitScore(mGoogleApiClient, astrLBNames[_idx], lTime);
        }
    }

}
[/code]

[b]IDs, achievement, and leaderboard strings[/b]
[code]
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_id">10XXXXXX130</string>
    <string name="banner_ad_unit_id">ca-app-pub-4xxxxxxxx/1xxxxxxxx</string>
    <string name="interstitial_ad_unit_id">ca-app-pub-4xxxxxx/31xxxxxxx</string>
    <string name="BASE64_PUBLIC_KEY">MIIBIjAxxxxxxxxxxxxxxxxxxxxxBCgKCAQEAkF4wRG9st6jp0qqswPsk0UgzWg/hkj3yzGGxr2o+ogLYbCwrqZsk7x7mDAvC277Je+xmBiKFCXp/qnR3xyW02xp3aebIr8dOUeRovJdbNYhOaRar+5gGOkFABxzcpykftaEhalHV5XSwRJmSQIox220/P/1bRoOgCKnzo9Qm81SzvjaMmnz27joAdPkdP7MLinR7N4tuCgh4UqlrevoAx1XIYLdCziMPR2YQ5lCNOuLM5VtPMc4djAPw3RNfgpPJgD0xbRqlvpdk0DXzlVPuSo/tuqsCRtFK2GSb0cM1oU/pJzCASp66SC+VztgvLhxjcFvSXb7iQ/STRL3kP0r0gwIDAQAB</string>
</resources>

[/code]
You get the following tags from Google Play Developer Console when you create achievements and leaderboard for you game/app.
[code]
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">MyGame</string>
    <string-array name="achievement_array">
        <item>CgkIyusYYYuIQAQ</item> <!-- novice    -->
        <item>CgkIyuYYYYeIQAg</item> <!-- skilled    -->
        <item>CgkIyuYYYYYIQAw</item> <!-- advanced    -->
        <item>CgkIyuYYseEAIQBA</item> <!-- expert    -->
        <item>CgkIsYYYYYEAIQBQ</item> <!-- master    -->
        <item>CgkIyufYYYYYeuBg</item> <!-- apprentice    -->
        <item>CgkIyufYYYYYeuw</item> <!-- journeyman    -->
        <item>CgkIyufYYYYYeuCA</item> <!-- master craftsman  -->
        <item>CgkIyufYYYYeYuCQ</item> <!-- gold    -->
    </string-array>
    <string-array name="leaderboard_array">
        <item>CgkIyYYyyyYufeuCg</item> <!-- stage 1    -->
        <item>CgkIyYYYYufeuQCw</item> <!-- stage 2    -->
        <item>CgkIyufYYYYYuQDA</item> <!-- stage 3    -->
        <item>CgkIyuYYYYYeuQDQ</item> <!-- stage 4    -->
        <item>CgkIyufYYYYYeuQDg</item> <!-- stage 5    -->
        <item>CgkIyufYYYYYeuQDw</item> <!-- artists    -->
    </string-array>

</resources>

[/code]
[b][size=150]4) JNI functions[/size][/b]
Java function [b]sendMessage(int, int)[/b] already exists and is called from [b]Android_JNI_SendMessage(int, int)[/b].
This part covers the Java function [b]public static native void nativeUserActivityCallback(int val, int istat, String file);[/b] that we declared in SDLActiviy in section 2).  Along with a callback function that we need to hook into from game side.
[code]
typedef void (*pfnUserActivityCallback)(int id1, int istat, const char *str, void *param);

static pfnUserActivityCallback gpUserActivityCallback = NULL;
static void *gActivityCallbackParam = NULL;

void RegisterUserActivityCallback(pfnUserActivityCallback callback, void *param)
{
    gpUserActivityCallback = callback;
    gActivityCallbackParam = param;
}

void Java_org_libsdl_app_SDLActivity_nativeUserActivityCallback(JNIEnv* env, jclass cls, jint id1, jint istat, jstring jstrParam)
{
    const char *str = (*env)->GetStringUTFChars(env, jstrParam, 0);

    if ( gpUserActivityCallback )
    {
        (*gpUserActivityCallback)( id1, istat, str, gActivityCallbackParam );
    }

    if ( str )
    {
        (*env)->ReleaseStringUTFChars(env, jstrParam, str);
    }

}

[/code]
[b][size=150]5) ServiceCmd singleton class[/size][/b]
This class handles messages to/from the Java class. It is designed as a singleton to allow access from main game class, classes to access achievement and leaderboard calls, and other classes.
[b]Note:[/b]This class is not thread safe, however, AdMob messages are state driven and the game side is also state driven to reduce the chance of over writing status during AdMob activities
ServiceCmd.cpp
[code]
//=============================================================================
// Copyright (c) 2015 LumakSoftware
//=============================================================================
#include <Urho3D/Urho3D.h>
#include <Urho3D/Core/CoreEvents.h>
#include <Urho3D/Core/Context.h>
#include <Urho3D/Engine/Engine.h>
#include <Urho3D/Input/InputEvents.h>
#include <Urho3D/Scene/Scene.h>
#include <Urho3D/Core/Timer.h>

#include "ServiceCmd.h"

#include <Urho3D/DebugNew.h>
#include <SDL/SDL_Log.h>
#include <SDL/SDL_assert.h>

//=============================================================================
//=============================================================================
#ifdef WIN32
typedef void (*pfnUserActivityCallback)(int id1, int istat, const char *str, void *param);

static pfnUserActivityCallback gpFnUserActivityCallback = NULL;
static void *gpActivityCallbackParam = NULL;

void RegisterUserActivityCallback(pfnUserActivityCallback callback, void *param)
{
}

int Android_JNI_SendMessage(int command, int param)
{
    return 0;
}
#endif

//#define DBG_DUMP_SVCLOG

//=============================================================================
//=============================================================================
ServiceCmd* ServiceCmd::s_pCAdMob = NULL;

//=============================================================================
//=============================================================================
ServiceCmd::ServiceCmd(Context *_pcontext)
    : Object( _pcontext )
{
    // init
    m_TimerWindowFocus.Reset();
    m_TimerVideo.Reset();
    m_TimerBanner.Reset();
    m_TimerLicense.Reset();

    // focus
    m_bWindowHasFocus = true;

    // connect
    m_bGooglePlayConnected = false; 
    m_strGooglePlayUserName.Clear();    
    m_iConnectErrorCode = INVALID_CONNECT_CODE;    

    // admob
    m_uAdInterval = 2 * 60 * 1000; // 2 mins
    m_iCmdTimeout = 5;
    m_bAdPlayedSinceStartup = false;

    m_iVideoState = kAdMobVideo_Ready;
    m_iBannerState = kAdMobBanner_NotLoaded;
    m_HasVideoPlayedOnce = false;
    m_bAppIsPaused = false;

    // license
    m_bContinueLicenseQuery = true;
    m_bLicenseQueryMade = false;
    m_bHasValidLicense = false;
    m_bHasLicenseQueryResp = false;
    m_iLicenseResp = -1;
    
    // register java callback
    RegisterUserActivityCallback( &ServiceCmd::JavaActivityCallback, this );
}

//=============================================================================
//=============================================================================
ServiceCmd::~ServiceCmd()
{
    RegisterUserActivityCallback( NULL, NULL );
}

//=============================================================================
//=============================================================================
void ServiceCmd::JavaActivityCallback(int _ival, int _istat, const char *_pstr, void *param)
{
    if ( param )
    {
        ((ServiceCmd*)param)->ActivityCallback( _ival, _istat, _pstr );
    }
}

//=============================================================================
//=============================================================================
void ServiceCmd::ActivityCallback(int _icmd, int _istat, const char *_pstr)
{
    #ifdef DBG_DUMP_SVCLOG
    if ( _icmd != COMMAND_WINDOW_HAS_FOCUS )
    {
        SDL_Log("ServiceCmd::ActivityCallback() icmd=%d, istat=%d, pstr='%s'\n", _icmd, _istat, _pstr?_pstr:" ");
    }
    #endif

    switch ( _icmd )
    {
    case COMMAND_ADMOB_STATE_VIDEO:
        switch ( _istat )
        {
        case kAdMobVideo_Stat_Loaded:    m_iVideoState = kAdMobVideo_Loaded; break;
        case kAdMobVideo_Stat_Playing:   m_iVideoState = kAdMobVideo_Playing; break;
        case kAdMobVideo_Stat_Closed:    m_iVideoState = kAdMobVideo_Ready; ResetVideoTimer(); break;
        case kAdMobVideo_Stat_Destroyed: m_iVideoState = kAdMobVideo_Ready; break;
        default: 
            // failed to load error - retry
            ResetVideoTimer();
            break;
        }
        break;

    case COMMAND_ADMOB_STATE_BANNER:
        switch ( _istat )
        {
        case kAdMobBanner_Stat_Loaded:    
            if ( m_iBannerState == kAdMobBanner_NotLoaded || m_iBannerState == kAdMobBanner_Requested )
            {
                m_iBannerState = kAdMobBanner_Ready;
            }
            // AdMob banner continuously loads new banners in the background, and any subsequent calls will automatically show itself
            // -- prevent it from being visible if not in the visible state
            else if ( m_iBannerState != kAdMobBanner_Visible )
            {
                RequestServiceCmd( COMMAND_ADMOB_HIDE_BANNER );
            }
            break;
        case kAdMobBanner_Stat_Visible:   m_iBannerState = kAdMobBanner_Visible; break;
        case kAdMobBanner_Stat_Hidden:    m_iBannerState = kAdMobBanner_Hidden; break;
        case kAdMobBanner_Stat_Destroyed: m_iBannerState = kAdMobBanner_NotLoaded; break;
        default:
            // failed to load error - retry
            ResetBannerTimer();
            break;
        }
        break;

    case COMMAND_GOOGLEAPI_CONNECT:
        if ( _istat == 1 )
        {
            m_bGooglePlayConnected = true;

            if ( _pstr )
            {
                m_strGooglePlayUserName = String( _pstr );
            }
            #ifdef DBG_DUMP_SVCLOG
            SDL_Log("COMMAND_GOOGLEAPI_CONNECT username='%s'\n", m_strGooglePlayUserName.CString() );
            #endif
        }
        else
        {
            m_bGooglePlayConnected = false;
        }
        break;

    case COMMAND_GOOGLEAPI_ERROR:
        m_iConnectErrorCode = _istat;
        break;

    case COMMAND_LICENSE_QUERY:
    case COMMAND_LICENSE_RETRY:
    case COMMAND_LICENSE_FAILED:
        m_bHasLicenseQueryResp = true;

        if ( _icmd == COMMAND_LICENSE_QUERY )
        {
            m_bHasValidLicense = true;
            m_iLicenseResp = 0;
        }
        else if ( _icmd == COMMAND_LICENSE_RETRY )
        {
            m_iLicenseResp = COMMAND_LICENSE_RETRY;
        }
        else
        {
            m_iLicenseResp = COMMAND_LICENSE_FAILED;
        }
        break;

    case COMMAND_WINDOW_HAS_FOCUS:
        m_bWindowHasFocus = _istat?true:false;
        break;

    }
}

//=============================================================================
//=============================================================================
void ServiceCmd::RequestServiceCmd(int _iCmdType, int _iSubCmd)
{
    if ( _iCmdType >= COMMAND_ADMOB_REQUEST_VIDEO && _iCmdType < COMMAND_END )
    {
        #ifdef DBG_DUMP_SVCLOG
        if ( _iCmdType != COMMAND_WINDOW_HAS_FOCUS )
        {
            SDL_Log( "ServiceCmd::RequestServiceCmd() _iCmdType=%d, sub=%d\n", _iCmdType, _iSubCmd );
        }
        #endif

        Android_JNI_SendMessage( _iCmdType, _iSubCmd );

        switch ( _iCmdType )
        {
        case COMMAND_WINDOW_HAS_FOCUS:   
            ResetWindowFocusTimer(); 
            break;

        case COMMAND_GOOGLEAPI_CONNECT:
            m_iConnectErrorCode = INVALID_CONNECT_CODE;
            break;

        //========================
        // admob video
        case COMMAND_ADMOB_REQUEST_VIDEO:   
            m_TimerVideo.Reset();
            m_iVideoState = kAdMobVideo_Requested;
            break;

        case COMMAND_ADMOB_SHOW_VIDEO:  
            m_HasVideoPlayedOnce = true;
            m_TimerVideo.Reset();
            m_TimerBanner.Reset();
            break;

        case COMMAND_ADMOB_HIDE_VIDEO:    
            // can't really send a request to hide video  
            break;

        case COMMAND_ADMOB_DELETE_VIDEO:    
            m_iVideoState = kAdMobVideo_Ready;
            break;

        //========================
        // admob banner
        case COMMAND_ADMOB_REQUEST_BANNER:  
            m_iBannerState = kAdMobBanner_Requested;
            m_TimerBanner.Reset();
            break;

        case COMMAND_ADMOB_SHOW_BANNER:
            m_TimerBanner.Reset();
            break;

        case COMMAND_ADMOB_HIDE_BANNER:
            break;

        case COMMAND_ADMOB_DELETE_BANNER:     
            break;

        case COMMAND_LICENSE_QUERY:
            m_bLicenseQueryMade = true;
            m_bHasLicenseQueryResp = false;
            m_iLicenseResp = -1;

            m_TimerLicense.Reset();
            break;
        }
    }
    else 
    {
        #ifdef DBG_DUMP_SVCLOG
        SDL_Log( "ServiceCmd::StartAd() unknown add type=%d\n", _iCmdType );
        #endif
    }
}

//=============================================================================
//=============================================================================
void ServiceCmd::SendUnlockAchievement(unsigned _idx)
{
    if ( _idx < APP_SIZE_NUM_ACHIEVEMENTS )
    {
        RequestServiceCmd( COMMAND_ACHIEVEMENT_SUBMIT, _idx );
    }
}

//=============================================================================
//=============================================================================
void ServiceCmd::SendLeaderboardUpdate(unsigned _idx, unsigned _uNumUnits)
{
    if ( _idx < APP_SIZE_NUM_LEADERBOARD )
    {
        RequestServiceCmd( COMMAND_LEADERBOARD_SETTIME_BEG + _idx, (int)_uNumUnits );
    }
}
[/code]
ServiceCmd.h
[code]
//=============================================================================
// Copyright (c) 2015 LumakSoftware
//=============================================================================
#pragma once



using namespace Urho3D;

//=============================================================================
//=============================================================================
#define INVALID_CONNECT_CODE    51123333 // arbitrary value

enum APPJAVASERVICECOMMANDS
{
    // admob
    COMMAND_ADMOB_REQUEST_VIDEO  = 4,
    COMMAND_ADMOB_SHOW_VIDEO     = 5,
    COMMAND_ADMOB_HIDE_VIDEO     = 6,
    COMMAND_ADMOB_DELETE_VIDEO   = 7,

    COMMAND_ADMOB_REQUEST_BANNER = 8,
    COMMAND_ADMOB_SHOW_BANNER    = 9,
    COMMAND_ADMOB_HIDE_BANNER    = 10,
    COMMAND_ADMOB_DELETE_BANNER  = 11,

    // Licensing
    COMMAND_LICENSE_QUERY    = 12,
    COMMAND_LICENSE_RETRY    = 13,
    COMMAND_LICENSE_FAILED   = 14,

    // GoogleApi
    COMMAND_GOOGLEAPI_CONNECT     = 15,
    COMMAND_GOOGLEAPI_ERROR       = 16,
    COMMAND_GOOGLEAPI_DISCONNECT  = 17,

    // achievement
    COMMAND_ACHIEVEMENT_QUERY   = 18,
    COMMAND_ACHIEVEMENT_SUBMIT  = 19,

    // leaderboard
    COMMAND_LEADERBOARD_QUERY      = 20,
    COMMAND_LEADERBOARD_SUBMIT     = 21,

    COMMAND_LEADERBOARD_SETTIME_BEG = COMMAND_LEADERBOARD_SUBMIT + 1,
    COMMAND_LEADERBOARD_SETTIME_END = COMMAND_LEADERBOARD_SETTIME_BEG + 5,

    // misc
    COMMAND_WINDOW_HAS_FOCUS = 28,

    // end of valid commands
    COMMAND_END, 

    // response only, not a valid command to send
    COMMAND_ADMOB_STATE_APP    = 1000,
    COMMAND_ADMOB_STATE_VIDEO  = 1001,
    COMMAND_ADMOB_STATE_BANNER = 1002,
};

enum APPSIZES
{
    APP_SIZE_NUM_ACHIEVEMENTS  = 9,
    APP_SIZE_NUM_LEADERBOARD   = 6,
};

enum VIDEOSTATE
{
    kAdMobVideo_Stat_Loaded    = 0,
    kAdMobVideo_Stat_Playing   = 1,
    kAdMobVideo_Stat_Closed    = 2,
    kAdMobVideo_Stat_Destroyed = 3,
    kAdMobVideo_Stat_Error     = 4,

    kAdMobVideo_Requested,
    kAdMobVideo_Loaded,
    kAdMobVideo_Ready,
    kAdMobVideo_Playing,
    kAdMobVideo_Done,
};

enum BANNERSTATE
{
    kAdMobBanner_Stat_Loaded    = 0,
    kAdMobBanner_Stat_Visible   = 1,
    kAdMobBanner_Stat_Hidden    = 2,
    kAdMobBanner_Stat_Destroyed = 3,
    kAdMobBanner_Stat_Error     = 4,

    kAdMobBanner_NotLoaded,
    kAdMobBanner_Requested,
    kAdMobBanner_Ready,
    kAdMobBanner_Visible,
    kAdMobBanner_Hidden,
    kAdMobBanner_Done,
};

//=============================================================================
//=============================================================================
class ServiceCmd : public Object
{
    OBJECT(ServiceCmd);
public:

    enum RESPTYPE{ kRespType_Invalid = -9999 };

    static void Create(Context *_pContext)
    {
        if ( s_pCAdMob == NULL )
        {
            s_pCAdMob = new ServiceCmd( _pContext );
        }
    }

    static void Destroy()
    {
        if ( s_pCAdMob )
        {
            delete s_pCAdMob;
            s_pCAdMob = NULL;
        }
    }

    static ServiceCmd& Instance()
    { 
        return *s_pCAdMob; 
    }

    static void JavaActivityCallback(int _ival, int _istat, const char *_pstr, void *param);
    void RequestServiceCmd(int _iAdType, int _iSubCmd=0);

    // window focus
    bool WindowHasFocus() const             { return m_bWindowHasFocus; }
    void ResetWindowFocusTimer()            { m_TimerWindowFocus.Reset();  }
    unsigned GetWindowFocusTimer()          { return m_TimerWindowFocus.GetMSec( false ); }

    // connection
    bool IsConnectedToGameServices() const      { return m_bGooglePlayConnected; }
    const String& GetGooglePlayUserName() const { return m_strGooglePlayUserName; }
    const int GetConnectErrorCode() const       { return m_iConnectErrorCode; }
    
    // achievement and leaderboard
    void SendUnlockAchievement(unsigned _idx);
    void SendLeaderboardUpdate(unsigned _idx, unsigned _uNumUnits);

    // admob
    void SetAdInterval(Uint32 _uInterval)   { m_uAdInterval = _uInterval; }
    void SetCmdTimeout(int _iMins)          { m_iCmdTimeout = _iMins; }
    void ResetVideoTimer()                  { m_TimerVideo.Reset();  }
    void ResetBannerTimer()                 { m_TimerBanner.Reset(); }
    unsigned GetVideoElapsedTime()          { return m_TimerVideo.GetMSec( false ); }
    unsigned GetBannerElapsedTime()         { return m_TimerBanner.GetMSec( false ); }

    int  GetVideoState() const              { return m_iVideoState; }
    int  GetBannerState() const             { return m_iBannerState; }
    bool HasVideoPlayedOnce() const         { return m_HasVideoPlayedOnce; }
    bool IsVideoHidden() const              { return m_bVideoHidden; }
    bool IsBannerVisible() const            { return m_bBannerVisible; }
    bool IsAppPaused() const                { return m_bAppIsPaused; }

    // license
    bool LicenseQueryMade() const           { return m_bLicenseQueryMade; }
    void SetContinueLicenseQuery(bool _bset){ m_bContinueLicenseQuery = _bset; }
    bool GetContinueLicenseQuery() const    { return m_bContinueLicenseQuery; }
    bool IsLicenseValid() const             { return m_bHasValidLicense; }
    bool IsLicenseRespReady() const         { return m_bHasLicenseQueryResp; }
    int GetLicenseResp() const              { return m_iLicenseResp; }
    int GetLicenseReason() const            { return m_iLicenseReason; }
    void ResetLicenseTimer()                { m_TimerLicense.Reset(); }
    unsigned GetLicenseQueryElapsedTime()   { return m_TimerLicense.GetMSec( false ); }

protected:
    ServiceCmd(Context *_pContext);
    ~ServiceCmd();

    void ActivityCallback(int _ival, int _istat, const char *_pstr);
    //void HandleUpdate(StringHash eventType, VariantMap& eventData);

protected:
    static ServiceCmd               *s_pCAdMob;

    Timer                           m_TimerWindowFocus;
    Timer                           m_TimerVideo;
    Timer                           m_TimerBanner;
    Timer                           m_TimerLicense;

    // focus
    bool                            m_bWindowHasFocus;

    // googleplay connection
    bool                            m_bGooglePlayConnected;
    String                          m_strGooglePlayUserName;
    int                             m_iConnectErrorCode;

    // AdMob 
    bool                            m_bAdPlayedSinceStartup;

    int                             m_iVideoState;
    int                             m_iBannerState;
    bool                            m_HasVideoPlayedOnce;
    bool                            m_bVideoHidden;
    bool                            m_bBannerVisible;

    // licensing
    bool                            m_bContinueLicenseQuery;
    bool                            m_bLicenseQueryMade;
    bool                            m_bHasValidLicense;
    bool                            m_bHasLicenseQueryResp;
    int                             m_iLicenseResp;
    int                             m_iLicenseReason;

    // misc
    bool                            m_bAppIsPaused;
    Uint32                          m_uAdInterval;
    int                             m_iCmdTimeout;
};

//=============================================================================
//=============================================================================
extern "C"
{
//#ifndef pfnUserActivityCallback
typedef void (*pfnUserActivityCallback)(int _id, int _istat, const char *_str, void *param);
//#endif
void RegisterUserActivityCallback(pfnUserActivityCallback callback, void *param);

int Android_JNI_SendMessage(int command, int param);

}

[/code]
[b][size=150]6) Game side sample code[/size][/b]
Sample code
[code]
// somewhere in your startup
     ServiceCmd::Create( GetContext() );

// some where in your shutdown process
    ServiceCmd::Destroy();

// in your handleUpdate() func
void GameMain::ProcessAdMob()
{
    // only play AdMob when game is not playing
    if ( m_pGamePlayFeature == NULL )
    {
        // video state
        switch ( ServiceCmd::Instance().GetVideoState() )
        {
        case kAdMobVideo_Ready:
            if ( ServiceCmd::Instance().GetVideoElapsedTime() > 12 * 60 * 1000 ) // 12 min wait
            {
                ServiceCmd::Instance().RequestServiceCmd( COMMAND_ADMOB_REQUEST_VIDEO );
            }
           break;

        case kAdMobVideo_Requested:
            if ( ServiceCmd::Instance().GetVideoElapsedTime() > 20 * 1000 ) // 20 sec wait
            {
                ServiceCmd::Instance().RequestServiceCmd( COMMAND_ADMOB_REQUEST_VIDEO );
            }
            break;

        case kAdMobVideo_Loaded:
            ServiceCmd::Instance().RequestServiceCmd( COMMAND_ADMOB_SHOW_VIDEO );
            break;

        case kAdMobVideo_Playing:
            // wait for it to go back to 'Ready'
            break;
        }
    }
}
[/code]

And I've run out of room for anything else.

-------------------------

Lumak | 2017-01-02 01:06:19 UTC | #2

It might help if you had the correct permissions in your AndroidManifest.xml.
[code]
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.mycompany.mygame"
    android:versionCode="1"
    android:versionName="1.0">

    <!-- Include required permissions for Google Mobile Ads to run-->
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="com.android.vending.CHECK_LICENSE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

    <application android:label="@string/app_name"
        android:icon="@drawable/icon"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
        android:hardwareAccelerated="true" >
        <!--This meta-data tag is required to use Google Play Services.-->
        <meta-data android:name="com.google.android.gms.games.APP_ID" android:value="@string/app_id"/>
        <meta-data android:name="com.google.android.gms.version" android:value="@integer/google_play_services_version"/>
        <activity android:name=".MyGame"
                  android:label="@string/app_name"
                  android:configChanges="keyboardHidden|orientation"
                  android:screenOrientation="landscape">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <!--Include the AdActivity configChanges and theme. -->
        <activity android:name="com.google.android.gms.ads.AdActivity"
            android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|uiMode|screenSize|smallestScreenSize"
            android:theme="@android:style/Theme.Translucent"/>
    </application>

    <uses-sdk android:minSdkVersion="10" android:targetSdkVersion="19" />
    <uses-feature android:glEsVersion="0x00020000" />

</manifest>
[/code]

-------------------------

weitjong | 2017-01-02 01:06:19 UTC | #3

Thanks for sharing this. It would be great if you can also sight any references that you use. The provided shared lib loader logic is required when your app depends on other 3rd party libs in *.so format. You can build Urho3D lib as shared lib and depend on it in this way for example.

-------------------------

Lumak | 2017-01-02 01:06:19 UTC | #4

[b][size=150]Resources[/size][/b]
SDL-2.0.3/android-project/src/org/libsdl/app/SDLActivity.java

This is what they have:
[code]
    // Load the .so
    static {
        System.loadLibrary("SDL2");
        //System.loadLibrary("SDL2_image");
        //System.loadLibrary("SDL2_mixer");
        //System.loadLibrary("SDL2_net");
        //System.loadLibrary("SDL2_ttf");
        System.loadLibrary("main");
    }
[/code]

Below links were the only ones that I had saved.  All others were searched on Google.

GooglePlay:
[url]https://developers.google.com/games/services/android/quickstart[/url]
[url]http://code.tutsplus.com/tutorials/google-play-game-services-leaderboards--cms-20700[/url]
[url]https://github.com/playgameservices/android-basic-samples[/url]

AdMob:
[url]https://developers.google.com/ads/#apps[/url]
[url]https://developers.google.com/admob/android/quick-start[/url]
[url]https://developers.google.com/admob/android/interstitial?hl=en[/url]
[url]https://github.com/googleads/googleads-mobile-android-examples[/url]

AppLicensing:
[url]http://developer.android.com/intl/ko/google/play/licensing/index.html[/url]
[url]https://developer.android.com/intl/ko/google/play/licensing/setting-up.html[/url]
[url]https://github.com/okamstudio/godot/tree/master/platform/android/libs/play_licensing[/url]

and Google :slight_smile: which will lead you to Stack Overflow.

Edit: added a few more links.

-------------------------

weitjong | 2017-01-02 01:06:19 UTC | #5

It's not important but I meant to say references for Google Play and the ads stuff if any.

If we do the *.so loading explicitly then it needs to be rewritten for every app. The one being provided by Urho3D will auto detect all the *.so list and load them in an orderly fashion automatically. It may be overkill though for a single main *.so app. I am just supplementing the rationale of the provided shared lib logic. It is perfectly fine to replace it as you have done.

-------------------------

Lumak | 2017-01-02 01:06:19 UTC | #6

They are there now.

-------------------------

Lumak | 2017-01-02 01:06:19 UTC | #7

I'm fully aware of how the shared object loader works and why it's there.  That's where I started learning about SDLAcitivity, and yes, it makes sense for that to be there if you're loading/testing multiple .so files.  But as you already noticed, I didn't need anything that intricate to load a single .so file.  :wink:

Perhaps, one can declare their gamelib.so in a string then do something like:
[code]
System.loadLibrary( getResources().getString( R.string.gameapp_lib ) );
[/code]

-------------------------

Lumak | 2017-01-02 01:06:19 UTC | #8

weitjong, 

I'm getting the impression that you think Urho3D.java code should be reused w/o any modifications in everyone's project.

I don't know if you are aware of the importance of the [b]package name[/b], i.e. com.mycompany.mygame, that you declare in the AndroidManifest.xml, build.gradle, and in your primary game Java code, but it must be unique for one reason:
when you release your game from Google Play Developer Console, the name has to be unique.  You can never load the same package name twice.  If you try, you'll get an error saying it's already in use.

So, you can't expect everyone to have [b]com.github.urho3d[/b] in their Android game.  Nor can you create a single project folder and release multiple games from that same folder many times over.  Every project would have to have a unique package name in their Java code, in build.gradle (if using Android SDK), and in AndroidManifest.xml.

If you already knew about this, then just ignore it.

-------------------------

rasteron | 2017-01-02 01:06:20 UTC | #9

Thanks for sharing this Lumak  :slight_smile: cheers.

-------------------------

weitjong | 2017-01-02 01:06:20 UTC | #10

[quote="Lumak"]weitjong, 

I'm getting the impression that you think Urho3D.java code should be reused w/o any modifications in everyone's project.

I don't know if you are aware of the importance of the [b]package name[/b], i.e. com.mycompany.mygame, that you declare in the AndroidManifest.xml, build.gradle, and in your primary game Java code, but it must be unique for one reason:
when you release your game from Google Play Developer Console, the name has to be unique.  You can never load the same package name twice.  If you try, you'll get an error saying it's already in use.

So, you can't expect everyone to have [b]com.github.urho3d[/b] in their Android game.  Nor can you create a single project folder and release multiple games from that same folder many times over.  Every project would have to have a unique package name in their Java code, in build.gradle (if using Android SDK), and in AndroidManifest.xml.

If you already knew about this, then just ignore it.[/quote]
Yes, I am aware of that. The logic I mentioned in my previous posts come from the Urho3D modified version of SDLActivity Java class in org.libsdl.app package, which can be reused by other external projects. The Urho3D Java class which extends from the modified SDLActivity class is of course not reusable.

-------------------------

Mike | 2017-01-02 01:06:20 UTC | #11

Thanks for detailed instructions Lumak :stuck_out_tongue:

-------------------------

sabotage3d | 2017-01-02 01:06:22 UTC | #12

Thanks for the in depth instructions :slight_smile:
Any chance for IOS one ?

-------------------------

Lumak | 2017-01-02 01:06:24 UTC | #13

[quote]posted by sabotage3d ? 08 Aug 2015, 04:22
Thanks for the in depth instructions :slight_smile:
Any chance for IOS one ?[/quote]

I haven't started working on iOS yet.  I'll post it if I do it.

-------------------------

Deveiss | 2017-01-02 01:07:11 UTC | #14

Do you have a complete example implementation? That would be really helpful to study, as right now I'm a bit confused on how to make this all come together. I'm unclear on where to define the JNI callbacks, and what else I'd have to include or link against to compile them. Additionally, how would I add Godot's Play Services library as a dependency for the ant build process?

-------------------------

Lumak | 2017-01-02 01:07:12 UTC | #15

Hi Deveiss,

I sent you a reply to your email but I'll also post it here.

//=================================================================================================
What I did was added the functions to \ThirdParty\SDL\src\main\android\SDL_android_main.c file
right below  void Java_org_libsdl_app_SDLActivity_nativeInit(JNIEnv* env, jclass cls, jstring filesDir)  function, and I can't remember why I chose that file instead of SDL_android.c.
Below is everything I have in that file below the Java_org_libsdl_app_SDLActivity_nativeInit() function.  Copy that into the file and you should be good to go.

There is no additional library that you need to get Google Play, i.e. Leaderboard and Achievement,or AdMob working. CMake files that I used was Urho's cmake_android w/o any modification.  I think I mentioned linking a library Android Studio in my thread. I can't remember the library name but you also don't need that. Only time you would need it is for licensing (or testing licensing feature), and is not part of Google Play, leaderboard, achievement, or AdMob. Remove that library if you have it linked in and also remove the line
    <uses-permission android:name="com.android.vending.CHECK_LICENSE" />
from AndroidManisfest.xml, along with section of Java code related to licensing - just comment of sections that give you error.

I hope this helps.

// code to copy
[code]
int Android_JNI_SendMessageStr(int command, const char *param)
{
    JNIEnv *mEnv = Android_JNI_GetEnv();
    if (!mEnv) {
        return -1;
    }
    jclass cActivity = Android_JNI_GetActivityClass();

    jmethodID mid = (*mEnv)->GetStaticMethodID(mEnv, cActivity, "sendMessageStr", "(ILjava/lang/String;)Z");
    if (!mid) {
        return -1;
    }

    jstring jparam = (jstring)((*mEnv)->NewStringUTF(mEnv, param));
    jboolean success = (*mEnv)->CallStaticBooleanMethod(mEnv, cActivity, mid, command, jparam);
    (*mEnv)->DeleteLocalRef(mEnv, jparam);

    return success ? 0 : -1;
}

//#include <SDL/SDL_events.h>

typedef void (*pfnUserActivityCallback)(int id1, int istat, const char *str, void *param);

static pfnUserActivityCallback gpUserActivityCallback = NULL;
static void *gActivityCallbackParam = NULL;

void RegisterUserActivityCallback(pfnUserActivityCallback callback, void *param)
{
    gpUserActivityCallback = callback;
    gActivityCallbackParam = param;
}

void Java_org_libsdl_app_SDLActivity_nativeUserActivityCallback(JNIEnv* env, jclass cls, jint id1, jint istat, jstring jstrParam)
{
    const char *str = (*env)->GetStringUTFChars(env, jstrParam, 0);

    if ( gpUserActivityCallback )
    {
        (*gpUserActivityCallback)( id1, istat, str, gActivityCallbackParam );
    }

    if ( str )
    {
        (*env)->ReleaseStringUTFChars(env, jstrParam, str);
    }
}
[/code]

-------------------------

extobias | 2017-01-31 17:56:52 UTC | #16

Hi there!
First, sorry about my english. isn't my native language
I've found that COMMAND_ADMOB_SHOW_VIDEO = 5  in ServiceCmd.h 
takes the same value that COMMAND_SET_KEEP_SCREEN_ON = 5 in SDLActivity.java
So SDLCommandHandler go in the wrong case when show video is requested.
I've change the enum in ServiceCmd.h, but i don't know if that is correct.
Thanks anyway for sharing this!
cheers!

-------------------------

Lumak | 2017-02-01 22:46:36 UTC | #17

At the time this was written, Urho3D was on 1.4 and the messages were declared as:
>     // Messages from the SDLMain thread
>     static final int COMMAND_CHANGE_TITLE = 1;
>     static final int COMMAND_UNUSED = 2;
>     static final int COMMAND_TEXTEDIT_HIDE = 3;

and now in 1.6:
>     // Messages from the SDLMain thread
>     static final int COMMAND_CHANGE_TITLE = 1;
>     static final int COMMAND_UNUSED = 2;
>     static final int COMMAND_TEXTEDIT_HIDE = 3;
>     static final int COMMAND_SET_KEEP_SCREEN_ON = 5;

So you are correct to change the values is in ServiceCmd.h.

-------------------------

vivienneanthony | 2017-05-16 20:36:10 UTC | #18

Hey 

  I'm trying to get some code to work. I'm at a lost. It does the OnProcessCommand() but the actual message sent to the Java side is not sent. Maybe someone has a idea????

Vivienne



       
    #include <jni.h>


    #include <Urho3D/Urho3D.h>
    #include <Urho3D/Core/CoreEvents.h>
    #include <Urho3D/Core/Context.h>
    #include <Urho3D/Engine/Engine.h>
    #include <Urho3D/Input/InputEvents.h>
    #include <Urho3D/Scene/Scene.h>
    #include <Urho3D/Core/Timer.h>

    #include "ServicesInterface_Admob.h"

    #include <Urho3D/DebugNew.h>

    #include <CornersStd.h>
    #include <Urho3D/ThirdParty/SDL/SDL_system.h>

    //=============================================================================
    //=============================================================================

    typedef void (*pfnUserActivityCallback)(int id1, int istat, const char *str, void *param);

    static pfnUserActivityCallback gpUserActivityCallback = NULL;
    static void *gActivityCallbackParam = NULL;

    static JavaVM *java_vm;
    static jclass activityClass = NULL;
    static JNIEnv *jenv = NULL;

    void RegisterUserActivityCallback(pfnUserActivityCallback callback, void *param) {
        gpUserActivityCallback = callback;
        gActivityCallbackParam = param;
    }


    // This is here but can only be set once so need to update
    // Maybe make this generic where command can be either both services
    // Hmmm


    int Android_JNI_SendMessage(int command, int param) {

        ALPHAENGINE_LOGINFO("Android_JNI_SENDMESSAGE");


        return 0;

    }

    //=============================================================================
    //=============================================================================
    ServicesInterface_Admob *ServicesInterface_Admob::s_pCAdMob = NULL;

    //=============================================================================
    //=============================================================================
    ServicesInterface_Admob::ServicesInterface_Admob(Context *_pcontext)
            : Object(_pcontext) {
        // init
        m_TimerWindowFocus.Reset();
        m_TimerVideo.Reset();
        m_TimerBanner.Reset();
        m_TimerLicense.Reset();

        // focus
        m_bWindowHasFocus = true;

        // admob
        m_uAdInterval = 2 * 60 * 1000; // 2 mins
        m_iCmdTimeout = 5;
        m_bAdPlayedSinceStartup = false;

        m_iVideoState = kAdMobVideo_Ready;
        m_iBannerState = kAdMobBanner_NotLoaded;
        m_HasVideoPlayedOnce = false;
        m_bAppIsPaused = false;


        // register java callback
        RegisterUserActivityCallback(&ServicesInterface_Admob::JavaActivityCallback, this);
    }

    //=============================================================================
    //=============================================================================
    ServicesInterface_Admob::~ServicesInterface_Admob() {
        RegisterUserActivityCallback(NULL, NULL);
    }

    //=============================================================================
    //=============================================================================
    void ServicesInterface_Admob::JavaActivityCallback(int _ival, int _istat, const char *_pstr,
                                                       void *param) {
        if (param) {
            ((ServicesInterface_Admob *) param)->ActivityCallback(_ival, _istat, _pstr);
        }
    }

    //=============================================================================
    //=============================================================================
    void ServicesInterface_Admob::ActivityCallback(int _icmd, int _istat, const char *_pstr) {
    #ifdef DBG_DUMP_SVCLOG
        if ( _icmd != COMMAND_WINDOW_HAS_FOCUS )
        {
            SDL_Log("ServicesInterface_Admob::ActivityCallback() icmd=%d, istat=%d, pstr='%s'\n", _icmd, _istat, _pstr?_pstr:" ");
        }
    #endif

        switch (_icmd) {
            case COMMAND_ADMOB_STATE_VIDEO:
                switch (_istat) {
                    case kAdMobVideo_Stat_Loaded:
                        m_iVideoState = kAdMobVideo_Loaded;
                        break;
                    case kAdMobVideo_Stat_Playing:
                        m_iVideoState = kAdMobVideo_Playing;
                        break;
                    case kAdMobVideo_Stat_Closed:
                        m_iVideoState = kAdMobVideo_Ready;
                        ResetVideoTimer();
                        break;
                    case kAdMobVideo_Stat_Destroyed:
                        m_iVideoState = kAdMobVideo_Ready;
                        break;
                    default:
                        // failed to load error - retry
                        ResetVideoTimer();
                        break;
                }
                break;

            case COMMAND_ADMOB_STATE_BANNER:
                switch (_istat) {
                    case kAdMobBanner_Stat_Loaded:
                        if (m_iBannerState == kAdMobBanner_NotLoaded ||
                            m_iBannerState == kAdMobBanner_Requested) {
                            m_iBannerState = kAdMobBanner_Ready;
                        }
                            // AdMob banner continuously loads new banners in the background, and any subsequent calls will automatically show itself
                            // -- prevent it from being visible if not in the visible state
                        else if (m_iBannerState != kAdMobBanner_Visible) {
                            RequestServiceCmd(COMMAND_ADMOB_HIDE_BANNER);
                        }
                        break;
                    case kAdMobBanner_Stat_Visible:
                        m_iBannerState = kAdMobBanner_Visible;
                        break;
                    case kAdMobBanner_Stat_Hidden:
                        m_iBannerState = kAdMobBanner_Hidden;
                        break;
                    case kAdMobBanner_Stat_Destroyed:
                        m_iBannerState = kAdMobBanner_NotLoaded;
                        break;
                    default:
                        // failed to load error - retry
                        ResetBannerTimer();
                        break;
                }
                break;


            case COMMAND_WINDOW_HAS_FOCUS:
                m_bWindowHasFocus = _istat ? true : false;
                break;

        }
    }


    //=============================================================================
    //=============================================================================
    void ServicesInterface_Admob::RequestServiceCmd(int _iCmdType, int _iSubCmd) {
        if (_iCmdType >= COMMAND_ADMOB_REQUEST_VIDEO && _iCmdType < COMMAND_END) {
    #ifdef DBG_DUMP_SVCLOG
            if ( _iCmdType != COMMAND_WINDOW_HAS_FOCUS )
            {
                SDL_Log( "ServicesInterface_Admob::RequestServiceCmd() _iCmdType=%d, sub=%d\n", _iCmdType, _iSubCmd );
            }
    #endif

            Android_JNI_SendMessage(_iCmdType, _iSubCmd);

            switch (_iCmdType) {
                case COMMAND_WINDOW_HAS_FOCUS:
                    ResetWindowFocusTimer();
                    break;


                    //========================
                    // admob video
                case COMMAND_ADMOB_REQUEST_VIDEO:
                    m_TimerVideo.Reset();
                    m_iVideoState = kAdMobVideo_Requested;
                    break;

                case COMMAND_ADMOB_SHOW_VIDEO:
                    m_HasVideoPlayedOnce = true;
                    m_TimerVideo.Reset();
                    m_TimerBanner.Reset();
                    break;

                case COMMAND_ADMOB_HIDE_VIDEO:
                    // can't really send a request to hide video
                    break;

                case COMMAND_ADMOB_DELETE_VIDEO:
                    m_iVideoState = kAdMobVideo_Ready;
                    break;

                    //========================
                    // admob banner
                case COMMAND_ADMOB_REQUEST_BANNER:
                    m_iBannerState = kAdMobBanner_Requested;
                    m_TimerBanner.Reset();
                    break;

                case COMMAND_ADMOB_SHOW_BANNER:
                    m_TimerBanner.Reset();
                    break;

                case COMMAND_ADMOB_HIDE_BANNER:
                    break;

                case COMMAND_ADMOB_DELETE_BANNER:
                    break;
            }
        } else {
    #ifdef DBG_DUMP_SVCLOG
            SDL_Log( "ServicesInterface_Admob::StartAd() unknown add type=%d\n", _iCmdType );
    #endif
        }
    }

    // JNI EXPORT BRIDGE

    extern "C" {

    JNIEXPORT void JNICALL
    Java_org_libsdl_app_SDLActivity_nativeUserActivityCallback(JNIEnv *env, jclass cls,
                                                               jint id1,
                                                               jint istat, jstring jstrParam) {
        const char *str = env->GetStringUTFChars(jstrParam, 0);
        if (gpUserActivityCallback) {
            (*gpUserActivityCallback)(id1, istat, str, gActivityCallbackParam);
        }

        if (str != NULL) {
            // If used show output string
            String s = String(str);
            ALPHAENGINE_LOGINFO("Java_org_libsdl_app_SDLActivity_nativeUserActivityCallback():" + s);

            env->ReleaseStringUTFChars(jstrParam, str);
        }
    }

    }}

-------------------------

vivienneanthony | 2017-05-16 19:41:48 UTC | #19

This is the androidmanifest.xml

    <?xml version="1.0" encoding="utf-8"?>
    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
              package="protocolseven"
              android:versionCode="1"
              android:versionName="1.0"
              android:installLocation="auto">

        <!-- Android 2.3.3 -->
        <uses-sdk
            android:minSdkVersion="14"
            android:targetSdkVersion="21"/>

        <!-- OpenGL ES 2.0 -->
        <uses-feature android:glEsVersion="0x00020000"/>

        <!-- Allow writing to external storage -->
        <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>


        <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
        <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
        <uses-permission android:name="android.permission.CHANGE_NETWORK_STATE" />
        <uses-permission android:name="android.permission.INTERNET" />
        <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
        <uses-permission android:name="android.permission.READ_PHONE_STATE" />
        <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

        <!-- Google Play filtering -->
        <uses-feature android:name="android.hardware.wifi.direct" android:required="true"/>

        <application
            android:label="@string/app_name"
            android:icon="@drawable/icon"
            android:theme="@android:style/Theme.NoTitleBar.Fullscreen"

            android:allowBackup="false">
            <activity android:name=".Corners"
                android:screenOrientation="portrait">
                <intent-filter>
                    <action android:name="android.intent.action.MAIN" />
                    <category android:name="android.intent.category.LAUNCHER" />
                </intent-filter>
            </activity>
        </application>




    </manifest>

-------------------------

extobias | 2017-05-17 16:05:47 UTC | #20

Hi there, have you added the code on SDL side as Lumak has posted?
[quote="Lumak, post:15, topic:1238"]
\ThirdParty\SDL\src\main\android\SDL_android_main.c
[/quote]

-------------------------

vivienneanthony | 2017-05-17 16:47:46 UTC | #21

I did. Its working. The issue i have the first ad with the adview load and show doesnt work off the bat. Subsequent test ads show. So i have to debug and two peculiar errors with that.

Also it seems order was important in the code itself.

-------------------------

