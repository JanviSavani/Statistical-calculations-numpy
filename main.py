import numpy as np

lm = [0,1,2,3,4,5,6,7,8]

def calculate(l):
  m = np.array(lm).reshape((3, 3))
  print(m)

  #Mean
  rowmean = m.mean(0)
  colmean = m.mean(1)
  flattenedmean = m.mean()

  #Variance
  rowvar = np.var(m, axis=0)
  colvar = np.var(m, axis=1)
  flattenedvar = np.var(m)

  #Standard Deviation
  rowstd = np.std(m, axis=0)
  colstd = np.std(m, axis=1)
  flattenedstd = np.std(m)

  #Max
  rowmax = m.max(0)
  colmax = m.max(1)
  flattenedmax = m.max()

  #Min
  rowmin = m.min(0)
  colmin = m.min(1)
  flattenedmin = m.min()

  #Sum
  rowsum = m.sum(0)
  colsum = m.sum(1)
  flattenedsum = m.sum()

  d = {
    'mean': [list(rowmean), list(colmean), flattenedmean],
    'variance': [list(rowvar), list(colvar), flattenedvar],
    'standard deviation': [list(rowstd), list(colstd), flattenedstd],
    'max': [list(rowmax), list(colmax), flattenedmax],
    'min': [list(rowmin), list(colmin), flattenedmin],
    'sum': [list(rowsum), list(colsum), flattenedsum]
  }
  
  return d
  
result = calculate(lm)
print(result)