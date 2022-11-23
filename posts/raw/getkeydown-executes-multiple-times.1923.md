sabotage3d | 2017-01-02 01:11:31 UTC | #1

Is that the normal behaviour of GetKeyDown to execute more than once on a single key press? For example the code below executes Run() more than 10 times when the key R is pressed only once is that expected?

[code]void Update(float timeStep)
{
    Input* input = GetSubsystem<Input>();
    if (input->GetKeyDown('R'))
    {
        Run();
    }
}[/code]

-------------------------

1vanK | 2017-01-02 01:11:31 UTC | #2

use GetKeyPress()

-------------------------

sabotage3d | 2017-01-02 01:11:32 UTC | #3

Thanks that works as expected.

-------------------------

