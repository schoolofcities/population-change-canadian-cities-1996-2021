## Population Change in Canadian Cities (1996 to 2021)

Mapping 25 years of population growth and decline in Canadian urban regions

View the interactive map here: https://schoolofcities.github.io/population-change-canadian-cities-1996-2021/

![maps](./src/assets/web-card.png)

Data for this map come from the 1996 and 2021 Canadian census. Data for 1996 were accessed at the University of Toronto via [CHASS](http://dc.chass.utoronto.ca/) and were linked to 2021 census tracts using the [Canadian Longitudinal Tract Database](https://github.com/jamaps/CLTD). Data for 2021 were downloaded from [Statistics Canada](https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/index.cfm?Lang=E). `json` data with population by census tract for both these years displayed on the map can be accessed [here](src/assets/ct-pts.geo.json). 

The interactive map was created using [Mapbox Studio](https://www.mapbox.com/mapbox-studio) (for styling the base map, creating the proportional symbols), [Mapbox GL JS](https://www.mapbox.com/mapbox-gljs) (interactivity), and bundled together using [Svelte](https://svelte.dev/).