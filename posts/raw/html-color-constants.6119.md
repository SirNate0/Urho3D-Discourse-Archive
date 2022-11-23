SirNate0 | 2020-04-25 16:55:31 UTC | #1

I wanted some additional color constants to use, so I converted the ones listed on https://htmlcolorcodes.com/ to `const Color` objects.

### ColorContstants.h
```
#include <Urho3D/Math/Color.h>

namespace Urho3D
{

namespace ColorConstants
{

// RED HTML COLOR NAMES
/// Hex #CD5C5C = RGB(205, 92, 92)
extern const Color INDIANRED;
/// Hex #F08080 = RGB(240, 128, 128)
extern const Color LIGHTCORAL;
/// Hex #FA8072 = RGB(250, 128, 114)
extern const Color SALMON;
/// Hex #E9967A = RGB(233, 150, 122)
extern const Color DARKSALMON;
/// Hex #FFA07A = RGB(255, 160, 122)
extern const Color LIGHTSALMON;
/// Hex #DC143C = RGB(220, 20, 60)
extern const Color CRIMSON;
/// Hex #FF0000 = RGB(255, 0, 0)
extern const Color RED;
/// Hex #B22222 = RGB(178, 34, 34)
extern const Color FIREBRICK;
/// Hex #8B0000 = RGB(139, 0, 0)
extern const Color DARKRED;

// PINK HTML COLOR NAMES
/// Hex #FFC0CB = RGB(255, 192, 203)
extern const Color PINK;
/// Hex #FFB6C1 = RGB(255, 182, 193)
extern const Color LIGHTPINK;
/// Hex #FF69B4 = RGB(255, 105, 180)
extern const Color HOTPINK;
/// Hex #FF1493 = RGB(255, 20, 147)
extern const Color DEEPPINK;
/// Hex #C71585 = RGB(199, 21, 133)
extern const Color MEDIUMVIOLETRED;
/// Hex #DB7093 = RGB(219, 112, 147)
extern const Color PALEVIOLETRED;

// ORANGE HTML COLOR NAMES
// Hex #FFA07A = RGB(255, 160, 122)
//extern const Color LIGHTSALMON; duplicated above
/// Hex #FF7F50 = RGB(255, 127, 80)
extern const Color CORAL;
/// Hex #FF6347 = RGB(255, 99, 71)
extern const Color TOMATO;
/// Hex #FF4500 = RGB(255, 69, 0)
extern const Color ORANGERED;
/// Hex #FF8C00 = RGB(255, 140, 0)
extern const Color DARKORANGE;
/// Hex #FFA500 = RGB(255, 165, 0)
extern const Color ORANGE;

// YELLOW HTML COLOR NAMES
/// Hex #FFD700 = RGB(255, 215, 0)
extern const Color GOLD;
/// Hex #FFFF00 = RGB(255, 255, 0)
extern const Color YELLOW;
/// Hex #FFFFE0 = RGB(255, 255, 224)
extern const Color LIGHTYELLOW;
/// Hex #FFFACD = RGB(255, 250, 205)
extern const Color LEMONCHIFFON;
/// Hex #FAFAD2 = RGB(250, 250, 210)
extern const Color LIGHTGOLDENRODYELLOW;
/// Hex #FFEFD5 = RGB(255, 239, 213)
extern const Color PAPAYAWHIP;
/// Hex #FFE4B5 = RGB(255, 228, 181)
extern const Color MOCCASIN;
/// Hex #FFDAB9 = RGB(255, 218, 185)
extern const Color PEACHPUFF;
/// Hex #EEE8AA = RGB(238, 232, 170)
extern const Color PALEGOLDENROD;
/// Hex #F0E68C = RGB(240, 230, 140)
extern const Color KHAKI;
/// Hex #BDB76B = RGB(189, 183, 107)
extern const Color DARKKHAKI;

// PURPLE HTML COLOR NAMES
/// Hex #E6E6FA = RGB(230, 230, 250)
extern const Color LAVENDER;
/// Hex #D8BFD8 = RGB(216, 191, 216)
extern const Color THISTLE;
/// Hex #DDA0DD = RGB(221, 160, 221)
extern const Color PLUM;
/// Hex #EE82EE = RGB(238, 130, 238)
extern const Color VIOLET;
/// Hex #DA70D6 = RGB(218, 112, 214)
extern const Color ORCHID;
/// Hex #FF00FF = RGB(255, 0, 255)
extern const Color FUCHSIA;
/// Hex #FF00FF = RGB(255, 0, 255)
extern const Color MAGENTA;
/// Hex #BA55D3 = RGB(186, 85, 211)
extern const Color MEDIUMORCHID;
/// Hex #9370DB = RGB(147, 112, 219)
extern const Color MEDIUMPURPLE;
/// Hex #663399 = RGB(102, 51, 153)
extern const Color REBECCAPURPLE;
/// Hex #8A2BE2 = RGB(138, 43, 226)
extern const Color BLUEVIOLET;
/// Hex #9400D3 = RGB(148, 0, 211)
extern const Color DARKVIOLET;
/// Hex #9932CC = RGB(153, 50, 204)
extern const Color DARKORCHID;
/// Hex #8B008B = RGB(139, 0, 139)
extern const Color DARKMAGENTA;
/// Hex #800080 = RGB(128, 0, 128)
extern const Color PURPLE;
/// Hex #4B0082 = RGB(75, 0, 130)
extern const Color INDIGO;
/// Hex #6A5ACD = RGB(106, 90, 205)
extern const Color SLATEBLUE;
/// Hex #483D8B = RGB(72, 61, 139)
extern const Color DARKSLATEBLUE;
/// Hex #7B68EE = RGB(123, 104, 238)
extern const Color MEDIUMSLATEBLUE;

// GREEN HTML COLOR NAMES
/// Hex #ADFF2F = RGB(173, 255, 47)
extern const Color GREENYELLOW;
/// Hex #7FFF00 = RGB(127, 255, 0)
extern const Color CHARTREUSE;
/// Hex #7CFC00 = RGB(124, 252, 0)
extern const Color LAWNGREEN;
/// Hex #00FF00 = RGB(0, 255, 0)
extern const Color LIME;
/// Hex #32CD32 = RGB(50, 205, 50)
extern const Color LIMEGREEN;
/// Hex #98FB98 = RGB(152, 251, 152)
extern const Color PALEGREEN;
/// Hex #90EE90 = RGB(144, 238, 144)
extern const Color LIGHTGREEN;
/// Hex #00FA9A = RGB(0, 250, 154)
extern const Color MEDIUMSPRINGGREEN;
/// Hex #00FF7F = RGB(0, 255, 127)
extern const Color SPRINGGREEN;
/// Hex #3CB371 = RGB(60, 179, 113)
extern const Color MEDIUMSEAGREEN;
/// Hex #2E8B57 = RGB(46, 139, 87)
extern const Color SEAGREEN;
/// Hex #228B22 = RGB(34, 139, 34)
extern const Color FORESTGREEN;
/// Hex #008000 = RGB(0, 128, 0)
extern const Color GREEN;
/// Hex #006400 = RGB(0, 100, 0)
extern const Color DARKGREEN;
/// Hex #9ACD32 = RGB(154, 205, 50)
extern const Color YELLOWGREEN;
/// Hex #6B8E23 = RGB(107, 142, 35)
extern const Color OLIVEDRAB;
/// Hex #808000 = RGB(128, 128, 0)
extern const Color OLIVE;
/// Hex #556B2F = RGB(85, 107, 47)
extern const Color DARKOLIVEGREEN;
/// Hex #66CDAA = RGB(102, 205, 170)
extern const Color MEDIUMAQUAMARINE;
/// Hex #8FBC8B = RGB(143, 188, 139)
extern const Color DARKSEAGREEN;
/// Hex #20B2AA = RGB(32, 178, 170)
extern const Color LIGHTSEAGREEN;
/// Hex #008B8B = RGB(0, 139, 139)
extern const Color DARKCYAN;
/// Hex #008080 = RGB(0, 128, 128)
extern const Color TEAL;

// BLUE HTML COLOR NAMES
/// Hex #00FFFF = RGB(0, 255, 255)
extern const Color AQUA;
/// Hex #00FFFF = RGB(0, 255, 255)
extern const Color CYAN;
/// Hex #E0FFFF = RGB(224, 255, 255)
extern const Color LIGHTCYAN;
/// Hex #AFEEEE = RGB(175, 238, 238)
extern const Color PALETURQUOISE;
/// Hex #7FFFD4 = RGB(127, 255, 212)
extern const Color AQUAMARINE;
/// Hex #40E0D0 = RGB(64, 224, 208)
extern const Color TURQUOISE;
/// Hex #48D1CC = RGB(72, 209, 204)
extern const Color MEDIUMTURQUOISE;
/// Hex #00CED1 = RGB(0, 206, 209)
extern const Color DARKTURQUOISE;
/// Hex #5F9EA0 = RGB(95, 158, 160)
extern const Color CADETBLUE;
/// Hex #4682B4 = RGB(70, 130, 180)
extern const Color STEELBLUE;
/// Hex #B0C4DE = RGB(176, 196, 222)
extern const Color LIGHTSTEELBLUE;
/// Hex #B0E0E6 = RGB(176, 224, 230)
extern const Color POWDERBLUE;
/// Hex #ADD8E6 = RGB(173, 216, 230)
extern const Color LIGHTBLUE;
/// Hex #87CEEB = RGB(135, 206, 235)
extern const Color SKYBLUE;
/// Hex #87CEFA = RGB(135, 206, 250)
extern const Color LIGHTSKYBLUE;
/// Hex #00BFFF = RGB(0, 191, 255)
extern const Color DEEPSKYBLUE;
/// Hex #1E90FF = RGB(30, 144, 255)
extern const Color DODGERBLUE;
/// Hex #6495ED = RGB(100, 149, 237)
extern const Color CORNFLOWERBLUE;
// Hex #7B68EE = RGB(123, 104, 238)
// extern const Color MEDIUMSLATEBLUE; (duplicated above)
/// Hex #4169E1 = RGB(65, 105, 225)
extern const Color ROYALBLUE;
/// Hex #0000FF = RGB(0, 0, 255)
extern const Color BLUE;
/// Hex #0000CD = RGB(0, 0, 205)
extern const Color MEDIUMBLUE;
/// Hex #00008B = RGB(0, 0, 139)
extern const Color DARKBLUE;
/// Hex #000080 = RGB(0, 0, 128)
extern const Color NAVY;
/// Hex #191970 = RGB(25, 25, 112)
extern const Color MIDNIGHTBLUE;

// BROWN HTML COLOR NAMES
/// Hex #FFF8DC = RGB(255, 248, 220)
extern const Color CORNSILK;
/// Hex #FFEBCD = RGB(255, 235, 205)
extern const Color BLANCHEDALMOND;
/// Hex #FFE4C4 = RGB(255, 228, 196)
extern const Color BISQUE;
/// Hex #FFDEAD = RGB(255, 222, 173)
extern const Color NAVAJOWHITE;
/// Hex #F5DEB3 = RGB(245, 222, 179)
extern const Color WHEAT;
/// Hex #DEB887 = RGB(222, 184, 135)
extern const Color BURLYWOOD;
/// Hex #D2B48C = RGB(210, 180, 140)
extern const Color TAN;
/// Hex #BC8F8F = RGB(188, 143, 143)
extern const Color ROSYBROWN;
/// Hex #F4A460 = RGB(244, 164, 96)
extern const Color SANDYBROWN;
/// Hex #DAA520 = RGB(218, 165, 32)
extern const Color GOLDENROD;
/// Hex #B8860B = RGB(184, 134, 11)
extern const Color DARKGOLDENROD;
/// Hex #CD853F = RGB(205, 133, 63)
extern const Color PERU;
/// Hex #D2691E = RGB(210, 105, 30)
extern const Color CHOCOLATE;
/// Hex #8B4513 = RGB(139, 69, 19)
extern const Color SADDLEBROWN;
/// Hex #A0522D = RGB(160, 82, 45)
extern const Color SIENNA;
/// Hex #A52A2A = RGB(165, 42, 42)
extern const Color BROWN;
/// Hex #800000 = RGB(128, 0, 0)
extern const Color MAROON;

// WHITE HTML COLOR NAMES
/// Hex #FFFFFF = RGB(255, 255, 255)
extern const Color WHITE;
/// Hex #FFFAFA = RGB(255, 250, 250)
extern const Color SNOW;
/// Hex #F0FFF0 = RGB(240, 255, 240)
extern const Color HONEYDEW;
/// Hex #F5FFFA = RGB(245, 255, 250)
extern const Color MINTCREAM;
/// Hex #F0FFFF = RGB(240, 255, 255)
extern const Color AZURE;
/// Hex #F0F8FF = RGB(240, 248, 255)
extern const Color ALICEBLUE;
/// Hex #F8F8FF = RGB(248, 248, 255)
extern const Color GHOSTWHITE;
/// Hex #F5F5F5 = RGB(245, 245, 245)
extern const Color WHITESMOKE;
/// Hex #FFF5EE = RGB(255, 245, 238)
extern const Color SEASHELL;
/// Hex #F5F5DC = RGB(245, 245, 220)
extern const Color BEIGE;
/// Hex #FDF5E6 = RGB(253, 245, 230)
extern const Color OLDLACE;
/// Hex #FFFAF0 = RGB(255, 250, 240)
extern const Color FLORALWHITE;
/// Hex #FFFFF0 = RGB(255, 255, 240)
extern const Color IVORY;
/// Hex #FAEBD7 = RGB(250, 235, 215)
extern const Color ANTIQUEWHITE;
/// Hex #FAF0E6 = RGB(250, 240, 230)
extern const Color LINEN;
/// Hex #FFF0F5 = RGB(255, 240, 245)
extern const Color LAVENDERBLUSH;
/// Hex #FFE4E1 = RGB(255, 228, 225)
extern const Color MISTYROSE;

// GRAY HTML COLOR NAMES
/// Hex #DCDCDC = RGB(220, 220, 220)
extern const Color GAINSBORO;
/// Hex #D3D3D3 = RGB(211, 211, 211)
extern const Color LIGHTGRAY;
/// Hex #C0C0C0 = RGB(192, 192, 192)
extern const Color SILVER;
/// Hex #A9A9A9 = RGB(169, 169, 169)
extern const Color DARKGRAY;
/// Hex #808080 = RGB(128, 128, 128)
extern const Color GRAY;
/// Hex #696969 = RGB(105, 105, 105)
extern const Color DIMGRAY;
/// Hex #778899 = RGB(119, 136, 153)
extern const Color LIGHTSLATEGRAY;
/// Hex #708090 = RGB(112, 128, 144)
extern const Color SLATEGRAY;
/// Hex #2F4F4F = RGB(47, 79, 79)
extern const Color DARKSLATEGRAY;
/// Hex #000000 = RGB(0, 0, 0)
extern const Color BLACK;

// Extra
/// Transparent Hex #000000 = RGB(0, 0, 0)
extern const Color TRANSPARENTBLACK;
/// Transparent Hex #FFFFFF = RGB(255, 255, 255)
extern const Color TRANSPARENTWHITE;
}
}

```

