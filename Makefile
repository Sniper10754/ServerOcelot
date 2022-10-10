clean:
	@rm -r __pycache__; exit 0

run: clean 
	@python3 ./main.py