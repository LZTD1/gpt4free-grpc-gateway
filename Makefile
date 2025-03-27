.PHONY: gen
gen:
	python -m grpc_tools.protoc -I=./protos \
			--python_out=./pypkg \
			--pyi_out=./pypkg \
			--grpc_python_out=./pypkg \
			./protos/*.proto
	protol \
	  --create-package \
	  --in-place \
	  --python-out ./pypkg \
	  protoc --proto-path=./protos ./protos/*.proto

.PHONY: build
build:
	pyinstaller --onefile --hidden-import=grpc ai.py
	
.PHONY: dev
dev:
	set CONFIG_PATH=config/dev.cfg.yaml && python ai.py