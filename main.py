import numpy as np
from statistics import mean

lm = [0,1,2,3,4,5,6,7,8]

def calculate(l):
  m = np.array(lm).reshape((3, 3))
  print(m)
  
  rowmean = m.mean(0)
  print("Row Mean: ", rowmean)

  colmean = m.mean(1)
  print("Col Mean: ", colmean)

  rowvariance = np.var(m, axis=0)
  print(rowvariance)

  colvariance = np.var(m, axis=1)
  print(colvariance)

  d = {
    'mean': [list(rowmean), list(colmean)],
    'variance': [list(rowvariance), list(colvariance)]
  }

  print(d)
  
calculate(lm)