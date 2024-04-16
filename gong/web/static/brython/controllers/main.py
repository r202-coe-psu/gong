# import datetime

from browser import ajax, document, html, window, timer, aio

import javascript as js

from maps import MainMap

# from gongs import Gong


class MainController:
    def __init__(self, lang_code="th", type_="shrine", center=[10, 100], **args):
        self.lang_code = lang_code

        self.get_shrines_url = f"/api/shrines"
        self.get_gongs_url = f"/api/gongs"
        self.get_gimsins_url = f"/api/gimsins"

        self.type_ = type_
        self.map = None

        self.zoom = 5
        self.min_zoom = 0
        self.center = center
        self.args = args
        if type_ == "shrine_gimsin":
            self.zoom = 18  # max leaf let zoom

    async def get_gimsins(self, params={}):
        response = await aio.get(self.get_gimsins_url, data=params)
        gimsins = js.JSON.parse(response.data)
        await self.map.update_gimsins(gimsins)

    async def get_shrines(self):
        response = await aio.get(self.get_shrines_url)
        shrines = js.JSON.parse(response.data)
        await self.map.update_shrines(shrines)

    async def run(self):
        await self.setup()
        # await self.get_gimsins()
        if self.type_ == "gimsin":
            await self.get_gimsins()
        elif self.type_ == "shrine":
            await self.get_shrines()
        elif self.type_ == "shrine_gimsin":
            shrine_id = self.args.get("shrine_id")
            await self.get_gimsins(params=dict(shrine_id=shrine_id))

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

        self.map = MainMap(self.center, self.zoom, self.min_zoom, self.lang_code)

        await self.map.render()

    def start(self):
        aio.run(self.run())
