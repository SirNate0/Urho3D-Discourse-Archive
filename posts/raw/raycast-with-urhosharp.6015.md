pldeschamps | 2020-03-25 21:21:14 UTC | #1

RayCast works on BillboardSet.

Continuing the discussion from [Making an interactive star field](https://discourse.urho3d.io/t/making-an-interactive-star-field/5833/13):

But with UrhoSharp (C# urho3d wrapper for Xamarin) there is quite a bug due to the 40 pixels black banner on top of the screen.
![raycastok|690x456](upload://puyeixvGBj2x0qkqgHIgGALPaSR.png) 

So I needed to add correction to the cursor coordinates before I sent a RayCast:
(int x and int y are only there to send multiple RayCasts to have a chance to hit my smalls billboard intems when the user touch the screen...)
```
        private uint? StarIndex(TouchEndEventArgs e, int x, int y)
        {
            {
                //The correction to do because of the 40 pixels Black Banner on top of the screen
                float ey = ((float)(e.Y + y) - 40f) * (float)Graphics.Height  / ((float)Graphics.Height - 40f) ;
                Ray cameraRay = camera.GetScreenRay((float)(e.X + x) / Graphics.Width, (float)ey / Graphics.Height);
                RayQueryResult? result = octree.RaycastSingle(cameraRay, RayQueryLevel.Triangle, 100, DrawableFlags.Geometry);
                if (result != null)
                {
                    return result.Value.SubObject;
                }
            }
            return null;
        }
```
This code works with Xamarin.Forms for Android and UWP.

-------------------------

najak3d | 2020-04-21 19:37:31 UTC | #2

The Touch Location Skew you mentioned, I think only happens on UWP (that's how it is for us).

We overcame this by using <AbsoluteLayout> for Xamarin, and then putting the UrhoSurface and a BoxView both consuming entire space -- and the BoxView is on top.  We then just read Input from the Invisible Box View.

But then we switched over to using MR.Gestures (can get from Nuget) which provides a much more robust Gesture reading event set.

Our resulting XAML looks like this:

===
 xmlns:mr="clr-namespace:MR.Gestures;assembly=MR.Gestures"
...
<ContentPage.Content>
        <mr:Grid RowSpacing="0" Padding="0">
            <Grid.RowDefinitions>
                <RowDefinition Height="*" />
                <RowDefinition Height="55" />
            </Grid.RowDefinitions>

            <Grid.ColumnDefinitions>
                <ColumnDefinition Width="*" />
            </Grid.ColumnDefinitions>

            <mr:StackLayout x:Name="mainGrid">
                <forms:UrhoSurface x:Name="UrhoSurface" VerticalOptions="FillAndExpand" />
                <!--<BoxView x:Name="map" Grid.Row="0" Grid.Column="0" BackgroundColor="#FFFF00" />-->
            </mr:StackLayout>
            <controls:MainButtonBar x:Name="btnBar" Grid.Row="1" Grid.Column="0" />
        </mr:Grid>


Notice here we stubbed out the BoxView, and placed the MR.Gestures GestureRecognizer on the "mr:Grid", using the code-behind:

		public MapView()
		{
			InitializeComponent();

			mainGrid.Down += MainGrid_Down;
			mainGrid.Panned += MainGrid_Panned;
			mainGrid.DoubleTapped += MainGrid_DoubleTapped;

		}

MR.Gestures is so much easier to use.  It just adds the events you want to the Grid class itself.  And now we can read the XY position perfectly, no skew.

-------------------------

pldeschamps | 2020-04-24 11:22:00 UTC | #3

@najak3d,
Thank you for your answer. That sounds very good.
I will first try the BoxView option:
```
    <ContentPage.Content>
            <Grid RowSpacing="0" Padding="0">
                <Grid.RowDefinitions>
                </Grid.RowDefinitions>
                <Grid.ColumnDefinitions>
                    <ColumnDefinition Width="*" />
                </Grid.ColumnDefinitions>
                    <urho:UrhoSurface
                    x:Name="urhoSurface"
                        Grid.Row="0" Grid.RowSpan="1"
                    VerticalOptions="FillAndExpand"/>
                    <BoxView x:Name="map"  BackgroundColor="#FFFF00"
                        Grid.Row="0" Grid.RowSpan="1" Opacity="0.2"
                        VerticalOptions="FillAndExpand"/>     
                <Label Text="{i18n:Translate labelTrueAltitude}"
                    HorizontalOptions="Start"
                    WidthRequest="140"
                    Grid.Row="1" Grid.Column="0" />
            </Grid>
    </ContentPage.Content>
```

-------------------------

najak3d | 2020-04-24 12:15:49 UTC | #4

How did that work out for you?

-------------------------

pldeschamps | 2020-04-24 13:14:53 UTC | #5

Well, I am trying to mix Xamarin UI code with Urho code.

My XAML code is:
```
           <BoxView x:Name="map"  BackgroundColor="#FFFF00"
                        Grid.Row="0" Grid.RowSpan="1" Opacity="0.2"
                        VerticalOptions="FillAndExpand">
                <BoxView.GestureRecognizers>
                    <PinchGestureRecognizer PinchUpdated="OnPinchUpdated"/>
                </BoxView.GestureRecognizers>
            </BoxView>
```
My code behind is this one:
```
namespace AlmicantaratXF.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class SkyUrhoSurface : ContentPage
    {
        public SkyUrhoSurface()
        {
            InitializeComponent();
        }
        protected override async void OnAppearing()
        {
            base.OnAppearing();
            await urhoSurface.Show<SkyUrho>(new Urho.ApplicationOptions(assetsFolder: "Data"));
        }
    }
}
```
I wonder where to write my OnPinchUpdated method in order to:
1. bind it to the xaml code
2. and to act on the SkyUrho class...

I am currently trying to set the SkyUrho class as the BindingContext of the XAML page but I am septic...

-------------------------

najak3d | 2020-04-24 13:33:28 UTC | #6

I am very new to XAML myself, and won't be much help on this.  I do know that our solution with MR.Gestures has worked out perfectly for us.   His product only costs $20 EUR, and has given us enhanced Gesture recognition and made resolution to this UrhoSurface a cinch (as shown in our code).  We just handle the gestures from the Grid, and treat them as though they were for the UrhoSurface (since they consume the exact same screen space).

I would think that you can read the gestures from BoxView and have it behave as a proxy for the UrhoSurface.  Are you able to read gestures on your BoxView correctly?  If so, then I think you should be all set (just route those gesture events as though they occurred on the UrhoSurface).

-------------------------

