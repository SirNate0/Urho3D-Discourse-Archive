Enhex | 2017-01-02 01:03:40 UTC | #1

Built on top of HiresTimer.
Stopwatch enables pausing, resuming, and starting the timer with a given initial time.

It would be nice if it gets added to Urho3D, skipping the HiresTimer layer.

StopWatch.hpp
[code]
#ifndef STOPWATCH_HPP
#define STOPWATCH_HPP


#include "Timer.h"

using namespace Urho3D;


/*
Stopwatch enables pausing, resuming, and starting the timer with a given initial time.
*/
class Stopwatch : protected HiresTimer
{
public:
	void pause();
	void resume();
	void start(long long microseconds = 0);
	long long getTime();


protected:
	bool isRunning = false;
	long long start_time = 0;
};


#endif//STOPWATCH_HPP
[/code]


StopWatch.cpp
[code]
#include "Stopwatch.hpp"


//
// pause
//
void Stopwatch::pause()
{
	start_time += GetUSec(true);
	isRunning = false;
}


//
// resume
//
void Stopwatch::resume()
{
	Reset();
	isRunning = true;
	
}


//
// start
//
void Stopwatch::start(long long microseconds)
{
	start_time = microseconds;
	Reset();
	isRunning = true;
}


//
// getTime
//
long long Stopwatch::getTime()
{
	if (isRunning)
		return start_time + GetUSec(false);
	else
		return start_time;
}
[/code]

-------------------------

