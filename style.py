#!/usr/local/bin/python3.4
# -*- coding: utf-8 -*-

"""
	author : Developed by Marc-Alexandre Blanchard
	date : june 2014
	define methods to apply style within terminal
"""

""" special characters et sequences """
__specials = { 'escape_sequence'   : '\033[',
			'attributes_separator' : ';',
			'ending_character'     : 'm' }

""" formmating attributes """
__format = {'reset'      : '0',
			'bright'     : '1',
			'dim'        : '2',
			'underscore' : '4',
			'blink'      : '5',
			'reverse'    : '7',
			'hidden'     : '8'}

""" foreground colors attributes """
__foreground_colors = {	'black'   : '30',
						'red'     : '31',
						'green'   : '32',
						'yellow'  : '33',
						'blue'    : '34',
						'magenta' : '35',
						'cyan'    : '36',
						'white'   : '37'}

"""	background colors attributes """

__background_colors = {	'black'   : '40',
						'red'     : '41',
						'green'   : '42',
						'yellow'  : '43',
						'blue'    : '44',
						'magenta' : '45',
						'cyan'    : '46',
						'white'   : '47'}

def __surround(attribute):
	""" surround atribute with escape_sequence and ending_character """
	return __specials['escape_sequence']+attribute+__specials['ending_character']

def __end_tag():
	"""	reset all style """
	return __specials['escape_sequence']+__format['reset']+__specials['ending_character']

def __apply_style(attribute,msg):
	""" apply style, corresponding to attribute, to msg """
	return __surround(attribute)+msg+__end_tag()

def black(msg):
	""" return msg with black font"""
	return __apply_style(__foreground_colors['black'],msg)

def blue(msg):
	""" return msg with blue font"""
	return __apply_style(__foreground_colors['blue'],msg)

def cyan(msg):
	""" return msg with cyan font"""
	return __apply_style(__foreground_colors['cyan'],msg)

def green(msg):
	""" return msg with green font"""
	return __apply_style(__foreground_colors['green'],msg)

def magenta(msg):
	""" return msg with magenta font"""
	return __apply_style(__foreground_colors['magenta'],msg)

def red(msg):
	""" return msg with red font"""
	return __apply_style(__foreground_colors['red'],msg)

def yellow(msg):
	""" return msg with yellow font"""
	return __apply_style(__foreground_colors['yellow'],msg)

def white(msg):
	""" return msg with white font"""
	return __apply_style(__foreground_colors['white'],msg)

def multicolor(msg):
	""" return multicolor msg"""
	i,res,colors=0,"",list(__foreground_colors)
	for letter in msg:
		res+=__apply_style(__foreground_colors[colors[i%len(colors)]],letter)
		i=i+1
	return res

def bg_black(msg):
	""" return msg with a black background """
	return __apply_style(__background_colors['black'],msg)

def bg_blue(msg):
	""" return msg with a blue background """
	return __apply_style(__background_colors['blue'],msg)

def bg_cyan(msg):
	""" return msg with a cyan background """
	return __apply_style(__background_colors['cyan'],msg)

def bg_green(msg):
	""" return msg with a green background """
	return __apply_style(__background_colors['green'],msg)

def bg_magenta(msg):
	""" return msg with a magenta background """
	return __apply_style(__background_colors['magenta'],msg)

def bg_red(msg):
	""" return msg with a red background """
	return __apply_style(__background_colors['red'],msg)

def bg_yellow(msg):
	""" return msg with a yellow background """
	return __apply_style(__background_colors['yellow'],msg)

def bg_white(msg):
	""" return msg with a white background """
	return __apply_style(__background_colors['white'],msg)

def blink(msg):
	""" return blinking msg """
	return __apply_style(__format['blink'],msg)

def bright(msg):
	""" return bright msg """
	return __apply_style(__format['bright'],msg)

def dim(msg):
	""" return dimmed msg """
	return __apply_style(__format['dim'],msg)

def hidden(msg):
	""" return hidden msg """
	return __apply_style(__format['hidden'],msg)

def underscore(msg):
	""" return underlined msg """
	return __apply_style(__format['underscore'],msg)

def reverse(msg):
	""" return swap bg and fg color then apply to msg """
	return __apply_style(__format['reverse'],msg)

def set_fg_color(color,msg):
	""" apply color to msg color must be a string in : 
	black,blue,cyan,green,magenta,red,yellow,white """
	if(color in __foreground_colors.keys()):
		return __apply_style(__foreground_colors[color],msg)
	return msg

