#!/bin/bash
docker build -t cc65-compiler-image .
(docker start cc65-compiler|| docker run --name cc65-compiler -ti -v C:/Users/giorgig/code/x16-demo:/x16-demo cc65-compiler-image:latest  bash ) && docker exec -ti cc65-compiler bash
