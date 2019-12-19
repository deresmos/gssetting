from gspread import Client as _Client
from gspread.models import Spreadsheet as _Spreadsheet

from gssetting.model.value_render_option import ValueRenderOption


class Spreadsheet(_Spreadsheet):
    #  Need refactoring
    value_render_option: ValueRenderOption = ValueRenderOption.FORMULA

    def values_get(self, *args, params=None):
        params = params or {"valueRenderOption": Spreadsheet.value_render_option.name}
        return super().values_get(*args, params=params)


class Client(_Client):
    def open_by_key(self, key) -> Spreadsheet:
        return Spreadsheet(client=self, properties={"id": key})
