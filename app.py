import panel as pn
from pathlib import Path

pn.extension()

file_input = pn.widgets.FileInput(accept='.png,.jpg,.jpeg,.gif,.bmp', name='选择图片')


image_pane = pn.pane.PNG(width=600, height=400)

def update_image(event):
    # event.new 是 bytes
    image_pane.object = event.new

file_input.param.watch(update_image, 'value')

layout = pn.Row(
    pn.Column("选择图片", file_input, width=200),
    pn.Column("图片预览", image_pane)
)

layout.servable()
