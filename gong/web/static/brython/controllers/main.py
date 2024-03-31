# import datetime

from browser import ajax, document, html, window, timer, aio

import javascript as js

from maps import MainMap

# from gongs import Gong


class MainController:
    def __init__(self, lang_code):
        self.lang_code = lang_code

        # self.get_token_url = f"/{lang_code}/get_token"

        self.gongs = dict()
        self.map = None

    # async def request_device_status(self, url, source):
    #     gongs = await self.get_device_status(url)
    #     await self.map.update(source, gongs)

    # async def get_api_data(self, url, params):
    #     headers = {"Authorization": f"Bearer {self.token}"}
    #     response = await aio.get(url, headers=headers, data=params)
    #     gongs = js.JSON.parse(response.data)
    #     return gongs

    async def run(self):
        await self.setup()

        # while self.running:
        #     print(f"monitor: wake up {datetime.datetime.now()}")

        #     source = "air4thai"
        #     params = dict(source=source)
        #     gongs = await self.get_api_data(
        #         self.get_station_latest_climate_url, params
        #     )
        #     await self.map.update(source, gongs)

        #     print(f"monitor: sleep {self.acquisition_interval}s")
        #     # wait for next aquisition
        #     await aio.sleep(self.acquisition_interval)

        # return data

    async def setup(self):
        # response = await aio.get(self.get_token_url)
        # response = js.JSON.parse(response.data)
        # self.token = response["access_token"]

        # headers = {"Authorization": f"Bearer {self.token}"}
        # response = await aio.get(self.get_system_setting_url, headers=headers)
        # self.system_setting = js.JSON.parse(response.data)

        # center = self.system_setting["center"]["coordinates"]
        # zoom = self.system_setting["zoom"]
        # min_zoom = self.system_setting["min_zoom"]

        zoom = 10
        min_zoom = 10
        self.map = MainMap([100, 7], zoom, min_zoom, self.lang_code)

        await self.map.render()

    # def get_sensor_on_complete(self, req, document_id):
    #     summary_data = js.JSON.parse(req.text)
    #     # print(summary_data)
    #     aio.run(self.map.update(document_id, summary_data))
    #     # self.map.update(document_id, summary_data)

    # def get_sensor_data(self, url, params, document_id):
    #     print("get data:", document_id)
    #     headers = {"Authorization": f"Bearer {self.token}"}
    #     ajax.get(
    #         url,
    #         headers=headers,
    #         data=params,
    #         oncomplete=lambda req: self.get_sensor_on_complete(req, document_id),
    #     )

    # def add_interpolation_summary(self, url, source, sensor_type, key):
    #     def interpolation_summary_on_complete(req):
    #         self.map.set_shape_with_key(js.JSON.parse(req.text), key)

    #     headers = {"Authorization": f"Bearer {self.token}"}

    #     params = dict(
    #         source=source,
    #         sensor_type=sensor_type,
    #         coordinate1=f"{self.system_setting['interpolation_coordinate_1']['coordinates'][1]},{self.system_setting['interpolation_coordinate_1']['coordinates'][0]}",
    #         coordinate2=f"{self.system_setting['interpolation_coordinate_2']['coordinates'][1]},{self.system_setting['interpolation_coordinate_2']['coordinates'][0]}",
    #     )

    #     ajax.get(
    #         url,
    #         headers=headers,
    #         data=params,
    #         oncomplete=interpolation_summary_on_complete,
    #     )

    # def remove_interpolation_summary_layer(self, shape_key):
    #     self.map.map.removeLayer(self.map.shapes[shape_key])

    # def get_current_data(self, document_id):
    #     params = dict()

    #     url = ""
    #     if "hotspots" in document_id:
    #         params = dict(
    #             satellite="modis",
    #             source="firms",
    #         )
    #         if document_id == "viir_hotspots":
    #             params["satellite"] = "noaa-20"
    #         url = self.get_latest_hotspot_url
    #     elif "airport" in document_id:
    #         url = self.get_station_latest_climate_url
    #         params["source"] = "port-api"

    #     self.get_sensor_data(url, params, document_id)

    # def on_interpolation_clicked(self, ev):
    #     if "grey" in ev.target.class_name:  # not clicked
    #         # get_viir_hotspots_data()
    #         ev.target.class_name = ev.target.class_name.replace("grey", "green")
    #         get_url = f"{self.get_kriging_summary_url}"
    #         self.add_interpolation_summary(
    #             get_url, "air4thai", "PM_2_5", "dust_interpolation"
    #         )
    #     else:
    #         ev.target.class_name = ev.target.class_name.replace("green", "grey")
    #         self.remove_interpolation_summary_layer("dust_interpolation")

    # def on_filter_clicked(self, ev):
    #     if "grey" in ev.target.class_name:  # not clicked
    #         # get_viir_hotspots_data()
    #         ev.target.class_name = ev.target.class_name.replace("grey", "green")
    #         if ev.target.id not in self.map.markers_layer:
    #             self.get_current_data(ev.target.id)
    #         self.map.set_all_sensor_marker(ev.target.id)
    #     else:
    #         ev.target.class_name = ev.target.class_name.replace("green", "grey")
    #         self.map.remove_all_sensor_marker(ev.target.id)

    # def on_search_clicked(self, ev):
    #     self.started_datetime = document["started_datetime"].value
    #     self.ended_datetime = document["ended_datetime"].value
    #     if "green" in document["airport"].class_name:
    #         params = {}
    #         get_hotspots_url = f"{self.get_weather_station_lasted_url}"
    #         self.get_sensor_data(get_hotspots_url, params, "airport")

    #     if "green" in document["viir_hotspots"].class_name:
    #         params = {}
    #         get_hotspots_url = f"{self.get_hotspots_url}/?started_datetime={self.started_datetime}&ended_datetime={self.ended_datetime}&satellite=noaa-20"
    #         self.get_sensor_data(get_hotspots_url, params, "viir_hotspots")

    #     if "green" in document["modis_hotspots"].class_name:
    #         params = {}
    #         get_hotspots_url = f"{self.get_hotspots_url}/?started_datetime={self.started_datetime}&ended_datetime={self.ended_datetime}&satellite=modis"
    #         self.get_sensor_data(get_hotspots_url, params, "modis_hotspots")

    def start(self):
        print(">>")

        aio.run(self.run())
