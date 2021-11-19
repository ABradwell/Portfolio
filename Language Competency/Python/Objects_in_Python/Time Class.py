#Assignment One:

class Time:
      def __init__(self,hh=12, mm=0, s=0):
            if s > 60:
                  s = s-60
                  mm = mm + 1
            if mm > 59:
                  mm = mm - 60
                  hh = hh + 1
            if hh > 23:
                  hh = hh-24
            self.hour = hh
            self.minute = mm
            self.second = s
      def setTime(self, hh=12,mm=0, s=0):
            if s > 60:
                  s = s-60
                  mm = mm + 1
            if mm > 59:
                  mm = mm - 60
                  hh = hh + 1
            if hh > 23:
                  hh = hh-24
            
            self.hour = hh
            self.minute = mm
            self.second = s
      def display(self):
            print("{0}:{1}:{2}".format(self.hour,self.minute,self.second))
      def  __repr__(self):
            return (str(self.hour) + ":" + str(self.minute) + ":" + str(self.second))
      def isBefore(self, other):
            if self.hour < other.hour:
                  return True
            elif self.hour == other.hour:
                  if self.minute < other.minute:
                        return True
                  elif self.minute == other.minute:
                        if self.second < other.second:
                              return True
                        elif self.second == other.second:
                              return False
                        else:
                              return False
                  else:
                        return False
            else:
                  return False
      def Duration(self,other):
            duration = Time((other.hour-self.hour),(other.minute - self.minute),(other.second-self.second))
            print(duration)
