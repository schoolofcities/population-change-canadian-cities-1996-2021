<script>
	import { onMount } from 'svelte'
	import mapboxgl from "mapbox-gl";
	// import 'mapbox-gl/dist/mapbox-gl.css';

	mapboxgl.accessToken = 'pk.eyJ1Ijoic2Nob29sb2ZjaXRpZXMiLCJhIjoiY2w3aml0dHdlMHlpazNwbWh0em4xOHNlaCJ9.fXNtPGq0DqYiFvPH6p4fjQ';
	
	onMount(() => {
		const map = new mapboxgl.Map({
		container: 'map', // container ID
		style: 'mapbox://styles/schoolofcities/cl7j75gbd003b14ocub8skc7c', // style URL
		center: [-79.45, 43.65], // starting position [lng, lat]
		zoom: 10, // starting zoom
		projection: 'globe' // display the map as a 3D globe
		});
		// map.on('style.load', () => {
		// map.setFog({}); // Set the default atmosphere style
		// });
	});



</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
	<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">

	<link href='https://api.mapbox.com/mapbox-gl-js/v2.10.0/mapbox-gl.css' rel='stylesheet' />
</svelte:head>

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

	#map {
		height: 100vh;
	}
</style>
