from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import pandas
import os
import json

water_sources_df = pandas.read_csv(os.path.join(os.getcwd(),"water_sources_data.csv"), header=0)
water_source_markers = []
icon = '//maps.google.com/mapfiles/ms/icons/blue-dot.png'
for i in range(water_sources_df.shape[0]):
    tmp = water_sources_df.loc[i]
    data = {'icon': icon,
            'title': tmp['ID'],
            'lat': tmp['Latitude'],
            'lng': tmp['Longitude'],
            'infobox': (
                "<h1>ID: <b style='color:blue;'>"+tmp['ID']+"</b></h1>"
                "<h2>Quality: "+tmp['Grade']+" ("+tmp['WQI']+")</h2>"
                "<h3>Lat: "+str(tmp['Latitude'])+" Lng: "+str(tmp['Longitude'])+" Updated: "+str(tmp['Updated'])+"</h3>"
                "<img src='//placehold.it/50'>"
                "<br>Location Image"
            )}
            # 'infobox': "ID: < b style='color:green;'>str(tmp['ID'])< / b >"}

        # , WQI: "+str(tmp['WQI'])+", Grade: "+str(tmp['Grade'])+", Updated: "+str(tmp['Updated'])}

    water_source_markers.append(data)

print(water_source_markers[0])

app = Flask(__name__, template_folder="templates")

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4"

# you can also pass key here
GoogleMaps(app, key="AIzaSyAZzeHhs-8JZ7i18MjFuM35dJHq70n3Hx4")

@app.route('/fullmap')
def fullmap():
    fullmap = Map(
        identifier="fullmap",
        varname="fullmap",
        style=(
            "height:75%;"
            "width:75%;"
            "top:10;"
            "left:10;"
            "position:absolute;"
            "z-index:200;"
        ),
        lat=12.067543,
        lng=0.359191,
        markers=water_source_markers,
        # maptype = "TERRAIN",
        zoom="14"
    )
    return render_template('example_fullmap.html', fullmap=fullmap)

if __name__ == "__main__":
    # TO RUN ON LOCAL MACHINE:
    #app.run(debug=True, use_reloader=True)

    # TO RUN ON GOOGLE CLOUD ENGINE:
    app.run(host="0.0.0.0", port=80, debug=False)
