By default, MacOS doesn't respect the System Preferences settings for key delay and repeat speed except in Terminal. Everywhere else in 
MacOS key repeat is disabled to allow the 'press and hold' feature that pops up foreign characters etc.

There is no gui way to disable the 'press and hold' feature, but it is possible in the Terminal (reboot required after issuing the command):

```
defaults write -g ApplePressAndHoldEnabled -bool false
```

See <https://www.howtogeek.com/267463/how-to-enable-key-repeating-in-macos/>
