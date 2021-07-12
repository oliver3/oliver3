from datetime import datetime
from pathlib import Path

from jinja2 import Environment, PackageLoader

weeks = [{"week": 1, "days": [1134, 613, 519, 907, 1280, 1206, 997]},
         {"week": 2, "days": [1539, 1075, 1125, 1009, 1245, 1318, 1601]},
         {"week": 3, "days": [1658, 1336, 1208, 1759, 1565, 1657, 1589]},
         {"week": 4, "days": [2191, 740, 598, 1190, 1581, 1504, 1853]},
         {"week": 5, "days": [2380, 1054, 1013, 1607, 2712, 2715, 3580]},
         {"week": 6, "days": [1611, 1148, 1420, 2492, 2537, 1883, 2276]},
         {"week": 7, "days": [1953, 992, 656, 1507, 1546, 1732, 1932]},
         {"week": 8, "days": [1623, 1373, 1276, 2334, 2128, 2002, 2130]},
         {"week": 9, "days": [2140, 796, 1165, 1892, 2712, 1808, 2673]},
         {"week": 10, "days": [2063, 1464, 1596, 2240, 3142, 2340, 2193]},
         {"week": 11, "days": [1994, 1043, 889, 2500, 2690, 2588, 2017]},
         {"week": 12, "days": [3735, 1386, 1431, 3347, 3023, 2905, 3849]},
         {"week": 13, "days": [2782, 2696, 1437, 2333, 3505, 2812, 2945]},
         {"week": 14, "days": [2235, 1630, 1741, 2302, 2167, 2188, 2030]},
         {"week": 15, "days": [2622, 1592, 1384, 2060, 2248, 2697, 2420]},
         {"week": 16, "days": [3100, 1380, 1226, 2730, 2928, 3379, 2827]},
         {"week": 17, "days": [2972, 1591, 1589, 2940, 3073, 2224, 2499]},
         {"week": 18, "days": [3592, 1542, 1500, 2374, 3177, 3280, 2918]}]

day_max = 3849

week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

jinja_env = Environment(
    loader=PackageLoader(package_name=__name__, package_path='.')
)
index_template = jinja_env.get_template('image.svg.j2')
image_file = Path('./image.svg')
print('Writing %s' % image_file.absolute())

image_file.write_text(index_template.render({
    'weeks': weeks,
    'day_max': day_max,
    'week_days': week_days,
    'now': datetime.now()
}))
