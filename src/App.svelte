<script>
	import { onMount } from 'svelte'
	import mapboxgl from "mapbox-gl";
	import Typeahead from "svelte-typeahead";
	import places from "./assets/places.geo.json";
	import Circle from "./lib/circle.svelte";
	import popupContent from "./lib/popupContent.js"

	mapboxgl.accessToken = 'pk.eyJ1Ijoic2Nob29sb2ZjaXRpZXMiLCJhIjoiY2w3aml0dHdlMHlpazNwbWh0em4xOHNlaCJ9.fXNtPGq0DqYiFvPH6p4fjQ';

	const data = places.features;

	let map;
	let ctuid = "0";
	
	onMount(() => {
		map = new mapboxgl.Map({
			container: 'map', 
			style: 'mapbox://styles/schoolofcities/cl7j75gbd003b14ocub8skc7c',
			center: [-79.45, 43.65], 
			zoom: 10,
			maxZoom: 12,
			minZoom: 9,
			projection: 'globe',
			scrollZoom: true
		});

		map.addControl(new mapboxgl.NavigationControl(), 'top-left');
		map.addControl(new mapboxgl.FullscreenControl(), 'top-right');

		map.on('mouseenter', 'ct_fill', () => {
			map.getCanvas().style.cursor = 'pointer';
		});
		map.on('mouseleave', 'ct_fill', () => {
			map.getCanvas().style.cursor = '';
		})

		map.on('click', 'ct_fill', (e) => {		

			var features = map.queryRenderedFeatures(e.point, { layers: ['ct_fill'] });

			if (ctuid != features[0].properties.CTUID) {
				var style = [
					"match",
					["get", "CTUID"],
					[features[0].properties.CTUID],
					"#f1c500",
					"#fff"
				]
				map.setPaintProperty('ct_fill', 'fill-color', style)
				ctuid = features[0].properties.CTUID

				new mapboxgl.Popup()
					.setLngLat(e.lngLat)
					.setHTML(popupContent(ctuid))
					.addTo(map);

			} else {
				map.setPaintProperty('ct_fill', 'fill-color', '#fff')
				ctuid = '0'
			}

			

			

			console.log(style)

		});

		
	});


	// function mapPan(city) {
	// 	console.log(city)
	// 	map.zoomTo(10)
	// }

	// https://svelte.dev/repl/a1b828d80de24f7e995b2365782c8d04?version=3.50.0

</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
	<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">

	<link href='https://api.mapbox.com/mapbox-gl-js/v2.10.0/mapbox-gl.css' rel='stylesheet' />
</svelte:head>


<main>

<div id="panel">

	<div id="title">
		<h1>25 Years of Population Growth & Decline in Canadian Cities</h1>
	</div>

	
	<div id="text">
		<p>
			<p>Visualizing by neighbourhood census tracts whether the population has increased <Circle stroke="#007FA3" fill="#6FC7EA"/> or decreased <Circle stroke="#dc4633" fill="#ff5842"/> between <b>1996</b> and <b>2021</b>. 
				<!-- The total population across these 33 urban regions increased from X to Y, but this growth was uneven, with QQQQ% of neighbourhoods experiencing population loss.  -->
		</p>
	</div>
	<!-- <div id="text">
		<p>	
			The maps show a general trend of population growth both in the suburban fringes and concentrated in some downtowns, with population decline occurring in many older pre-1996 residential neighbourhoods. But these trends aren't evident everywhere. Click and explore below:
		</p>
	</div> -->

	<div id="text">
		<Typeahead
			{data}
			label=""
			inputAfterSelect="clear"
			placeholder={`search and zoom to a city`}
			limit={5}
			extract={(item) => item.properties.GEONAME}
			on:select={({ detail }) => map.panTo(detail.original.geometry.coordinates)}
			let:result
		>
		<span id="search-results">{@html result.string}</span>
		</Typeahead>
	</div>


</div>



<div id="map"></div>

</main>


<style>
	
	
	@font-face {
		font-family: TradeGothicBold;
		src: url("./assets/Trade Gothic LT Bold.ttf");
	}
	:root {
		font-family: 'Roboto', sans-serif;
	}
	
	:global([data-svelte-search] label) {
		display: none;
	}
	:global([data-svelte-typeahead] mark)  {
		color: #1E3765;
		background-color: #F1C500;
	}
	:global(body) {
		padding: 0px;
		margin: 0px;
		background-color: #fff;
	}
	#search-results {
		color: #1E3765;
		font-family: Roboto, sans-serif;
	}

	main {
		margin: auto;
		width: 100%;
		background-color: rgb(250, 250, 250);
	}

	#panel {
		margin: auto;
		width: 399px;
		height: 100vh;
		border-right: solid 1px #1E3765;
		float: left;
	}

	#title {
		max-width: 600px;
		margin-left: 20px;
		margin-right: 20px;
		/* border-bottom: solid 1px #1E3765;
		padding-bottom: 7px; */
	}

	#title h1 {
		font-family: TradeGothicBold, sans-serif;
		font-size: 20px;
		color: #1E3765
	}

	#title p {
		font-family: 'Roboto', sans-serif;
		font-size: 15px;
		color: #1E3765
	}

	#text {
		max-width: 600px;
		line-height: 1.5;
		/* border-left: solid 1px #1E3765; */
		/* padding-left: 20px; */
		margin-left: 20px;
		margin-right: 20px;
		color: rgb(70, 70, 70);
	}

	#zoom {
		height: 50px;
	}

	#cityZoom {
		color: #007FA3
	}
	#cityZoom:hover {
		cursor: pointer;
	}


	#map {
		height: 100vh;
		width: calc(100vw - 400px);
	}
</style>
