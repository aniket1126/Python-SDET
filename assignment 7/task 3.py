from datetime import datetime

current_datetime = datetime.now()
print("Current Date and Time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

specific_datetime = datetime(2025, 7, 27, 12, 0)

formatted_datetime = specific_datetime.strftime("%d %B, %Y at %H:%M")
print("Specific Date and Time:", formatted_datetime)
