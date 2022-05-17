from numpy import save
from reanalysis_downloading import download_reanalysis_data_planetos

vars = {
    "eastward_wind_at_100_metres": "u_100",
    "northward_wind_at_100_metres": "v_100",
    # "significant_height_of_wind_and_swell_waves": "hs"
}

df = download_reanalysis_data_planetos(
    dataset="era5",
    lat=39.9094,
    lon=-73.1903,
    st_date="1979-01-01 00:00:00",
    en_date=None,
    num_years=42,
    var_dict=vars,
    save_pathname=".",
    save_filename="ny_bight_uv_1979_present.csv",
    apikey_file="APIKEY.txt"
)