from datetime import datetime

input = (input("please enter a time: "))

input_time = datetime.fromisoformat(input)

new_format_date = input_time.strftime("%d:%m:%Y")
new_format_time = input_time.strftime("%I:%M:%S").lstrip("0")


if int(input_time.strftime("%z")[1:2]) == 0:
    new_timezone = input_time.strftime("%z")[:3:2]
else:
    new_timezone = input_time.strftime("%z")[:3:1]

print(f"{new_format_date} {new_format_time} {new_timezone}")



