# Description
The program visualizes the most common sorting algorithms using `matplotlib`'s `FuncAnimation`class. Furthermore for User Interface purposes I used `tkinter` module, and another addition module `random`.





## Setup

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tkinter, matplotlib and random.

```
pip install tkinter
```
```
pip install matplotlib
```
```
pip install random
```


## Usage

You could use the program to understand how each algotigthm works, or sorts a list!

After setup; run the code, you must see the following window,

![figure](Images/tkinter.1.png) ![figure](Images/tkinter.2.png) 

here you choose the size of array and sorting algorithm. Then hit **Animate**.

This is the first stage of process, program keep repeating the sorting until it is fully sorted.

![figure](Images/figure2.png) 

This is the final stage and the program has completed the sorting!

![figure](Images/figure.png)


## Code

The program is fully self-explanatory, one thing may stand out and that is `yield` and `yield from`.`FuncAnimation` class takes four parameters and other additional parameters; and makes an animation by repeatedly calling a function _func_. In order to pass data to _func_ and each _frame_, we need to use __generator functions__. Generator functions allow us to declare a function that behaves like an iterator, i.e. it behaves as _for loop_. Therefore to convert simple function(that returns just one value in the end) to generator functions we use `yield` and `yield from`( to be able to access value one value at a time).


| Parameter | Description |
| ------ | ----------- |
| fig    | The figure object used to get needed events, such as draw or resize. |
| func   | The function to call at each frame. The first argument will be the next value in frames. |
|frames  | Source of data to pass func and each frame of the animation |
| fargs  | Additional arguments to pass to each call to func. |




