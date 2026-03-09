# OpenClaw News Tracker 部署指南

## 项目概述
这是一个自动化的OpenClaw新闻追踪网站，每天早上8点在全球范围内收集有关OpenClaw的最新报道，并生成移动友好的网站。

## 功能特性
- 📱 **移动端优化**: 响应式设计，完美适配手机浏览
- 🌍 **全球新闻收集**: 自动搜索全球网络上的OpenClaw相关报道
- ⏰ **自动更新**: 每天早上8点自动更新内容
- 🚀 **一键部署**: 支持GitHub Pages免费托管
- 🔒 **安全可靠**: 使用虚拟环境和依赖管理

## 部署选项

### 选项1: GitHub Pages (推荐 - 免费托管)
1. **Fork此仓库**到你的GitHub账户
2. **启用GitHub Pages**:
   - 进入仓库 Settings → Pages
   - Source选择 "GitHub Actions"
3. **配置定时任务**:
   - 工作流文件 `.github/workflows/deploy.yml` 已配置为每天UTC 0:00 (北京时间8:00) 自动运行
4. **访问网站**: `https://your-username.github.io/openclaw-news-tracker/`

### 选项2: 本地部署 (适合开发测试)
1. **克隆仓库**:
   ```bash
   git clone https://github.com/your-username/openclaw-news-tracker.git
   cd openclaw-news-tracker
   ```

2. **设置虚拟环境**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或 venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

3. **手动运行**:
   ```bash
   python main.py
   ```
   这将生成 `index.html` 文件，可以直接在浏览器中打开。

4. **设置本地定时任务**:
   ```bash
   ./setup_local_cron.sh
   ```
   这将在你的系统crontab中添加每天8点的定时任务。

## 目录结构
```
openclaw-news-tracker/
├── README.md              # 项目介绍
├── requirements.txt       # Python依赖
├── main.py               # 主执行脚本
├── news_scraper.py       # 新闻爬取模块
├── enhanced_scraper.py   # 增强版爬取模块 (使用OpenClaw工具)
├── website_generator.py  # 网站生成模块
├── deploy.sh            # 部署脚本
├── setup_local_cron.sh  # 本地定时任务设置
├── data/                # 新闻数据存储目录
├── templates/           # HTML模板目录
│   └── index.html       # 网站模板
└── .github/workflows/   # GitHub Actions工作流
    └── deploy.yml       # 自动部署配置
```

## 自定义配置
- **修改搜索关键词**: 编辑 `enhanced_scraper.py` 中的搜索查询
- **调整更新频率**: 修改 `.github/workflows/deploy.yml` 中的cron表达式
- **自定义样式**: 修改 `templates/index.html` 中的CSS样式

## 故障排除
- **依赖安装失败**: 确保使用Python 3.7+
- **新闻抓取失败**: 检查网络连接，某些地区可能需要代理
- **网站显示异常**: 清除浏览器缓存或检查HTML语法

## 技术栈
- **后端**: Python 3.7+
- **前端**: HTML5 + CSS3 + JavaScript
- **模板引擎**: Jinja2
- **部署**: GitHub Pages + GitHub Actions
- **定时任务**: cron (Linux/Mac) 或 Task Scheduler (Windows)

## 许可证
MIT License - 免费使用和修改

---
**注意**: 此项目使用OpenClaw的web_search工具进行新闻搜索，确保你已正确配置Brave API密钥以获得最佳效果。