#!/usr/bin/env python3
"""
OpenClaw News Website Generator
根据JSON数据生成静态HTML网站
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

class WebsiteGenerator:
    def __init__(self, template_dir="templates", output_dir="."):
        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # 设置Jinja2环境
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            autoescape=True
        )
        
        # 添加日期格式化过滤器
        self.env.filters['format_date'] = self.format_date
        
    def format_date(self, date_string):
        """格式化日期显示"""
        if not date_string:
            return "未知时间"
        try:
            dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
            # 转换为本地时间
            local_dt = dt.astimezone()
            return local_dt.strftime("%Y-%m-%d %H:%M")
        except:
            return date_string
            
    def generate_website(self, news_data, last_updated=None):
        """生成网站HTML"""
        if last_updated is None:
            last_updated = datetime.now(timezone.utc).isoformat()
            
        # 准备模板数据
        template_data = {
            'news_items': news_data,
            'last_updated': self.format_date(last_updated)
        }
        
        # 渲染模板
        template = self.env.get_template('index.html')
        html_content = template.render(**template_data)
        
        # 保存到输出目录
        output_file = self.output_dir / "index.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"Website generated: {output_file}")
        return output_file
        
    def run(self):
        """主执行函数"""
        # 读取新闻数据
        data_file = Path("data/openclaw_news.json")
        if not data_file.exists():
            print("No news data found, creating empty website...")
            news_data = []
        else:
            try:
                with open(data_file, 'r', encoding='utf-8') as f:
                    news_data = json.load(f)
            except Exception as e:
                print(f"Error reading news data: {e}")
                news_data = []
                
        # 生成网站
        self.generate_website(news_data)
        return news_data

if __name__ == "__main__":
    generator = WebsiteGenerator()
    generator.run()