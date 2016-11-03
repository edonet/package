<!-- just a comments: this is a markdown dome -->

A First Level Header
====================

A Second Level Header
---------------------
text.html.markdown
meta.paragraph.markdown
markup.heading.2.markdown
punctuation.definition.heading.markdown

Now is the time for all good men to come to
the aid of their country. This is just a
regular paragraph.

The quick brown fox jumped over the lazy
dog's back.

### Header 3

> ## This is an H2 in a blockquote
>
> This is a blockquote.
>
> This is the second paragraph in the blockquote.
>
> this is new line
>
> this is another new line

<!----------------------------->
text.html.markdown
meta.block-level.markdown
markup.quote.markdown


#### Header 4
Some of these words *are emphasized*.
Some of these words _are emphasized also_.

<!----------------------------->
text.html.markdown
meta.paragraph.markdown
markup.italic.markdown


* Use two asterisks for **strong emphasis**.
* Or, if you prefer, __use two underscores instead__.

<!----------------------------->
text.html.markdown
meta.paragraph.markdown
markup.bold.markdown


*   Candy.
*   Gum.
*   Booze.

<!----------------------------->
text.html.markdown
markup.list.unnumbered.markdown
meta.paragraph.list.markdown


### Unnumbered list
+   Candy.
+   Gum.
+   Booze.

-   Candy.
-   Gum.
-   Booze.


### Numbered list
1.  Red
2.  Green
3.  Blue

--------------------------------------------------
text.html.markdown
markup.list.numbered.markdown
meta.paragraph.list.markdown

1. This is an [example link](http://example.com/).
2. This is an [example link](http://example.com/ "With a Title").

<!----------------------------->
text.html.markdown
meta.paragraph.markdown
meta.link.inline.markdown
string.other.link.title.markdown

<!----------------------------->
text.html.markdown
meta.paragraph.markdown
meta.link.inline.markdown
markup.underline.link.markdown

text.html.markdown markup.list.numbered.markdown meta.paragraph.list.markdown meta.link.inline.markdown string.other.link.description.title.markdown

I get 10 times more traffic from [Google][1] than from
[Yahoo][2] or [MSN][3].

<!----------------------------->
text.html.markdown
meta.paragraph.markdown
meta.link.reference.markdown
string.other.link.title.markdown

<!----------------------------->
text.html.markdown
meta.paragraph.markdown
meta.link.reference.markdown
constant.other.reference.link.markdown

[1]: http://google.com/        "Google"
[2]: http://search.yahoo.com/  "Yahoo Search"
[3]: http://search.msn.com/    "MSN Search"

<!----------------------------->
text.html.markdown
meta.link.reference.def.markdown
constant.other.reference.link.markdown

<!----------------------------->
text.html.markdown
meta.link.reference.def.markdown
markup.underline.link.markdown

<!----------------------------->
text.html.markdown
meta.link.reference.def.markdown
string.other.link.description.title.markdown

[PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
[PlGh]:  <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
[PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
[PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>


I start my morning with a cup of coffee and
[The New York Times][NY Times].

[ny times]: http://www.nytimes.com/

![alt text][id]

![alt text](https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo_top_ca79a146.png "Title")

[id]: https://g2.liuker.xyz/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png "Title"

I strongly recommend against using any `<blink>` tags.

I wish SmartyPants used named entities like `&mdash;`
instead of decimal-encoded entites like `&#8212;`.

---------

==============

***
text.html.markdown
meta.block-level.markdown
meta.separator.markdown

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |



```sh
$ npm install --production
$ npm run predeploy
$ NODE_ENV=production node app
```

```javascript

    // 异步创建文件目录
    function mkdirAsync(dir, callback) {
            stat(dir, err => {
                    if (!err) {
                            return callback(null);
                    }

                    let parent = path.dirname(dir);

                    if (parent === dir) {
                            return callback(new Error('the dir root is not exists!'));
                    }

                    mkdirAsync(parent, err => {
                            if (err) {
                                    return callback(err);
                            }

                            fs.mkdir(dir, callback);
                    });
            });
    }

```

```json
    {
        "name": "ntils",
        "version": "0.0.1",
        "description": "node utils",
        "main": "./src/index.js",
        "scripts": {
            "test": "echo \"Error: no test specified\" && exit 1"
        },
        "repository": {
            "type": "git",
            "url": "git+https://github.com/edonet/ntils.git"
        },
        "keywords": [
            "node",
            "utils"
        ],
        "author": "lifx",
        "license": "MIT",
        "bugs": {
            "url": "https://github.com/edonet/ntils/issues"
        },
        "homepage": "https://github.com/edonet/ntils#readme"
    }
```

```html
    <tr>
        <td class="left">受理人</td>
        <td class="detail">
            <span class="origin" data-type="accept_operator">李芳雄</span>
            <a href="javascript:;" class="edit-a">修改</a>
        </td>
    </tr>
```

```sass
    @charset "utf-8";

    // arrow
    @mixin arrow-r($size: 10px, $color: $borderColor) {
            position: relative;

            &::after {
                    content: "";
                    display: block;
                    width: rem($size);
                    height: rem($size);
                    position: absolute;
                    top: 50%;
                    right: rem(10px);
                    transform: translateY(-50%) rotate(45deg);
                    border-width: rem(1px, 1px, 0, 0);
                    border-style: solid;
                    border-color: $color;
            }
    }

```

```css
    blockquote:before, blockquote:after,
    q:before, q:after {
            content: '';
            content: none;
    }

    table {
            border-collapse: collapse;
            border-spacing: 0;
    }
```
