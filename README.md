# OpenClaw News Tracker

A mobile-friendly website that automatically collects and displays OpenClaw-related news from around the world.

## Features
- 📱 Mobile-optimized responsive design
- 🌍 Global news collection using Brave Search API
- ⏰ Daily updates at 8:00 AM (automated)
- 🔗 Direct links to original articles
- 📊 Clean, readable interface

## How it works
1. Daily at 8:00 AM, a Python script searches for "OpenClaw" news globally
2. Extracts title, summary, URL, and publication date
3. Generates a static HTML page with all collected news
4. Automatically deploys to GitHub Pages for global access

## Files
- `news_collector.py` - Main news collection script
- `templates/index.html` - Mobile-friendly HTML template
- `data/news.json` - Stored news data
- `.github/workflows/deploy.yml` - GitHub Actions workflow
- `style.css` - Responsive CSS styling