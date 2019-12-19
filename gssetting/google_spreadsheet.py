from typing import List, Optional

from google.auth.transport.requests import AuthorizedSession
from google.oauth2.service_account import Credentials

from gssetting.inheritance import Client, Spreadsheet
from gssetting.model.value_render_option import ValueRenderOption


class GoogleSpreadSheet:
    scopes: List[str] = ["https://spreadsheets.google.com/feeds"]

    def __init__(self, service_account_path: str, sheet_doc_id: str) -> None:
        self.service_account_path = service_account_path
        self.sheet_doc_id = sheet_doc_id

        self.client = self.load_client(service_account_path)

    def load_client(self, service_account_path) -> Client:
        credentials = Credentials.from_service_account_file(
            service_account_path, scopes=self.scopes
        )

        client = Client(auth=credentials)
        client.session = AuthorizedSession(credentials)

        return client

    def load_cells(
        self,
        sheet_name: str,
        sheet_range: str,
        value_render_option: Optional[ValueRenderOption] = None,
    ) -> List:
        gfile = self.client.open_by_key(self.sheet_doc_id)
        value_render_option = value_render_option or ValueRenderOption.FORMULA

        # TODO: refactoring
        Spreadsheet.value_render_option = value_render_option

        worksheet = gfile.worksheet(sheet_name)
        cells = worksheet.range(sheet_range)

        return cells
