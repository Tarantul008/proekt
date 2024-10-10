import cianparser

data = cianparser.parse(
    deal_type="sale",
    accommodation_type="flat",
    location="Москва",
    rooms=("all"),
    start_page=1,
    end_page=50,
    additional_settings={
    "min_house_year": 1990,
    "max_house_year": 2023,
    "metro_foot_minute": "all",
    },
    is_saving_csv=True,
proxies = [
'85.26.146.169:80',
'178.140.177.145:8889',
'95.66.138.21:8880',
'93.123.226.23:81',
'46.47.197.210:3128',
'213.184.153.66:8080',
'62.33.207.201:3128',
'172.67.182.55',
'192.111.139.162',
]
)

[cian_parsing_result_sale_1_50_moskva_10_Dec_2023_18_25_25_942997.csv](https://github.com/Tarantul008/proekt/files/14098500/cian_parsing_result_sale_1_50_moskva_10_Dec_2023_18_25_25_942997.csv)
