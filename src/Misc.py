import datetime

class RefOutArgWrapper:
    def __init__(self, val): 
        self.value = val

class EventHandler:
    def call(self, sender, arg): pass
    
class ProgressEventArgs:
    def __init__(self, p, st): 
        self.progressPercentage = p
        self.userState = st

class PropertyChangedEventArgs:
    def __init__(self, n): 
        self.propertyName = n

class CancelEventArgs:
    def __init__(self, c = False): 
        self.cancel = c

class Stopwatch:
    def __init__(self):
        self.dt0 = datetime.datetime.now()
        self.dt1 = None
    def start(self):
        self.dt0 = datetime.datetime.now()
        self.dt1 = None
    def reset(self):
        self.dt0 = datetime.datetime.now()
        self.dt1 = None
    def stop(self):
        self.dt1 = datetime.datetime.now()
    @property
    def isrunning(self):
        return self.dt0 != None and self.dt1 == None
    @property
    def elapsedMilliseconds(self):
        sp = self.dt1 - self.dt0
        return sp.total_seconds() * 1000
    @property
    def elapsed(self):
        return self.dt1 - self.dt0
    
     
        
        