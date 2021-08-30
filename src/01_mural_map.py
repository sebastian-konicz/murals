from pathlib import Path
import pandas as pd
import base64
from folium import IFrame
import folium
from folium.plugins import MarkerCluster
import time
# from IPython.display import display

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def main():
    # start time of function
    start_time = time.time()

    # project directory
    project_dir = str(Path(__file__).resolve().parents[1])

    # loading mural data
    data_path = r'\data\interim\murale_ursynow.xlsx'
    data = pd.read_excel(project_dir + data_path)

    print(data)

    lat = data['lat']
    lng = data['lng']
    name = data['name']
    photo = data['photo']


    # creating folium map
    map_graph = folium.Map([52.145259, 21.051619], zoom_start=13)

    marker_cluster = MarkerCluster().add_to(map_graph)

    folium.LayerControl().add_to(map_graph)

    # encoded = base64.b64encode(open('mypict.jpg', 'rb').read())

    # Plot Markers
    for lat, lng, name, photo in zip(lat, lng, name, photo):
        # photo path
        photo_path = project_dir + r'\data\murale_img\{photo_path}.jpg'.format(photo_path=photo)
        # marker setting
        encoded = base64.b64encode(open(photo_path, 'rb').read())
        html = '<img style="width:100%; height:100%;" src="data:image/png;base64,{}">'.format
        iframe = IFrame(html(encoded.decode('UTF-8')), width=200, height=200)
        popup = folium.Popup(iframe, max_width=800)

        folium.Marker(location=[lat, lng],
                      tooltip=html, popup=popup,
                      # popup='<img src={path}>'.format(path=photo_path),
                      icon=folium.Icon(color='blue', icon='camera', prefix='fa')).add_to(marker_cluster)

    # saving map
    print('saving map')
    map_graph.save(project_dir + r'\data\final\mural_map.html')
    map_graph.save(project_dir + r'\templates\mural_map.html')

    # end time of program + duration
    end_time = time.time()
    execution_time = int(end_time - start_time)
    print('\n', 'exectution time = ', execution_time, 'sec')

if __name__ == "__main__":
    main()