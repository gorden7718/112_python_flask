import numpy as np
import pandas as pa
import streamlit as st

scores_array = np.random.randint(50,high=101,size=(50,5))
student_dataFrame=pa.DataFrame(data=scores_array,columns=["國文","英文","數學","地埋","化學"],index=range(1,51))

st.header("9年仁班成積表")
#st.table(data=student_dataFrame)
st.dataframe(data=student_dataFrame)