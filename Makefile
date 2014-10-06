INSTALL_DIR=/usr/local/lib/sassytray
BIN_DIR=/usr/local/bin
all:
		echo "Use with install or uninstall parameter only"

install: check
		mkdir $(INSTALL_DIR)
			chmod a+x sassytray.py
				cp -ra icons sassytray.py $(INSTALL_DIR)
					ln -s $(INSTALL_DIR)/sassytray.py $(BIN_DIR)/sassytray 

uninstall:
		rm -rf $(INSTALL_DIR) || echo folder not there
			rm $(BIN_DIR)/sassytray || echo file not there

check:
		which acpi

reinstall: uninstall install
