SirNate0 | 2020-02-24 20:53:17 UTC | #1

I've been pondering creating a nice script-timeline format for use in scripting attacks for my game, and have thrown together a plausible Python prototype. Anyone know if there is a good way to implement something like this in AngelScript or Lua?

```py
from time import time,sleep
from dataclasses import dataclass
from typing import Sequence, Callable

@dataclass
class Finished:
  pass

@dataclass
class Until:
  time: float

@dataclass
class NewTimeline:
  timelineCall: Callable
  arguments: Sequence = tuple([])

def FinishedGenerator():
  while True:
    yield Finished()

class Timeline(object):
  def __init__(self,primaryTimeline):
    self.start = time()
    self.waitTill = 0
    self.status = Until(0)
    self.timeline = primaryTimeline
    self.generator = None

  def run(self):
    if self.generator is None:
      self.generator = self.timeline.timelineCall(*self.timeline.arguments)
      if self.generator is None:
        self.generator = FinishedGenerator()
    try:
      while self.waitTill <= time() - self.start:
        result = next(self.generator)
        if isinstance(result,Until):
          self.waitTill = result.time
        elif isinstance(result,NewTimeline):
          makeTimeline(Timeline(result))
          self.waitTill = 0
        elif isinstance(result,Finished) or result is None:
          raise StopIteration()
        else:
          print(result)
          self.waitTill = float(result)
      #print(self.status,self.waitTill,time()-self.start)
      return False
    except StopIteration:
      removeTimeline(self)
      return True
    

defaultCount = 3
def exampleTimeline(name,count = defaultCount):
  if count <= 0:
    return
  print(name+'Initial behavior {}'.format(time()-fullStart))
  yield 1
  print(name+'Waited 1 second {}'.format(time()-fullStart))
  yield Until(1.25)
  print(name+'Waited until 1.25 seconds {}'.format(time()-fullStart))
  yield NewTimeline(exampleTimeline,['Child{}: '.format(defaultCount-count),count-1])
  print(name+'Made new timeline {}'.format(time()-fullStart))
  yield Until(2)
  print(name+'Waited until 2 {}'.format(time()-fullStart))
  yield Finished()


timelines = []

def makeTimeline(timelineCall):
  print('Added new timeline ' + str(timelineCall))
  timelines.append(timelineCall)

def removeTimeline(timelineCall):
  print('Removed timeline ' + str(timelineCall))
  timelines.remove(timelineCall)

makeTimeline(Timeline(NewTimeline(exampleTimeline,['Hello: '])))

fullStart = time()
i = 0
while len(timelines):
#while not all(t.run() for t in timelines):
  i+=1
  #print(i,':',time() - fullStart,len(timelines))
  for t in timelines:
    t.run()
  sleep(1/60)

print('\nFinished')
```
Output:
```
Added new timeline <__main__.Timeline object at 0x7f2ed5cba1c0>
Hello: Initial behavior 1.621246337890625e-05
1
Hello: Waited 1 second 0.9997529983520508
Hello: Waited until 1.25 seconds 1.253164291381836
Added new timeline <__main__.Timeline object at 0x7f2ed584eac0>
Hello: Made new timeline 1.2533085346221924
Child0: Initial behavior 1.2533459663391113
1
Hello: Waited until 2 2.014037847518921
Removed timeline <__main__.Timeline object at 0x7f2ed5cba1c0>
Child0: Waited 1 second 2.259462594985962
Child0: Waited until 1.25 seconds 2.504365921020508
Added new timeline <__main__.Timeline object at 0x7f2ed5c32ee0>
Child0: Made new timeline 2.506049633026123
Child1: Initial behavior 2.50616192817688
1
Child0: Waited until 2 3.2673180103302
Removed timeline <__main__.Timeline object at 0x7f2ed584eac0>
Child1: Waited 1 second 3.5204973220825195
Child1: Waited until 1.25 seconds 3.758823871612549
Added new timeline <__main__.Timeline object at 0x7f2ed584eac0>
Child1: Made new timeline 3.7622861862182617
Removed timeline <__main__.Timeline object at 0x7f2ed584eac0>
Child1: Waited until 2 4.511084794998169
Removed timeline <__main__.Timeline object at 0x7f2ed5c32ee0>
Finished
```

-------------------------

