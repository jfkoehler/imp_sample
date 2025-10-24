import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.header('My data app')

tips = sns.load_dataset('tips')
x = tips[['total_bill']]
y = tips['tip']
model = LinearRegression().fit(x, y)
total_bill = st.number_input('Total Bill')
total_bill = np.array([[total_bill]])
prediction = model.predict(total_bill)
st.write(f'Your predicted tip is {prediction[0]: .2f}')

# a = st.slider(label = 'mean', min_value = .1, max_value = 10.)
# b = st.slider(label = 'std', min_value = 0., max_value = 10.)
# x = np.random.normal(loc = a, scale = b, size = 1000)
# fig = plt.figure()
# sns.distplot(x)
# st.pyplot(fig)