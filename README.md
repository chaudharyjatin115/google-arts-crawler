# Google Arts & Culture crawler

Google Arts & Culture high quality image downloader.

Download images from Google Arts & Culture in high resolution.

Using this script you can download many zoomable images from
https://artsandculture.google.com/ in very high quality (even 12k).

Warning: this project started as a quick script and may still have rough edges.
Feel free to modify and improve it.

---
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1d143a23-8916-4c20-9986-31e9efc32610" />


## What changed in this fork

* updated for modern Python and Selenium
* removed deprecated Selenium calls
* improved Linux compatibility
* added optional GTK (libadwaita) frontend
* added Arch Linux packaging support
* improved headless Chrome stability
* fixed various small bugs

---

## Requirements

* Python 3.9+
* Chromium or Google Chrome
* ChromeDriver (usually bundled with Chromium on Linux)

Python dependencies are listed in `requirements.txt`.

---

## Installation

### Quick setup (recommended, Linux/macOS)

```bash
git clone https://github.com/chaudharyjatin115/google-arts-crawler.git
cd google-arts-crawler
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run:

```bash
python crawler.py
```

---

### Arch Linux (package build)

This repository includes Meson + PKGBUILD support.

Build and install:

```bash
makepkg -si
```

Run the installed app:

```bash
arts-crawler
```

Required system packages:

* chromium
* gtk4
* libadwaita
* python-gobject

---

### Windows

1. Install Python: https://www.python.org/
2. Install Google Chrome or Chromium
3. Install dependencies:

```bat
pip install -r requirements.txt
python crawler.py
```

Make sure ChromeDriver matches your browser version and is in PATH if required.

---

## Usage

If your clipboard contains a URL with
`artsandculture.google.com`, the script will try to use it automatically.

Otherwise you will be prompted for:

* url
* maximum size (px)

Example URL:

```
https://artsandculture.google.com/asset/madame-moitessier/hQFUe-elM1npbw
```

---

## GTK Frontend (optional)

A simple libadwaita GUI is included.

Run locally:

```bash
python app.py
```

Or if installed via package:

```bash
arts-crawler
```

---

## Output

After the script finishes, the image will be saved to:

```
output/image_name.jpg
```

Note: older upstream versions used `outputs/`. This fork uses `output/`.

---

## Common problems

### chromedriver not found

On Arch Linux, installing `chromium` is usually enough because the driver is bundled.

Check:

```bash
which chromium
which chromedriver
```

On other systems, ensure ChromeDriver matches your Chrome version.

---

### Chrome fails to start

Make sure headless flags are present (already handled in this fork):

* --headless=new
* --no-sandbox
* --disable-dev-shm-usage

---

### Nothing downloads

Possible causes:

* Google changed page layout
* network blocked
* headless Chrome failed
* URL is not a zoomable artwork

Try running the crawler directly to see logs:

```bash
python crawler.py --url "<your url>"
```

---

## Disclaimer

This project is for educational and personal use.
Google may change their frontend at any time which can break scraping.

Use responsibly.
