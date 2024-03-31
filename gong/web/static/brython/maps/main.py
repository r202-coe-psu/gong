from datetime import datetime, timezone, timedelta

from browser import ajax, document, html, window, timer
import javascript as js

from .map import Map


class MainMap(Map):
    def __init__(
        self,
        center,
        zoom,
        min_zoom,
        lang_code,
    ):
        super().__init__(center, zoom, min_zoom)

        self.lang_code = lang_code

        self.sensor_marker_layers = {}
        self.sensor_markers = {}
        self.markers_layer = {}

        self.station_view_url = f"/{self.lang_code}/stations/"

    async def render(self):
        self.map.on(
            "click", lambda ev: print(f"location: {ev.latlng.lat}, {ev.latlng.lng}")
        )  # map clicked will print mouse location

    async def update(self, document_id, data):
        # print(document_id)
        # print(data)
        if document_id == "air4thai":
            await self.update_climate_marker(document_id, data)
        if document_id == "airport":
            await self.update_climate_marker(document_id, data)
        if document_id == "viir_hotspots":
            await self.update_hotspot_marker(document_id, data)
        if document_id == "modis_hotspots":
            await self.update_hotspot_marker(document_id, data)

    def remove_all_sensor_marker(self, marker_id):
        if marker_id in self.sensor_marker_layers.keys():
            self.map.removeLayer(self.sensor_marker_layers.get(marker_id))

    def set_all_sensor_marker(self, marker_id):
        if marker_id in self.sensor_marker_layers.keys():
            self.sensor_marker_layers[marker_id] = self.leaflet.layerGroup(
                self.markers_layer[marker_id]
            ).addTo(self.map)

    def on_click_station(self, station_id):
        url = f"{self.station_view_url}{station_id}"

        window.open(url)

    async def get_sensor_color(self, sensor_type, value):
        return sensor_colors.get_sensor_color(sensor_type, value)

    async def update_climate_marker(self, source, stations):
        # self.map.removeLayer(self.sensor_marker_layers.get("dust_sensor"))

        markers = []

        bangkok_timezone = timezone(timedelta(hours=7), name="Asia/Bangkok")

        for station in stations["stations"]:
            animate = True
            sensor_color = "DeepSkyBlue"
            tooltip_detail = ""

            if station["climates"]:
                # online need improve
                sensor_texts = []
                DISPLAY_ORDERS = [
                    sensor_type.lower()
                    for sensor_type in sensor_infos.HTML_SENSOR_NAMES.keys()
                ]

                climates = station["climates"].copy()

                for sensor in station["climates"]:
                    sensor_type = sensor["sensor_type"].lower()
                    if sensor_type not in DISPLAY_ORDERS:
                        DISPLAY_ORDERS.append(sensor_type)

                for key in DISPLAY_ORDERS:
                    found = False
                    for i, sensor_data in enumerate(climates):

                        if sensor_data["sensor_type"].lower() == key:
                            found = True
                            break

                    if not found:
                        continue

                    sensor = climates.pop(i)
                    sensor_type = sensor["sensor_type"].lower()

                    value = sensor["value"]
                    value_str = f"{value:.2f}" if type(value) is float else f"{value}"
                    sensor_texts.append(
                        f"""
                        {sensor_infos.HTML_SENSOR_NAMES.get(sensor_type, sensor_type)}:
                        <b>{value_str}</b> {sensor_infos.HTML_SENSOR_UNITS.get(sensor_type,'')}<br/>
                        """
                    )

                timestamp = datetime.fromisoformat(sensor["timestamp"])
                ict_date = timestamp.replace(tzinfo=timezone.utc).astimezone(
                    tz=bangkok_timezone
                )
                timestamp = timestamp.replace(tzinfo=timezone.utc)

                tooltip_detail = f"""
                    <div align="left" style="font-size: 15px;"> 
                        <b>{station["name"]}</b><br/>
                        <b>{station["name_th"]}</b><br/>
                        {''.join(sensor_texts)}
                        {timestamp.strftime("%d/%m/%Y %H:%M:%S %Z")}<br/>
                        {ict_date.strftime("%d/%m/%Y %H:%M:%S %Z")}<br/>
                    </div>
                    """
            else:
                animate = False

                sensor_color = "DarkGrey"
                disactive_txt = {"th": "ขาดการเชื่อมต่อ", "en": "lost connection"}
                tooltip_detail = f"""
                <div align="left" style="font-size: 15px;"> 
                    <b>{station["name"]}</b><br/>
                    {disactive_txt[self.lang_code]}
                </div>
                """

            sensors = {
                sensor["sensor_type"].lower(): sensor["value"]
                for sensor in station["climates"]
            }
            for sensor_type in sensor_infos.HTML_SENSOR_NAMES:
                if sensor_type in sensors.keys():
                    sensor_color = await self.get_sensor_color(
                        sensor_type, sensors[sensor_type]
                    )
                    break
            sensor_marker = self.leaflet.icon.pulse(
                {
                    "iconSize": [15, 15],
                    "color": sensor_color,
                    "fillColor": sensor_color,
                    "animate": animate,
                }
            )

            marker = self.sensor_markers.get(station["id"], None)
            if not marker:
                coordinates = station["coordinates"]["coordinates"]
                marker = (
                    self.leaflet.marker(
                        [coordinates[1], coordinates[0]],
                        {
                            "customId": station["id"],
                            "icon": sensor_marker,
                        },
                    )
                    .bindTooltip(
                        tooltip_detail,
                        {"offset": (0, 30), "className": "tooltip-marker"},
                    )
                    .addTo(self.map)
                    .on(
                        "click",
                        lambda e: self.on_click_station(
                            e.sourceTarget.options.customId
                        ),
                    )
                )

                markers.append(marker)
                self.sensor_markers[station["id"]] = marker
            else:
                marker.setIcon(sensor_marker)
                marker.setTooltipContent(tooltip_detail)

        self.markers_layer[source] = markers

        layer = self.sensor_marker_layers.get(source)

        if not layer:
            print(f"add layer", source)
            self.sensor_marker_layers[source] = self.leaflet.layerGroup(
                self.markers_layer[source]
            ).addTo(self.map)

    async def update_hotspot_marker(self, document_id, hotspots):
        # self.map.removeLayer(self.sensor_marker_layers.get("dust_sensor"))
        markers = []

        for hotspot in hotspots["hotspots"]:
            marker = self.sensor_markers.get(hotspot["id"], None)
            if not marker:
                coordinates = hotspot["metadata"]["coordinates"]["coordinates"]
                marker = (
                    self.leaflet.circle(
                        [coordinates[1], coordinates[0]],
                        color="red",
                        fillColor="#f03",
                        fillOpacity=0.5,
                        radius=100,
                    )
                    .addTo(self.map)
                    .on(
                        "click",
                        lambda e: self.on_click_station(
                            e.sourceTarget.options.customId, ""
                        ),
                    )
                )

                markers.append(marker)
                self.sensor_markers[hotspot["id"]] = marker

        self.markers_layer[document_id] = markers

        layer = self.sensor_marker_layers.get(document_id)

        if not layer:
            print(f"add layer {document_id} in update map")
            self.sensor_marker_layers[document_id] = self.leaflet.layerGroup(
                self.markers_layer[document_id]
            ).addTo(self.map)
