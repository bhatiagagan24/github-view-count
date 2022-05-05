from flask import Flask, request
import flask

from svg_generator import Svg_Generator, View_Ops

app = Flask(__name__)


@app.route("/fetch/view/count")
def temp_method():
    view_ops_obj.increase_views()
    bg_color = "white" if request.args.get('bg-color') == None else request.args.get('bg-color')
    text_color = "black" if request.args.get('text-color') == None else request.args.get('text-color') 
    print(bg_color)
    return flask.Response(svg_gen_obj.svg_generator(bg_fill=bg_color, text_fill=text_color), 
        mimetype="image/svg+xml")
    
if __name__ == '__main__':
    view_ops_obj = View_Ops()
    svg_gen_obj = Svg_Generator(view_obj=view_ops_obj)
    app.run()