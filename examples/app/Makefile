# Always random
UUID:=$(shell uuidgen)

build:
	docker build -t registry.local/hello:$(UUID) .
	docker push registry.local/hello:$(UUID)

.PHONY: build
