import sublime, re

# HTML Tag List
tag_list = [
    ("a\tTag", "a href=\"$1\">$2</a>"),
    ("abbr\tTag", "abbr>$1</abbr>"),
    ("acronym\tTag", "acronym>$1</acronym>"),
    ("address\tTag", "address>$1</address>"),
    ("area\tTag", "area shape=\"${1:rect}\" coords=\"$2\" href =\"$3\" alt=\"$4\" />"),
    ("article\tTag", "article>$1</article>"),
    ("aside\tTag", "aside>$1</aside>"),
    ("audio\tTag", "audio src=\"$1\">$2</audio>"),
    ("b\tTag", "b>$1</b>"),
    ("base\tTag", "base href=\"$1\" />"),
    ("bdi\tTag", "bdi>$1</bdi>"),
    ("bdo\tTag", "bdo>$1</bdo>"),
    ("big\tTag", "big>$1</big>"),
    ("blockquote\tTag", "blockquote>$1</blockquote>"),
    ("body\tTag", "body>$1</body>"),
    ("br\tTag", "br />"),
    ("button\tTag", "button>$1</button>"),
    ("canvas\tTag", "canvas>$1</canvas>"),
    ("caption\tTag", "caption>$1</caption>"),
    ("cite\tTag", "cite>$1</cite>"),
    ("code\tTag", "code>$1</code>"),
    ("col\tTag", "col />"),
    ("colgroup\tTag", "colgroup>$1</colgroup>"),
    ("command\tTag", "command>$1</command>"),
    ("datalist\tTag", "datalist>$1</datalist>"),
    ("dd\tTag", "dd>$1</dd>"),
    ("del\tTag", "del>$1</del>"),
    ("details\tTag", "details>$1</details>"),
    ("div\tTag", "div>$1</div>"),
    ("dfn\tTag", "dfn>$1</dfn>"),
    ("dialog\tTag", "dialog>$1</dialog>"),
    ("dl\tTag", "dl>$1</dl>"),
    ("dt\tTag", "dt>$1</dt>"),
    ("em\tTag", "em>$1</em>"),
    ("embed\tTag", "embed src=\"$1\" />"),
    ("fieldset\tTag", "fieldset>$1</fieldset>"),
    ("figcaption\tTag", "figcaption>$1</figcaption>"),
    ("figure\tTag", "figure>$1</figure>"),
    ("footer\tTag", "footer>$1</footer>"),
    ("form\tTag", "form action=\"$1\" method=\"${2:post}\">$1</form>"),
    ("frame\tTag", "frame src=\"$1\" />"),
    ("frameset\tTag", "frameset>$1</frameset>"),
    ("h1\tTag", "h1>$1</h1>"),
    ("h2\tTag", "h2>$1</h2>"),
    ("h3\tTag", "h3>$1</h3>"),
    ("h4\tTag", "h4>$1</h4>"),
    ("h5\tTag", "h5>$1</h5>"),
    ("h6\tTag", "h6>$1</h6>"),
    ("head\tTag", "head>$1</head>"),
    ("header\tTag", "header>$1</header>"),
    ("hr\tTag", "hr />"),
    ("i\tTag", "i>$1</i>"),
    ("iframe\tTag", "iframe>$1</iframe>"),
    ("img\tTag", "img src=\"$1\" alt=\"$2\" />"),
    ("input\tTag", "input type=\"${1:text}\" />"),
    ("ins\tTag", "ins>$1</ins>"),
    ("kbd\tTag", "kbd>$1</kbd>"),
    ("keygen\tTag", "keygen>$1</keygen>"),
    ("label\tTag", "label>$1</label>"),
    ("legend\tTag", "legend>$1</legend>"),
    ("li\tTag", "li>$1</li>"),
    ("link\tTag", "link type=\"text/css\" rel=\"stylesheet\" href=\"$1\">"),
    ("main\tTag", "main>$1</main>"),
    ("map\tTag", "map id=\"$1\">$2</map>"),
    ("mark\tTag", "mark>$1</mark>"),
    ("menu\tTag", "menu>$1</menu>"),
    ("menuitem\tTag", "menuitem>$1</menuitem>"),
    ("meta\tTag", "meta name=\"$1\" content=\"$2\">"),
    ("meter\tTag", "meter>$1</meter>"),
    ("nav\tTag", "nav>$1</nav>"),
    ("noframes\tTag", "noframes>$1</noframes>"),
    ("noscript\tTag", "noscript>$1</noscript>"),
    ("object\tTag", "object>$1</object>"),
    ("ol\tTag", "ol>$1</ol>"),
    ("optgroup\tTag", "optgroup label=\"$1\">$2</optgroup>"),
    ("option\tTag", "option>$1</option>"),
    ("output\tTag", "output>$1</output>"),
    ("p\tTag", "p>$1</p>"),
    ("param\tTag", "param name=\"$1\" value=\"$2\" />"),
    ("pre\tTag", "pre>$1</pre>"),
    ("progress\tTag", "progress value=\"$1\" max=\"$2\">$3</progress>"),
    ("q\tTag", "q>$1</q>"),
    ("rp\tTag", "rp>$1</rp>"),
    ("rt\tTag", "rt>$1</rt>"),
    ("ruby\tTag", "ruby>$1</ruby>"),
    ("samp\tTag", "samp>$1</samp>"),
    ("script\tTag", "script type=\"text/javascript\" src=\"$1\" defer></script>"),
    ("section\tTag", "section>$1</section>"),
    ("select\tTag", "select>$1</select>"),
    ("small\tTag", "small>$1</small>"),
    ("source\tTag", "source src=\"$1\" type=\"$2\" >"),
    ("span\tTag", "span>$1</span>"),
    ("strong\tTag", "strong>$1</strong>"),
    ("style\tTag", "style type=\"${1:text/css}\">$0</style>"),
    ("sub\tTag", "sub>$1</sub>"),
    ("summary\tTag", "summary>$1</summary>"),
    ("sup\tTag", "sup>$1</sup>"),
    ("table\tTag", "table>$1</table>"),
    ("tbody\tTag", "tbody>$1</tbody>"),
    ("td\tTag", "td>$1</td>"),
    ("textarea\tTag", "textarea>$1</textarea>"),
    ("tfoot\tTag", "tfoot>$1</tfoot>"),
    ("th\tTag", "th>$1</th>"),
    ("thead\tTag", "thead>$1</thead>"),
    ("time\tTag", "time>$1</time>"),
    ("title\tTag", "title>$1</title>"),
    ("tr\tTag", "tr>$1</tr>"),
    ("track\tTag", "track>$1</track>"),
    ("tt\tTag", "tt>$1</tt>"),
    ("ul\tTag", "ul>$1</ul>"),
    ("var\tTag", "var>$1</var>"),
    ("video\tTag", "video src=\"$1\">$2</video>"),

    ("doctype\tTag", "!doctype html>"),
    ("DOCTYPE\tTag", "!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">"),
    ("html\tSnippet", "!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n<html xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" >\n<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">\n<title>${1:Index}</title>\n<meta name=\"keywords\" content=\"\">\n<meta name=\"description\" content=\"\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no\">\n<link rel=\"shortcut icon\" href=\"favicon.ico\" type=\"image/x-icon\">\n</head>\n\n<body>\n\t$2\n</body>\n</html>"),
    ("html:5\tSnippet", "!doctype html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">\n<title>${1:Index}</title>\n<meta name=\"keywords\" content=\"\">\n<meta name=\"description\" content=\"\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no\">\n<link rel=\"shortcut icon\" href=\"favicon.ico\" type=\"image/x-icon\">\n</head>\n\n<body>\n\t$2\n</body>\n</html>"),
    ("html:fix\tSnippet", "!doctype html>\n<!--[if lt IE 7]><html class=\"ie6\"><![endif]-->\n<!--[if IE 7]><html class=\"ie7\"><![endif]-->\n<!--[if IE 8]><html class=\"ie8\"><![endif]-->\n<!--[if IE 9]><html class=\"ie9\"><![endif]-->\n<!--[if (gt IE 9)|!(IE)]><!--><html><!--<![endif]-->\n<head>\n<meta charset=\"utf-8\">\n<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">\n<title>${1:Index}</title>\n<meta name=\"keywords\" content=\"\">\n<meta name=\"description\" content=\"\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no\">\n<link rel=\"shortcut icon\" href=\"favicon.ico\" mce_href=\"favicon.ico\" type=\"image/x-icon\">\n</head>\n\n<body>\n\t$2\n</body>\n</html>"),

    ("ie\tFix", "!--[if IE]>$2<![endif]-->"),
    ("ie:6\tFix", "!--[if IE ${1:6}]>$2<![endif]-->"),
    ("ie:not\tFix", "!--[if !IE]> -->$2<!-- <![endif]-->"),
    ("ie:lt\tFix", "!--[if lt IE ${1:9}]>$2<![endif]-->"),
    ("ie:gt\tFix", "!--[if gt IE ${1:8}]>$2<![endif]-->"),
    ("ie:lte\tFix", "!--[if lte IE ${1:8}]>$2<![endif]-->"),
    ("ie:gte\tFix", "!--[if gte IE ${1:8}]>$2<![endif]-->"),


    ("svg\tSVG", "svg version=\"1.1\" \n\txmlns=\"http://www.w3.org/2000/svg\" \n\txmlns:xlink=\"http://www.w3.org/1999/xlink\" \n\txmlns:ev=\"http://www.w3.org/2001/xml-events\" \n\tx=\"${1:0}\" y=\"${2:0}\" width=\"${3:100%}\" height=\"${4:100%}\" viewBox=\"${5:0 0 100 100}\" \n\txml:space=\"preserve\">\n\t$6\n</svg>"),
    ("desc\tSVG", "desc>$1</desc>"),
    ("defs\tSVG", "defs>\n\t$1\n</defs>"),
    ("g\tSVG", "g id=\"$1\">\n\t$2\n</g>"),
    ("line\tSVG", "line x1=\"$1\" y1=\"$2\" x2=\"$3\" y2=\"$4\"></line>"),
    ("rect\tSVG", "rect x=\"$1\" y=\"$2\" width=\"$3\" height=\"$4\"></rect>"),
    ("circle\tSVG", "circle r=\"$1\" cx=\"$2\" cy=\"$3\"></circle>"),
    ("ellipse\tSVG", "ellipse rx=\"$1\" ry=\"$2\" cx=\"$3\" cy=\"$4\"></ellipse>"),
    ("polyline\tSVG", "polyline points=\"$1\"></polyline>"),
    ("polygon\tSVG", "polygon points=\"$1\"></polygon>"),
    ("path\tSVG", "path d=\"$1\"></path>"),
    ("text\tSVG", "text x=\"$1\" y=\"$2\">$3</text>"),
    ("tspan\tSVG", "tspan x=\"$1\" y=\"$2\">$3</tspan>"),
    ("use\tSVG", "use xlink:href=\"#$1\" x=\"$2\" y=\"$3\"></use>"),
    ("clipPath\tSVG", "clipPath id=\"$1\">\n\t$2\n</clipPath>"),
    ("pattern\tSVG", "pattern id=\"$1\" width=\"$2\" height=\"$3\">\n\t$4\n</pattern>"),
    ("symbol\tSVG", "symbol id=\"$1\">\n\t$2\n</symbol>"),
    ("linearGadient\tSVG", "linearGradient id=\"$1\" gradientUnits=\"objectBoundingBox\" x1=\"$2\" y1=\"$3\" x2=\"$4\" y2=\"$5\">\n\t$6\n</linearGradient>"),
    ("radialGradient\tSVG", "radialGradient id=\"$1\" gradientUnits=\"objectBoundingBox\" x1=\"$2\" y1=\"$3\" x2=\"$4\" y2=\"$5\">\n\t$6\n</radialGradient>"),
    ("stop\tSVG", "stop offset=\"$1\" stop-color=\"$2\" stop-opacity=\"${3:1}\"></stop>")
]

# SVG Tag List
svg_tag = [
    'svg',
    'desc',
    'defs',
    'g',
    'line',
    'rect',
    'circle',
    'ellipse',
    'polyline',
    'polygon',
    'path',
    'text',
    'tspan',
    'use',
    'clipPath',
    'pattern',
    'symbol',
    'linearGadient',
    'radialGradient',
    'stop'
]

# Base Attr
base_attr = [
    ("id\tAttr", 'id="$1"'),
    ("class\tAttr", 'class="$1"'),
    ("style\tAttr", 'style="$1"'),
    ("title\tAttr", 'title="$1"'),
    ("accesskey\tAttr", 'accesskey="$1"'),
    ("contenteditable\tAttr", 'contenteditable="$1"'),
    ("contextmenu\tAttr", 'contextmenu="$1"'),
    ("data-*\tAttr", 'data-$1="$2"'),
    ("dir\tAttr", 'dir="$1"'),
    ("draggable\tAttr", 'draggable="$1"'),
    ("dropzone\tAttr", 'dropzone="$1"'),
    ("hidden\tAttr", 'hidden="$1"'),
    ("lang\tAttr", 'lang="$1"'),
    ("spellcheck\tAttr", 'spellcheck="$1"'),
    ("tabindex\tAttr", 'tabindex="$1"'),
    ("translate\tAttr", 'translate="$1"'),

    ("onclick\tAttr", 'onclick="$1"'),
    ("ondblclick\tAttr", 'ondblclick="$1"'),
    ("onmousedown\tAttr", 'onmousedown="$1"'),
    ("onmousemove\tAttr", 'onmousemove="$1"'),
    ("onmouseout\tAttr", 'onmouseout="$1"'),
    ("onmouseover\tAttr", 'onmouseover="$1"'),
    ("onmouseup\tAttr", 'onmouseup="$1"'),
    ("onmousewheel\tAttr", 'onmousewheel="$1"'),
    ("onscroll\tAttr", 'onscroll="$1"'),

    ("ondrag\tAttr", 'ondrag="$1"'),
    ("ondragend\tAttr", 'ondragend="$1"'),
    ("ondragenter\tAttr", 'ondragenter="$1"'),
    ("ondragleave\tAttr", 'ondragleave="$1"'),
    ("ondragover\tAttr", 'ondragover="$1"'),
    ("ondragstart\tAttr", 'ondragstart="$1"'),
    ("ondrop\tAttr", 'ondrop="$1"'),

    ("onblur\tAttr", 'onblur="$1"'),
    ("onfocus\tAttr", 'onfocus="$1"'),
    ("onchange\tAttr", 'onchange="$1"'),
    ("onselect\tAttr", 'onselect="$1"'),
    ("onreset\tAttr", 'onreset="$1"'),
    ("onsubmit\tAttr", 'onsubmit="$1"'),
    ("onformchange\tAttr", 'onformchange="$1"'),
    ("onforminput\tAttr", 'onforminput="$1"'),
    ("oninput\tAttr", 'oninput="$1"'),
    ("oninvalid\tAttr", 'oninvalid="$1"'),

    ("onkeydown\tAttr", 'onkeydown="$1"'),
    ("onkeypress\tAttr", 'onkeypress="$1"'),
    ("onkeyup\tAttr", 'onkeyup="$1"'),

    ("onload\tAttr", 'onload="$1"'),
    ("onunload\tAttr", 'onunload="$1"'),
    ("onresize\tAttr", 'onresize="$1"'),
    ("onerror\tAttr", 'onerror="$1"'),
    ("onafterprint\tAttr", 'onafterprint="$1"'),
    ("onbeforeprint\tAttr", 'onbeforeprint="$1"'),
    ("onbeforeunload\tAttr", 'onbeforeunload="$1"'),
    ("onhaschange\tAttr", 'onhaschange="$1"'),
    ("onmessage\tAttr", 'onmessage="$1"'),
    ("onoffline\tAttr", 'onoffline="$1"'),
    ("ononline\tAttr", 'ononline="$1"'),
    ("onpagehide\tAttr", 'onpagehide="$1"'),
    ("onpageshow\tAttr", 'onpageshow="$1"'),
    ("onpopstate\tAttr", 'onpopstate="$1"'),
    ("onredo\tAttr", 'onredo="$1"'),
    ("onstorage\tAttr", 'onstorage="$1"'),
    ("onundo\tAttr", 'onundo="$1"')
]

# SVG Attr
svg_attr = [
    ("fill\tSVG", 'fill="$1"'),
    ("fill-opacity\tSVG", 'fill-opacity="$1"'),
    ("fill-rule\tSVG", 'fill-rule="$1"'),
    ("stroke\tSVG", 'stroke="$1"'),
    ("stroke-width\tSVG", 'stroke-width="$1"'),
    ("stroke-dasharray\tSVG", 'stroke-dasharray="$1"'),
    ("stroke-dashoffset\tSVG", 'stroke-dashoffset="$1"'),
    ("stroke-linecap\tSVG", 'stroke-linecap="$1"'),
    ("stroke-linejoin\tSVG", 'stroke-linejoin="$1"'),
    ("stroke-miterlimit\tSVG", 'stroke-miterlimit="$1"'),
    ("stroke-opacity\tSVG", 'stroke-opacity="$1"'),
    ("opacity\tSVG", 'opacity="$1"'),
    ("transform\tSVG", 'transform="$1"'),
    ("mask\tSVG", 'mask="$1"'),
    ("clip-path\tSVG", 'clip-path="$1"'),
    ("clip-rule\tSVG", 'clip-rule="$1"'),
    ("filter\tSVG", 'filter="$1"'),
    ("xlink:href\tSVG", 'xlink:href="$1"')
]

# Tag Attr
tag_attr = {
    'a': ['charset', 'coords', 'download', 'href', 'hreflang', 'media', 'name', 'rel', 'rev', 'shape', 'default', 'target', 'type'],
    'area': ['alt', 'coords', 'href', 'nohref', 'shape', 'target'],
    'audio': ['autoplay', 'controls', 'loop', 'muted', 'preload', 'src'],
    'base': ['href', 'target'],
    'bdi': ['dir'],
    'bdo': ['dir'],
    'blockquote': ['cite'],
    'button': ['autofocus', 'disabled', 'form', 'formaction', 'formenctype', 'formmethod', 'formnovalidate', 'formtarget', 'framename', 'name', 'type', 'value'],
    'canvas': ['width', 'height'],
    'col': ['align', 'char', 'charoff', 'span', 'valign', 'width'],
    'colgroup': ['align', 'char', 'charoff', 'span', 'valign', 'width'],
    'command': ['checked', 'disabled', 'icon', 'label', 'radiogroup', 'type'],
    'del': ['cite', 'datetime'],
    'details': ['open'],
    'embed': ['height', 'src', 'type', 'width'],
    'fieldset': ['disabled', 'form', 'name'],
    'form': ['accept', 'accept-charset', 'action', 'autocomplete', 'method', 'name', 'novalidate', 'target'],
    'frame': ['frameborder', 'longdesc', 'marginheight', 'marginwidth', 'name', 'noresize', 'scrolling', 'src'],
    'frameset': ['cols', 'rows'],
    'iframe': ['frameborder', 'height', 'longdesc', 'marginheight', 'marginwidth', 'name', 'sandbox', 'scrolling', 'seamless', 'src', 'srcdoc', 'width'],
    'img': ['alt', 'src', 'width', 'height', 'ismap', 'longdesc', 'usemap'],
    'input': ['type', 'accept', 'alt', 'autocomplete', 'autofocus', 'checked', 'disabled', 'form', 'formaction', 'formenctype', 'formmethod', 'formnovalidate', 'formtarget', 'height', 'list', 'max', 'maxlength', 'min', 'multiple', 'name', 'pattern', 'placeholder', 'readonly', 'required', 'size', 'src', 'step', 'value', 'width'],
    'ins': ['cite', 'datetime'],
    'keygen': ['autofocus', 'challenge', 'disabled', 'form', 'keytype', 'name'],
    'label': ['for', 'form'],
    'link': ['charset', 'href', 'hreflang', 'media', 'rel', 'rev', 'sizes', 'target', 'type'],
    'map': ['name'],
    'meta': ['content', 'http-equiv', 'name', 'scheme'],
    'meter': ['form', 'high', 'low', 'max', 'min', 'optimum', 'value'],
    'object': ['align', 'archive', 'border', 'classid', 'codebase', 'codetype', 'data', 'declare', 'form', 'height', 'hspace', 'name', 'standby', 'type', 'usemap', 'vspace', 'width'],
    'ol': ['compact', 'reversed', 'start', 'type'],
    'optgroup': ['label', 'disabled'],
    'option': ['label', 'value', 'disabled', 'selected'],
    'output': ['for', 'form', 'name'],
    'param': ['name', 'value', 'value', 'valuetype'],
    'pre': ['width'],
    'progress': ['value', 'max'],
    'q': ['cite'],
    'script': ['type', 'async', 'charset', 'defer', 'language', 'src', "xml:space"],
    'section': ['cite'],
    'select': ['autofocus', 'disabled', 'form', 'multiple', 'name', 'required', 'size'],
    'source': ['media', 'src', 'type'],
    'style': ['type', 'media'],
    'table': ['border', 'cellpadding', 'cellspacing', 'frame', 'rules', 'summary', 'width'],
    'tbody': ['align', 'char', 'charoff', 'valign'],
    'td': ['abbr', 'align', 'axis', 'char', 'charoff', 'colspan', 'headers', 'rowspan', 'scope', 'valign'],
    'textarea': ['autofocus', 'cols', 'disabled', 'form', 'maxlength', 'name', 'placeholder', 'readonly', 'required', 'rows', 'wrap'],
    'tfoot': ['align', 'char', 'charoff', 'valign'],
    'th': ['abbr', 'align', 'axis', 'char', 'charoff', 'colspan', 'headers', 'rowspan', 'scope', 'valign'],
    'thead': ['align', 'char', 'charoff', 'valign'],
    'time': ['datetime', 'pubdate'],
    'title': ['dir', 'lang', "xml:lang"],
    'tr': ['align', 'char', 'charoff', 'valign'],
    'track': ['default', 'kind', 'label', 'src', 'srclang'],
    'video': ['autoplay', 'controls', 'height', 'loop', 'muted', 'poster', 'preload', 'src', 'width']
}

# Boolean Attr
boolean_attr = ['defer', 'async', 'autofocus', 'autoplay', 'checked', 'disabled', 'loop', 'muted', 'multiple', 'preload', 'readonly', 'required']

# Attr Value
attr_value = {
    'align': ['left', 'right', 'top', 'middle', 'bottom'],
    'autocomplete': ['on', 'off'],
    'target': ['_blank', '_self', '_parent', '_top'],
    'formtarget': ['_blank', '_self', '_parent', '_top'],
    'method': ['get', 'post'],
    'formmethod': ['get', 'post'],
    'rel': ['alternate', 'author', 'help', 'icon', 'licence', 'next', 'pingback', 'prefetch', 'prev', 'search', 'sidebar', 'stylesheet', 'tag'],
    'media': ['screen', 'tty', 'tv', 'projection', 'handheld', 'print', 'braille', 'aural', 'all'],
    'scrolling': ['yes', 'no', 'auto'],
    'inputType': ['button', 'checkbox', 'file', 'hidden', 'image', 'password', 'radio', 'reset', 'submit', 'text'],
    'buttonType': ['button', 'submit', 'reset'],
    'commandType': ['command', 'checkbox', 'radio'],
    'olType': ["1", 'A', 'a', 'I', 'i'],
    'scriptType': ['text/javascript', 'text/ecmascript', 'application/ecmascript', 'application/javascript', 'text/vbscript'],
    'sourceType': ['video/ogg', "video/mp4", 'video/webm', 'audio/ogg', 'audio/mpeg'],
    'styleType': ['text/css'],

    'fill': ['none'],
    'fill-rule': ['evenodd', 'nonzero'],
    'stroke': ['none'],
    'stroke-linecap': ['butt', 'round', 'square'],
    'stroke-linejoin': ['miter', 'round', 'bevel']
}

# Completions Flag
flag = sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS

# Attr Dictionary
attr_list = {}

# Value Dictionary
value_list = {}


# 获取当前【HTML】标签内容
def filterCode(code):
    pt = len(code) - 1
    while pt > -1:
        ch = code[pt]
        if ch == '<' or ch == '>':
            return code[pt:]

        pt -= 1

    return code

# 【HTML】补全方法
def completions(self, view, prefix, locations):

    # 获取当前代码位置
    pt = locations[0] - len(prefix)

    # 获取当前标签内容
    code = filterCode(view.substr(sublime.Region(0, pt)))
    if not code:
        return tag_list

    st = code[0]

    if st == '<':

        # 获取当前标签名
        m = re.match(re.compile("^<([a-zA-Z]+\d*)\s"), code)
        if m:
            tag = m.group(1)
        else:
            return tag_list

        # 获取当前标签属性名
        m = re.search(re.compile("([a-zA-Z:-]+)=\"[^\"]*$"), code)
        if m:
            attr = m.group(1)

            if attr == 'type':
                attr = tag + 'Type'

            if attr in value_list:
                return value_list[attr]

            if attr in attr_value:
                l = attr_value[attr]
                r = []
                for x in l:
                    r.append((x + "\tValue", x))

                value_list[attr] = r
                return value_list[attr]

            value_list[attr] = None
            return value_list[attr]

        # 返回缓存中的标签属性
        if tag in attr_list:
            return attr_list[tag]

        # 返回【SVG】标签属性
        if tag in svg_tag:
            attr_list[tag] = base_attr + svg_attr
            return attr_list[tag]

        # 返回【HTML】标签属性
        if tag in tag_attr:
            l = tag_attr[tag]
            r = []
            for x in l:
                if x in boolean_attr:
                    r.append((x + "\tAttr", x))
                else:
                    r.append((x + "\tAttr", x + '="$1"'))

            attr_list[tag] = base_attr + r
            return attr_list[tag]

        # 返回默认的标签属性
        attr_list[tag] = base_attr
        return attr_list[tag]

    return []
