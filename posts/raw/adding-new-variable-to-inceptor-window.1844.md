dragonCASTjosh | 2017-01-02 01:10:37 UTC | #1

Im looking to add a new variable for lights that is changeable in the impactor window, so far i have created the variable with Getters and Setters along with script functionality but im unsure how to have it show in the inspector

-------------------------

cadaver | 2017-01-02 01:10:38 UTC | #2

Look into the attribute registration in Light::RegisterObject() static function.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:38 UTC | #3

Thanks :slight_smile: i didnt see that stuff before

-------------------------

