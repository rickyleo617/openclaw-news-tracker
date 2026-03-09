#!/usr/bin/env python3
"""
OpenClaw News Tracker - 主执行脚本
每天8点执行：爬取新闻 -> 生成网站 -> 部署
"""

import sys
import os
from pathlib import Path

# 添加当前目录到Python路径
sys.path.insert(0, str(Path(__file__).parent))

from news_scraper import OpenClawNewsScraper
from website_generator import WebsiteGenerator

def main():
    """主执行函数"""
    print("🚀 Starting OpenClaw News Tracker...")
    
    # 1. 爬取新闻
    print("📰 Collecting OpenClaw news...")
    scraper = OpenClawNewsScraper(data_dir="data")
    news_data = scraper.run()
    
    # 2. 生成网站
    print("🌐 Generating website...")
    generator = WebsiteGenerator(template_dir="templates", output_dir=".")
    generator.generate_website(news_data)
    
    print("✅ OpenClaw News Tracker completed successfully!")
    print(f"📊 Total news items: {len(news_data)}")
    print("📁 Website saved as index.html")

if __name__ == "__main__":
    main()