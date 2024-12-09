import panel as pn
import io
pn.extension()
file_input = pn.widgets.FileInput(accept=".mp4")

def video_player(file):
    if file is not None:
        file_input.save('test.mp4')
        return pn.pane.Video('test.mp4', width=640)

layout = pn.Column(file_input, pn.bind(video_player,file_input.value))
pn.bind(print, file_input.param.filename, watch=True)

layout.show()

# layout.servable()
# server = pn.serve(layout, threaded=True) 