#!/bin/bash
# 设置本地定时任务脚本

set -e

echo "Setting up local cron job for OpenClaw News Tracker..."

# 获取当前目录的绝对路径
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$SCRIPT_DIR"

# 创建crontab条目
CRON_JOB="0 8 * * * cd $WORKSPACE_DIR && source venv/bin/activate && python enhanced_scraper.py && python website_generator.py >> openclaw-news.log 2>&1"

# 检查是否已存在相同的cron job
if crontab -l 2>/dev/null | grep -F "$CRON_JOB" > /dev/null; then
    echo "Cron job already exists."
else
    # 添加新的cron job
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo "Cron job added successfully!"
fi

echo "Local cron setup complete!"
echo "The script will run daily at 8:00 AM to update OpenClaw news."