<script>
	import { onMount } from 'svelte'
	import mapboxgl from "mapbox-gl";
	import Typeahead from "svelte-typeahead";
	import Places from "./assets/places.geo.json";
	import Info from "./lib/Info.svelte";
	import Select from "./lib/Select.svelte"
	import Top from "./lib/Top.svelte"

	mapboxgl.accessToken = 'pk.eyJ1Ijoic2Nob29sb2ZjaXRpZXMiLCJhIjoiY2w3aml0dHdlMHlpazNwbWh0em4xOHNlaCJ9.fXNtPGq0DqYiFvPH6p4fjQ';

	const data = Places.features;

	let map;
	let ctuid = "0";

	let pageWidth;
	
	onMount(() => {
		map = new mapboxgl.Map({
			container: 'map', 
			style: 'mapbox://styles/schoolofcities/cl7j75gbd003b14ocub8skc7c',
			center: [-79.45, 43.65], 
			zoom: 10,
			maxZoom: 12,
			minZoom: 5,
			projection: 'globe',
			scrollZoom: true,
			attributionControl: false
		});
		
		
		map.addControl(new mapboxgl.AttributionControl({
			customAttribution: 'Map by <a href="http://jamaps.github.io/about.html">Jeff Allen</a>'
		}), 'bottom-right');
		map.addControl(new mapboxgl.NavigationControl(), 'top-right');

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

			} else {
				map.setPaintProperty('ct_fill', 'fill-color', '#fff')
				ctuid = '0'
			}

		});

	});

	

	function placeClick(city) {
		ctuid = "0";
		map.setPaintProperty('ct_fill', 'fill-color', '#fff');
		map.panTo(city.original.geometry.coordinates);
		map.zoonTo(10);
	}


</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
	<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">

	<link href='https://api.mapbox.com/mapbox-gl-js/v2.10.0/mapbox-gl.css' rel='stylesheet' />
	<link href='popupStyle.css' rel='stylesheet' />
</svelte:head>


<main>

<Top/>

<div id='map-wrapper' class="{pageWidth < 755 ? 'maps-small' : 'maps-big'}" >
	<!-- class="{pageWidth < 755 ? 'maps-small' : 'maps-big'}" -->
<div id="map" bind:offsetWidth={pageWidth} ></div>
</div>

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

<Select ctuid={ctuid}/>

<Info pageWidth={pageWidth}/>













</main>


<style>
	
	
	@font-face {
		font-family: TradeGothicBold;
		src: url("./assets/Trade Gothic LT Bold.ttf");
	}
	:root {
		font-family: 'Roboto', sans-serif;
	}


	main {
		margin: auto;
		width: 100%;
		margin-bottom: -15px;
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
		width: 260px;
		top: 62px;
		left: 5px;
		z-index: 99;
		opacity: 0.93;
	}

	#map-wrapper {
		margin-top: 50px;
		/*  height: calc(100vh - 50px); */
		width: 100%;
		top: 0;
        left: 0;
		position: absolute;
		z-index: -99;
	}

	#map {
		/* margin-top: 50px; */
		height: 100%;
		width: 100%;
		top: 0;
        left: 0;
		position: absolute;
		z-index: -99;
	}

	.maps-big {
		height: calc(100vh - 50px);
	}

	.maps-small {
		height: calc(100vh - 255px - 50px);
	}

	
	
</style>
