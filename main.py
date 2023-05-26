# import csv
#
#
# data = []
# temperatures = []
#
# with open("weather_data.csv", "r") as weather_data:
#     weather_data = csv.reader(weather_data)
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#     print(weather_data)


import pandas

# Reading the csv file with pandas
data = pandas.read_csv("weather_data.csv")

# # using pandas to change the csv to a dict
# data_dict = data.to_dict()
# print(data_dict)
#
# # not using pandas to return the average
# temp_list = data["temp"].to_list()
# print(int(sum(temp_list) / len(temp_list)))
#
# # using pandas to return the average
# print(data["temp"].mean())
#
# # returns the biggest number
# print(data["temp"].max())
#
# #Get data in colums... 2 different ways to do it
# print(data["condition"])
# print(data.condition)

# Get data in the row

#print(data[data["day"] == "Monday"])


# # finds the row with the max temp
# max_temp = data["temp"].max()
# print(data[data["temp"] == max_temp])
#
#
# monday = data[data["day"] == "Monday"]
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9/5 + 32
#
# print(monday_temp_F)

# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

print(data)


# print(type(data))
# print(data["temp"])
# print(data)
