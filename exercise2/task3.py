class AlarmClock:
    def __init__(self):
        self.current_time_hr = 0
        self.current_time_min = 0
        self.alarm_time_hr = 0
        self.alarm_time_min = 0
        self.alarm_status = False
        self.alarm_message = ""

    def current_time_set(self, hour, minute):
        self.current_time_hr = hour
        self.current_time_min = minute

    def display_current_time(self):
        print(
            "Current time:", f"{self.current_time_hr:02d}:{self.current_time_min:02d}"
        )

    def alarm_set(self, hour, minute, message):
        self.alarm_time_hr = hour
        self.alarm_time_min = minute
        self.alarm_message = message

    def turn_alarm_on(self):
        self.alarm_status = True

    def turn_alarm_off(self):
        self.alarm_status = False

    # Function for time passing and the hour changing when minutes reach 60
    def increment_time(self, minutes):
        self.current_time_min += minutes
        while self.current_time_min >= 60:
            self.current_time_min -= 60
            self.current_time_hr += 1
            if self.current_time_hr == 24:
                self.current_time_hr = 0

    # Checking if alarm is on and alarm going off
    def check_alarm(self):
        if (
            self.current_time_hr == self.alarm_time_hr
            and self.current_time_min == self.alarm_time_min
            and self.alarm_status
        ):
            print("Alarm!", self.alarm_message)
            self.turn_alarm_off()


alarm_clock = AlarmClock()

# Setting current time, alarm time, alarm message and alarm on
alarm_clock.current_time_set(8, 0)
alarm_clock.alarm_set(8, 5, "Wake up!")
alarm_clock.turn_alarm_on()

# Simulating time
for _ in range(10):  # Time between current time and alarm time in minutes
    alarm_clock.display_current_time()
    alarm_clock.increment_time(1)
    alarm_clock.check_alarm()
