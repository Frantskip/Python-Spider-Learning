# Python-Spider-Learning

> 🕷️ A comprehensive, progressive learning repository for Python web scraping — from zero to advanced techniques.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Python 爬虫系统学习仓库** — 从基础 HTTP 请求到 Scrapy 框架、Selenium 自动化、JS 逆向工程，涵盖 10 大模块、420+ 文件、真实网站实战。

---

## 📖 Table of Contents / 目录

- [Project Overview / 项目概述](#-project-overview--项目概述)
- [Learning Roadmap / 学习路线](#-learning-roadmap--学习路线)
- [Module Details / 模块详解](#-module-details--模块详解)
  - [01 — urllib 基础](#01--urllib-基础)
  - [02 — XPath & JsonPath 解析](#02--xpath--jsonpath-解析)
  - [03 — BeautifulSoup 解析](#03--beautifulsoup-解析)
  - [04 — Selenium 浏览器自动化](#04--selenium-浏览器自动化)
  - [05 — PhantomJS 无头浏览器](#05--phantomjs-无头浏览器)
  - [06 — Chrome Headless 模式](#06--chrome-headless-模式)
  - [07 — requests 库进阶](#07--requests-库进阶)
  - [08 — Scrapy 框架实战](#08--scrapy-框架实战)
  - [09 — requests 库综合案例](#09--requests-库综合案例)
  - [10 — JS 逆向工程](#10--js-逆向工程)
- [Additional Content / 附加内容](#-additional-content--附加内容)
  - [多线程 / Multithreading](#多线程--multithreading)
  - [大学英语 / Utility Scripts](#大学英语--utility-scripts)
  - [Standalone Scripts / 独立脚本](#standalone-scripts--独立脚本)
- [Tech Stack / 技术栈](#-tech-stack--技术栈)
- [Target Websites / 实战目标网站](#-target-websites--实战目标网站)
- [Project Structure / 项目结构](#-project-structure--项目结构)
- [Getting Started / 快速开始](#-getting-started--快速开始)
- [Key Techniques Summary / 核心技术总结](#-key-techniques-summary--核心技术总结)
- [Notes & Caveats / 注意事项](#-notes--caveats--注意事项)
- [License / 许可证](#-license--许可证)

---

## 🎯 Project Overview / 项目概述

This repository documents a **complete, progressive learning journey** through the Python web scraping ecosystem. Starting from the standard library's `urllib`, it systematically covers every major scraping library and framework, culminating in Scrapy projects, browser automation with Selenium, and a primer on JavaScript reverse engineering.

**本仓库记录了一个完整、渐进式的 Python 爬虫学习历程。** 从标准库 `urllib` 起步，系统性地覆盖了每一个主流的爬虫库和框架，最终深入到 Scrapy 项目实战、Selenium 浏览器自动化以及 JS 逆向工程入门。

### Learning Philosophy / 学习理念

| Phase / 阶段 | Focus / 重点 | Modules / 模块 |
|:---:|---|---|
| **Foundation**<br>基础夯实 | HTTP protocol, request/response, URL encoding, headers | 01, 07, 09 |
| **Parsing**<br>数据解析 | XPath, CSS selectors, JSON extraction | 02, 03 |
| **Automation**<br>浏览器自动化 | Selenium WebDriver, headless browsers | 04, 05, 06 |
| **Framework**<br>框架实战 | Scrapy architecture, pipelines, middleware | 08 |
| **Advanced**<br>进阶技术 | JS reverse engineering, multithreading | 10, 多线程 |

---

## 🗺️ Learning Roadmap / 学习路线

```
01_urllib ────► 02_xpath ────► 03_bs4 ────► 04_selenium
     │                                          │
     ▼                                          ▼
05_phantomjs ◄──────────────────────── 06_chrome_headless
     │
     ▼
07_requests ────► 08_scrapy ────► 09_requests_advanced
                                             │
                                             ▼
                                    10_js_reverse_eng
```

---

## 📚 Module Details / 模块详解

### 01 — urllib 基础

> **Python 标准库入门：零依赖的 HTTP 请求**

| File / 文件 | Technique / 技术点 | Target / 目标 |
|---|---|---|
| `study.py` | `urlopen()` 基本使用 | 百度首页 |
| `爬虫_设置headers.py` | 自定义请求头，User-Agent 伪装 | 百度 |
| `get请求的quote方法.py` | `urllib.parse.quote()` 单参数 URL 编码 | 百度搜索 "周杰伦" |
| `get方式encode方法.py` | `urllib.parse.urlencode()` 多参数拼接 | 百度搜索 |
| `post请求百度翻译.py` | POST 请求 + `json.loads()` 解析 JSON 响应 | 百度翻译 API |
| `豆瓣电影.py` | JSON API 单页抓取 + 文件写入 | 豆瓣电影 Top 榜单 |
| `豆瓣电影前十页数据.py` | **分页爬取**：函数式分解 (`create_request` → `get_content` → `down_load`) | 豆瓣电影 |
| `肯德基餐厅地点.py` | POST 分页：城市→餐厅位置数据 | 肯德基官网 API |
| `爬虫异常urlerror,httperror.py` | `try/except` 异常处理 | CSDN (故意错误 URL) |
| `微博的cookie登录.py` | **Cookie 认证**：携带 Cookie 访问需登录页面 | 微博个人主页 |
| `Handler处理器.py` | `HTTPHandler` + `build_opener()` 处理器模式 | 百度 |
| `代理ip.py` | `ProxyHandler` 代理 IP 配置 | 百度 (通过代理) |

**Key Takeaway / 核心收获**: 在无任何第三方依赖的情况下，使用 Python 标准库完成 HTTP 请求的完整生命周期 — GET/POST、参数编码、请求头定制、Cookie 管理、代理配置、异常处理与分页抓取。

---

### 02 — XPath & JsonPath 解析

> **结构化数据提取：从 HTML 和 JSON 中精准定位**

| File / 文件 | Technique / 技术点 | Key API |
|---|---|---|
| `1xpath.py` | XPath 语法全解：属性选择、`contains()`、`starts-with()`、AND 逻辑、管道 `\|` 联合 | `etree.parse()` |
| `2解析百度网站的百度一下.py` | **实时网页 XPath 解析**：对比 `etree.parse()` vs `etree.HTML()` | `etree.HTML()` |
| `03_站长素材.py` | **多页图片爬虫**：懒加载图片 (`@data-original`)、`urlretrieve()` 批量下载（85+ 张图片） | XPath + `urlretrieve` |
| `04_jsonpath基本语法.py` | JsonPath 语法：递归搜索 `$..`、索引 `[2]`、切片 `[1:2]`、过滤器 `[?(@.price<10)]` | `jsonpath` 库 |
| `05_解析淘票票.py` | JSONP 接口抓取 + 完整浏览器请求头模拟 (Cookie, Referer, Sec-* 系列) | `urllib.request` |

**Key Takeaway / 核心收获**: XPath 是结构化提取 HTML 数据的利器 — 掌握属性定位、函数过滤、条件组合三大模式即可应对大多数网页；JsonPath 则是对 JSON 数据的等价解决方案，尤其适合 API 响应解析。

---

### 03 — BeautifulSoup 解析

> **HTML 解析的另一利器：Pythonic 的 DOM 操作**

| File / 文件 | Technique / 技术点 |
|---|---|
| `01_bs4的基本使用.py` | BS4 API 全览：`soup.a`（属性访问）、`find()`、`find_all()`、`select()`（CSS 选择器）、`class_` 过滤、`limit` 限制 |
| `02_京东首页.py` | `urllib` + BS4 工作流：获取京东首页 HTML（为后续解析做准备） |

**Key Takeaway / 核心收获**: BeautifulSoup 提供了比 XPath 更 Pythonic 的 API — `find()` / `find_all()` 配合 CSS 选择器，适合快速原型开发和对复杂嵌套结构的手工探索。

---

### 04 — Selenium 浏览器自动化

> **12 课渐进式教程：从打开浏览器到多标签页实战**

| # | File / 文件 | Technique / 技术点 |
|:---:|---|---|
| 01 | `01_基本使用.py` | Chrome WebDriver 启动、Service 配置、`get()` / `quit()` |
| 02 | `02_元素定位.py` | 四大定位策略：`By.ID`、`By.NAME`、`By.XPATH`、`By.CSS_SELECTOR` |
| 03 | `03_元素信息以及交互.py` | 元素属性读取：`get_attribute()`、`tag_name`、`.text` |
| 04 | `04_交互.py` | **完整交互链**：`send_keys()` → `click()` → `execute_script()`（JS 滚动）→ `back()` / `forward()` |
| 05 | `05-最大化和最小化.py` | 窗口管理 + `detach` 选项（浏览器保持打开） |
| 06 | `06-位置,尺寸.py` | `set_window_position()` / `set_window_size()` 精准控制 |
| 07 | `07-浏览器截图刷新页面.py` | `get_screenshot_as_file()` / `refresh()` |
| 08 | `08-元素定位.py` | `By.LINK_TEXT` 定位 + Bilibili 实战 |
| 09 | `09-元素交互.py` | 长页面截图：`set_window_size(2000, 10000)` → 全页捕获 |
| 10 | `10-实例.py` | 豆瓣电影实战：`implicitly_wait()` 隐式等待 + 复杂 XPath 定位 |
| 11 | `11-获取句柄，切换标签页.py` | **多标签页管理**：`window_handles` + `switch_to.window()` + 跨标签页操作 |
| 12 | `12-查看信息工程学院导师介绍.py` | **综合实战**：百度搜索 → 点击结果 → 切换标签 → 多层导航 → `try/except` 异常处理 |

**Key Takeaway / 核心收获**: Selenium 是应对 JavaScript 动态渲染页面的终极武器。本模块覆盖了元素定位、用户交互模拟、窗口/标签页管理、截图等完整技能链，并以大学官网信息查询为综合案例串联全部知识点。

---

### 05 — PhantomJS 无头浏览器

> ⚠️ **已废弃技术** — PhantomJS 已于 Selenium 4.x 中移除，现代爬虫推荐使用 Chrome Headless（见模块 06）。

| File / 文件 | Status / 状态 |
|---|---|
| `01_基本使用.py` | 仅完成 `webdriver.PhantomJS(path)` 初始化，未实现导航和数据提取 |

**Historical Note / 历史记录**: PhantomJS 是最早的无头浏览器方案之一，基于 WebKit 内核。该模块作为技术发展史的见证保留在此。

---

### 06 — Chrome Headless 模式

> **现代无头浏览器方案：Chrome 后台运行**

| File / 文件 | Technique / 技术点 |
|---|---|
| `01_.py` | `--headless` + `--disable-gpu` 参数配置、`binary_location` 自定义 Chrome 路径、`save_screenshot()` 截图保存 |

**Key Takeaway / 核心收获**: Chrome Headless 是 PhantomJS 的现代替代方案，无需 GUI 即可完成页面渲染、截图和 JS 执行，是服务端爬虫和自动化测试的首选。

---

### 07 — requests 库进阶

> **第三方 HTTP 库：简洁、强大、人性化**

| File / 文件 | Technique / 技术点 | Target / 目标 |
|---|---|---|
| `01-基本使用.py` | `requests.get()` + 响应属性 (`.text`, `.url`, `.status_code`, `.headers`) | 百度 |
| `02-get请求.py` | GET + `params=` 查询参数 + `User-Agent` | 百度搜索 "北京" |
| `03-post请求.py` | POST + `data=` + `json.loads()` JSON 解析 | 百度翻译 API |
| `04-代理ip.py` | 完整浏览器请求头模拟 (Accept, Cookie, Sec-*, Upgrade-Insecure-Requests) | 百度搜索 "ip" |
| `05-cookie登录（古诗文网）.py` | **⭐ 重点：Session + 验证码处理完整流程** | 古诗文网 |
| | ① `requests.Session()` 保持会话 | |
| | ② BeautifulSoup 提取 ASP.NET `__VIEWSTATE` / `__VIEWSTATEGENERATOR` 隐藏 token | |
| | ③ 下载图形验证码 → `input()` 人工输入 → POST 登录 | |
| `06-汽车之家.py` | `urllib` + `lxml.etree` + XPath 提取汽车品牌/型号 (@title 属性) | 汽车之家 |

**Key Takeaway / 核心收获**: `requests` 库是 Python 爬虫的事实标准 — 它的 Session 机制让 Cookie 管理透明化，配合 BeautifulSoup/lxml 可覆盖 80% 以上的爬虫场景。文件 05 的古诗文网登录案例是本仓库中最完整的反爬对抗示例。

---

### 08 — Scrapy 框架实战

> **企业级爬虫框架：4 个完整项目**

```
08_爬虫scrapy/
├── scrapy_01_58tc/          # 58同城 — 招聘信息
├── scrapy_02_carhome/       # 汽车之家 — 车型数据
├── scrapy_03_dangdangwang/  # 当当网 — 图书数据 ✅ (完整实现)
└── scrapy_04_dytt/          # 电影天堂 — 电影资源
```

#### scrapy_03_dangdangwang — 当当网图书爬虫 (唯一完整实现)

| Component / 组件 | Implementation / 实现 |
|---|---|
| **Spider** (`dang.py`) | 抓取 "两性关系/情感" 类图书：封面图片 (懒加载 `@data-original`)、书名 (`@alt`)、价格 |
| **Items** | 定义 3 个字段：`src`, `name`, `price` |
| **Pipeline** | 自定义管道 `Scrapy03DangdangwangPipeline`：`open_spider` → `process_item` → `close_spider`，输出至 `book.json`（60 条记录） |
| **Settings** | `ROBOTSTXT_OBEY = True`, `ITEM_PIPELINES` 已激活 |

#### 其他项目状态

| Project / 项目 | Spider | Status / 状态 |
|---|---|---|
| `scrapy_01_58tc` | `tc` — 荆州 58同城 "前端开发" 职位 | ⚠️ 仅骨架，`parse()` 未完成 |
| `scrapy_02_carhome` | `carhome` — 汽车之家品牌页车型提取 | ⚠️ 部分实现，存在 `extract()` API 错误 |
| `scrapy_04_dytt` | `movie` — 电影天堂列表页→详情页二级爬取 | ⚠️ 二级解析未产出 Item |

**Key Takeaway / 核心收获**: Scrapy 是企业级爬虫的首选框架 — 它提供了 Spider、Item、Pipeline、Middleware 四大核心抽象。本模块包含 4 个真实项目骨架，其中当当网项目完整实现了 "爬取 → 解析 → 管道 → 存储" 的全链路。

---

### 09 — requests 库综合案例

> **requests 实战：从搜索引擎到图片批量下载**

| File / 文件 | Technique / 技术点 | Target / 目标 |
|---|---|---|
| `01-基本使用(获取网页源码).py` | `requests.get()` + `params=` + `input()` 动态搜索词 | 搜狗搜索 |
| `02-制作一个在线翻译.py` | POST + JSON API 解析 + `requests` vs `urllib` 双版本对比 | 百度翻译 |
| `03-爬取豆瓣电影海报.py` | **⭐ 分页 + BeautifulSoup + 批量下载 + 进度条** | 豆瓣电影 Top 250 |
| | ① `range(start_page, end_page+1)` 分页循环 | |
| | ② `BeautifulSoup(html, 'html.parser')` 解析 | |
| | ③ `find_all('div', class_='pic')` → `img['alt'/'src']` | |
| | ④ `urlretrieve()` 下载至 `./img/` | |
| | ⑤ `\r` 实现百分比进度条 (`已下载 45.00%`) | |
| `1.py` | 等效 `urllib` 实现：`urlencode()` + `urlopen()` | 搜狗搜索 |

**Key Takeaway / 核心收获**: 本模块展示了 `requests` 在真实场景中的灵活运用 — 搜索接口调用、翻译 API 对接、以及包含进度反馈的海报批量下载器。

---

### 10 — JS 逆向工程

> 🔧 **入门模块 — 未完待续**

| File / 文件 | Status / 状态 |
|---|---|
| `01.py` | 仅 `import execjs`，未实现具体逆向逻辑 |

**Intended Direction / 预期方向**: 使用 `PyExecJS` 库在 Python 中执行目标网站的 JavaScript 加密/签名逻辑，绕过前端反爬机制。这是爬虫进阶的 "最后一公里" — 常见的应用场景包括：参数加密破解、签名算法还原、Cookie 生成模拟。

---

## 🔧 Additional Content / 附加内容

### 多线程 / Multithreading

| File / 文件 | Technique / 技术点 |
|---|---|
| `01.py` | `threading.Thread(target=func)` → `start()` → `join()` 基础入门 |

演示了 Python 多线程的基本模式：创建线程、启动、等待线程结束。这为后续实现并发爬虫奠定了基础。

---

### 大学英语 / Utility Scripts

| File / 文件 | Technique / 技术点 | Target / 目标 |
|---|---|---|
| `爬取答案.py` | XPath (`//div[@id="js_content"]//img/@data-src`) + `urlretrieve()` 批量下载 | 微信公众号文章图片 |

一个实用的微信公众号图片抓取工具，针对微信文章中的 `data-src` 懒加载机制，已成功下载 178 张答案图片至 `daan/` 目录。

---

### Standalone Scripts / 独立脚本

| File / 文件 | Description / 描述 | Libraries / 使用的库 |
|---|---|---|
| `horse.py` | 站长素材图片搜索与批量下载 — `input()` 输入关键词 → `requests` 请求 → XPath 提取 `data-src` → 下载至 `./img/`（40 张图片） | `requests`, `lxml.etree` |
| `text.py` | 中文名单格式化工具 — `str.replace("、", "\n")` 将顿号分隔转为换行 | 无 (纯 Python) |
| `爆破.py` | 占位脚本 — 仅 `import requests, selenium`，暗示自动化/爆破意图 | `requests`, `selenium` |

---

## 🛠️ Tech Stack / 技术栈

### HTTP Clients / HTTP 客户端

| Library / 库 | Usage / 用途 | Modules / 模块 |
|---|---|---|
| `urllib.request` | Python 标准库 HTTP 客户端 | 01, 02, 05, 07, 09 |
| `urllib.parse` | URL 编码 (`quote`, `urlencode`) | 01, 09 |
| `requests` | 第三方 HTTP 库 (Session, Cookie 管理) | 07, 09, `horse.py` |

### Parsing & Extraction / 解析与数据提取

| Library / 库 | Usage / 用途 | Modules / 模块 |
|---|---|---|
| `lxml.etree` | XPath 解析引擎 (HTML/XML) | 02, 06, 07, `horse.py`, 大学英语 |
| `BeautifulSoup4` | HTML DOM 解析 + CSS 选择器 | 03, 07, 09 |
| `jsonpath` | JSON 路径表达式解析 | 02 |
| `json` (stdlib) | JSON 序列化/反序列化 | 01, 07, 09 |

### Browser Automation / 浏览器自动化

| Library / 库 | Usage / 用途 | Modules / 模块 |
|---|---|---|
| `selenium` | WebDriver 浏览器控制 | 04, 05, 06, `爆破.py` |
| `ChromeDriver` | Chrome 浏览器驱动 | 04, 06 |
| `PhantomJS` | (已废弃) 无头 WebKit 浏览器 | 05 |

### Frameworks & Advanced / 框架与进阶

| Library / 库 | Usage / 用途 | Modules / 模块 |
|---|---|---|
| `Scrapy` | 企业级爬虫框架 | 08 |
| `PyExecJS` | Python ↔ JavaScript 桥接 | 10 |
| `threading` | Python 多线程 | 多线程 |

---

## 🌐 Target Websites / 实战目标网站

This repository practices against **20+ real-world websites**:

| Category / 类别 | Websites / 网站 |
|---|---|
| **Search Engines** 搜索引擎 | 百度 (Baidu), 搜狗 (Sogou) |
| **E-commerce** 电商 | 京东 (JD.com), 当当网 (Dangdang) |
| **Movies & Media** 影视 | 豆瓣电影 (Douban), 淘票票 (Taopiaopiao), 电影天堂 (DyTT) |
| **Classifieds & Recruitment** 分类/招聘 | 58同城 (58.com) |
| **Automotive** 汽车 | 汽车之家 (Autohome) |
| **Social Media** 社交 | 微博 (Weibo), Bilibili |
| **Education** 教育 | 武汉理工大学 (WHUT), 古诗文网 (Gushiwen) |
| **Food & Services** 餐饮 | 肯德基 (KFC) |
| **Stock Images** 素材 | 站长素材 (Chinaz) |

---

## 📁 Project Structure / 项目结构

```
Python-Spider-Learning/
│
├── 01_爬虫urllib/              # urllib 基础 (14 .py + 12 .json)
├── 02_爬虫xpath/               # XPath / JsonPath 解析 (5 .py)
├── 03_爬虫beautifulsoup/       # BeautifulSoup 入门 (2 .py)
├── 04_爬虫selenium/            # Selenium 自动化 (12 .py)
├── 05_爬虫phantomjs/           # PhantomJS (1 .py, stub)
├── 06_爬虫chrome handless/     # Chrome Headless (1 .py)
├── 07_爬虫requests/            # requests 进阶 (6 .py)
├── 08_爬虫scrapy/              # Scrapy 框架
│   ├── scrapy_01_58tc/         #   58同城项目
│   ├── scrapy_02_carhome/      #   汽车之家项目
│   ├── scrapy_03_dangdangwang/ #   当当网项目 ✅
│   └── scrapy_04_dytt/         #   电影天堂项目
├── 09-爬虫requests库/          # requests 综合案例 (4 .py)
├── 10-爬虫逆向/                # JS 逆向工程 (1 .py, stub)
├── 多线程/                     # 多线程基础 (1 .py)
├── 大学英语/                   # 微信公众号图片爬取
│   └── daan/                   #   178 张答案图片
├── img/                        # 下载的图片 (40 张)
├── horse.py                    # 图片搜索爬虫
├── text.py                     # 文本格式化工具
├── 爆破.py                     # 占位脚本
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started / 快速开始

### Prerequisites / 环境要求

```bash
Python >= 3.8
pip >= 20.0
```

### Installation / 安装依赖

```bash
# 核心爬虫库
pip install requests
pip install lxml
pip install beautifulsoup4
pip install jsonpath

# Selenium 浏览器自动化
pip install selenium
# 下载 ChromeDriver: https://chromedriver.chromium.org/

# Scrapy 框架
pip install scrapy

# JS 逆向 (可选)
pip install PyExecJS
```

### Run Examples / 运行示例

```bash
# 01 - urllib 基础
cd 01_爬虫urllib
python study.py                          # 最简单的百度首页请求
python 豆瓣电影前十页数据.py              # 豆瓣电影 Top 榜单分页抓取

# 02 - XPath 解析
cd 02_爬虫xpath
python 1xpath.py                         # XPath 语法练习
python 03_站长素材.py                     # 图片批量下载
python 04_jsonpath基本语法.py             # JsonPath 语法练习

# 03 - BeautifulSoup
cd 03_爬虫beautifulsoup
python 01_bs4的基本使用.py               # BS4 API 练习

# 04 - Selenium (需先配置 ChromeDriver 路径)
cd 04_爬虫selenium
# 修改各文件中 ChromeDriver 的绝对路径后运行
python 01_基本使用.py

# 07 - requests 进阶
cd 07_爬虫requests
python 05-cookie登录（古诗文网）.py       # Session + 验证码登录流程

# 08 - Scrapy
cd 08_爬虫scrapy/scrapy_03_dangdangwang
scrapy crawl dang                        # 当当网图书爬虫

# 09 - 综合案例
cd 09-爬虫requests库
python 03-爬取豆瓣电影海报.py             # 豆瓣 Top 250 海报批量下载
```

---

## 🔑 Key Techniques Summary / 核心技术总结

### Anti-Anti-Spider Techniques / 反反爬技术

| Technique / 技术 | Implementation / 实现位置 |
|---|---|
| **User-Agent 伪装** | 几乎所有文件均使用 |
| **完整请求头模拟** (Cookie, Referer, Sec-*, Accept) | `07/04-代理ip.py`, `07/05-cookie登录`, `02/05_解析淘票票.py` |
| **Session 会话保持** | `07/05-cookie登录（古诗文网）.py` |
| **验证码 (CAPTCHA) 人工处理** | `07/05-cookie登录（古诗文网）.py` |
| **ASP.NET Token 提取** (`__VIEWSTATE`, `__VIEWSTATEGENERATOR`) | `07/05-cookie登录（古诗文网）.py` |
| **懒加载图片处理** (`@data-original` / `@data-src`) | `02/03_站长素材.py`, `08/scrapy_03`, 大学英语 |
| **代理 IP** | `01/代理ip.py` |

### Data Extraction Patterns / 数据提取模式

| Pattern / 模式 | Code / 代码示例 |
|---|---|
| **XPath 属性选择** | `//div[@class="container"]//img/@data-original` |
| **XPath 函数过滤** | `//li[contains(@id, "l") and @class="c1"]/text()` |
| **CSS 选择器** | `soup.select('#imgCode')` |
| **BS4 类过滤** | `soup.find_all('div', class_='pic')` |
| **JsonPath 过滤** | `$..book[?(@.price < 10)]` |
| **Selenium 定位** | `find_element(By.XPATH, '//a[@class="n"]')` |

### Pagination Strategies / 分页策略

| Strategy / 策略 | Example / 示例 |
|---|---|
| **URL 参数递增** (`start` / `page`) | 豆瓣 `?start=(page-1)*20` |
| **POST body 参数** (`pageIndex`) | 肯德基 API `pageIndex` |
| **URL 路径拼接** | 站长素材 `qinglvtupian_{page}.html` |

---

## ⚠️ Notes & Caveats / 注意事项

### Educational Purpose / 教学目的声明

> **This repository is for educational and learning purposes only.** All scraping targets are publicly accessible websites. The techniques demonstrated are intended to teach web scraping fundamentals, not for commercial data collection. Always respect `robots.txt`, website Terms of Service, and applicable laws.

> **本仓库仅供学习与教育用途。** 所有爬取目标均为公开可访问的网站，所演示的技术旨在教授爬虫基础知识，而非用于商业数据采集。请始终遵守目标网站的 `robots.txt`、服务条款及相关法律法规。

### Technical Notes / 技术提示

1. **ChromeDriver 路径**: 模块 04 和 06 中的脚本使用了硬编码的 ChromeDriver 绝对路径 (`D:\\桌面\\chromedriver-win64\\chromedriver.exe`)，请按需修改或添加到系统 PATH。

2. **Cookie 时效性**: 模块 07 中硬编码的 Cookie 字符串已过期，运行时需替换为当前有效的 Cookie。

3. **PhantomJS 已废弃**: 模块 05 仅作为技术历史参考保留，不推荐在新项目中使用。

4. **Stub Files**: 以下模块为未完成的占位，期待后续完善：
   - `05_爬虫phantomjs/01_基本使用.py` — 仅初始化
   - `08_爬虫scrapy/scrapy_01_58tc` — parse() 未完成
   - `08_爬虫scrapy/scrapy_04_dytt` — 二级解析未产出
   - `10-爬虫逆向/01.py` — 仅 `import execjs`
   - `爆破.py` — 仅 `import`

5. **Python 版本**: 代码基于 Python 3.x 编写，请注意 `urllib` 在 Python 2/3 之间的差异。

6. **依赖安装**: 建议在虚拟环境 (venv) 中运行，避免污染全局 Python 环境。

---

## 📄 License / 许可证

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

本项目采用 MIT 许可证 — 详见 [LICENSE](LICENSE) 文件。

---

<p align="center">
  <b>Happy Scraping! 🕷️</b><br>
  <sub>Built with ❤️ for Python learners</sub>
</p>
