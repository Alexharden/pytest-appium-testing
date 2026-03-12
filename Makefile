# 前方沒有空格
lint:
	poetry run isort .
	poetry run black .
.PHONY: lint	