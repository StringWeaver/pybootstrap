import panel as pn
import io

pn.extension()
# 文件选择组件

file_input = pn.widgets.FileInput()
a_slider = pn.widgets.FloatSlider(start=0, end=10)
b_slider = pn.widgets.FloatSlider(start=0, end=10)

def add(a, b):
    return pn.pane.Str(f'{a} + {b} = {a+b}')

layout = pn.Column(a_slider, b_slider, pn.bind(add, a_slider.param.value, b_slider.param.value))



layout.servable()
server = pn.serve(layout, threaded=True) 
server.show()
