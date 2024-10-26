# videogen-dataset_toolkit
dataset toolkit for fine-tuning video generation model such as cogvideox.

## Features

- Scrap data from sakugabooru
- Preprocess image dataset (clean it from image, split the video to X-second/video (ex: 6second/video), and move or delete < X-second video.
- Captioning (comingsoon)

## Installation


```bash
#make sure you already install git and python(>3.10, i use 3.12.0)
git clone https://github.com/saikanov/videogen-dataset_toolkit.git
python -m venv venv
venv\Scripts\activate.bat (if you use linux, look for a way to activate the venv, or just use conda)
pip install -r requirements.py
```

## Usage

There is 2 way to scrap sakugabooru, from their [Tags]([https://www.example.com](https://www.sakugabooru.com/tag)) and their [Pools](https://www.example.com](https://www.sakugabooru.com/pool))
```bash
#for Tags
scrapy crawl sakugaTags -a tag="jojo's_bizarre_adventure_series" -a total_pages=27

#for pools pool id can be checked in the page link, is like this "https://www.sakugabooru.com/pool/show/142"
scrapy crawl sakugaPools -a PoolID=142 -a total_pages=1
```

For preprocess the video
```bash
python split.py --video_dir=/path/to/video_dir --output_dir=/path/to/output_dir --lessthansix_folder=/path/to/lessthansix_folder
```

## Contact

- saikanov - [Discord](discordapp/user/693444397055868948)
