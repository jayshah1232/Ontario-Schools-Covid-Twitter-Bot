import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import chart_studio
import chart_studio.plotly as py
import urllib.request
import json
import config
import os
from datetime import datetime

print("Creating dataframe from Ontario data API...")

#creating a dataFrame
df = pd.read_csv('https://data.ontario.ca/dataset/b1fef838-8784-4338-8ef9-ae7cfd405b41/resource/7fbdbb48-d074-45d9-93cb-f7de58950418/download/schoolcovidsummary.csv')

today = datetime.today().strftime('%Y-%m-%d')

dt_all = pd.date_range(start=df['reported_date'].iloc[0],end=df['reported_date'].iloc[-1]) #creating date range that only includes dates that have data (no weekends)
print(dt_all)

print("Logging in to Chart Studio...")
chart_studio.tools.set_credentials_file(username=config.plotlyUsername, api_key=config.plotlyAPIKey)
print("Logged in")

#sets the x axis to the date range and creates lines based on all the data retrieved and creates the figure
print("Creating Total Cases line chart...")
x = df['reported_date']
totalCasesFig = go.Figure(go.Scatter(x = x, y = df['cumulative_school_related_student_cases'], mode='lines+markers', name = 'Student Cases', line_shape='spline'))
totalCasesFig.add_trace(go.Scatter(x = x, y = df['cumulative_school_related_staff_cases'], mode='lines+markers', name = 'Staff Cases', line=dict(color="purple")))
totalCasesFig.add_trace(go.Scatter(x = x, y = df['cumulative_school_related_cases'], mode='lines+markers', name = 'Total Cases', line=dict(color="red")))
totalCasesFig.add_trace(go.Scatter(x = x, y = df['cumulative_school_related_unspecified_cases'], mode='lines+markers', name = 'Unspecified Cases', line=dict(color="green")))
totalCasesFig.update_layout(title='Total Student and Staff Cases Over Time', title_x=0.5, showlegend=True)

#totalCasesFig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])

#updates the figure with Axis titles
totalCasesFig.update_layout(
    xaxis_title="Date",
    yaxis_title="Number of Cases"
)
totalCasesFig.update_xaxes(
    rangebreaks=[
        dict(bounds=["sat", "mon"]),
        dict(values=["2020-10-12"])
    ]
)
print("Chart created")

print("Creating New Cases line chart...")

df['rolling_average'] = df.iloc[:,6].rolling(window=5).mean()

newCasesFig = go.Figure(go.Scatter(x = x, y = df['new_school_related_student_cases'], mode='lines', name = 'Student Cases'))
newCasesFig.add_trace(go.Scatter(x = x, y = df['new_school_related_staff_cases'], mode='lines', name = 'Staff Cases', line=dict(color="purple")))
newCasesFig.add_trace(go.Scatter(x = x, y = df['new_total_school_related_cases'], mode='lines', name = 'Total New Cases', line=dict(color="red")))
newCasesFig.add_trace(go.Scatter(x = x, y = df['new_school_related_unspecified_cases'], mode='lines', name = 'Unspecified Cases', line=dict(color="green")))
newCasesFig.add_trace(go.Scatter(x = x, y = df['rolling_average'], mode='lines', name = 'Rolling Average', line=dict(color="red", dash='dash')))
newCasesFig.update_layout(title='New Student and Staff Cases Over Time', plot_bgcolor='rgb(255, 255, 255)', showlegend=True)

#newCasesFig.update_xaxes(rangebreaks=[dict(values=dt_breaks)])

newCasesFig.update_yaxes(range=[0, 300])

newCasesFig.update_layout(
    xaxis_title="Date",
    yaxis_title="Number of Cases"
)
print("Chart created")

print("Creating bar graphs for both charts...")
totalFig = px.bar(df, x="reported_date", y=["cumulative_school_related_student_cases", "cumulative_school_related_staff_cases", "cumulative_school_related_unspecified_cases"], title="Total Cases")
#totalFig.show()

newFig = px.bar(df, x="reported_date", y=["new_school_related_student_cases", "new_school_related_staff_cases", "new_school_related_unspecified_cases"], title="New Cases")
#newFig.show()

newGo = go.Figure(data=[
    go.Bar(name='New Student Cases', x=df['reported_date'], y=df['new_school_related_student_cases']),
    go.Bar(name='New Staff Cases', x=df['reported_date'], y=df['new_school_related_staff_cases']),
    go.Bar(name='New Unspecified Cases', x=df['reported_date'], y=df['new_school_related_unspecified_cases']),
])
newGo.add_trace(go.Scatter(
    name='Rolling Average',
    x=x,
    y=df['rolling_average'],
    line=dict(color="#4f5175", width=4)
))

newGo.update_layout(barmode='stack')
newGo.update_xaxes(
    rangebreaks=[
        dict(bounds=["sat", "mon"]),
        dict(values=["2020-10-12"])
    ]
)

newGo.update_layout(
    title="New School Related Cases Over Time",
    title_x=0.5,
    xaxis_title="Date",
    yaxis_title="Number of Cases"
)
newGo.show()
print("Bar graphs created")

print("Adding charts to Chart Studio...")
py.plot(newGo, filename = 'New_School_Related_Cases_Over_Time', auto_open=True)
py.plot(totalCasesFig, filename = 'Total_School_Related_Cases_Over_Time', auto_open=True)
print("Charts added")

print("Creating html and image files of charts...")
#creating html files
totalCasesFig.write_html(r'D:\Documents\Schools Data\Schools Data - Charts\html_files\totalCasesFigure.html', auto_open=True)
# newFig.write_html(r'D:\Documents\Schools Data\Schools Data - Charts\html_files\newCasesFigure.html', auto_open=True)

#creating images for line plots
totalCasesFig.write_image(r'D:\Documents\Schools Data\Schools Data - Charts\images\totalCasesFig.jpeg')
newFig.write_image(r'D:\Documents\Schools Data\Schools Data - Charts\images\newStaffFig.jpeg')
print("Files created")
print("Charts script completed")