from flask import Flask, render_template, Markup
import folium

app = Flask(__name__)


@app.route('/')
def hello_world():
    start_coords = (-26.52, 153.09)
    folium_map = folium.Map(location=start_coords, zoom_start=13, width='80%')
    _ = folium_map._repr_html_()
    # get definition of map in body
    map_div = Markup(folium_map.get_root().html.render())
    # html to be included in header
    hdr_txt = Markup(folium_map.get_root().header.render())
    # html to be included in <script>
    script_txt = Markup(folium_map.get_root().script.render())
    return render_template(
        'index.html', map_div=map_div, hdr_txt=hdr_txt, script_txt=script_txt
    )

if __name__ == '__main__':
    app.run(port=4005)
