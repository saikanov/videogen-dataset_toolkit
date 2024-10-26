# videogen-dataset_toolkit
Dataset toolkit for fine-tuning video generation models such as CogVideoX.

## Features
- Scrap data from SakugaBooru
- Preprocess image dataset:
  - Clean images
  - Split videos into X-second segments (e.g., 6 seconds/video)
  - Handle videos shorter than X seconds (move or delete)
- Captioning (coming soon)

## Installation
```bash
# Make sure you have git and Python (>3.10, recommended: 3.12.0) installed
git clone https://github.com/saikanov/videogen-dataset_toolkit.git
python -m venv venv

# Activate virtual environment
# For Windows:
venv\Scripts\activate.bat
# For Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

## Usage
There are 2 ways to scrape SakugaBooru: using [Tags](https://www.sakugabooru.com/tag) or [Pools](https://www.sakugabooru.com/pool).

### Scraping by Tags
```bash
scrapy crawl sakugaTags -a tag="jojo's_bizarre_adventure_series" -a total_pages=27
```

### Scraping by Pools
Pool ID can be found in the page URL (e.g., "https://www.sakugabooru.com/pool/show/142")
```bash
scrapy crawl sakugaPools -a PoolID=142 -a total_pages=1
```

### Video Preprocessing
```bash
python split.py --video_dir=/path/to/video_dir --output_dir=/path/to/output_dir --lessthansix_folder=/path/to/lessthansix_folder
```

## Contact
- **Discord:** [saikanov](https://discord.com/users/693444397055868948)
