import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import clear_output
from statsmodels.tsa.seasonal import seasonal_decompose

pd.set_option('display.max_columns', None)  # Show all columns