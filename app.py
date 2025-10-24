import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.header('My data app')

a = st.slider(label = 'mean', min_value = .1, max_value = 10.)
b = st.slider(label = 'std', min_value = 0., max_value = 10.)
x = np.random.normal(loc = a, scale = b, size = 1000)
fig = plt.figure()
sns.distplot(x)
st.pyplot(fig)