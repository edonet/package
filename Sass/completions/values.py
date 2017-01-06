# FUNCTIONS
annotation   = ("annotation()\tValue", "annotation(${1})")
attr         = ("attr()\tValue", "attr(${1:name})")
blur         = ("blur()\tValue", "blur(${1:<length>})")
brightness   = ("brightness()\tValue", "brightness(${1})")
calc         = ("calc()\tValue", "calc(${1})")
character_variant = ("character-variant()\tValue", "character-variant(${1})")
circle       = ("circle()\tValue", "circle(${1})")
color_func   = ("color()\tValue", "color(${1})")
content      = ("content()\tValue", "content(${1})")
contrast     = ("contrast()\tValue", "contrast(${1})")
counter      = ("counter()\tValue", "counter(${1:<ident>}${2:, ${3:<list-style-type>}})")
counters     = ("counters()\tValue", "counters(${1:<ident>}, \"${2:<string>}\"${3:, ${4:<list-style-type>}})")
cross_fade   = ("cross-fade()\tValue", "cross-fade(${1})")
cubic_bezier = ("cubic-bezier()\tValue", "cubic-bezier(${1:0}, ${2:0}, ${3:0}, ${4:0})")
device_cmyk  = ("device-cmyk()\tValue", "device-cmyk(${1:0}, ${2:0}, ${3:0}, ${4:0}${5:, ${6:0.0}}${7:, ${8:<color>}})")
drop_shadow  = ("drop-shadow()\tValue", "drop-shadow(${1:<length>} ${2:<length>})")
element      = ("element()\tValue", "element(#${1})")
ellipse      = ("ellipse()\tValue", "ellipse(${1})")
filter_func  = ("filter()\tValue", "filter(${1})")
format_func  = ("format()\tValue", "format(\"${1}\")")
gray         = ("gray()\tValue", "gray(${1})")
grayscale    = ("grayscale()\tValue", "grayscale(${1})")
hsl          = ("hsl()\tValue", "hsl(${1:<hue>}, ${2}%, ${3}%)")
hsla         = ("hsla()\tValue", "hsla(${1:<hue>}, ${2}%, ${3}%, ${4:0.0})")
hwb          = ("hwb()\tValue", "hwb(${1:<hue>}, ${2}%, ${3}%${4:, ${5:0.0}})")
hue_rotate   = ("hue-rotate()\tValue", "hue-rotate(${1:<angle>})")
icc_color    = ("icc-color()\tValue", "icc-color(${1})")
image_func   = ("image()\tValue", "image(${1})")
image_set    = ("image-set()\tValue", "image-set(${1})")
inset        = ("inset()\tValue", "inset(${1})")
invert       = ("invert()\tValue", "invert(${1})")
local        = ("local()\tValue", "local(${1})")
matrix       = ("matrix()\tValue", "matrix(${1:0}, ${2:0}, ${3:0}, ${4:0}, ${5:0}, ${6:0})")
matrix3d     = ("matrix3d()\tValue", "matrix3d(${1:0}, ${2:0}, ${3:0}, ${4:0}, ${5:0}, ${6:0}, ${7:0}, ${8:0}, ${9:0}, ${10:0}, ${11:0}, ${12:0}, ${13:0}, ${14:0}, ${15:0}, ${16:0})")
minmax       = ("minmax()\tValue", "minmax(${1}, ${2})")
opacity      = ("opacity()\tValue", "opacity(${1})")
ornaments    = ("ornaments()\tValue", "ornaments(${1})")
path         = ("path()\tValue", "path(${1})")
perspective  = ("perspective()\tValue", "perspective(${1:<length>})")
polygon      = ("polygon()\tValue", "polygon(${1})")
repeat       = ("repeat()\tValue", "repeat(${1})")
rgb          = ("rgb()\tValue", "rgb($1)")
rgba         = ("rgba()\tValue", "rgba($1)")
rotate       = ("rotate()\tValue", "rotate(${1:<angle>})")
rotate3d     = ("rotate3d()\tValue", "rotate3d(${1:0}, ${2:0}, ${3:0}, ${4:<angle>})")
rotateX      = ("rotateX()\tValue", "rotateX(${1:<angle>})")
rotateY      = ("rotateY()\tValue", "rotateY(${1:<angle>})")
rotateZ      = ("rotateZ()\tValue", "rotateZ(${1:<angle>})")
saturate     = ("saturate()\tValue", "saturate(${1})")
scale        = ("scale()\tValue", "scale(${1:0}${2:, ${3:0}})")
scale3d      = ("scale3d()\tValue", "scale3d(${1:0}, ${2:0}, ${3:0})")
scaleX       = ("scaleX()\tValue", "scaleX(${1:0})")
scaleY       = ("scaleY()\tValue", "scaleY(${1:0})")
scaleZ       = ("scaleZ()\tValue", "scaleZ(${1:0})")
sepia        = ("sepia()\tValue", "sepia(${1})")
skew         = ("skew()\tValue", "skew(${1:<angle>}${2:, ${3:<angle>}})")
skewX        = ("skewX()\tValue", "skewX(${1:<angle>})")
skewY        = ("skewY()\tValue", "skewY(${1:<angle>})")
steps        = ("steps()\tValue", "steps(${1})")
styleset     = ("styleset()\tValue", "styleset(${1})")
stylistic    = ("stylistic()\tValue", "stylistic(${1})")
symbols      = ("symbols()\tValue", "symbols(${1})")
swash        = ("swash()\tValue", "swash(${1})")
toggle       = ("toggle()\tValue", "toggle(${1})")
translate    = ("translate()\tValue", "translate(${1:<length>}${2:, ${3:<length>}})")
translate3d  = ("translate3d()\tValue", "translate3d(${1:<length>}, ${2:<length>}, ${3:<length>})")
translateX   = ("translateX()\tValue", "translateX(${1:<length>})")
translateY   = ("translateY()\tValue", "translateY(${1:<length>})")
translateZ   = ("translateZ()\tValue", "translateZ(${1:<length>})")
url          = ("url()\tValue", "url(${1})")
var          = ("var()\tValue", "var(--${1:name}, ${2:value})")
conic_gradient  = ("conic-gradient()\tValue", "conic-gradient(${1})")
linear_gradient = ("linear-gradient()\tValue", "linear-gradient(${1})")
radial_gradient = ("radial-gradient()\tValue", "radial-gradient(${1})")
repeating_conic_gradient  = ("repeating-conic-gradient()\tValue", "repeating-conic-gradient(${1})")
repeating_linear_gradient = ("repeating-linear-gradient()\tValue", "repeating-linear-gradient(${1})")
repeating_radial_gradient = ("repeating-radial-gradient()\tValue", "repeating-radial-gradient(${1})")


