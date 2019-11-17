#!/usr/bin/env bash

# 镜像名
image_name=$1

# 标签名
tag_name=$2

# 构建时间
build_time=`date %F`

# 构建镜像
docker build -t ${image_name}:${tag_name} .
