import curses
from curses.textpad import rectangle

class key:
	def __init__(self):
		self.up=curses.KEY_UP
		self.down=curses.KEY_DOWN
		self.left=curses.KEY_LEFT
		self.right=curses.KEY_RIGHT
keys=key()

def set_color_pair(n, fore, back):
	eval(f"curses.initpair({n}, curses.COLOR_{fore}, curses.COLOR_{back})")
def get_color_pair(n):
	return curses.color_pair(n)

class object:
	def __init__(self, x, y, texture, params={}):
		self.x=x
		self.y=y
		self.texture=texture
		self.params=params
	def go_to(self, x, y):
		self.x=x
		self.y=y
	def update_params(self, key, value):
		self.params.update({key:value})

class scene:
	def __init__(self, stdscr, objects={}):
		self.scr=curses.initscr()
		curses.noecho()
		curses.cbreak()
		self.scr.keypad(1)
		self.height, self.width=self.scr.getmaxyx()
		self.objects=objects
	def add_object(self, object_name, object):
		self.objects.update({object_name:object})
	def pop_object(self, object_name):
		self.objects.pop(object_name)
	def show(self, object):
		self.o=self.objects[object]
		self.scr.addstr(self.o.y,self.o.x,self.o.texture)
	def get(self):
		return self.scr.getch()
	def refresh(self):
		self.scr.clear()
	def border(self, x1, y1, x2, y2):
		rectangle(self.scr,y1,x1,y2,x2)

def wrapper(func):
	curses.wrapper(func)
