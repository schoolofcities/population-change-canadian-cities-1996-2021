<script>
	import { onMount } from 'svelte'
	import mapboxgl from "mapbox-gl";
	import Typeahead from "svelte-typeahead";
	import data from "./lib/cities.js";

	mapboxgl.accessToken = 'pk.eyJ1Ijoic2Nob29sb2ZjaXRpZXMiLCJhIjoiY2w3aml0dHdlMHlpazNwbWh0em4xOHNlaCJ9.fXNtPGq0DqYiFvPH6p4fjQ';

	let map;
	let city = "Toronto"

	let events = [];
	
	onMount(() => {
		map = new mapboxgl.Map({
			container: 'map', 
			style: 'mapbox://styles/schoolofcities/cl7j75gbd003b14ocub8skc7c',
			center: [-79.45, 43.65], 
			zoom: 10, // starting zoom
			maxZoom: 12,
			minZoom: 9,
			projection: 'globe',
			scrollZoom: false
		});

		map.addControl(new mapboxgl.NavigationControl(), 'top-left');
		map.addControl(new mapboxgl.FullscreenControl(), 'top-right');
	});

	function mapPan(city) {
		console.log(city)
		map.zoomTo(10)
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

<div id="panel">

	<div id="title">
		<h1>25 Years of Population Growth & Decline in Canadian Cities</h1>
		<p>Visualizing neighbourhood change from 1996 to 2021</p>
	</div>

	<div id="text">
		<p>
			Canadian urban regions have undergone substantial changes over the the past several decades. In the maps below we visualize by neighbourhood (represented by census tracts) whether the population has grown (QQQ) or declined (QQQ) between 1996 and 2021. The total population across these 33 urban regions increased from X to Y, but this growth was uneven, with QQQQ% of neighbourhoods experiencing population loss. 
		</p>
	</div>
	<div id="text">
		<p>	
			The maps show a general trend of population growth both in the suburban fringes and concentrated in some downtowns, with population decline occurring in many older pre-1996 residential neighbourhoods. But these trends aren't evident everywhere. Click and explore below:
		</p>
	</div>

	<div id="text">
		<Typeahead
			{data}
			label="Select a city to zoom to:"
			placeholder={`Search`}
			extract={(item) => item.city}
			disable={(item) => /Carolina/.test(item.city)}
			on:select={({ detail }) => map.panTo([detail.original.x,detail.original.y])}
			on:clear={() => events = [...events, "clear"]}
		/>
	</div>	



</div>

<div id="map"></div>

</main>


<style>

	:global([data-svelte-search] listbox) {
		width: 100%;
		font-size: 12px;
		padding: 0.5rem;
		margin: 0.5rem 0;
		border: 1px solid #e0e0e0;
		border-radius: 0.25rem;
	}
	
	@font-face {
		font-family: TradeGothicBold;
		src: url("./assets/Trade Gothic LT Bold.ttf");
	}
	:root {
		font-family: 'Roboto', sans-serif;
	}
	:global(body) {
		padding: 0px;
		margin: 0px;
		background-color: #fff;
	}

	main {
		margin: auto;
		width: 100%;
	}

	#panel {
		margin: auto;
		width: 499px;
		height: 100vh;
		border-right: solid 1px #1E3765;
		float: left;
	}

	#title {
		max-width: 600px;
		margin-left: 20px;
		margin-right: 20px;
		border-bottom: solid 1px #1E3765;
		padding-bottom: 7px;
	}

	#title h1 {
		font-family: TradeGothicBold, sans-serif;
		font-size: 28px;
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
		border-left: solid 1px #1E3765;
		padding-left: 20px;
		margin-left: 20px;
		margin-right: 20px;
		color: #1e3765bd
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
		width: calc(100vw - 500px);
	}
</style>
