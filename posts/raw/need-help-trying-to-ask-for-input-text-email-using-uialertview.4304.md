galileolajara | 2018-06-10 15:44:00 UTC | #1

Hi, I'm wondering if someone knows how can I ask for input text popout using UIAlert. I have a single ".m" file which I use to open url, so basically I have a setup where I can call native iOS functions.

`
#import <sys/sysctl.h>
#import "UIKit/UIKit.h"

int urho3d_open_url(const char* url) {
 UIAlertController *alert = [UIAlertController alertControllerWithTitle:@"Get notified on our launch" message:@"Enter your email address" preferredStyle:UIAlertControllerStyleAlert];
 [alert addAction:[UIAlertAction actionWithTitle:@"Subscribe" style:UIAlertActionStyleDefault handler:nil]];
  [alert addTextFieldWithConfigurationHandler:^(UITextField *textField) {
  textField.placeholder = @"Enter email address";                                                                                                                                              
  textField.secureTextEntry = NO;
  }];                                                                                                                                                                                        
  [self presentViewController:alert animated:YES completion:nil];
}

int urho3d_open_url(const char* url) {
  [[UIApplication sharedApplication] openURL:[NSURL URLWithString:[NSString stringWithUTF8String:url]]];
  return 0;
}
`

I'm receiving an error from Xcode saying that "self" is undefined.

I also have no idea how to get the string that the user typed. If this would be in javascript, what I'm trying to do is simply:

var email = prompt("Enter your email", "sample@gmail.com");

Any help would be appreaciated!

-------------------------

