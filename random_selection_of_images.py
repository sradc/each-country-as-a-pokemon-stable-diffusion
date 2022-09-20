import random
from pathlib import Path

imdir = Path("images/the_country_of_x_as_pokemon_20220920-203730")
image_paths = list(imdir.glob("*.png"))

for p in random.choices(image_paths, k=11):
    print(
        f"""
<p align="center">
  <img src="./{p}" width=200>
</p>
    """.strip()
    )
