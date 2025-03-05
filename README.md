---

# Alarm Clock Program

## Project Overview
This is a simple alarm clock program written in Python. It displays the current time in either 12-hour or 24-hour format, and allows the user to set an alarm. When the set time matches the current time, the program will sound an alert.

## Features
- **Real-Time Clock Display:** Displays the current time in either 12-hour or 24-hour format.
- **Manual or Auto Time Setup:** Choose whether to manually input the current time or set it automatically based on the system time.
- **Alarm Functionality:** Allows the user to set an alarm time, and the program will alert when the time comes.
- **Time Format Flexibility:** Switch between 12-hour AM/PM format and 24-hour format.

## Technologies Used
- **Python:** The main programming language used for the program.
- **Datetime and Time Modules:** Used to handle real-time clock and alarms.

## Installation Instructions
1. Ensure you have Python 3.x installed on your system.
2. Download or clone this repository.
3. Run the program:
   ```
   python alarm_clock.py
   ```

## Usage Instructions
1. Upon starting, you can choose whether to set the time manually or let the program automatically fetch the system time.
2. You can select between a 24-hour or 12-hour format for displaying the time.
3. Enter the alarm time (hour and minute).
4. The program will continue running and check every second if the current time matches the alarm time. When the alarm time is reached, it will display an alert message.

## Files Structure
```
/alarm_clock
    alarm_clock.py    # Main script for the alarm clock.
    README.md         # Project documentation.
```

## License
This project is free of rights and can be used, modified, and distributed by anyone. No restrictions apply.

---
