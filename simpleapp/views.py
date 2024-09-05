from django.views import View
from django.http import HttpResponse

from config import config


class IndexView(View):
    async def get(self, request):
        first_example = await config.FirstExample().aget()
        simple_body = f"""
        <p>Hello, world. You're at the async page</p>
        <p>Some data from config are here:</p>
        <p>DAYS={first_example.DAYS}</p>
        <p>FIRST_DAY_OF_WEEK={first_example.FIRST_DAY_OF_WEEK}</p>
        <p>FUEL_PRICES={first_example.FUEL_PRICES}</p>
        <p>USE_CALENDAR={first_example.USE_CALENDAR}</p>
        <p>SECRET_SWITCH={first_example.SECRET_SWITCH}</p>
        <p>CONSOLIDATION_GROUPS={first_example.CONSOLIDATION_GROUPS}</p>
        <p>TEST (NOT FROZEN - DON'T USE THIS WAY WITH ASYNC!!!)={config.FirstExample.TEST}</p>

        <p>
        You can change configs <a href="/admin/liveconfigs/configrow/">here</a> and reload this page for checking changes.
        </p>
        """
        return HttpResponse(simple_body)

class IndexSyncView(View):
    def get(self, request):
        first_example = config.FirstExample().get()
        simple_body = f"""
        <p>Hello, world. You're at the sync page</p>
        <p>Some data from config are here:</p>
        <p>DAYS={first_example.DAYS}</p>
        <p>FIRST_DAY_OF_WEEK={first_example.FIRST_DAY_OF_WEEK}</p>
        <p>FUEL_PRICES={first_example.FUEL_PRICES}</p>
        <p>USE_CALENDAR={first_example.USE_CALENDAR}</p>
        <p>SECRET_SWITCH={first_example.SECRET_SWITCH}</p>
        <p>CONSOLIDATION_GROUPS={first_example.CONSOLIDATION_GROUPS}</p>
        <p>TEST (NOT FROZEN)={config.FirstExample.TEST}</p>

        <p>
        You can change configs <a href="/admin/liveconfigs/configrow/">here</a> and reload this page for checking changes.
        </p>
        """
        return HttpResponse(simple_body)
