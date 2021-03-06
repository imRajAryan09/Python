<p align="center">
  <h1>manim</h1> 
</p>

### Learning the best way of combining your love for math and programming

<p align="center">
  <img src="https://cdn.dribbble.com/users/43762/screenshots/1193016/mtn-graph-dribbbble.gif">
</p>

Animating technical concepts is traditionally pretty tedious since it can be difficult to make the animations precise enough to convey them accurately.
Manim uses Python to generate animations programmatically, making it possible to specify exactly how each one should run.

</br>

Manim stands for mathematical animation engine and was created by Grant Sanderson to produce high-precision math animation videos. 
The main objective of the [Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) channel and this Python library is to complement
traditional textbook-based math learning with visual intuition.

</br>

Manim was created as a bridge between the FFmpeg video encoding engine and Python.
Since you can’t communicate built-in Python data structures to FFmpeg, Manim implements several mathematical object representation and animation classes.


### Requirements : 
- Python
- manim
- LaTeX
- ffmpeg

After meeting all the requirements run this command in the terminal to export your code to animation : 
</br>

    manim -pqh file_name.py ClassName
    
</br>
</br>

This gif has been coded using manim and it requires only 5 lines of code : 

<p align="center">
  <img src="https://github.com/imRajAryan09/Python/blob/main/manim/output.gif">
</p>


    class Example2(Scene):
        def construct(self):
            text = Text("Thank you for reading!!!", color=RED).scale(1.25)
            self.play(Write(text), run_time=3)
            self.wait(10)
