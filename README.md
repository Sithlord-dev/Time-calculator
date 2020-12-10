# Time-calculator

Here is a function named `add_time` that takes in a 12-hour clock format time : e.g. "3:00 PM", a period of time composed out of hours and minutes and, optionally, a starting day of the week! This function adds the period of time to the initial time and gives the result in a precise way.

Here are som examples:

```py
add_time("2:59 AM", "24:00")
# Returns: 2:59 AM

add_time("11:59 PM", "24:05")
# Returns: 12:04 AM (2 days later)

add_time("8:16 PM", "466:02", "tuesday")
# Returns: 6:18 AM, Monday (20 days later)
```

This is done without importing any Python libraries, as a project in Freecodecamp.org.
