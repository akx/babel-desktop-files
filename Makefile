# Pythonpath is used so we can import `babel_desktop`

.PHONY: desktop.ini

org.gnome.Polari.desktop: desktop.pot
	python explode_into_desktop.py \
		-i example-data/polari/data/org.gnome.Polari.desktop.in \
		-d example-data/polari/po \
		-k Name -k GenericName -k Comment -k Icon -k Keywords \
		-o org.gnome.Polari.desktop

desktop.pot:
	env PYTHONPATH=$(CURDIR) \
		pybabel extract \
		-k Name -k GenericName -k Comment -k Icon -k Keywords \
		-F setup.cfg \
		-o desktop.pot \
		example-data/polari/data/
