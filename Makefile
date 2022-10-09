install-command:
	@pip install .

remove-command:
	@pip uninstall -y serverocelot; exit 0

reinstall-command: remove-command install-command

clean:
	@rm -r __pycache__; exit 0

run: install-command
	@serverocelot
