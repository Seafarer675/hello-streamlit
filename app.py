import streamlit as st
import pandas as pd
import numpy as np

df =pd.DataFrame({'first cplumn': [1, 2, 3, 4], 'second column': [10, 20, 30, 40]})
df

#第三行與第七行做的事情是一樣的 皆為創建表格
st.write("Here's our first attempt using data to create a table:")
st.write(pd.DataFrame({'first cplumn': [1, 2, 3, 4], 'second column': [10, 20, 30, 40]}))

#創建一個隨機表格 st.write 與 st.dataframe 與 st.table 都能畫出表格
dataframe = np.random.randn(10, 20) #只是一種普通的多維數組
st.write(dataframe) #會自己使用最適合的方式繪製表格

dataframe = pd.DataFrame(np.random.randn(10, 20)) #功能更強大的二維數據結構 適用於數據分析與處理
columns = ('col %d' %i for i in range(20))
st.dataframe(dataframe.style.highlight_max(axis=0)) #建立「動態」表格

dataframe = pd.DataFrame(np.random.randn(10, 20))
columns = ('col %d' %i for i in range(20))
st.table(dataframe.style.highlight_max(axis=0)) #建立「靜態」表格

chart_data = pd.DataFrame(np.random.randn(20, 3))
columns = ['a', 'b', 'c']
st.line_chart(chart_data) #畫折線圖

map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon']) #lat:經度 lon:緯度
st.write(map_data) #畫出1000行 2列的座標表格
st.map(map_data) #將表格以地圖的方式繪製出來

x = st.slider('x', 0, 50) #widgets slider button selectbox 等等
st.write(x, "squared is", x * x)  