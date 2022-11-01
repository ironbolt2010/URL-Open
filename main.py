class URLOpener():
	import webbrowser
	def open(URLS = [] , ARGS = [] , filename = 'URLS.txt'):
		if '-load' in args:
			ARGS.remove('-load')
			with open(f'{filename}' , 'wt')as f:
				for URL in URLS:
					f.write(f'{URL}\n')
				f.close()
		if '-read' in ARGS:
			with open(f'{filename}' , 'rt')as f:
				for URL in f:
					webbrowser.open_new_tab(URL)
				f.close()
				ARGS.remove('-read')
		else:
			for URL in URLS:
				webbrowser.open_new_tab(URL)

