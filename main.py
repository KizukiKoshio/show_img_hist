import numpy as np
import pandas as pd
import streamlit as st
from skimage.io import imread


# download the image
img_url = 'https://static.wixstatic.com/media/551be4_80cab8b432e144e2a2a1cf5cb7844a44~mv2.png/v1/fill/w_266,h_266,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/emp_tunecore%20(0%3B00%3B00%3B00)_2.png'

im = imread(img_url)

st.image(im, caption='the jacket of the EmpError',
         use_column_width=True)


# show histgram of all colors
hist_red, _ = np.histogram(im[:, :, 0], bins=64)
hist_green, _ = np.histogram(im[:, :, 1], bins=64)
hist_blue, _ = np.histogram(im[:, :, 2], bins=64)
hist = np.stack((hist_red, hist_green, hist_blue), axis=1)

df_hist = pd.DataFrame(hist, columns=['R', 'G', 'B'])
st.bar_chart(df_hist)


# choose one color
color = st.radio(
    "choose R, G, or B",
    ('R', 'G', 'B'))
if color == 'R':
    df_hist = pd.DataFrame(hist_red)
    st.bar_chart(df_hist)
if color == 'G':
    df_hist = pd.DataFrame(hist_green)
    st.bar_chart(df_hist)
if color == 'B':
    df_hist = pd.DataFrame(hist_blue)
    st.bar_chart(df_hist)
