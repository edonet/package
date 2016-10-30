import sublime, sublime_plugin
import re

def filterCode(code):
    pt = len(code) - 1
    while pt > -1:
        ch = code[pt]
        if ch == '<' or ch == '>':
            return code[pt:]

        pt -= 1

    return code


class SVGCompletions(sublime_plugin.EventListener):

    # SVG Tag List
    tagList = [
        ("svg\tTag", "?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\" \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n<svg version=\"1.1\" \n\txmlns=\"http://www.w3.org/2000/svg\" \n\txmlns:xlink=\"http://www.w3.org/1999/xlink\" \n\txmlns:ev=\"http://www.w3.org/2001/xml-events\" \n\tx=\"${1:0}\" y=\"${2:0}\" width=\"${3:100%}\" height=\"${4:100%}\" viewBox=\"${5:0 0 100 100}\" \n\txml:space=\"preserve\">\n\t$6\n</svg>"),
        ("svg:html\tTag", "svg version=\"1.1\" \n\txmlns=\"http://www.w3.org/2000/svg\" \n\txmlns:xlink=\"http://www.w3.org/1999/xlink\" \n\txmlns:ev=\"http://www.w3.org/2001/xml-events\" \n\tx=\"${1:0}\" y=\"${2:0}\" width=\"${3:100%}\" height=\"${4:100%}\" viewBox=\"${5:0 0 100 100}\" \n\txml:space=\"preserve\">\n\t$6\n</svg>"),
        ("title\tTag", 'title>$1</title>'),
        ("desc\tTag", "desc>$1</desc>"),
        ("defs\tTag", "defs>\n\t$1\n</defs>"),
        ("g\tTag", "g id=\"$1\">\n\t$2\n</g>"),
        ("line\tTag", "line x1=\"$1\" y1=\"$2\" x2=\"$3\" y2=\"$4\"></line>"),
        ("rect\tTag", "rect x=\"$1\" y=\"$2\" width=\"$3\" height=\"$4\"></rect>"),
        ("circle\tTag", "circle r=\"$1\" cx=\"$2\" cy=\"$3\"></circle>"),
        ("ellipse\tTag", "ellipse rx=\"$1\" ry=\"$2\" cx=\"$3\" cy=\"$4\"></ellipse>"),
        ("polyline\tTag", "polyline points=\"$1\"></polyline>"),
        ("polygon\tTag", "polygon points=\"$1\"></polygon>"),
        ("path\tTag", "path d=\"$1\"></path>"),
        ("text\tTag", "text x=\"$1\" y=\"$2\">$3</text>"),
        ("textPath\tTag", "textPath xlink:href=\"$1\">$2</textPath>"),
        ("tref\tTag", "tref xlink:href=\"$1\"/>"),
        ("tspan\tTag", "tspan x=\"$1\" y=\"$2\">$3</tspan>"),
        ("use\tTag", "use xlink:href=\"#$1\" x=\"$2\" y=\"$3\"></use>"),
        ("clipPath\tTag", "clipPath id=\"$1\">\n\t$2\n</clipPath>"),
        ("pattern\tTag", "pattern id=\"$1\" width=\"$2\" height=\"$3\">\n\t$4\n</pattern>"),
        ("symbol\tTag", "symbol id=\"$1\">\n\t$2\n</symbol>"),
        ("linearGadient\tTag", "linearGradient id=\"$1\" gradientUnits=\"objectBoundingBox\" x1=\"$2\" y1=\"$3\" x2=\"$4\" y2=\"$5\">\n\t$6\n</linearGradient>"),
        ("radialGradient\tTag", "radialGradient id=\"$1\" gradientUnits=\"objectBoundingBox\" x1=\"$2\" y1=\"$3\" x2=\"$4\" y2=\"$5\">\n\t$6\n</radialGradient>"),
        ("stop\tTag", "stop offset=\"$1\" stop-color=\"$2\" stop-opacity=\"${3:1}\"></stop>"),
        ("font-face\tTag", "font-face>$1</font-face>"),
        
        ("a\tTag", 'a xlink:href="$1" target="${2:_blank}">$3</a>'),
        ("animate\tTag", 'animate attributeName="$1" values="$2" begin="$3" dur="$4" />'),
        ("animateMotion\tTag", 'animateMotion path="$1" begin="$2" dur="$3" />'),
        ("animateTransform\tTag", 'animateTransform attributeName="transform" type="${1:rotate}" values="$2" begin="$3" dur="$4" />'),
        ("animateTransform:rotate\tTag", 'animateTransform attributeName="transform" type="rotate" values="$1" begin="$2" dur="$3" />'),
        ("animateTransform:scale\tTag", 'animateTransform attributeName="transform" type="scale" values="$1" begin="$2" dur="$3" />'),
        ("animateTransform:translate\tTag", 'animateTransform attributeName="transform" type="translate" values="$1" begin="$2" dur="$3" />'),
        ("animateTransform:skewX\tTag", 'animateTransform attributeName="transform" type="skewX" values="$1" begin="$2" dur="$3" />'),
        ("animateTransform:skewY\tTag", 'animateTransform attributeName="transform" type="skewY" values="$1" begin="$2" dur="$3" />'),
        ("marker\tTag", 'marker id="$1" viewBox="$2" refX="$3" refY="$4" markerWidth="$5" markerHeight="$6" orient="${7:auto}">\n\t$8\n</marker>'),
        ("mask\tTag", 'mask id="$1" maskUnits="${2:userSpaceOnUse}">\n\t$3\n</mask>'),
        ("image\tTag", 'image xlink:href="$1" />'),


        ("filter\tFilter", "filter id=\"$1\">\n\t$2\n</filter>"),
        ("feBlend\tFilter", 'feBlend in="${1:SourceGraphic}" in2="${2}" mode="${3:normal}" />'),
        ("feColorMatrix\tFilter", 'feColorMatrix in="${1:SourceGraphic}" type="${2:hueRotate}" values="$3" />'),
        ("feComponentTransfer\tFilter", 'feComponentTransfer in="${1:SourceGraphic}" />'),
        ("feComposite\tFilter", 'feComposite in="${1:SourceGraphic}" in2="$2" />'),
        ("feConvolveMatrix\tFilter", 'feConvolveMatrix in="${1:SourceGraphic}" />'),
        ("feDiffuseLighting\tFilter", 'feDiffuseLighting in="${1:SourceGraphic}" />'),
        ("feDisplacementMap\tFilter", 'feDisplacementMap in="${1:SourceGraphic}" />'),
        ("feFlood\tFilter", 'feFlood in="${1:SourceGraphic}" />'),
        ("feFuncA\tFilter", 'feFuncA in="${1:SourceGraphic}" type="$2" />'),
        ("feFuncB\tFilter", 'feFuncB in="${1:SourceGraphic}" type="$2" />'),
        ("feFuncG\tFilter", 'feFuncG in="${1:SourceGraphic}" type="$2" />'),
        ("feFuncR\tFilter", 'feFuncR in="${1:SourceGraphic}" type="$2" />'),
        ("feGaussianBlur\tFilter", 'feGaussianBlur in="${1:SourceGraphic}" stdDeviation="${2:3}" />'),
        ("feImage\tFilter", 'feImage in="${1:SourceGraphic}" />'),
        ("feMerge\tFilter", 'feMerge in="${1:SourceGraphic}" />'),
        ("feMergeNode\tFilter", 'feMergeNode in="${1:SourceGraphic}" />'),
        ("feMorphology\tFilter", 'feMorphology in="${1:SourceGraphic}" />'),
        ("feOffset\tFilter", 'feOffset in="${1:SourceGraphic}" dx="$2" dy="$3" />'),
        ("feSpecularLighting\tFilter", 'feSpecularLighting in="${1:SourceGraphic}" />'),
        ("feTile\tFilter", 'feTile in="${1:SourceGraphic}" />'),
        ("feTurbulence\tFilter", 'feTurbulence in="${1:SourceGraphic}" type="$2" />')
    ]

    # SVG Base Attr
    baseAttr = [
        ("fill\tAttr", 'fill="$1"'),
        ("fill-opacity\tAttr", 'fill-opacity="$1"'),
        ("fill-rule\tAttr", 'fill-rule="$1"'),
        ("stroke\tAttr", 'stroke="$1"'),
        ("stroke-width\tAttr", 'stroke-width="$1"'),
        ("stroke-dasharray\tAttr", 'stroke-dasharray="$1"'),
        ("stroke-dashoffset\tAttr", 'stroke-dashoffset="$1"'),
        ("stroke-linecap\tAttr", 'stroke-linecap="$1"'),
        ("stroke-linejoin\tAttr", 'stroke-linejoin="$1"'),
        ("stroke-miterlimit\tAttr", 'stroke-miterlimit="$1"'),
        ("stroke-opacity\tAttr", 'stroke-opacity="$1"'),
        ("opacity\tAttr", 'opacity="$1"'),
        ("transform\tAttr", 'transform="$1"'),
        ("mask\tAttr", 'mask="$1"'),
        ("clip-path\tAttr", 'clip-path="$1"'),
        ("clip-rule\tAttr", 'clip-rule="$1"'),
        ("filter\tAttr", 'filter="$1"'),

        ("id\tAttr", 'id="$1"'),
        ("class\tAttr", 'class="$1"'),
        ("style\tAttr", 'style="$1"'),
        ("xml:base\tAttr", 'xml:base="$1"'),
        ("xml:lang\tAttr", 'xml:lang="$1"'),
        ("xml:space\tAttr", 'xml:space="$1"'),
    ]

    # SVG Animate Attr
    animateAttr = ['attributeType', 'attributeName', 'begin', 'dur', 'end', 'min', 'max', 'restart', 'repeatCount', 'repeatDur', 'fill', 'calcMode', 'values', 'keyTimes', 'keySplines', 'from', 'to', 'by', 'autoReverse', 'accelerate', 'decelerate', 'additive', 'accumulate', 'onbegin', 'onend', 'onload', 'onrepeat', 'onactivate', 'onclick', 'onfocusin', 'onfocusout', 'onload', 'onmousedown', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onabort', 'onerror', 'onresize', 'onscroll', 'onunload', 'onzoom']

    # SVG Attr Map
    attrMap = {
        'a': ['xlink:show', 'xlink:actuate', 'xlink:href', 'target'],
        'image': ['x', 'y', 'width', 'height', 'xlink:href', 'preserveAspectRatio'],
        'circle': ['cx', 'cy', 'r'],
        'clip-path': ['clipPathUnits'],
        'ellipse': ['cx', 'cy', 'rx', 'ry'],
        'line': ['x1', 'x2', 'y1', 'y2'],
        'linearGradient': ['gradientUnits', 'gradientTransform', 'x1', 'y1', 'x2', 'y2', 'spreadMethod', 'xlink:href'],
        'marker': ['markerUnits', 'refX', 'refY', 'markerWidth', 'markerHeight', 'orient'],
        'mask': ['maskUnits', 'maskContentUnits', 'x', 'y', 'width', 'height'],
        'path': ['d', 'pathLength'],
        'pattern': ['patternUnits', 'patternContentUnits', 'patternTransform', 'x', 'y', 'width', 'height', 'xlink:href', 'preserveAspectRatio'],
        'polygon': ['points'],
        'polyline': ['points'],
        'radialGradient': ['gradientUnits', 'gradientTransform', 'cx', 'cy', 'r', 'fx', 'fy', 'spreadMethod', 'xlink:href'],
        'rect': ['x', 'y', 'width', 'height', 'rx', 'ry'],
        'stop': ['offset', 'stop-color', 'stop-opacity'],
        'svg': ['version', 'baseProfile', 'x', 'y', 'width', 'height', 'preserveAspectRatio', 'contentScriptType', 'contentStyleType', 'viewBox'],
        'symbol': ['preserveAspectRatio', 'viewBox'],
        'text': ['x', 'y', 'dx', 'dy', 'text-anchor', 'rotate', 'textLength', 'lengthAdjust'],
        'textPath': ['startOffset', 'method', 'spacing', 'xlink:href'],
        'tspan': ['x', 'y', 'dx', 'dy', 'rotate', 'textLength', 'lengthAdjust'],
        'use': ['x', 'y', 'width', 'height', 'xlink:href'],
        'font-face': ['font-family', 'font-style', 'font-variant', 'font-weight', 'font-stretch', 'font-size', 'accent-height', 'ascent', 'underline-position', 'underline-thickness', 'strikethrough-position', 'strikethrough-thickness', 'overline-position', 'overline-thickness'],

        'filter': ['x', 'y', 'width', 'height', 'filterRes', 'filterUnits', 'primitiveUnits', 'xlink:href'],
        'feBlend': ['in', 'in2', 'mode', 'result', 'x', 'y', 'width', 'height'],
        'feColorMatrix': ['in', 'type', 'Values', 'result', 'x', 'y', 'width', 'height'],
        'feComponentTransfer': ['in', 'result', 'x', 'y', 'width', 'height'],
        'feComposite': ['in', 'in2', 'operator', 'k1', 'k2', 'k3', 'k4', 'result', 'x', 'y', 'width', 'height'],
        'feConvolveMatrix': ['in', 'order', 'kernelMatrix', 'divisor', 'bias', 'targetX', 'targetY', 'edgeMode', 'kernelUnitLength', 'preserveAlpha', 'result', 'x', 'y', 'width', 'height'],
        'feDiffuseLighting': ['in', 'surfaceScale', 'diffuseConstant', 'kernelUnitLength', 'result', 'x', 'y', 'width', 'height'],
        'feDisplacementMap': ['in', 'in2', 'scale', 'xChannelSelector', 'yChannelSelector', 'result', 'x', 'y', 'width', 'height'],
        'feFlood': ['flood-color', 'flood-opacity', 'result', 'x', 'y', 'width', 'height'],
        'feFuncA': ['type', 'tableValues', 'slope', 'intercept', 'amplitude', 'exponent', 'offset'],
        'feFuncB': ['type', 'tableValues', 'slope', 'intercept', 'amplitude', 'exponent', 'offset'],
        'feFuncG': ['type', 'tableValues', 'slope', 'intercept', 'amplitude', 'exponent', 'offset'],
        'feFuncR': ['type', 'tableValues', 'slope', 'intercept', 'amplitude', 'exponent', 'offset'],
        'feGaussianBlur': ['in', 'stdDeviation', 'result', 'x', 'y', 'width', 'height'],
        'feImage': ['preserveAspectRatio', 'xlink:href', 'result', 'x', 'y', 'width', 'height'],
        'feMerge': ['result', 'x', 'y', 'width', 'height'],
        'feMergeNode': ['in'],
        'feMorphology': ['in', 'operator', 'radius', 'result', 'x', 'y', 'width', 'height'],
        'feOffset': ['in', 'dx', 'dy', 'result', 'x', 'y', 'width', 'height'],
        'feSpecularLighting': ['in', 'surfaceScale', 'specularConstant', 'specularExponent', 'kernelUnitLength', 'result', 'x', 'y', 'width', 'height'],
        'feTile': ['in', 'result', 'x', 'y', 'width', 'height'],
        'feTurbulence': ['baseFrequency', 'numOctaves', 'seed', 'stitchTiles', 'type', 'result', 'x', 'y', 'width', 'height'],

        'animate': animateAttr,
        'animateTransform': ['type'] + animateAttr,
        'animateMotion': ['path', 'keyPoints', 'rotate', 'origin'] + animateAttr,
    }

    # SVG Value Map
    valueMap = {
        'fill': ['none'],
        'fill-rule': ['evenodd', 'nonzero'],
        'stroke': ['none'],
        'stroke-linecap': ['butt', 'round', 'square'],
        'stroke-linejoin': ['miter', 'round', 'bevel'],
        'transform': ['matrix($1)', 'rotate($1)', 'scale($1)', 'translate($1)', 'skewX($1)', 'skewY($1)'],
        'gradientTransform': ['matrix($1)', 'rotate($1)', 'scale($1)', 'translate($1)', 'skewX($1)', 'skewY($1)'],
        'patternTransform': ['matrix($1)', 'rotate($1)', 'scale($1)', 'translate($1)', 'skewX($1)', 'skewY($1)'],
        'text-anchor': ['start', 'middle', 'end', 'inherit'],
        'target': ['_blank', '_self', '_parent', '_top'],
        'clipPathUnits': ['userSpaceOnUse', 'objectBoundingBox'],
        'preserveAspectRatio': ['none', 'meet', 'slice', 'xMinYMin', 'xMidYMin', 'xMaxYMin', 'xMinYMid', 'xMidYMid', 'xMaxYMid', 'xMinYMax', 'xMidYMax', 'xMaxYMax'],
        'gradientUnits': ['userSpaceOnUse', 'objectBoundingBox'],
        'markerUnits': ['userSpaceOnUse', 'strokeWidth'],
        'maskUnits': ['userSpaceOnUse', 'objectBoundingBox'],
        'maskContentUnits': ['userSpaceOnUse', 'objectBoundingBox'],
        'patternUnits': ['userSpaceOnUse', 'objectBoundingBox'],
        'patternContentUnits': ['userSpaceOnUse', 'objectBoundingBox'],
        'font-style': ['normal', 'italic', 'oblique', 'inherit'],
        'font-variant': ['normal', 'small-caps', 'inherit'],
        'font-weight': ['normal', 'bold', 'bolder', 'lighter', '100', '200', '300', '400', '500', '600', '700', '800', '900', 'inherit'],
        'font-stretch': ['normal', 'wider', 'narrower', 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded', 'inherit'],

        'in': ['SourceGraphic', 'SourceAlpha', 'BackgroundImage', 'BackgroundAlpha', 'FillPaint', 'StrokePaint'],
        'in2': ['SourceGraphic', 'SourceAlpha', 'BackgroundImage', 'BackgroundAlpha', 'FillPaint', 'StrokePaint'],
        'mode': ['normal', 'multiply', 'screen', 'darken', 'lighten'],
        'animateTransformType': ['translate','scale','rotate','skewX','skewY'],
        'feColorMatrixType': ['matrix', 'saturate', 'hueRotate', 'luminanceToAlpha'],
        'feFuncAType': ['identity', 'table', 'discrete', 'linear', 'gamma'],
        'feFuncBType': ['identity', 'table', 'discrete', 'linear', 'gamma'],
        'feFuncGType': ['identity', 'table', 'discrete', 'linear', 'gamma'],
        'feFuncRType': ['identity', 'table', 'discrete', 'linear', 'gamma'],
        'feTurbulenceType': ['fractalNoise', 'turbulence'],

        'attributeType': ['CSS', 'XML', 'auto'],
        'repeatCount': ['indefinite'],
        'repeatDur': ['indefinite'],
        'calcMode': ['discrete', 'linear', 'paced', 'spline'],
        'fill': ['remove', 'freeze']
    }

    # SVG Completions Flag
    flag = sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS

    # Attr Dictionary
    attrList = {}

    # Value Dictionary
    valueList = {}

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "text.svg"):
            return []
        
        pt = locations[0] - len(prefix)
        ch = view.substr(sublime.Region(pt - 1, pt))
        code = filterCode(view.substr(sublime.Region(0, pt)))
        if not code:
            return self.tagList, self.flag
        st = code[0]

        if st == '<':
            m = re.match(re.compile("^<([a-zA-Z]+)\s"), code)
            if m:
                tag = m.group(1)
            else:
                return self.tagList, self.flag

            m = re.search(re.compile("([a-zA-Z:-]+\d*)=\"[^\"]*$"), code)
            if m:
                attr = m.group(1)

                if attr == 'type':
                    attr = tag + 'Type'

                if attr in self.valueList:
                    return self.valueList[attr]

                if attr in self.valueMap:
                    l = self.valueMap[attr]
                    r = []
                    for x in l:
                        r.append((re.compile("\((\$\d+,?\s*)+\)").sub('()', x) + "\tValue", x))

                    self.valueList[attr] = (r, self.flag)
                    return self.valueList[attr]

                self.valueList[attr] = None
                return self.valueList[attr]

            if tag in self.attrList:
                return self.attrList[tag]

            if tag in self.attrMap:
                l = self.attrMap[tag]
                r = []
                for x in l:
                    r.append((x + "\tAttr", x + '="$1"'))

                self.attrList[tag] = (r + self.baseAttr, self.flag)
                return self.attrList[tag]

            self.attrList[tag] = (self.baseAttr, self.flag)
            return self.attrList[tag]


        return [], self.flag