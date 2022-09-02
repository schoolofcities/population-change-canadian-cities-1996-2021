<script>
	import { onMount } from 'svelte'
	import mapboxgl from "mapbox-gl";
	// import 'mapbox-gl/dist/mapbox-gl.css';

	mapboxgl.accessToken = 'pk.eyJ1Ijoic2Nob29sb2ZjaXRpZXMiLCJhIjoiY2w3aml0dHdlMHlpazNwbWh0em4xOHNlaCJ9.fXNtPGq0DqYiFvPH6p4fjQ';

	let map;
	
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

	function mapZoom() {
		map.zoomTo(12)
	}

</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
	<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">

	<link href='https://api.mapbox.com/mapbox-gl-js/v2.10.0/mapbox-gl.css' rel='stylesheet' />
</svelte:head>

<div id="title">

	
</div>

<div id="text">
	<p>
		Canadian urban regions have undergone substantial change over the the past several decades. In the map below we visualize by neighbourhood (represented by census tracts) whether the population has grown (QQQ) or declined (QQQ) between 1996 and 2021. Despite the total population across the 33 urban regions increasing by QQQQQ, QQQQ% of neighbourhoods witnessed population loss. A general trend is sprawling population growth in the suburban fringes and concentrated development in central nodes, with population decline occurring in many older pre-1996 residential neighbourhoods, but this isn't evident everywhere. Explore the map below to see more.
	</p>
</div>

<div id="zoom">
	<button on:click={mapZoom}>
		click
	</button>
</div>

<div id="map"></div>

<div id="text"></div>


<style>
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

	#text {
		margin: auto;
		width: 600px;
		line-height: 1.5;
		
	}

	#zoom {
		height: 50px;
	}

	#map {
		height: calc(100vh - 80px);
		border-top: solid 1px grey;
		border-bottom: solid 1px grey;
	}
</style>
