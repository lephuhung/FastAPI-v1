from typing import Optional
def return_json_data(data: any) ->Optional[any]:
    if data is None:
        return {"success": True, "data": None}
    return {"success": True, "data": data}
