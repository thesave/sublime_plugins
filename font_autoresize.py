import sublime, sublime_plugin

class WindowListener( sublime_plugin.EventListener ):
	def on_activate( self, view ):
		self.check_Width( view )

	def on_deactivated( self, view ):
		self.check_Width( view )

	def check_Width( self, view ):
		width = view.viewport_extent()[ 0 ]
		s = sublime.load_settings("Preferences.sublime-settings")
		sf=20
		if width < 300:
			sf=10
		elif width < 600:
			sf=13
		elif width < 900:
			sf=16
		s.set( "font_size", sf)
		# sublime.message_dialog( str( width ) )