import plotly.offline as py
import csv
import plotly.graph_objs as go

fig = go.Figure(
    data=[
        go.Bar(
            name="User1",
            x=["d1", "d2", "d3"],
            y=[5, 2, 6],
            offsetgroup=0
        ),
        go.Bar(
            name="User2",
            x=["d1", "d2", "d3"],
            y=[2, 4, 1],
            base=[5, 2, 6],
            offsetgroup=0
        )
    ],
    layout=go.Layout(
        title="Messages per hour of day",
        yaxis_title="Message Count"
    )
)


def graph_mph():
    try:
        stat_file = open("res/stat.txt", "r")
        hours = {}
        for i in range(24):
            hours[str(i)] = 0

        for line in stat_file:
            new_line = str(int(standarize_stat(0, 0, line)[3]))
            hours[new_line] += 1

        trace = go.Bar(x=getKeyList(hours),
                       y=getValueList(hours))
        py.plot([trace])

    except FileNotFoundError:
        print("Error")

fig.show()