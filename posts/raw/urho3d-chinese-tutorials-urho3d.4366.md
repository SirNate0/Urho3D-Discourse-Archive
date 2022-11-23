DinS | 2018-06-30 12:19:31 UTC | #1

This topic is written for chinese developers who want to find a guide to Urho3D.

Urho3D is a great game engine. However, few developers in China know about it. I happened to come across Urho3D and find it fascinating. I worked my way through it and, with tutorials and documentations, wrote a few articles about it, all in chinese. 

Here is a list of these ariticles:
      |  —  Urho3d
                       |  —  编译Urho3D库
                       |  —  Urho3D自建项目
                       |  —  Urho3D引擎框架
                       |  —  Urho3D数据结构
                       |  —  初识子系统与场景模型
                       |  —  事件与使用
                       |  —  响应用户输入
                       |  —  文字与国际化
                       |  —  场景模型进阶-逻辑与脚本
                       |  —  UI研究
                       |  —  场景模型进阶-切换场景
                       |  —  2D场景概述
                       |  —  2D场景-实现鼠标选中场景物体（一）
                       |  —  2D场景-实现鼠标选中场景物体（二）

You can find the details on my site, https://dins.site/navi-coding-chs/. This is a navi page about coding. There're something else about c++. Just search for Urho3D and you'll get it.

These articles are not translation. I mixed my own understanding in it, with working codes. I hope this will help chinese developers to get the hang of Urho3D.

-------------------------

cjmxp | 2018-12-12 03:20:15 UTC | #2

不容易啊就为了给你订个帖子我注册了半天又是翻墙又是激活的，我就想说哥们文章写的不错可惜没后续更新了可惜啊

-------------------------

Virgo | 2018-12-12 09:17:18 UTC | #3

Spam confirmed...jk :relieved:

-------------------------

DinS | 2018-12-13 01:29:57 UTC | #4

感谢支持:grin:
把主要框架介绍完了感觉剩下的就是根据项目需求自己探索了。应该不会有更新了吧:sweat_smile:

-------------------------

cjmxp | 2018-12-24 15:50:26 UTC | #5

@ [DinS](https://discourse.urho3d.io/u/DinS)
正好碰到了中文帖子顺便问个问题，场景里的2d node 怎么放到UI里 角色背包里需要用到。。。

-------------------------

weitjong | 2018-12-26 04:01:16 UTC | #6

Please observe the forum rule. Use English language for the main message in your post.

-------------------------

DinS | 2018-12-27 00:59:43 UTC | #7

You can't put node into UI. Node belongs to Scene and is different from UI system. 
However, you can try to use the same textures for the node and UI. This will look as if they are the same thing.

-------------------------

