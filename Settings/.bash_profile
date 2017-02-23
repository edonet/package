
##
# Tell ls to be colourful
# ————————————————————————————————————————————————————
# LSCOLORS中一共11组颜色设置，按照先后顺序，分别对以下的文件类型进行设置文本和背景：
# ————————————————————————————————————————————————————
# 　　directory
# 　　symbolic link
# 　　socket
# 　　pipe
# 　　executable
# 　　block special
# 　　character special
# 　　executable with setuid bit set
# 　　executable with setgid bit set
# 　　directory writable to others, with sticky bit
# 　　directory writable to others, without sticky bit
#
# ————————————————————————————————————————————————————
# LSCOLORS中，字母代表的颜色如下：
# ————————————————————————————————————————————————————
# 　　a 黑色       A 黑色粗体
# 　　b 红色       B 红色粗体
# 　　c 绿色       C 绿色粗体
# 　　d 棕色       D 棕色粗体
# 　　e 蓝色       E 蓝色粗体
# 　　f 洋红色     F 洋红色粗体
# 　　g 青色       G 青色粗体
# 　　h 浅灰色     H 浅灰色粗体
# 　　x 系统默认颜色
#
##
export CLICOLOR=1
export LS_OPTIONS='--color=auto'
export LSCOLORS=gxfxaxdxbxegedabagacdx

##
# Tell grep to highlight matches
##
export GREP_OPTIONS='--color=auto'


##
#
# ————————————————————————————————————————————————————
# 环境变量PS1就是终端的提示文字格式，默认为: \h:\W \u\$
# PS2则是换行后的提示符，默认为: >
# ————————————————————————————————————————————————————
# \d – 现在的系统日期
# \t – 现在的系统时间
# \h – 主机名
# \# – 命令号（Comannd Number）
# \u – 用户名
# \W – 当前所在的路径
# \w – 当前所在的完整路径
#
#
# ————————————————————————————————————————————————————
# 颜色样式设置，格式为：\[\033[<文本属性>;<文本颜色>;<背景颜色>m
# ————————————————————————————————————————————————————
# 文本属性：00（默认值）、01（粗体）、22（非粗体）、04（下划线）、24（非下划线）、05（闪烁）、25（非闪烁）、07（反显）、27（非反显）
# 文本颜色：30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋红）、36（青色）、37（白色）
# 背景颜色：40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋红）、46（青色）、47（白色）
#
##
export TERM="xterm-color"
export PS1='\n\[\033[33m\][\t] \[\033[00m\]\u@\h: \[\033[36m\]\w/ \n\[\033[00m\]\$ '