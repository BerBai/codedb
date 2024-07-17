#!/bin/bash

# 将脚本放置在项目根路径
SCRIPT_PATH=$(readlink -f "$0")
SCRIPT_DIR=$(dirname "$SCRIPT_PATH")

echo $SCRIPT_DIR

cd $SCRIPT_DIR # 切换到项目路径

# 获取时间日期对象
NOW=$(date '+%Y-%m-%d %H:%M:%S')
MSG="==> $NOW commit <=="

# 将提交信息输出到日志文件gitpush.log
echo $MSG >> gitpush.log
echo $(git status) >> gitpush.log

# 将代码的相关信息输出到日志文件gitpush.log
git add . >> gitpush.log
git commit -m "$MSG" >> gitpush.log
git push origin main >> gitpush.log