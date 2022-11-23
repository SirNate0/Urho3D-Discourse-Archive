majhong | 2019-06-26 12:17:55 UTC | #1

i got a building error when my android studio upgraded.

it is ok  before the upgrade.

then  i downloaded the leatest version  (master branch)
i got the same error.



* Where:
Build file '/Users/leeco/prj_2020/Urho3D-master/buildSrc/build.gradle.kts' line: 23

* What went wrong:
Plugin [id: 'org.gradle.kotlin.kotlin-dsl', version: '1.2.6'] was not found in any of the following sources:





./gradlew -v

------------------------------------------------------------
Gradle 5.4.1
------------------------------------------------------------

Build time:   2019-04-26 08:14:42 UTC
Revision:     261d171646b36a6a28d5a19a69676cd098a4c19d

Kotlin:       1.3.21
Groovy:       2.5.4
Ant:          Apache Ant(TM) version 1.9.13 compiled on July 10 2018
JVM:          1.8.0_131 (Oracle Corporation 25.131-b11)
OS:           Mac OS X 10.14.5 x86_64

-------------------------

weitjong | 2019-06-26 16:08:11 UTC | #2

We have recently made a few changes in the master branch that requires dependencies that only Android Studio 3.5 Preview/Beta able to provide. Are you using 3.5 already?

Alternatively our Android build would also work with Gradle wrapper on CLI or with the latest release of InteliJ IDEA.

-------------------------

majhong | 2019-06-27 01:39:58 UTC | #3

thank you！ weitjong  , i will try it again.

-------------------------

