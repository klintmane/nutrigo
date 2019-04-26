"""
To get better results when matching ingredients to products in database we need to
change the naming convention for products. This module is used to rename products in database.

Usage:
    >>> manage.py collectnames
"""

# Legend:
# ID: [name, description, common_name]
# Description and common name may be null.
names = {
    # Butter
    1145: ["Butter"],
    1001: ["Butter", "salted"],
    1002: ["Butter", "whipped"],
    1323: ["Clarified butter", "", "Ghee"],
    4617: ["Margarine"],
    # Cheese
    1004: ["Blue cheese"],
    1005: ["Brick cheese"],
    1006: ["Brie cheese"],
    1007: ["Camembert cheese"],
    1008: ["Caraway cheese"],
    1009: ["Cheddar cheese"],
    1010: ["Cheshire cheese"],
    1014: ["Cottage cheese"],
    1012: ["Colby cheese"],
    1017: ["Cream cheese"],
    1018: ["Edam cheese"],
    1019: ["Feta cheese"],
    1020: ["Fontina cheese"],
    1021: ["Gjetost cheese"],
    1022: ["Gouda cheese", "", "Cheese"], # I (MakuZo) have chosen gouda as a default cheese; fite me if u disagree
    1023: ["Gruyere cheese"],
    1024: ["Limburger cheese"],
    1025: ["Monterey cheese"],
    1026: ["Mozarella cheese"],
    1030: ["Muenster cheese"],
    1031: ["Neufchatel cheese"],
    1032: ["Parmesan cheese", "grated"],
    1033: ["Parmesan cheese"],
    1034: ["Port Salut cheese"],
    1035: ["Provolone cheese"],
    1036: ["Ricotta cheese"],
    1038: ["Romano cheese"],
    1039: ["Roquefort cheese"],
    1040: ["Swiss cheese"],
    1041: ["Tilsit cheese"],
    1156: ["Goat cheese"],
    # Cream
    1049: ["Fluid cream"],
    1054: ["Whipped cream", "", "Cream topping"],
    1056: ["Sour cream"],
    # Milk
    1211: ["Milk", "3.25% fat", "Milk"], # Default for now - debatable though
    1175: ["Milk", "1% fat"],
    1174: ["Milk", "2% fat"],
    1212: ["Dry milk"],
    16120: ["Soymilk"], # Might move it to other category
    # Yogurt
    1116: ["Yogurt"],
    1117: ["Yogurt", "low fat"],
    1293: ["Greek yogurt"],
    1287: ["Greek yogurt", "low fat"],
    1119: ["Vanilla yogurt", "low fat"],
    # Whey
    1112: ["Whey", "acid fluid"], 
    1113: ["Whey", "acid dried"],
    1114: ["Whey", "sweet fluid"],
    1115: ["Whey", "sweet dried"],
    # Egg
    1123: ["Egg", "", "Egg"],
    1124: ["Egg white", "", "White"], # Might affect results with adjective e.g white chocolate - to be checked
    1125: ["Egg yolk", "", "Yolk"],
    # Kefir
    1289: ["Kefir"],
    1290: ["Strawberry kefir"],
    # Ice cream
    19095: ["Vanilla ice cream"],
    19270: ["Chocolate ice cream"],
    # Spices and vinegars
    2001: ["Allspice", "ground"],
    2002: ["Anise seed"],
    2003: ["Basil", "dried"],
    2004: ["Bay leaf"],
    2005: ["Caraway seed"],
    2006: ["Cardamom"],
    2007: ["Celery seed"],
    2008: ["Chervil", "dried"],
    2009: ["Chili powder"],
    2010: ["Cinnamon", "ground"],
    2011: ["Cloves", "ground"],
    2012: ["Coriander leaf", "dried"],
    2013: ["Coriander seed"],
    2014: ["Cumin seed"],
    2015: ["Curry powder"],
    2016: ["Dill seed"],
    2017: ["Dill weed", "dried"],
    2018: ["Fennel seed"],
    2019: ["Fenugreek seed"],
    2020: ["Garlic powder"],
    2021: ["Ginger", "ground"],
    2022: ["Mace", "ground"],
    2023: ["Marjoram", "dried"],
    2024: ["Mustard seed", "ground"],
    2025: ["Nutmeg", "ground"],
    2026: ["Onion powder"],
    2027: ["Oregano", "dried"],
    2028: ["Paprika", "dried"],
    2029: ["Parsley", "dried"],
    2030: ["Black pepper"],
    2031: ["Cayenne pepper"],
    2032: ["White pepper"],
    2033: ["Poppy seed"],
    2034: ["Poultry seasoning"],
    2035: ["Pumpkin pie spice"],
    2036: ["Rosemary", "dried"],
    2037: ["Saffron"],
    2038: ["Sage", "ground"],
    2039: ["Savory", "ground"],
    2041: ["Tarragon", "dried"],
    2042: ["Thyme", "dried"],
    2043: ["Turmeric", "ground"],
    2044: ["Basil", "fresh"],
    2045: ["Dill weed", "fresh"],
    2046: ["Mustard"],
    2047: ["Salt"],
    2048: ["Cider vinegar"],
    2049: ["Thyme", "fresh"],
    2050: ["Vanilla extract"],
    2054: ["Capers"],
    2055: ["Horseradish"],
    2063: ["Rosemary", "fresh"],
    2064: ["Peppermint", "fresh"],
    2065: ["Spearmint", "fresh"],
    2066: ["Spearmint", "dried"],
    2068: ["Red wine vinegar"],
    2069: ["Balsamic vinegar"],
    # Animal Fats
    4001: ["Beef tallow"],
    4002: ["Lard"],
    4575: ["Turkey fat"],
    4576: ["Goose fat"],
    # Oils
    4044: ["Soybean oil"],
    4037: ["Rice bran oil"],
    4038: ["Wheat germ oil"],
    4042: ["Peanut oil"],
    4047: ["Coconut oil"],
    4053: ["Olive oil"],
    4055: ["Palm oil"],
    4058: ["Sesame oil"],
    4060: ["Sunflower oil", "", "Vegetable oil"], # Probably most used vegetable oil?
    4528: ["Walnut oil"],
    4581: ["Avocado oil"],
    # Mayonnaise
    4708: ["Mayonnaise"],
    # Chicken
    5006: ["Chicken", "whole"],
    5011: ["Chicken", "skinless"],
    5015: ["Chicken skin"],
    5020: ["Chicken giblet"],
    5025: ["Chicken heart"],
    5027: ["Chicken liver"],
    5048: ["Chicken back"],
    5053: ["Chicken back", "skinless"],
    5057: ["Chicken breast"],
    5062: ["Chicken breast", "skinless"],
    5066: ["Chicken drumstick"],
    5075: ["Chicken leg"],
    5080: ["Chicken leg", "skinless"],
    5084: ["Chicken neck"],
    5088: ["Chicken neck", "skinless"],
    5091: ["Chicken thigh"],
    5096: ["Chicken thigh", "skinless"],
    5100: ["Chicken wing"],
    5105: ["Chicken wing", "skinless"],
    # Duck
    5139: ["Duck", "whole"],
    5141: ["Duck", "skinless"],
    5143: ["Duck liver"],
    5145: ["Duck breast"],
    # Goose
    5146: ["Goose", "whole"],
    5148: ["Goose", "skinless"],
    5150: ["Goose liver"],
    # Guinea hen
    5151: ["Guinea hen", "whole"],
    5152: ["Guinea hen", "skinless"],
    # Pheasant
    5153: ["Pheasant", "whole"],
    5154: ["Pheasant", "skinless"],
    # Quail
    5157: ["Quail", "whole"],
    5158: ["Quail", "skinless"],
    5159: ["Quail breast"],
    # Squab
    5160: ["Squab", "whole", "Pigeon"],
    5161: ["Squab", "skinless", "Pigeon"],
    # Turkey
    5165: ["Turkey", "whole"],
    5167: ["Turkey", "skinless"],
    5169: ["Turkey skin"],
    5171: ["Turkey giblets"],
    5175: ["Turkey heart"],
    5177: ["Turkey liver"],
    5179: ["Turkey neck"],
    5191: ["Turkey breast"],
    5193: ["Turkey leg"],
    5195: ["Turkey wing"],
    5215: ["Turkey back"],
    5738: ["Turkey drumstick"],
}   
