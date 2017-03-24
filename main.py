from kivy.app import App
from kivy.uix.screenmanager import ScreenManager , Screen , FadeTransition
from kivy.uix.label import Label
from kivy.uix.image import Image
from io import BytesIO
from kivy.core.image.img_pygame import ImageLoaderPygame
from kivy.clock import Clock
from socket import socket

class SwiftScreenManager( ScreenManager ):
	pass

class HomeScreen( Screen ):
	pass

class Display( Image ):
	def connect(self):
		self.host = "192.168.43.147"
		self.port = 12345
		Clock.schedule_interval( self.refresh_display , 0.03 )
		self.refresh_display()
		
	def refresh_display( self , *args):
		s = socket()
		s.connect( ( self.host , self.port ) )
		f = BytesIO()
		l = s.recv(1024)
		while l:
			f.write(l)
			l = s.recv(1024)
		s.close()
		f.seek(0)
		img = ImageLoaderPygame(f , nocache = True )
		self.texture = img.texture
		self.size = self.texture_size 
		f.close()

class ClientScreen1( Screen ):
	def __init__( self , *args  , **kwargs ):
		super( ClientScreen1 , self ).__init__( *args , **kwargs )
		self.disp = Display( nocache = True , size_hint = (None , None) )
		self.add_widget( self.disp )

class swiftApp( App ):
	def on_pause( self ):
		return True
	def build( self ):
		ssm = SwiftScreenManager( transition = FadeTransition() )
		ssm.add_widget( HomeScreen() )
		global clientscr1
		clientscr1 = ClientScreen1()
		ssm.add_widget( clientscr1 )
		return ssm
		

if __name__ == '__main__':
    swiftApp().run()