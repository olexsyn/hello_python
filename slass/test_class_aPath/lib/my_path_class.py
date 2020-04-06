from re import search, sub

class aPath:
	"""
	 see os.path.* or Screenshot_20190225_081400.png

	Splits path to file or directory in parts. Works only
	with a string. Doesn't define real object type (file
	or dir) and it existing.
	Return a tuple of parts.

	Example for file "/root/dir1/dir2/file.ext":
		fullpat  = "/root/path/to/file.ext"
		path     = "/root/path/to"
		file     = "file.ext"
		filename = "file"
		fileext  = "ext"

	Example for dir "/root/dir1/dir2/dir3":
		fullpath = "/root/dir1/dir2/dir3"
		path     = "/root/dir1/dir2"
		file     = "dir3"
		filename = "dir3"
		fileext  = ""=

	"""

	def __init__(self, fp):
		# if path ends with a slash - delete it
		self.fp = sub('/$', '', fp)


		# self.path = ''
		# self.file = ''
		# self.filename = ''
		# self.fileext  = ''

		# last of /
		found = search('^(.+)/(.+)$', self.fp)
		if found:
			self.path = found.group(1)
			self.file = found.group(2)
		else:
			self.path = ''
			self.file = fp

		# last of .
		found = search('^(.+)\.(.+)$', self.file)
		if found:
			self.filename = found.group(1)
			self.fileext  = found.group(2)
		else:
			self.filename = self.file
			self.fileext  = ''
	#def


	def prn(self):
		"""
		Just print all properties

		"""
		print('---------------')
		print('fp =',self.fp)  # fullpath
		print('path =',self.path)
		print('file =',self.file)
		print('filename =',self.filename)
		print('fileext =',self.fileext)
	#def


	def __repr__(self):
		return (f'{self.__class__.__name__}('
				f'fp={self.fp!r}, path={self.path!r}, file={self.file!r}, filename={self.filename!r}, fileext={self.fileext!r})')
		# флаг '!r' - в выводимом строковом значении вместо str(self.*) будут использованы repr(self.*)
		# "Чистый Python" стр.110
		# визуальной отличие: с '!r' значения выводятся в кавычках


#class