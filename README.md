# MALScraping: Automated Anime Data Pipeline



## 🚀 Overview

A pipeline to scrape, process, and prepare anime data from MyAnimeList.net.

Built with **Scrapy**, **Bash automation**, and structured with plans for **vector database** and **AI-powered recommendation system** integration.

## 🧩 Features

- Scrapes **top anime list** (title, link, rank, score) from MAL.
- Crawls **individual anime pages** for detailed metadata (studios, genres, synopsis, scores, etc.).
- Exports JSON data for further processing.
- Includes bash scripts for automated cron scheduling.
- Organized project directory for ease of use.

## 📂 Directory Structure

```plaintext
mal_scraper/
├── data/                # Output folder for JSON files & cleaned datasets
├── scripts/             # Automation scripts (bash)
├── spiders/             # Scrapy spiders (list + details)
├── venv/                # Virtual environment
├── merged.csv           # Merged output file (post-cleaning)
├── cleaning.py          # Data cleaning utility
├── cleaning.ipynb       # Data cleaning notebook
├── requirements.txt     # Python dependencies
├── scrapy.cfg           # Scrapy project config
└── README.md            # This file
```

## ⚙️ Tech Stack

- **Python 3.x**
- **Scrapy**
- **Bash (for automation)**
- **Linux cron jobs**
- **(Planned) Vector DB: Qdrant/Milvus**
- **(Planned) FastAPI + Streamlit frontend**

## 🚦 How It Works

1. **`scrape_anime_list.sh`** – Scrapes top anime list & outputs JSON.
2. **`scrape_anime_details.sh`** – Scrapes full anime details for each link found.
3. **Data cleaning** – Done via `cleaning.py` or Jupyter notebook.
4. **(Next step)** – Feed into a Vector DB for AI-powered recommendations.

## 🕷️ Usage

### 1️⃣ Run manually

```bash
bash scripts/scrape_anime_list.sh
bash scripts/scrape_anime_details.sh
```

### 2️⃣ Automate with cron

```bash
0 0 * * 0 bash /path/to/scrape_anime_list.sh
0 3 * * 0 bash /path/to/scrape_anime_details.sh
```

## ✨ Goals

- Fully automated anime data pipeline
- Future-ready for **semantic search** & **AI recommendations**
- Dockerized deployment (planned)

## 💡 Author

**Kanan Majidzade**

---

> "Built with respect for data, systems, and the web."

---

Stay tuned for more updates!

