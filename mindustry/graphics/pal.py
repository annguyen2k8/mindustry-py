from .color import *

class Pal:
    dark_outline = Color.valueOf("2d2f39")
    thorium_pink = Color.valueOf("f9a3c7")
    coal_black = Color.valueOf("272727")

    items = Color.valueOf("2ea756")
    command = Color.valueOf("eab678")

    sap = Color.valueOf("665c9f")
    sap_bullet = Color.valueOf("bf92f9")
    sap_bullet_back = Color.valueOf("6d56bf")

    suppress = sap.mul(1.6)

    regen = Color.valueOf("d1efff")

    reactor_purple = Color.valueOf("bf92f9")
    reactor_purple2 = Color.valueOf("8a73c6")

    spore = Color.valueOf("7457ce")

    shield = Color.valueOf("ffd37f").cpy().set_a(0.7)

    bullet_yellow = Color.valueOf("fff8e8")
    bullet_yellow_back = Color.valueOf("f9c27a")

    dark_metal = Color.valueOf("6e7080")
    darker_metal = Color.valueOf("565666")
    darkest_metal = Color.valueOf("38393f")

    missile_yellow = Color.valueOf("ffd2ae")
    missile_yellow_back = Color.valueOf("e58956")

    meltdown_hit = Color.valueOf("ffb98b")

    plastanium_back = Color.valueOf("d8d97f")
    plastanium_front = Color.valueOf("fffac6")

    light_flame = Color.valueOf("ffdd55")
    dark_flame = Color.valueOf("db401c")

    light_pyra_flame = Color.valueOf("ffb855")
    dark_pyra_flame = Color.valueOf("db661c")

    turret_heat = Color.valueOf("ab3400")

    light_orange = Color.valueOf("f68021")
    lightish_orange = Color.valueOf("f8ad42")
    lighter_orange = Color.valueOf("f6e096")

    lightish_gray = Color.valueOf("a2a2a2")
    darkish_gray = Color(0.3, 0.3, 0.3, 1.0)
    darker_gray = Color(0.2, 0.2, 0.2, 1.0)
    darkest_gray = Color(0.1, 0.1, 0.1, 1.0)
    shadow = Color(0, 0, 0, 0.22)
    ammo = Color.valueOf("ff8947")
    rubble = Color.valueOf("1c1817")

    boost_to = Color.valueOf("ffad4d")
    boost_from = Color.valueOf("ff7f57")

    lancer_laser = Color.valueOf("a9d8ff")

    stone_gray = Color.valueOf("8f8f8f")
    engine = Color.valueOf("ffbb64")

    health = Color.valueOf("ff341c")
    heal = Color.valueOf("98ffa9")
    bar = Color.valueOf("708090")  # Assuming slate color
    accent = Color.valueOf("ffd37f")
    stat = Color.valueOf("ffd37f")
    negative_stat = Color.valueOf("e55454")
    gray = Color.valueOf("454545")
    metal_gray_dark = Color.valueOf("6e7080")
    accent_back = Color.valueOf("d4816b")
    place = Color.valueOf("6335f8")
    remove = Color.valueOf("e55454")
    noplace = Color.valueOf("ffa697")
    remove_back = Color.valueOf("a73e3e")
    place_rotate = accent
    break_invalid = Color.valueOf("d44b3d")
    range = Color.valueOf("f4ba6e")
    power = Color.valueOf("fbad67")
    power_bar = Color.valueOf("ec7b4c")
    power_light = Color.valueOf("fbd367")
    placing = accent

    unit_front = Color.valueOf("ffa665")
    unit_back = Color.valueOf("d06b53")

    light_trail = Color.valueOf("ffe2a9")

    surge = Color.valueOf("f3e979")

    plastanium = Color.valueOf("a1b46e")

    red_spark = Color.valueOf("fbb97f")
    orange_spark = Color.valueOf("d2b29c")

    red_dust = Color.valueOf("ffa480")
    redder_dust = Color.valueOf("ff7b69")

    plastic_smoke = Color.valueOf("f1e479")

    admin_chat = Color.valueOf("ff4000")

    neoplasm_outline = Color.valueOf("2e191d")

    neoplasm1 = Color.valueOf("f98f4a")
    neoplasm_mid = Color.valueOf("e05438")
    neoplasm2 = Color.valueOf("9e172c")

    logic_blocks = Color.valueOf("d4816b")
    logic_control = Color.valueOf("6bb2b2")
    logic_operations = Color.valueOf("877bad")
    logic_io = Color.valueOf("a08a8a")
    logic_units = Color.valueOf("c7b59d")
    logic_world = Color.valueOf("6b84d4")

    beryl_shot = Color.valueOf("b1dd7e")
    tungsten_shot = Color.valueOf("768a9a")

    plastic_burn = Color.valueOf("e9ead3")

    muddy = Color.valueOf("432722")

    red_light = Color.valueOf("feb380")
    slag_orange = Color.valueOf("ffa166")
    tech_blue = Color.valueOf("8ca9e8")

    vent = Color.valueOf("6b4e4e")
    vent2 = Color.valueOf("3b2a2a")