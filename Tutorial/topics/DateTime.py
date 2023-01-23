from datetime import datetime

x = datetime.strptime("Sun 10 May 2015 13:54:36 -0700", "%a %d %b %Y %H:%M:%S %z")
y = datetime.strptime("Sun 10 May 2015 13:54:36 -0000", "%a %d %b %Y %H:%M:%S %z")
print((x-y).seconds)

