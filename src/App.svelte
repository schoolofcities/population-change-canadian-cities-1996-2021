<script>
	import { onMount } from 'svelte'
	import mapboxgl from "mapbox-gl";

	mapboxgl.accessToken = 'pk.eyJ1Ijoic2Nob29sb2ZjaXRpZXMiLCJhIjoiY2w3aml0dHdlMHlpazNwbWh0em4xOHNlaCJ9.fXNtPGq0DqYiFvPH6p4fjQ';

	let map;
	let city = "Toronto"
	
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

</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin> 
	<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">

	<link href='https://api.mapbox.com/mapbox-gl-js/v2.10.0/mapbox-gl.css' rel='stylesheet' />
</svelte:head>

<main>

<div id="title">
	<h1>25 Years of Population Growth & Decline in Canadian Cities</h1>
	<p>Visualizing neighbourhood change from 1996 to 2021</p>
</div>

<div id="text">
	<p>
		Canadian urban regions have undergone substantial changes over the the past several decades. In the maps below we visualize by neighbourhood (represented by census tracts) whether the population has grown (QQQ) or declined (QQQ) between 1996 and 2021. The total population across the 3X urban regions increased from X to Y, but this growth was uneven, with QQQQ% of neighbourhoods experiencing population loss. 
	</p>
</div>
<div id="text">
	<p>	
		The maps show a general trend of population growth both in the suburban fringes and concentrated in some downtowns, with population decline occurring in many older pre-1996 residential neighbourhoods. But these trends aren't evident everywhere. Click on a city to zoom to it.
	</p>
</div>

<div id="text">
	<p>
		<span id="cityZoom" on:click={mapPan}>Victoria</span> |
		<span id="cityZoom" on:click={mapPan}>Vancouver</span> | 
		<span id="cityZoom" on:click={mapPan}>Kamploops</span> |
		<span id="cityZoom" on:click={mapPan}>Kelowna</span>

	</p>
</div>

</main>




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

	main {
		margin: auto;
		max-width: 600px;
	}

	#title {
		max-width: 600px;
		margin-left: 20px;
		margin-right: 20px;
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
		border-left: solid 1px grey;
		padding-left: 20px;
		margin-left: 20px;
		margin-right: 20px;
		color: #454545
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
		height: calc(100vh - 80px);
		border-top: solid 1px grey;
		border-bottom: solid 1px grey;
	}
</style>