def set_bg_color(color,msg):
	""" set background color to msg color must be a string in : 
	black,blue,cyan,green,magenta,red,yellow,white """
	if(color in __background_colors.keys()):
		return __apply_style(__background_colors[color],msg)
	return msg

def set_bg_fg_color(bgcolor,fgcolor,msg):
	""" set background,foreground color and format msg 
	colors must be a string in : black,blue,cyan,green,magenta,red,yellow,white 
	format must be a string in : blink,bright,dim,hidden,reverse,underscore"""
	if(bgcolor in __background_colors.keys() and fgcolor in __foreground_colors.keys()):
		return __apply_style(__foreground_colors[fgcolor],__apply_style(__background_colors[bgcolor],msg))
	return msg	

def set_fg_style_color(color,format,msg):
	""" set foreground color and format msg 
	color must be a string in : black,blue,cyan,green,magenta,red,yellow,white
	format must be a string in : blink,bright,dim,hidden,reverse,underscore"""
	if(color in __foreground_colors.keys() and format in __format.keys()):
		return __apply_style(__format[format],__apply_style(__foreground_colors[color],msg))
	return msg

def set_bg_style_color(color,format,msg):
	""" set background color and format msg 
	color must be a string in : black,blue,cyan,green,magenta,red,yellow,white
	format must be a string in : blink,bright,dim,hidden,reverse,underscore"""
	if(color in __background_colors.keys() and format in __format.keys()):
		return __apply_style(__format[format],__apply_style(__background_colors[color],msg))
	return msg

def set_style(bgcolor,fgcolor,format,msg):
	""" set background and foreground color to msg colors must be a string in : 
	black,blue,cyan,green,magenta,red,yellow,white 
	"""
	if(bgcolor in __background_colors.keys() and fgcolor in __foreground_colors.keys() and format in __format.keys()):
		return __apply_style(__foreground_colors[fgcolor],__apply_style(__background_colors[bgcolor],__apply_style(__format[format],msg)))
	return msg	

def test():
	print(black("test 1 : black"))
	print(blue("test 2 : blue"))
	print(cyan("test 3 : cyan"))
	print(green("test 4 : green"))
	print(magenta("test 5 : magenta"))
	print(red("test 6 : red"))
	print(yellow("test 7 : yellow"))
	print(white("test 8 : white"))
	print(bg_black("test 9 : bg_black"))
	print(bg_blue("test 10 : bg_blue"))
	print(bg_cyan("test 11 : bg_cyan"))
	print(bg_green("test 12 : bg_green"))
	print(bg_magenta("test 13 : bg_magenta"))
	print(bg_red("test 14 : bg_red"))
	print(bg_yellow("test 15 : bg_yellow"))
	print(bg_white("test 16 : bg_white"))
	print(blink("test 17 : blink"))
	print(bright("test 18 : bright"))
	print(dim("test 19 : dim"))
	print(hidden("test 20 : hidden"))
	print(underscore("test 21 : underscore"))
	print(reverse("test 22 : reverse"))
	print(set_fg_color("blue","test 23 : set_fg : existing color blue"))
	print(set_fg_color("marron","test 24 : set_fg : non existing color marron"))
	print(set_bg_color("green","test 25 : set_bg : existing background color green"))
	print(set_bg_color("violet","test 26 : set_fg : non existing background color violet"))
	print(set_bg_fg_color("yellow","black","test 27 : set_bg_fg : yellow bg, black fg"))
	print(set_bg_fg_color("violet","pink","test 28 : set_bg_fg : violet bg, pink fg : should fail"))
	print(set_style("blue","red","blink","test 29 : set_style : blue bg, red fg, blink"))
	print(set_fg_style_color("blue","blink","test 30 : set_fg_style_color : blue fg, blink"))
	print(set_fg_style_color("violet","blink","test 21 : set_fg_style_color : violet bg, blink : should fail"))
	print(set_bg_style_color("blue","blink","test 32 : set_bg_style_color : blue bg, blink"))
	print(set_bg_style_color("violet","blink","test 33 : set_bg_style_color : violet bg, blink : should fail"))
	print(set_style("marroon","violet","transluscent","test 34 : set_style : marron bg, violet fg, transluscent style : should fail"))
	print(multicolor("test 25 : bonus multicolor"))

if __name__ == '__main__':
	test()