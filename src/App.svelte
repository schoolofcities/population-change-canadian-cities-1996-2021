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
			projection: 'globe' 
		});

		map.addControl(new mapboxgl.NavigationControl());
		map.addControl(new mapboxgl.FullscreenControl());
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

<div id="zoom">
	<button on:click={mapZoom}>
		click
	</button>
</div>

<div id="map"></div>


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

	#zoom {
		height: 50px;
	}

	#map {
		height: 750px;
	}
</style>
