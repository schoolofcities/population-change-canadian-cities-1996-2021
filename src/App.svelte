<script>
	import { onMount } from 'svelte'
	import mapboxgl from "mapbox-gl";
	import Typeahead from "svelte-typeahead";
	import Places from "./assets/places.geo.json";
	import Circle from "./lib/circle.svelte";
	import popupContent from "./lib/popupContent.js"
	import Top from "./lib/Top.svelte"

	mapboxgl.accessToken = 'pk.eyJ1Ijoic2Nob29sb2ZjaXRpZXMiLCJhIjoiY2w3aml0dHdlMHlpazNwbWh0em4xOHNlaCJ9.fXNtPGq0DqYiFvPH6p4fjQ';

	const data = Places.features;

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
		
		map.addControl(new mapboxgl.FullscreenControl(), 'top-left');
		map.addControl(new mapboxgl.NavigationControl(), 'top-left');
		
		const scale = new mapboxgl.ScaleControl({
			maxWidth: 100,
			unit: 'metric'
			});
		map.addControl(scale, 'bottom-right');

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

		});

	});

	function hideShow() {
		console.log("meow")
	}

	function placeClick(city) {
		map.panTo(city.original.geometry.coordinates);
	}

	// https://svelte.dev/repl/a1b828d80de24f7e995b2365782c8d04?version=3.50.0

</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
	<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">

	<link href='https://api.mapbox.com/mapbox-gl-js/v2.10.0/mapbox-gl.css' rel='stylesheet' />
</svelte:head>


<main>

<Top/>

<div id="map"></div>


<div id="search">
	<Typeahead
			{data}
			label=""
			inputAfterSelect="clear"
			placeholder={`search and zoom to a city`}
			limit={5}
			extract={(item) => item.properties.GEONAME}
			on:select={({ detail }) => placeClick(detail)}
			let:result
		>
		<span id="search-results">{@html result.string}</span>
	</Typeahead>
</div>



<div id="panel">

	<div id="title">
		<h1>25 Years of Population Growth & Decline in Canadian Cities</h1>

		<p>
			<p>Visualizing by neighbourhood census tracts how the population has increased <Circle stroke="#007FA3" fill="#6FC7EA"/> or decreased <Circle stroke="#dc4633" fill="#ff5842"/> between <span id="bold">1996</span> and <span id="bold">2021</span>. 

		</p>
	</div>

	<div id="more-less" on:click={hideShow}>
		<p>▼ read more ▼</p>
	</div>
	
	<div id="text">
		<p>
			<p>Visualizing by neighbourhood census tracts whether the population has increased <Circle stroke="#007FA3" fill="#6FC7EA"/> or decreased <Circle stroke="#dc4633" fill="#ff5842"/> between <b>1996</b> and <b>2021</b>. 
				<!-- The total population across these 33 urban regions increased from X to Y, but this growth was uneven, with QQQQ% of neighbourhoods experiencing population loss.  -->
		</p>
	
		<p>	
			The area of the circles are proportional to the number of people who moved in or moved out of each neighbourhood.
		</p>
	
		<p>	
			Click on the map to view numbers for a specific neighbourhood.
		</p>
	</div>

</div>





</main>


<style>
	
	
	@font-face {
		font-family: TradeGothicBold;
		src: url("./assets/Trade Gothic LT Bold.ttf");
	}
	:root {
		font-family: 'Roboto', sans-serif;
	}



	:global([data-svelte-search]) {
		/* height: 50px; */
		border: solid 1px lightgrey;
		border-radius: 4px;
		background-color: none;
	}
	:global([data-svelte-search] li) {
		height: 50px;
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
	#search {
		position: absolute;
		width: 300px;
		top: 55px;
		right: 5px;
		z-index: 99;
		opacity: 0.93;
	}




	main {
		margin: auto;
		width: 100%;
		margin-bottom: -15px;

		/* position: relative; */
	}

	#panel {
		margin: auto;
		width: 385px;
		height: 142px;
		border-right: solid 1px #1E3765;
		border-top: solid 1px #1E3765;
		border-top-right-radius: 25px;
		float: left;
		z-index: 99;
		background-color: rgb(250, 250, 250);
		bottom: 0;
		position: absolute;
		opacity: 0.9
		/* display: none; */
	}

	#title {
		max-width: 600px;
		margin-left: 20px;
		margin-right: 20px;
		padding-bottom: 8px;
		margin-bottom: 0px;
	}

	#title h1 {
		font-family: TradeGothicBold, sans-serif;
		font-size: 20px;
		color: #1E3765
	}

	#title p {
		margin-top: -5px;
		color: rgb(70, 70, 70);
		font-family: Roboto, sans-serif;
		font-size: 12px;
		line-height: 1.75;
	}

	#bold {
		color: black;
		font-weight: bold;
		font-size: 14px;
	}

	#more-less {
		height: 20px;
		margin: 0px;
		padding: 0px;
		padding-bottom: -5px;		
		margin-top: -15px;
		padding-left: 20px;
		padding-right: 20px;
		border-top: solid 1px #1E3765;
		/* border-bottom: solid 1px #1E3765; */
		font-family: Roboto, sans-serif;
		font-size: 12px;
		background-color: rgb(225, 225, 225);
		text-align: center;
	}
	#more-less:hover {
		cursor: pointer;
		background-color: #F1C500;
	}

	#more-less p {
		color: #1E3765;
		font-family: Roboto, sans-serif;
		padding: 0px;
		margin: 0px;
	}

	#text {
		display: none;
		max-width: 600px;
		line-height: 1.5;
		margin-left: 20px;
		margin-right: 20px;
		color: rgb(70, 70, 70);
	}

	#map {
		margin-top: 50px;
		height: calc(100vh - 50px);
		width: 100%;
		top: 0;
        left: 0;
		position: absolute;
		z-index: -99;
	}

	
</style>
