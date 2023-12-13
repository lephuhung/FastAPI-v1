from typing import Optional
import random

def return_json_data(data: any) ->Optional[any]:
    if data is None:
        return {"success": True, "data": None}
    return {"success": True, "data": data}

def random_hex_color():
  """
  Generates a random hex color code.

  Returns:
    A string representing a random hex color code.
  """
  hex_digits = "0123456789abcdef"
  return "#" + "".join([random.choice(hex_digits) for _ in range(6)])