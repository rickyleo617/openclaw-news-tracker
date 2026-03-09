#!/bin/bash
# OpenClaw News Tracker 部署脚本

set -e

echo "🚀 Deploying OpenClaw News Tracker..."

# 创建数据目录
mkdir -p data

# 安装依赖（如果需要）
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate
pip install -r requirements.txt

# 运行主程序
python main.py

echo "✅ Deployment completed!"
echo "🌐 Website is ready at index.html"