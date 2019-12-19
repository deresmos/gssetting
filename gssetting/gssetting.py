from typing import Generator, List, Optional, Type

from gssetting.google_spreadsheet import GoogleSpreadSheet
from gssetting.model.gssetting import GSSetting
from gssetting.model.value_render_option import ValueRenderOption


class GoogleSpreadSheetSetting:
    def __init__(self, service_account_path: str, sheet_doc_id: str) -> None:
        spreadsheet = GoogleSpreadSheet(service_account_path, sheet_doc_id)
        self.spreadsheet = spreadsheet

    def load(
        self,
        sheet_name: str,
        sheet_range: str,
        model: Type[GSSetting],
        value_render_option: Optional[ValueRenderOption] = None,
    ) -> List:
        rows_generator = self.load_rows_generator(
            sheet_name, sheet_range, value_render_option=value_render_option
        )

        if model.is_cls_headers():
            header_cells = next(rows_generator)
            indices = self.find_indices_from_header_cells(header_cells, model.headers)
            return self._generate_model_list(rows_generator, model, indices)

        if model.is_cls_indices():
            return self._generate_model_list(rows_generator, model, model.indices)

        return []

    def load_rows_generator(
        self,
        sheet_name: str,
        sheet_range: str,
        value_render_option: Optional[ValueRenderOption] = None,
    ) -> Generator:
        cells = self.spreadsheet.load_cells(
            sheet_name, sheet_range, value_render_option
        )
        return self.reshape_rows(cells)

    def reshape_rows(self, cells: List) -> Generator:
        if not cells:
            return []

        col_count = self.culc_col_count(cells)
        row_count = len(cells) // col_count

        #  cells -> rows
        for i in range(row_count):
            start_index = i * col_count
            end_index = start_index + col_count
            yield cells[start_index:end_index]

    def find_indices_from_header_cells(
        self, header_cells: List, headers: List[str]
    ) -> List[int]:
        indices = [i for i, cell in enumerate(header_cells) if cell.value in headers]

        return indices

    def culc_col_count(self, cells: List) -> int:
        first_col = cells[0].col
        last_col = cells[0].col

        now_row = cells[0].row
        for cell in cells:
            if now_row != cell.row:
                break

            last_col = cell.col

        return (last_col - first_col) + 1

    def _generate_model_list(
        self, rows, model: Type[GSSetting], indices: List[int]
    ) -> List:
        def _find_gs_values(row):
            return [cell for i, cell in enumerate(row) if i in indices]

        models = [model(*_find_gs_values(row)) for row in rows]
        return models
