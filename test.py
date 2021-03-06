import plotly
import plotly.graph_objs as go

timeStamps = []
temperatures = []
data = open("log.csv", "r")
for line in data:
    temp = line.split(",")
    timeStamps.append(temp[0])
    temperatures.append(temp[1])

trace_high = go.Scatter(
    x = timeStamps,
    y = temperatures,
    name = "Temperature (F)",
    line = dict(color = '#17BECF'),
    opacity = 0.8)

data = [trace_high]

layout = dict(
    title='Thermal Sensor readings',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1min',
                     step='minute',
                     stepmode='backward'),
                 dict(count=5,
                      label='5min',
                      step='minute',
                      stepmode='backward'),
                dict(count=1,
                     label='1d',
                     step='day',
                     stepmode='backward'),
                 dict(count=7,
                      label='1w',
                      step='day',
                      stepmode='backward'),
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(),
        type='date'
    )
)

# fig = dict(data=data, layout=layout)
# py.offline.plot(fig, filename = "Time Series with Rangeslider")
plotly.offline.plot({
    "data": data,
    "layout": layout
}, auto_open=True)
