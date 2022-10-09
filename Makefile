install:
	

reinstall-command: remove-command install-command

clean:
	@rm -r __pycache__; exit 0

run: install-command
	@serverocelot
