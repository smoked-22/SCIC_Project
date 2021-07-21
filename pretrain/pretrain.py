import os
import wget
import zipfile
import math


def bar_custom(current, total, width=80):
    avail_dots = width - 2
    shaded_dots = int(math.floor(float(current) / total * avail_dots))
    percent_bar = '[' + '■'*shaded_dots + ' '*(avail_dots-shaded_dots) + ']'
    progress = "%d%% %s [%d / %d]" % (current / total * 100,
                                      percent_bar, current, total)
    return progress


class Pretrainer():
    def __init__(self, config: dict):
        pretrain_config = config['pretrain']
        self.url = pretrain_config['url']
        self.model_dir = pretrain_config['model_path']

    def download_and_extract(self):
        print('downloading pretrained BERT multilingual model')
        os.makedirs(self.model_dir)
        zip_path = wget.download(url=self.url, out=self.model_dir,
                                 bar=bar_custom)
        with zipfile.ZipFile(zip_path, 'r') as zipObj:
            # Extract all the contents of zip file in current directory
            zipObj.extractall(os.path.dirname(zip_path))

    def pretrain(self):
        """pretrain execution function"""
        print('pretrain in progress')
        self.download_and_extract()
        return 0