### ColorConstants.cpp
```
#include "ColorConstants.h"

namespace Urho3D
{

namespace ColorConstants
{

//RED HTML COLOR NAMES
const Color INDIANRED(0xFFCD5C5C, Color::ARGB); // #CD5C5C = RGB(205, 92, 92)
const Color LIGHTCORAL(0xFFF08080, Color::ARGB); // #F08080 = RGB(240, 128, 128)
const Color SALMON(0xFFFA8072, Color::ARGB); // #FA8072 = RGB(250, 128, 114)
const Color DARKSALMON(0xFFE9967A, Color::ARGB); // #E9967A = RGB(233, 150, 122)
const Color LIGHTSALMON(0xFFFFA07A, Color::ARGB); // #FFA07A = RGB(255, 160, 122)
const Color CRIMSON(0xFFDC143C, Color::ARGB); // #DC143C = RGB(220, 20, 60)
const Color RED(0xFFFF0000, Color::ARGB); // #FF0000 = RGB(255, 0, 0)
const Color FIREBRICK(0xFFB22222, Color::ARGB); // #B22222 = RGB(178, 34, 34)
const Color DARKRED(0xFF8B0000, Color::ARGB); // #8B0000 = RGB(139, 0, 0)
//PINK HTML COLOR NAMES
const Color PINK(0xFFFFC0CB, Color::ARGB); // #FFC0CB = RGB(255, 192, 203)
const Color LIGHTPINK(0xFFFFB6C1, Color::ARGB); // #FFB6C1 = RGB(255, 182, 193)
const Color HOTPINK(0xFFFF69B4, Color::ARGB); // #FF69B4 = RGB(255, 105, 180)
const Color DEEPPINK(0xFFFF1493, Color::ARGB); // #FF1493 = RGB(255, 20, 147)
const Color MEDIUMVIOLETRED(0xFFC71585, Color::ARGB); // #C71585 = RGB(199, 21, 133)
const Color PALEVIOLETRED(0xFFDB7093, Color::ARGB); // #DB7093 = RGB(219, 112, 147)
//ORANGE HTML COLOR NAMES
//const Color LIGHTSALMON(0xFFFFA07A, Color::ARGB); (duplicate) // #FFA07A = RGB(255, 160, 122)
const Color CORAL(0xFFFF7F50, Color::ARGB); // #FF7F50 = RGB(255, 127, 80)
const Color TOMATO(0xFFFF6347, Color::ARGB); // #FF6347 = RGB(255, 99, 71)
const Color ORANGERED(0xFFFF4500, Color::ARGB); // #FF4500 = RGB(255, 69, 0)
const Color DARKORANGE(0xFFFF8C00, Color::ARGB); // #FF8C00 = RGB(255, 140, 0)
const Color ORANGE(0xFFFFA500, Color::ARGB); // #FFA500 = RGB(255, 165, 0)
//YELLOW HTML COLOR NAMES
const Color GOLD(0xFFFFD700, Color::ARGB); // #FFD700 = RGB(255, 215, 0)
const Color YELLOW(0xFFFFFF00, Color::ARGB); // #FFFF00 = RGB(255, 255, 0)
const Color LIGHTYELLOW(0xFFFFFFE0, Color::ARGB); // #FFFFE0 = RGB(255, 255, 224)
const Color LEMONCHIFFON(0xFFFFFACD, Color::ARGB); // #FFFACD = RGB(255, 250, 205)
const Color LIGHTGOLDENRODYELLOW(0xFFFAFAD2, Color::ARGB); // #FAFAD2 = RGB(250, 250, 210)
const Color PAPAYAWHIP(0xFFFFEFD5, Color::ARGB); // #FFEFD5 = RGB(255, 239, 213)
const Color MOCCASIN(0xFFFFE4B5, Color::ARGB); // #FFE4B5 = RGB(255, 228, 181)
const Color PEACHPUFF(0xFFFFDAB9, Color::ARGB); // #FFDAB9 = RGB(255, 218, 185)
const Color PALEGOLDENROD(0xFFEEE8AA, Color::ARGB); // #EEE8AA = RGB(238, 232, 170)
const Color KHAKI(0xFFF0E68C, Color::ARGB); // #F0E68C = RGB(240, 230, 140)
const Color DARKKHAKI(0xFFBDB76B, Color::ARGB); // #BDB76B = RGB(189, 183, 107)
//PURPLE HTML COLOR NAMES
const Color LAVENDER(0xFFE6E6FA, Color::ARGB); // #E6E6FA = RGB(230, 230, 250)
const Color THISTLE(0xFFD8BFD8, Color::ARGB); // #D8BFD8 = RGB(216, 191, 216)
const Color PLUM(0xFFDDA0DD, Color::ARGB); // #DDA0DD = RGB(221, 160, 221)
const Color VIOLET(0xFFEE82EE, Color::ARGB); // #EE82EE = RGB(238, 130, 238)
const Color ORCHID(0xFFDA70D6, Color::ARGB); // #DA70D6 = RGB(218, 112, 214)
const Color FUCHSIA(0xFFFF00FF, Color::ARGB); // #FF00FF = RGB(255, 0, 255)
const Color MAGENTA(0xFFFF00FF, Color::ARGB); // #FF00FF = RGB(255, 0, 255)
const Color MEDIUMORCHID(0xFFBA55D3, Color::ARGB); // #BA55D3 = RGB(186, 85, 211)
const Color MEDIUMPURPLE(0xFF9370DB, Color::ARGB); // #9370DB = RGB(147, 112, 219)
const Color REBECCAPURPLE(0xFF663399, Color::ARGB); // #663399 = RGB(102, 51, 153)
const Color BLUEVIOLET(0xFF8A2BE2, Color::ARGB); // #8A2BE2 = RGB(138, 43, 226)
const Color DARKVIOLET(0xFF9400D3, Color::ARGB); // #9400D3 = RGB(148, 0, 211)
const Color DARKORCHID(0xFF9932CC, Color::ARGB); // #9932CC = RGB(153, 50, 204)
const Color DARKMAGENTA(0xFF8B008B, Color::ARGB); // #8B008B = RGB(139, 0, 139)
const Color PURPLE(0xFF800080, Color::ARGB); // #800080 = RGB(128, 0, 128)
const Color INDIGO(0xFF4B0082, Color::ARGB); // #4B0082 = RGB(75, 0, 130)
const Color SLATEBLUE(0xFF6A5ACD, Color::ARGB); // #6A5ACD = RGB(106, 90, 205)
const Color DARKSLATEBLUE(0xFF483D8B, Color::ARGB); // #483D8B = RGB(72, 61, 139)
const Color MEDIUMSLATEBLUE(0xFF7B68EE, Color::ARGB); // #7B68EE = RGB(123, 104, 238)
//GREEN HTML COLOR NAMES
const Color GREENYELLOW(0xFFADFF2F, Color::ARGB); // #ADFF2F = RGB(173, 255, 47)
const Color CHARTREUSE(0xFF7FFF00, Color::ARGB); // #7FFF00 = RGB(127, 255, 0)
const Color LAWNGREEN(0xFF7CFC00, Color::ARGB); // #7CFC00 = RGB(124, 252, 0)
const Color LIME(0xFF00FF00, Color::ARGB); // #00FF00 = RGB(0, 255, 0)
const Color LIMEGREEN(0xFF32CD32, Color::ARGB); // #32CD32 = RGB(50, 205, 50)
const Color PALEGREEN(0xFF98FB98, Color::ARGB); // #98FB98 = RGB(152, 251, 152)
const Color LIGHTGREEN(0xFF90EE90, Color::ARGB); // #90EE90 = RGB(144, 238, 144)
const Color MEDIUMSPRINGGREEN(0xFF00FA9A, Color::ARGB); // #00FA9A = RGB(0, 250, 154)
const Color SPRINGGREEN(0xFF00FF7F, Color::ARGB); // #00FF7F = RGB(0, 255, 127)
const Color MEDIUMSEAGREEN(0xFF3CB371, Color::ARGB); // #3CB371 = RGB(60, 179, 113)
const Color SEAGREEN(0xFF2E8B57, Color::ARGB); // #2E8B57 = RGB(46, 139, 87)
const Color FORESTGREEN(0xFF228B22, Color::ARGB); // #228B22 = RGB(34, 139, 34)
const Color GREEN(0xFF008000, Color::ARGB); // #008000 = RGB(0, 128, 0)
const Color DARKGREEN(0xFF006400, Color::ARGB); // #006400 = RGB(0, 100, 0)
const Color YELLOWGREEN(0xFF9ACD32, Color::ARGB); // #9ACD32 = RGB(154, 205, 50)
const Color OLIVEDRAB(0xFF6B8E23, Color::ARGB); // #6B8E23 = RGB(107, 142, 35)
const Color OLIVE(0xFF808000, Color::ARGB); // #808000 = RGB(128, 128, 0)
const Color DARKOLIVEGREEN(0xFF556B2F, Color::ARGB); // #556B2F = RGB(85, 107, 47)
const Color MEDIUMAQUAMARINE(0xFF66CDAA, Color::ARGB); // #66CDAA = RGB(102, 205, 170)
const Color DARKSEAGREEN(0xFF8FBC8B, Color::ARGB); // #8FBC8B = RGB(143, 188, 139)
const Color LIGHTSEAGREEN(0xFF20B2AA, Color::ARGB); // #20B2AA = RGB(32, 178, 170)
const Color DARKCYAN(0xFF008B8B, Color::ARGB); // #008B8B = RGB(0, 139, 139)
const Color TEAL(0xFF008080, Color::ARGB); // #008080 = RGB(0, 128, 128)
//BLUE HTML COLOR NAMES
const Color AQUA(0xFF00FFFF, Color::ARGB); // #00FFFF = RGB(0, 255, 255)
const Color CYAN(0xFF00FFFF, Color::ARGB); // #00FFFF = RGB(0, 255, 255)
const Color LIGHTCYAN(0xFFE0FFFF, Color::ARGB); // #E0FFFF = RGB(224, 255, 255)
const Color PALETURQUOISE(0xFFAFEEEE, Color::ARGB); // #AFEEEE = RGB(175, 238, 238)
const Color AQUAMARINE(0xFF7FFFD4, Color::ARGB); // #7FFFD4 = RGB(127, 255, 212)
const Color TURQUOISE(0xFF40E0D0, Color::ARGB); // #40E0D0 = RGB(64, 224, 208)
const Color MEDIUMTURQUOISE(0xFF48D1CC, Color::ARGB); // #48D1CC = RGB(72, 209, 204)
const Color DARKTURQUOISE(0xFF00CED1, Color::ARGB); // #00CED1 = RGB(0, 206, 209)
const Color CADETBLUE(0xFF5F9EA0, Color::ARGB); // #5F9EA0 = RGB(95, 158, 160)
const Color STEELBLUE(0xFF4682B4, Color::ARGB); // #4682B4 = RGB(70, 130, 180)
const Color LIGHTSTEELBLUE(0xFFB0C4DE, Color::ARGB); // #B0C4DE = RGB(176, 196, 222)
const Color POWDERBLUE(0xFFB0E0E6, Color::ARGB); // #B0E0E6 = RGB(176, 224, 230)
const Color LIGHTBLUE(0xFFADD8E6, Color::ARGB); // #ADD8E6 = RGB(173, 216, 230)
const Color SKYBLUE(0xFF87CEEB, Color::ARGB); // #87CEEB = RGB(135, 206, 235)
const Color LIGHTSKYBLUE(0xFF87CEFA, Color::ARGB); // #87CEFA = RGB(135, 206, 250)
const Color DEEPSKYBLUE(0xFF00BFFF, Color::ARGB); // #00BFFF = RGB(0, 191, 255)
const Color DODGERBLUE(0xFF1E90FF, Color::ARGB); // #1E90FF = RGB(30, 144, 255)
const Color CORNFLOWERBLUE(0xFF6495ED, Color::ARGB); // #6495ED = RGB(100, 149, 237)
//const Color MEDIUMSLATEBLUE(0xFF7B68EE, Color::ARGB); (duplicate) // #7B68EE = RGB(123, 104, 238)
const Color ROYALBLUE(0xFF4169E1, Color::ARGB); // #4169E1 = RGB(65, 105, 225)
const Color BLUE(0xFF0000FF, Color::ARGB); // #0000FF = RGB(0, 0, 255)
const Color MEDIUMBLUE(0xFF0000CD, Color::ARGB); // #0000CD = RGB(0, 0, 205)
const Color DARKBLUE(0xFF00008B, Color::ARGB); // #00008B = RGB(0, 0, 139)
const Color NAVY(0xFF000080, Color::ARGB); // #000080 = RGB(0, 0, 128)
const Color MIDNIGHTBLUE(0xFF191970, Color::ARGB); // #191970 = RGB(25, 25, 112)
//BROWN HTML COLOR NAMES
const Color CORNSILK(0xFFFFF8DC, Color::ARGB); // #FFF8DC = RGB(255, 248, 220)
const Color BLANCHEDALMOND(0xFFFFEBCD, Color::ARGB); // #FFEBCD = RGB(255, 235, 205)
const Color BISQUE(0xFFFFE4C4, Color::ARGB); // #FFE4C4 = RGB(255, 228, 196)
const Color NAVAJOWHITE(0xFFFFDEAD, Color::ARGB); // #FFDEAD = RGB(255, 222, 173)
const Color WHEAT(0xFFF5DEB3, Color::ARGB); // #F5DEB3 = RGB(245, 222, 179)
const Color BURLYWOOD(0xFFDEB887, Color::ARGB); // #DEB887 = RGB(222, 184, 135)
const Color TAN(0xFFD2B48C, Color::ARGB); // #D2B48C = RGB(210, 180, 140)
const Color ROSYBROWN(0xFFBC8F8F, Color::ARGB); // #BC8F8F = RGB(188, 143, 143)
const Color SANDYBROWN(0xFFF4A460, Color::ARGB); // #F4A460 = RGB(244, 164, 96)
const Color GOLDENROD(0xFFDAA520, Color::ARGB); // #DAA520 = RGB(218, 165, 32)
const Color DARKGOLDENROD(0xFFB8860B, Color::ARGB); // #B8860B = RGB(184, 134, 11)
const Color PERU(0xFFCD853F, Color::ARGB); // #CD853F = RGB(205, 133, 63)
const Color CHOCOLATE(0xFFD2691E, Color::ARGB); // #D2691E = RGB(210, 105, 30)
const Color SADDLEBROWN(0xFF8B4513, Color::ARGB); // #8B4513 = RGB(139, 69, 19)
const Color SIENNA(0xFFA0522D, Color::ARGB); // #A0522D = RGB(160, 82, 45)
const Color BROWN(0xFFA52A2A, Color::ARGB); // #A52A2A = RGB(165, 42, 42)
const Color MAROON(0xFF800000, Color::ARGB); // #800000 = RGB(128, 0, 0)
//WHITE HTML COLOR NAMES
const Color WHITE(0xFFFFFFFF, Color::ARGB); // #FFFFFF = RGB(255, 255, 255)
const Color SNOW(0xFFFFFAFA, Color::ARGB); // #FFFAFA = RGB(255, 250, 250)
const Color HONEYDEW(0xFFF0FFF0, Color::ARGB); // #F0FFF0 = RGB(240, 255, 240)
const Color MINTCREAM(0xFFF5FFFA, Color::ARGB); // #F5FFFA = RGB(245, 255, 250)
const Color AZURE(0xFFF0FFFF, Color::ARGB); // #F0FFFF = RGB(240, 255, 255)
const Color ALICEBLUE(0xFFF0F8FF, Color::ARGB); // #F0F8FF = RGB(240, 248, 255)
const Color GHOSTWHITE(0xFFF8F8FF, Color::ARGB); // #F8F8FF = RGB(248, 248, 255)
const Color WHITESMOKE(0xFFF5F5F5, Color::ARGB); // #F5F5F5 = RGB(245, 245, 245)
const Color SEASHELL(0xFFFFF5EE, Color::ARGB); // #FFF5EE = RGB(255, 245, 238)
const Color BEIGE(0xFFF5F5DC, Color::ARGB); // #F5F5DC = RGB(245, 245, 220)
const Color OLDLACE(0xFFFDF5E6, Color::ARGB); // #FDF5E6 = RGB(253, 245, 230)
const Color FLORALWHITE(0xFFFFFAF0, Color::ARGB); // #FFFAF0 = RGB(255, 250, 240)
const Color IVORY(0xFFFFFFF0, Color::ARGB); // #FFFFF0 = RGB(255, 255, 240)
const Color ANTIQUEWHITE(0xFFFAEBD7, Color::ARGB); // #FAEBD7 = RGB(250, 235, 215)
const Color LINEN(0xFFFAF0E6, Color::ARGB); // #FAF0E6 = RGB(250, 240, 230)
const Color LAVENDERBLUSH(0xFFFFF0F5, Color::ARGB); // #FFF0F5 = RGB(255, 240, 245)
const Color MISTYROSE(0xFFFFE4E1, Color::ARGB); // #FFE4E1 = RGB(255, 228, 225)
//GRAY HTML COLOR NAMES
const Color GAINSBORO(0xFFDCDCDC, Color::ARGB); // #DCDCDC = RGB(220, 220, 220)
const Color LIGHTGRAY(0xFFD3D3D3, Color::ARGB); // #D3D3D3 = RGB(211, 211, 211)
const Color SILVER(0xFFC0C0C0, Color::ARGB); // #C0C0C0 = RGB(192, 192, 192)
const Color DARKGRAY(0xFFA9A9A9, Color::ARGB); // #A9A9A9 = RGB(169, 169, 169)
const Color GRAY(0xFF808080, Color::ARGB); // #808080 = RGB(128, 128, 128)
const Color DIMGRAY(0xFF696969, Color::ARGB); // #696969 = RGB(105, 105, 105)
const Color LIGHTSLATEGRAY(0xFF778899, Color::ARGB); // #778899 = RGB(119, 136, 153)
const Color SLATEGRAY(0xFF708090, Color::ARGB); // #708090 = RGB(112, 128, 144)
const Color DARKSLATEGRAY(0xFF2F4F4F, Color::ARGB); // #2F4F4F = RGB(47, 79, 79)
const Color BLACK(0xFF000000, Color::ARGB); // #000000 = RGB(0, 0, 0)
//Extra
const Color TRANSPARENTBLACK(0x00000000, Color::ARGB); // Transparent #000000 = RGB(0, 0, 0)
const Color TRANSPARENTWHITE(0x00FFFFFF, Color::ARGB); // Transparent #FFFFFF = RGB(255, 255, 255)
}
}
```

-------------------------

