import math
import plotly.express as px
import pandas as pd
# df = pd.DataFrame(dict(
#     r=[1, 5, 2, 2, 3],
#     theta=['processing cost','mechanical properties','chemical stability',
#            'thermal stability', 'device integration']))
# fig = px.line_polar(df, r='r', theta='theta', line_close=True)
# fig.show()
import plotly.graph_objects as go

categories = ['processing cost','mechanical properties','chemical stability',
              'thermal stability', 'device integration']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[1, 5, 2, 2, 3],
      theta=categories,
      fill='toself',
      name='Product A'
))
fig.add_trace(go.Scatterpolar(
      r=[4, 3, 2.5, 1, 2],
      theta=categories,
      fill='toself',
      name='Product B'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=False
)

fig.show()
import matplotlib.pyplot as plt
# print(math.comb(5, 2))
# for i in range(1,10):
#     print( 'n=',i)
#     for j in range(1,i):
#         print(math.comb(i,j),end=" ")
#     print()
# for i in range(20,40):
#     a=i
#     b=40-a
#     x=range(a)
#     y=[(math.comb(a,j)+math.comb(b,j))for j in x]
#     plt.plot(x, y)  # Plot the line using x and y data
#
#     # Add labels and title for clarity
#     plt.xlabel("X-axis")
#     plt.ylabel("Y-axis")
#     plt.title('a= \{a}')
#
#     # Display the plot
#     plt.show()

# x = range(0, 100)  # Generate x-axis values (0 to 99)
# y = [math.sin(i * math.pi / 50) for i in x]  # Calculate sine values for each x













