# fbgroups-album-downloader
Facebook Groups Album Downloader

## Requirements
- Python 3.6 or higher
- Firefox
- Selenium web driver for Firefox
- Jupyter Notebook (optional)

## Command line
1. Download the latest [Firefox Selenium webdriver](https://github.com/mozilla/geckodriver/releases).

1. In your terminal, activate your environment, `cd` to your working directory and run

```
> pip install -r requirements.txt
```

3. Run the script by

```
> python fb-album-dl.py -h [URL] -s [SAVENAME] -w [WAIT_TIME]
```

Here, `[URL]` is the FB album URL and is the only required input. `[SAVENAME]` and `[WAIT_TIME]` both default to `captions.txt` and `1.5`, respectively.