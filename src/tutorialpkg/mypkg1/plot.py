import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [4, 3, 2, 1]
})

# Using pandas.plot directly creates the figure, axes and allows for some customisation
# matplotlib examples typically split this into separate commands defining fig and ax then adding customisation
ax = df.plot(title='Sample Plot', xlabel='X-axis Label', ylabel='Y-axis Label')

# Show the plot
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
df.boxplot()
df.plot.box()  # This syntax is also valid
plt.show()

 # Create a histogram of the DataFrame
df.hist()

 # Show the plot
plt.show()