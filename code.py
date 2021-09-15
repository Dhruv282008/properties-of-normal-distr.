import plotly.figure_factory as ff 
import statistics  
import pandas as pd 
import plotly.graph_objects as go
df = pd.read_csv("StudentsPerformance.csv")
reading_score = df["reading score"].to_list()
stdev = statistics.stdev(reading_score)
mean = statistics.mean(reading_score)
median = statistics.median(reading_score)
mode = statistics.mode(reading_score)

firststdev_start, firststdev_end = mean - stdev, mean + stdev
secondstdev_start, secondstdev_end = mean - (2*stdev), mean + (2*stdev)
thirdstdev_start, thirdstdev_end = mean - (3*stdev), mean + (3*stdev)

#Lists
datawithin_firststdev = [result for result in reading_score if result > firststdev_start and result < firststdev_end]
datawithin_secondstdev = [result for result in reading_score if result > secondstdev_start and result < secondstdev_end]
datawithin_thirdstdev = [result for result in reading_score if result > thirdstdev_start and result < thirdstdev_end]

print("Standard Deviation of the READING SCORE is {}".format(stdev))
print("Median of the data is {}".format(median))
print("Mode of the data is {}".format(mode))
print("Mean of the data is {}".format(mean))

print("{}% of data lies with 1 Standard Deviation".format(len(datawithin_firststdev)*100 / len(reading_score)))
print("{}% of data lies with 2 Standard Deviation".format(len(datawithin_secondstdev)*100 / len(reading_score)))
print("{}% of data lies with 3 Standard Deviation".format(len(datawithin_thirdstdev)*100 / len(reading_score)))

fig = ff.create_distplot([reading_score], ["READING SCORE"])
fig.add_trace(go.Scatter(x = [firststdev_start,firststdev_start], y = [0, 0.2], mode = "lines", name = "1 Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [firststdev_end,firststdev_end], y = [0, 0.2], mode = "lines", name = "1 Standard Deviation End"))
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.2], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [secondstdev_start, secondstdev_start], y = [0, 0.2], mode = "lines", name = "2 Standard Deviation Start"))
fig.add_trace(go.Scatter(x = [secondstdev_end, secondstdev_end], y = [0, 0.2], mode = "lines", name = "2 Standard Deviation End"))
fig.show()