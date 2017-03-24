from socket import *
from StringIO import StringIO
import gtk

w = gtk.gdk.get_default_root_window()
sz = w.get_size()
s = socket()
host =  gethostbyname( gethostname() )
port = 12345
s.bind( (host,port) )
s.listen(5)
while True:
	c , addr = s.accept()
	f = StringIO()
	pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
	pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
	pb.save_to_callback(  f.write , 'jpeg', {"quality":"10"}  )
	f.seek(0)
	l = f.read(1024)
	while l:
		c.send(l)
		l  = f.read(1024)
	f.close()
	c.close()