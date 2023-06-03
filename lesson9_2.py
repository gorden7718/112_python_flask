import numpy as np
import pandas as pa

scores_array = np.random.randint(50,high=101,size=(50,5))
student_dataFrame=pa.DataFrame(data=scores_array,columns=["國文","英文","數學","地埋","化學"],index=range(1,51))
print(student_dataFrame)