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

        self.markers_layer = {}
        self.gimsin_markers = {}
        self.gimsin_marker_layers = {}
        self.shrine_markers = {}
        self.shrine_marker_layers = {}

        self.gimsin_view_url = "/gimsins/{gimsin_id}"
        self.shrine_view_url = "/shrines/{shrine_id}"

    async def render(self):
        self.map.on(
            "click", lambda ev: print(f"location: {ev.latlng.lat}, {ev.latlng.lng}")
        )  # map clicked will print mouse location

    async def update_gimsins(self, data):
        await self.update_gimsin_markers(data)

    async def update_shrines(self, data):
        await self.update_shrine_markers(data)

    def remove_all_gimsin_marker(self, marker_id):
        if marker_id in self.gimsin_marker_layers.keys():
            self.map.removeLayer(self.gimsin_marker_layers.get(marker_id))

    def remove_all_shrine_marker(self, marker_id):
        if marker_id in self.shrine_marker_layers.keys():
            self.map.removeLayer(self.shrine_marker_layers.get(marker_id))

    def set_all_gimsin_marker(self, marker_id):
        if marker_id in self.gimsin_marker_layers.keys():
            self.gimsin_marker_layers[marker_id] = self.leaflet.layerGroup(
                self.markers_layer[marker_id]
            ).addTo(self.map)

    def set_all_shrine_marker(self, marker_id):
        if marker_id in self.shrine_marker_layers.keys():
            self.shrine_marker_layers[marker_id] = self.leaflet.layerGroup(
                self.markers_layer[marker_id]
            ).addTo(self.map)

    def on_click_gimsin(self, gimsin_id):
        url = self.gimsin_view_url.format(gimsin_id=gimsin_id)
        window.open(url)

    def on_click_shrine(self, shrine_id):
        url = self.shrine_view_url.format(shrine_id=shrine_id)
        window.open(url)

    async def get_obj_name(self, obj):
        name = obj["name"]
        for key in ["name_zh", "name_en"]:
            if obj[key]:
                name = f"{name} | {obj[key]}"

        return name

    async def update_shrine_markers(self, shrines):

        markers = []

        for shrine in shrines:
            image_html = ""
            if shrine["cover_image_url"]:
                image_html = f"""
                <img class="ui centered medium image" src="{ shrine['cover_image_url'] }">
                """
            else:
                image_html = """
                    <div class="ui placeholder">
                        <div class="rectangular image"></div>
                    </div>
                """

            shrine_name = await self.get_obj_name(shrine)
            president_html = ""

            for president in shrine["presidents"]:
                president_html += f"""
                      <div class="item">
                        <div class="ui tiny image">
                          <img src="{ president['cover_image_url'] }" >
                        </div>
                        <div class="middle aligned content">
                          <i class="ui user tag icon"></i> { president['name'] }
                        </div>
                      </div>
                    """

            tooltip_detail = f"""
                <div style="min-width:300px;">
                   <h3>{ shrine_name }</h3>
                   <div>
                        { image_html }
                        <div class="ui message big text">
                            <div class="ui items">
                            { president_html }
                            </div>
                        <div>
                   </div>
                </div>
                """

            coordinates = shrine["coordinates"]["coordinates"]
            # red_icon = self.leaflet.divIcon(
            #     dict(
            #         html="""<i class="ui map marker alternate icon fitted huge red"
            #         style="position:absolute;left:-0.8rem;top:-2.2rem;  border: 1px solid #FFFFFF">
            #         </i>""",
            #         className="dummy",
            #     )
            # )

            shrine_marker = self.leaflet.marker(
                coordinates,
                dict(
                    # icon=red_icon,
                    shrine_id=shrine["id"],
                ),
            )

            marker = (
                shrine_marker.bindTooltip(
                    tooltip_detail,
                    {"offset": (0, 30), "className": "tooltip-marker"},
                )
                .addTo(self.map)
                .on(
                    "click",
                    lambda e: self.on_click_shrine(e.sourceTarget.options.shrine_id),
                )
            )
            # marker._icon.classList.add("huechange")
            marker._icon.style.filter = "hue-rotate(140deg)"

            markers.append(marker)
            self.shrine_markers[shrine["id"]] = marker
            marker.setTooltipContent(tooltip_detail)

        self.markers_layer["shrines"] = markers
        layer = self.shrine_marker_layers.get("shrines")

        if not layer:
            print(f"add layer", "shrines")
            self.shrine_marker_layers["shrines"] = self.leaflet.layerGroup(
                self.markers_layer["shrines"]
            ).addTo(self.map)

    async def update_gimsin_markers(self, gimsins):

        markers = []

        for gimsin in gimsins:
            image_html = ""
            if gimsin["cover_image_url"]:
                image_html = f"""
                <img class="ui medium image" src="{ gimsin['cover_image_url'] }" style="max-height: 300px; overflow: clip; object-fit: cover; object-position: 100% 0;">
                """

            gimsin_name = await self.get_obj_name(gimsin)
            shrine_name = await self.get_obj_name(gimsin["shrine"])
            gong_name = await self.get_obj_name(gimsin["gong"])

            tooltip_detail = f"""
                <div style="min-width:300px;">
                   <h3>{ gimsin_name }</h3>
                   <div>
                        { image_html }
                        <div class="ui message big text">
                            <i class="yin yang icon"></i> {gong_name} <br/>
                            <i class="torii gate icon"></i> {shrine_name} <br/>
                        <div>
                   </div>
                </div>
                """

            coordinates = gimsin["coordinates"]["coordinates"]

            gimsin_marker = self.leaflet.marker(
                coordinates,
                dict(
                    gimsin_id=gimsin["id"],
                ),
            )

            marker = (
                gimsin_marker.bindTooltip(
                    tooltip_detail,
                    {"offset": (0, 30), "className": "tooltip-marker"},
                )
                .addTo(self.map)
                .on(
                    "click",
                    lambda e: self.on_click_gimsin(e.sourceTarget.options.gimsin_id),
                )
            )
            marker._icon.style.filter = "hue-rotate(140deg)"

            markers.append(marker)
            self.gimsin_markers[gimsin["id"]] = marker
            marker.setTooltipContent(tooltip_detail)

        self.markers_layer["gimsins"] = markers
        layer = self.gimsin_marker_layers.get("gimsins")

        if not layer:
            print(f"add layer", "gimsins")
            self.gimsin_marker_layers["gimsins"] = self.leaflet.layerGroup(
                self.markers_layer["gimsins"]
            ).addTo(self.map)
