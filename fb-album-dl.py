import wget
from time import sleep as wait
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from bs4 import BeautifulSoup
from argparse import ArgumentParser


def main(url, savename='captions.txt', wait_time=1.5):
    driver = webdriver.Firefox()
    driver.get(url)
    captions = []

    with open(savename, 'w', encoding='utf-8') as f:
        for i, thumb in enumerate(driver.find_elements_by_class_name('uiMediaThumb')):
            thumb.click()
            wait(wait_time)
            see_more = driver.find_elements_by_class_name('see_more_link_inner')
            if len(see_more) > 0:
                see_more[0].click()
                caption = driver.find_element_by_class_name('text_exposed').get_attribute('innerHTML')
            else:
                caption = driver.find_element_by_class_name('hasCaption').get_attribute('innerHTML')
            caption = caption.replace('<br>', '')
            if len(see_more) > 0:
                caption = caption.replace('<span class="text_exposed_hide">...</span><span class="text_exposed_show">', '')
            end_span = caption.find('</span>')
            if end_span != -1:
                caption = caption[:end_span]
            purl = driver.find_element_by_class_name('spotlight').get_attribute('src')
            wget.download(purl, f'{i}.jpg')
            f.write(f'{i}: {caption}\n')
            driver.find_elements_by_class_name('_xlt')[0].click()
            wait(wait_time)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-h', '--hyperlink', help='album URL')
    parser.add_argument('-s', '--savename', help='Name of (.txt) file to save to (default = ./captions.txt')
    parser.add_argument('-w', '--wait-time', help='Delay in seconds to wait for spotlight DOM to finish loading (default = 1.5)')
    args = parser.parse_args()
    args_dict = dict()

    if args.hyperlink:
        args_dict['url'] = args.hyperlink
    else:
        raise ValueError('URL is required')

    if args.savename:
        args_dict['savename'] = args.savename

    if args.wait_time:
        args_dict['wait_time'] = args.wait_time

    main(**args_dict)