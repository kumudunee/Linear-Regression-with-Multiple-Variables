import pandas as pd
import numpy as np
from sklearn import linear_model
import math

df = pd.read_csv("hr_info.csv")
print(df)
#median for experience
median_experience = math.floor(df.experience.median())

print(median_experience)

df.experience=df.experience.fillna(median_experience)
print(df.experience)

print(df)

#median for test score
median_test_score = math.floor(df.test_score.median())

print(median_test_score)

df.test_score=df.test_score.fillna(median_test_score)
print(df.test_score)

print(df)
