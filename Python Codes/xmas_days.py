items = ["a partridge in a pear tree","two turtle doves","three french hens","four calling birds","five golden rings"]
days = ["1st","2nd","3rd","4th","5th"]
message = "On the {} day of Christmas my true love gave to me: {}"

for i in range(len(items)):
    print(message.format(days[i], items[i]))
