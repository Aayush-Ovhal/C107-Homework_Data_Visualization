import pandas as pd
import plotly.graph_objects as go
import csv

idInput = input("Input ur name u dumb student: ")

dv = pd.read_csv("data_visualization.csv")

studentdv = dv.loc[dv["student_id"] == idInput]

meanOfThings = studentdv.groupby("level")["attempt"].mean()

fig = go.Figure(go.Bar(
                             x = meanOfThings,
                             y = ["level1", "level2", "level3", "level4"],
                             orientation = "h"
                        ))

fig.show()