# TYPES
basic_shape = [inset, circle, ellipse, polygon]
color       = [("aliceblue\tColor", 'aliceblue'), ("antiquewhite\tColor", 'antiquewhite'), ("aqua\tColor", 'aqua'), ("aquamarine\tColor", 'aquamarine'), ("azure\tColor", 'azure'), ("beige\tColor", 'beige'), ("bisque\tColor", 'bisque'), ("black\tColor", 'black'), ("blanchedalmond\tColor", 'blanchedalmond'), ("blue\tColor", 'blue'), ("blueviolet\tColor", 'blueviolet'), ("brown\tColor", 'brown'), ("burlywood\tColor", 'burlywood'), ("cadetblue\tColor", 'cadetblue'), ("chartreuse\tColor", 'chartreuse'), ("chocolate\tColor", 'chocolate'), ("coral\tColor", 'coral'), ("cornflowerblue\tColor", 'cornflowerblue'), ("cornsilk\tColor", 'cornsilk'), ("crimson\tColor", 'crimson'), ("currentColor\tColor", 'currentColor'), ("currentcolor\tColor", 'currentcolor'), ("cyan\tColor", 'cyan'), ("darkblue\tColor", 'darkblue'), ("darkcyan\tColor", 'darkcyan'), ("darkgoldenrod\tColor", 'darkgoldenrod'), ("darkgray\tColor", 'darkgray'), ("darkgreen\tColor", 'darkgreen'), ("darkgrey\tColor", 'darkgrey'), ("darkkhaki\tColor", 'darkkhaki'), ("darkmagenta\tColor", 'darkmagenta'), ("darkolivegreen\tColor", 'darkolivegreen'), ("darkorange\tColor", 'darkorange'), ("darkorchid\tColor", 'darkorchid'), ("darkred\tColor", 'darkred'), ("darksalmon\tColor", 'darksalmon'), ("darkseagreen\tColor", 'darkseagreen'), ("darkslateblue\tColor", 'darkslateblue'), ("darkslategray\tColor", 'darkslategray'), ("darkslategrey\tColor", 'darkslategrey'), ("darkturquoise\tColor", 'darkturquoise'), ("darkviolet\tColor", 'darkviolet'), ("deeppink\tColor", 'deeppink'), ("deepskyblue\tColor", 'deepskyblue'), ("dimgray\tColor", 'dimgray'), ("dimgrey\tColor", 'dimgrey'), ("dodgerblue\tColor", 'dodgerblue'), ("firebrick\tColor", 'firebrick'), ("floralwhite\tColor", 'floralwhite'), ("forestgreen\tColor", 'forestgreen'), ("fuchsia\tColor", 'fuchsia'), ("gainsboro\tColor", 'gainsboro'), ("ghostwhite\tColor", 'ghostwhite'), ("gold\tColor", 'gold'), ("goldenrod\tColor", 'goldenrod'), ("gray\tColor", 'gray'), ("green\tColor", 'green'), ("greenyellow\tColor", 'greenyellow'), ("grey\tColor", 'grey'), ("honeydew\tColor", 'honeydew'), ("hotpink\tColor", 'hotpink'), ("indianred\tColor", 'indianred'), ("indigo\tColor", 'indigo'), ("ivory\tColor", 'ivory'), ("khaki\tColor", 'khaki'), ("lavender\tColor", 'lavender'), ("lavenderblush\tColor", 'lavenderblush'), ("lawngreen\tColor", 'lawngreen'), ("lemonchiffon\tColor", 'lemonchiffon'), ("lightblue\tColor", 'lightblue'), ("lightcoral\tColor", 'lightcoral'), ("lightcyan\tColor", 'lightcyan'), ("lightgoldenrodyellow\tColor", 'lightgoldenrodyellow'), ("lightgray\tColor", 'lightgray'), ("lightgreen\tColor", 'lightgreen'), ("lightgrey\tColor", 'lightgrey'), ("lightpink\tColor", 'lightpink'), ("lightsalmon\tColor", 'lightsalmon'), ("lightseagreen\tColor", 'lightseagreen'), ("lightskyblue\tColor", 'lightskyblue'), ("lightslategray\tColor", 'lightslategray'), ("lightslategrey\tColor", 'lightslategrey'), ("lightsteelblue\tColor", 'lightsteelblue'), ("lightyellow\tColor", 'lightyellow'), ("lime\tColor", 'lime'), ("limegreen\tColor", 'limegreen'), ("linen\tColor", 'linen'), ("magenta\tColor", 'magenta'), ("maroon\tColor", 'maroon'), ("mediumaquamarine\tColor", 'mediumaquamarine'), ("mediumblue\tColor", 'mediumblue'), ("mediumorchid\tColor", 'mediumorchid'), ("mediumpurple\tColor", 'mediumpurple'), ("mediumseagreen\tColor", 'mediumseagreen'), ("mediumslateblue\tColor", 'mediumslateblue'), ("mediumspringgreen\tColor", 'mediumspringgreen'), ("mediumturquoise\tColor", 'mediumturquoise'), ("mediumvioletred\tColor", 'mediumvioletred'), ("midnightblue\tColor", 'midnightblue'), ("mintcream\tColor", 'mintcream'), ("mistyrose\tColor", 'mistyrose'), ("moccasin\tColor", 'moccasin'), ("navajowhite\tColor", 'navajowhite'), ("navy\tColor", 'navy'), ("oldlace\tColor", 'oldlace'), ("olive\tColor", 'olive'), ("olivedrab\tColor", 'olivedrab'), ("orange\tColor", 'orange'), ("orangered\tColor", 'orangered'), ("orchid\tColor", 'orchid'), ("palegoldenrod\tColor", 'palegoldenrod'), ("palegreen\tColor", 'palegreen'), ("paleturquoise\tColor", 'paleturquoise'), ("palevioletred\tColor", 'palevioletred'), ("papayawhip\tColor", 'papayawhip'), ("peachpuff\tColor", 'peachpuff'), ("peru\tColor", 'peru'), ("pink\tColor", 'pink'), ("plum\tColor", 'plum'), ("powderblue\tColor", 'powderblue'), ("purple\tColor", 'purple'), ("rebeccapurple\tColor", 'rebeccapurple'), ("red\tColor", 'red'), ("rosybrown\tColor", 'rosybrown'), ("royalblue\tColor", 'royalblue'), ("saddlebrown\tColor", 'saddlebrown'), ("salmon\tColor", 'salmon'), ("sandybrown\tColor", 'sandybrown'), ("seagreen\tColor", 'seagreen'), ("seashell\tColor", 'seashell'), ("sienna\tColor", 'sienna'), ("silver\tColor", 'silver'), ("skyblue\tColor", 'skyblue'), ("slateblue\tColor", 'slateblue'), ("slategray\tColor", 'slategray'), ("slategrey\tColor", 'slategrey'), ("snow\tColor", 'snow'), ("springgreen\tColor", 'springgreen'), ("steelblue\tColor", 'steelblue'), ("tan\tColor", 'tan'), ("teal\tColor", 'teal'), ("thistle\tColor", 'thistle'), ("tomato\tColor", 'tomato'), ("transparent\tColor", 'transparent'), ("turquoise\tColor", 'turquoise'), ("violet\tColor", 'violet'), ("wheat\tColor", 'wheat'), ("white\tColor", 'white'), ("whitesmoke\tColor", 'whitesmoke'), ("yellow\tColor", 'yellow'), ("yellowgreen\tColor", 'yellowgreen'), color_func, device_cmyk, gray, hsl, hsla, hwb, rgb, rgba]
counter_style = [("afar\tValue", 'afar'), ("agaw\tValue", 'agaw'), ("ancient-tamil\tValue", 'ancient-tamil'), ("arabic-indic\tValue", 'arabic-indic'), ("ari\tValue", 'ari'), ("armenian\tValue", 'armenian'), ("bengali\tValue", 'bengali'), ("binary\tValue", 'binary'), ("blin\tValue", 'blin'), ("cambodian\tValue", 'cambodian'), ("cambodian-consonant\tValue", 'cambodian-consonant'), ("circle\tValue", 'circle'), ("circled-decimal\tValue", 'circled-decimal'), ("circled-ideograph\tValue", 'circled-ideograph'), ("circled-katakana\tValue", 'circled-katakana'), ("circled-korean-consonant\tValue", 'circled-korean-consonant'), ("circled-korean-syllable\tValue", 'circled-korean-syllable'), ("circled-lower-latin\tValue", 'circled-lower-latin'), ("circled-upper-latin\tValue", 'circled-upper-latin'), ("cjk-decimal\tValue", 'cjk-decimal'), ("cjk-earthly-branch\tValue", 'cjk-earthly-branch'), ("cjk-heavenly-stem\tValue", 'cjk-heavenly-stem'), ("cjk-ideographic\tValue", 'cjk-ideographic'), ("decimal\tValue", 'decimal'), ("decimal-leading-zero\tValue", 'decimal-leading-zero'), ("devanagari\tValue", 'devanagari'), ("disc\tValue", 'disc'), ("disclosure-closed\tValue", 'disclosure-closed'), ("disclosure-open\tValue", 'disclosure-open'), ("dizi\tValue", 'dizi'), ("dotted-decimal\tValue", 'dotted-decimal'), ("double-circled-decimal\tValue", 'double-circled-decimal'), ("ethiopic-numeric\tValue", 'ethiopic-numeric'), ("filled-circled-decimal\tValue", 'filled-circled-decimal'), ("fullwidth-decimal\tValue", 'fullwidth-decimal'), ("fullwidth-lower-alpha\tValue", 'fullwidth-lower-alpha'), ("fullwidth-lower-roman\tValue", 'fullwidth-lower-roman'), ("fullwidth-upper-alpha\tValue", 'fullwidth-upper-alpha'), ("fullwidth-upper-roman\tValue", 'fullwidth-upper-roman'), ("gedeo\tValue", 'gedeo'), ("georgian\tValue", 'georgian'), ("greek\tValue", 'greek'), ("gujarati\tValue", 'gujarati'), ("gumuz\tValue", 'gumuz'), ("gurmukhi\tValue", 'gurmukhi'), ("hadiyya\tValue", 'hadiyya'), ("harari\tValue", 'harari'), ("hebrew\tValue", 'hebrew'), ("hebrew-extended\tValue", 'hebrew-extended'), ("hindi\tValue", 'hindi'), ("hiragana\tValue", 'hiragana'), ("hiragana-iroha\tValue", 'hiragana-iroha'), ("japanese-formal\tValue", 'japanese-formal'), ("japanese-informal\tValue", 'japanese-informal'), ("kaffa\tValue", 'kaffa'), ("kannada\tValue", 'kannada'), ("katakana\tValue", 'katakana'), ("katakana-iroha\tValue", 'katakana-iroha'), ("kebena\tValue", 'kebena'), ("kembata\tValue", 'kembata'), ("khmer\tValue", 'khmer'), ("khmer-consonant\tValue", 'khmer-consonant'), ("konso\tValue", 'konso'), ("korean-consonant\tValue", 'korean-consonant'), ("korean-hangul-formal\tValue", 'korean-hangul-formal'), ("korean-hanja-formal\tValue", 'korean-hanja-formal'), ("korean-hanja-informal\tValue", 'korean-hanja-informal'), ("korean-syllable\tValue", 'korean-syllable'), ("kunama\tValue", 'kunama'), ("lao\tValue", 'lao'), ("lepcha\tValue", 'lepcha'), ("lower-alpha\tValue", 'lower-alpha'), ("lower-alpha-symbolic\tValue", 'lower-alpha-symbolic'), ("lower-armenian\tValue", 'lower-armenian'), ("lower-belorussian\tValue", 'lower-belorussian'), ("lower-bulgarian\tValue", 'lower-bulgarian'), ("lower-greek\tValue", 'lower-greek'), ("lower-hexadecimal\tValue", 'lower-hexadecimal'), ("lower-latin\tValue", 'lower-latin'), ("lower-macedonian\tValue", 'lower-macedonian'), ("lower-oromo-qubee\tValue", 'lower-oromo-qubee'), ("lower-roman\tValue", 'lower-roman'), ("lower-russian\tValue", 'lower-russian'), ("lower-russian-full\tValue", 'lower-russian-full'), ("lower-serbo-croatian\tValue", 'lower-serbo-croatian'), ("lower-ukrainian\tValue", 'lower-ukrainian'), ("lower-ukrainian-full\tValue", 'lower-ukrainian-full'), ("malayalam\tValue", 'malayalam'), ("meen\tValue", 'meen'), ("mongolian\tValue", 'mongolian'), ("myanmar\tValue", 'myanmar'), ("new-base-60",), ("none\tValue", 'none'), ("octal\tValue", 'octal'), ("oriya\tValue", 'oriya'), ("oromo\tValue", 'oromo'), ("parenthesized-decimal\tValue", 'parenthesized-decimal'), ("parenthesized-hangul-consonant\tValue", 'parenthesized-hangul-consonant'), ("parenthesized-hangul-syllable\tValue", 'parenthesized-hangul-syllable'), ("parenthesized-ideograph\tValue", 'parenthesized-ideograph'), ("parenthesized-lower-latin\tValue", 'parenthesized-lower-latin'), ("persian\tValue", 'persian'), ("persian-abjad\tValue", 'persian-abjad'), ("persian-alphabetic\tValue", 'persian-alphabetic'), ("saho\tValue", 'saho'), ("shan\tValue", 'shan'), ("sidama\tValue", 'sidama'), ("silti\tValue", 'silti'), ("simp-chinese-formal\tValue", 'simp-chinese-formal'), ("simp-chinese-informal\tValue", 'simp-chinese-informal'), ("simple-lower-roman\tValue", 'simple-lower-roman'), ("simple-upper-roman\tValue", 'simple-upper-roman'), ("square\tValue", 'square'), ("super-decimal\tValue", 'super-decimal'), ("tamil\tValue", 'tamil'), ("telugu\tValue", 'telugu'), ("thai\tValue", 'thai'), ("thai-alphabetic\tValue", 'thai-alphabetic'), ("tibetan\tValue", 'tibetan'), ("tigre\tValue", 'tigre'), ("trad-chinese-formal\tValue", 'trad-chinese-formal'), ("trad-chinese-informal\tValue", 'trad-chinese-informal'), ("upper-alpha\tValue", 'upper-alpha'), ("upper-alpha-symbolic\tValue", 'upper-alpha-symbolic'), ("upper-armenian\tValue", 'upper-armenian'), ("upper-belorussian\tValue", 'upper-belorussian'), ("upper-bulgarian\tValue", 'upper-bulgarian'), ("upper-hexadecimal\tValue", 'upper-hexadecimal'), ("upper-latin\tValue", 'upper-latin'), ("upper-macedonian\tValue", 'upper-macedonian'), ("upper-oromo-qubee\tValue", 'upper-oromo-qubee'), ("upper-roman\tValue", 'upper-roman'), ("upper-russian\tValue", 'upper-russian'), ("upper-russian-full\tValue", 'upper-russian-full'), ("upper-serbo-croatian\tValue", 'upper-serbo-croatian'), ("upper-ukrainian\tValue", 'upper-ukrainian'), ("upper-ukrainian-full\tValue", 'upper-ukrainian-full'), ("wolaita\tValue", 'wolaita'), ("yemsa\tValue", 'yemsa')]
filters     = [blur, brightness, contrast, drop_shadow, grayscale, hue_rotate, invert, opacity, saturate, sepia]
image       = [conic_gradient, cross_fade, element, filter_func, image_func, image_set, linear_gradient, radial_gradient, repeating_conic_gradient, repeating_linear_gradient, repeating_radial_gradient, url]
# TODO: this should be enabled only inside the color(), hsl(), hsla(), and hwb() functions
# hue         = [("blue\tValue", 'blue'), ("bluish\tValue", 'bluish'), ("bluish()", "bluish(${1}%)"), ("green\tValue", 'green'), ("greenish\tValue", 'greenish'), ("greenish()", "greenish(${1}%)"), ("orange\tValue", 'orange'), ("orangish\tValue", 'orangish'), ("orangish()", "orangish(${1}%)"), ("purple\tValue", 'purple'), ("purplish\tValue", 'purplish'), ("purplish()", "purplish(${1}%)"), ("red\tValue", 'red'), ("reddish\tValue", 'reddish'), ("reddish()", "reddish(${1}%)"), ("yellow\tValue", 'yellow'), ("yellowish\tValue", 'yellowish'), ("yellowish()", "yellowish(${1}%)"), angle, number]
position    = [("bottom\tValue", 'bottom'), ("center\tValue", 'center'), ("left\tValue", 'left'), ("right\tValue", 'right'), ("top\tValue", 'top')]
timing_function = [("ease\tValue", 'ease'), ("ease-in\tValue", 'ease-in'), ("ease-in-out\tValue", 'ease-in-out'), ("ease-out\tValue", 'ease-out'), ("linear\tValue", 'linear'), ("step-end\tValue", 'step-end'), ("step-start\tValue", 'step-start'), cubic_bezier, steps]
transform   = [matrix, matrix3d, perspective, rotate, rotate3d, rotateX, rotateY, rotateZ, scale, scale3d, scaleX, scaleY, scaleZ, skew, skewX, skewY, translate, translate3d, translateX, translateY, translateZ]



# TODO
# add completions to the scopes inside functions.
#   missing lots of completion opportunities, e.g. all the <hue> and color() funcs
#     e.g. reddish, purplish, lightness, l, whiteness, w
#     <hue> should only be available inside color(), hsl(), hsla(), and hwb()
#   need to go through every #type-function-* rule and add completions for all the contents of those rules
