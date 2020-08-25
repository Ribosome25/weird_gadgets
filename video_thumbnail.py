# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:44:53 2020

@author: Ruibo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%%

#%%
def video_to_imgs(file_path, n_img, n_rows, put_lable=True, start_frame=1, end_frame=None):
    """
    Quick thumbnail for video clips, and show the thumbnails in a plt figure.
    The pictures are evenly distributed along the time span of video.


    Params:
        file_path: the path and name for the wanted video.
        n_img: how many thumbnail pics you want.
        n_rows: how many rows are in the plt figure.
        put_label: generate a sequence of numbers and put at the upper left corner
        start_frame: if you want to skip some frames in the biginning, pass the frame i to it.
        end_frame: similarly, if you want to skip some frames in the end.
    """
    videoCapture = cv2.VideoCapture(file_path)
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fNUMS = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    i_plot = 1
    i_frame = 1
    if end_frame is None:
        end_frame = fNUMS
    p = np.linspace(start_frame, end_frame, n_img).astype(int)
    l = list(p)
    text_pos = tuple([int(x/10) for x in size])
    n_cols = np.ceil(n_img/n_rows)
    figure = plt.figure(figsize=(1.5*n_cols, 1.8*n_rows))
    #读帧
    success, frame = videoCapture.read()
    while success :
        if i_frame in l:
            ax = figure.add_subplot(n_rows, n_cols, i_plot)
            ax.axes.xaxis.set_visible(False)
            ax.axes.yaxis.set_visible(False)
            plt_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            if put_lable:
                cv2.putText(plt_img, "#{}".format(i_plot), text_pos,
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
            plt.imshow(plt_img)
            i_plot += 1
        success, frame = videoCapture.read() #下一帧
        i_frame += 1
    plt.tight_layout()
    videoCapture.release()
#%%
if __name__ == '__main__':
    f = '.test.AVI'
    video_to_imgs(f, 10, 2, True)
    plt.suptitle('Test Video')
