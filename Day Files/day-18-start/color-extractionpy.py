import colorgram

colors = colorgram.extract('Super_Mario_64_box_cover.jpg', 10)
first_color = colors[0]
print(first_color.rgb)