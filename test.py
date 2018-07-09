import plotly.plotly as py
import plotly.graph_objs as go

timeStamps = []
temperatures = []
data = open("log.csv", "r")
for line in data:
    temp = line.split(",")
    x.append(temp[0])
    y.append(temp[1])

trace_high = go.Scatter(
    x = timeStamps,
    y = temperatures,
    name = "Temperature (°F)",
    line = dict(color = '#17BECF'),
    opacity = 0.8)

data = [trace_high]

layout = dict(
    title='Thermal Sensor readings',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
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

fig = dict(data=data, layout=layout)
py.iplot(fig, filename = "Time Series with Rangeslider")
