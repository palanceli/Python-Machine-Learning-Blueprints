
# -*- coding:utf-8 -*-

import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

def Sample():
    plt.style.use('ggplot')
    # 使用%matplotlib命令可以将matplotlib的图表直接嵌入到Notebook之中，
    # 或者使用指定的界面库显示图表，它有一个参数指定matplotlib图表的显示方式。
    # inline表示将图表嵌入到Notebook中。
    %matplotlib inline

    pd.set_option('display.max_columns', 30)
    pd.set_option('display.max_colwidth', 100)
    pd.set_option('display.precision', 3)


    CSV_PATH=r'~/Documents/GitHub/Python-Machine-Learning-Blueprints/Datasets/sample#2.csv'

    df = pd.read_csv(CSV_PATH)

    df.head(10)

if __name__ == '__main__':
    logFmt = '%(asctime)s %(lineno)04d %(levelname)-8s %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=logFmt, datefmt='%H:%M',)
    Sample()