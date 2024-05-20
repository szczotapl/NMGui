.PHONY: install uninstall

install:
	sudo pacman -S python-gobject
	sudo cp -r src/nmgui.py /usr/local/bin/nmgui.py
	sudo cp -r src/nmgui /usr/local/bin/nmgui
	sudo chmod +x /usr/local/bin/nmgui

uninstall:
	sudo rm /usr/local/bin/nmgui.py
	sudo rm /usr/local/bin/nmgui
