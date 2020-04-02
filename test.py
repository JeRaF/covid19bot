import COVID19Py

covid = COVID19Py.COVID19()

latest = covid.getLatest()
location = covid.getLocationByCountryCode("CN")
print(location)
