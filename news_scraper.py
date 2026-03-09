#!/usr/bin/env python3
"""
OpenClaw News Tracker - 爬取全球OpenClaw相关报道
每天8点自动执行，收集最新报道并更新网站
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import feedparser
from dateutil import parser as date_parser

class OpenClawNewsScraper:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.news_file = self.data_dir / "openclaw_news.json"
        
    def search_openclaw_news(self):
        """使用多种方式搜索OpenClaw相关新闻"""
        all_news = []
        
        # 1. 使用Brave Search API（通过web_search工具）
        # 这里先模拟API调用，实际会通过OpenClaw的web_search工具
        news_items = self._search_via_brave()
        all_news.extend(news_items)
        
        # 2. 检查技术博客RSS源
        rss_sources = [
            "https://feeds.feedburner.com/TechCrunch/",
            "https://www.theverge.com/rss/index.xml",
            "https://hnrss.org/newest?q=openclaw",
        ]
        for rss_url in rss_sources:
            try:
                rss_news = self._parse_rss_feed(rss_url)
                all_news.extend(rss_news)
            except Exception as e:
                print(f"Failed to parse RSS {rss_url}: {e}")
                
        # 3. 去重和排序
        unique_news = self._deduplicate_news(all_news)
        sorted_news = sorted(unique_news, key=lambda x: x.get('published_at', ''), reverse=True)
        
        return sorted_news[:50]  # 保留最新的50条
        
    def _search_via_brave(self):
        """模拟Brave搜索结果 - 实际会通过OpenClaw工具调用"""
        # 这个方法会在实际执行时被替换为真正的web_search调用
        return []
        
    def _parse_rss_feed(self, feed_url):
        """解析RSS feed"""
        feed = feedparser.parse(feed_url)
        news_items = []
        
        for entry in feed.entries[:10]:  # 每个feed最多取10条
            if 'openclaw' in (entry.title + entry.get('summary', '')).lower():
                item = {
                    'title': entry.title,
                    'summary': entry.get('summary', '')[:300] + '...' if len(entry.get('summary', '')) > 300 else entry.get('summary', ''),
                    'url': entry.link,
                    'source': feed.feed.get('title', 'Unknown RSS'),
                    'published_at': self._parse_date(entry.get('published', entry.get('updated', '')))
                }
                news_items.append(item)
                
        return news_items
        
    def _parse_date(self, date_str):
        """解析日期字符串"""
        if not date_str:
            return datetime.now(timezone.utc).isoformat()
        try:
            parsed_date = date_parser.parse(date_str)
            return parsed_date.isoformat()
        except:
            return datetime.now(timezone.utc).isoformat()
            
    def _deduplicate_news(self, news_list):
        """基于URL去重"""
        seen_urls = set()
        unique_news = []
        
        for item in news_list:
            url = item.get('url', '')
            if url and url not in seen_urls:
                seen_urls.add(url)
                unique_news.append(item)
                
        return unique_news
        
    def save_news(self, news_data):
        """保存新闻数据到JSON文件"""
        # 读取现有数据
        existing_data = []
        if self.news_file.exists():
            try:
                with open(self.news_file, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            except:
                existing_data = []
                
        # 合并新旧数据并去重
        all_data = news_data + existing_data
        unique_data = self._deduplicate_news(all_data)
        
        # 保存到文件
        with open(self.news_file, 'w', encoding='utf-8') as f:
            json.dump(unique_data, f, ensure_ascii=False, indent=2)
            
        print(f"Saved {len(unique_data)} news items to {self.news_file}")
        return unique_data
        
    def run(self):
        """主执行函数"""
        print("Starting OpenClaw news collection...")
        news_data = self.search_openclaw_news()
        saved_data = self.save_news(news_data)
        print(f"Collection completed. Total items: {len(saved_data)}")
        return saved_data

if __name__ == "__main__":
    scraper = OpenClawNewsScraper()
    scraper.run()