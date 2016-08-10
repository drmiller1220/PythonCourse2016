class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    def __str__(self):
		return "The time is %s hours and %s minutes" % (self.hour, self.minutes)
	
    def __add__(self,minutes):
		selfTime = self.hour * 60 + self.minutes
		newMinutes = selfTime + minutes
		self.hour = newMinutes / 60
		if self.hour >23: self.hour = self.hour -24
		if self.hour <0: self.hour +24
		self.minutes = newMinutes % 60
			
    def __sub__(self,minutes):
		selfTime = self.hour * 60 + self.minutes
		newMinutes = selfTime - minutes
		self.hour = newMinutes / 60
		if self.hour >23: self.hour -24
		if self.hour <0: self.hour +24
		self.minutes = newMinutes % 60
    
    def __eq__(self, other):
		return self.hour == other.hour and self.minutes == other.minutes
    
    def __ne__(self, other):
		return self.hour != other.hour or self.minutes != other.minutes