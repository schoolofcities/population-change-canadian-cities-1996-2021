<script>
    import Circle from "./circle.svelte";
    import Legend from "./Legend.svelte";
    function hideShow() {
		console.log("meow")
	}
</script>



<div id="panel">

	<div id="title">
		<h1>25 Years of Population Growth & Decline in Canadian Cities</h1>

		<p>
			<p>Visualizing by neighbourhood census tracts how the population has increased <Circle stroke="#007FA3" fill="#6FC7EA"/> or decreased <Circle stroke="#dc4633" fill="#ff5842"/> between <span id="bold">1996</span> and <span id="bold">2021</span>. The area of the circles are proportional to the number of people who moved in or moved out of each neighbourhood.

		</p>

        <Legend/>
        
	</div>

	<div id="more-less" on:click={hideShow}>
		<p>click here to read more</p>
	</div>
	
	<!-- <div id="text">
		<p>
			The total population across these 33 urban regions increased from X to Y, but this growth was uneven, with QQQQ% of neighbourhoods experiencing population loss. 
		</p>
	
		<p>	
			The area of the circles are proportional to the number of people who moved in or moved out of each neighbourhood.
		</p>
	
		<p>	
			Click on the map to view numbers for a specific neighbourhood. 
		</p>
	</div> -->

</div>


<style>
    #panel {
		margin: auto;
		width: 335px;
		height: 255px;
		border-right: solid 1px #1E3765;
		border-top: solid 1px #1E3765;
		border-top-right-radius: 25px;
		float: left;
		z-index: 99;
		background-color: rgb(250, 250, 250);
		bottom: 0;
        left: 0;
		position: absolute;
		opacity: 0.9;
	}

	#title {
		max-width: 600px;
		margin-left: 20px;
		margin-right: 20px;
		padding-bottom: 8px;
		margin-bottom: 0px;
	}

	#title h1 {
		font-family: Roboto, sans-serif;
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

</style>