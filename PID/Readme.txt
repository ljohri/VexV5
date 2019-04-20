PID Theory:
http://www.ni.com/en-us/innovations/white-papers/06/pid-theory-explained.html
https://www.csimn.com/CSI_pages/PIDforDummies.html
https://www.elprocus.com/the-working-of-a-pid-controller/

The process of setting the optimal gains for P, I and D to get an ideal response from a control system is called tuning. There are different methods of tuning of which the “guess and check” method and the Ziegler Nichols method will be discussed.
The gains of a PID controller can be obtained by trial and error method. Once an engineer understands the significance of each gain parameter, this method becomes relatively easy. 
In this method, the I and D terms are set to zero first and the proportional gain is increased until the output of the loop oscillates. As one increases the proportional gain, the system becomes faster, 
but care must be taken not make the system unstable. 
Once P has been set to obtain a desired fast response, the integral term is increased to stop the oscillations. The integral term reduces the steady state error, but increases overshoot. 
Some amount of overshoot is always necessary for a fast system so that it could respond to changes immediately. The integral term is tweaked to achieve a minimal steady state error. 
Once the P and I have been set to get the desired fast control system with minimal steady state error, the derivative term is increased until the loop is acceptably quick to its set point. 
Increasing derivative term decreases overshoot and yields higher gain with stability but would cause the system to be highly sensitive to noise. 
Often times, engineers need to tradeoff one characteristic of a control system for another to better meet their requirements.