<script>
    import Circle from "./circle.svelte";
    import Legend from "./Legend.svelte";
    function hideShow() {
		console.log("meow")
	}

    export let pageWidth;

</script>



<div id="panel" class="{pageWidth < 755 ? 'mobile' : 'web'}">

	<div id="title">
		<h1>25 Years of Population Growth & Decline in Canadian Cities</h1>

		<p>
			<p>Visualizing by neighbourhood census tracts how the population has increased <Circle stroke="#007FA3" fill="#6FC7EA"/> or decreased <Circle stroke="#dc4633" fill="#ff5842"/> between <span id="bold">1996</span> and <span id="bold">2021</span>. <br> The area of the circles are proportional to the growth or decline in population in each neighbourhood:

		</p>

        <Legend/>
        
	</div>

	<a href="https://github.com/schoolofcities/population-change-canadian-cities-1996-2021/">
		<div id="more-less" >
			<p>click here to read more</p>
		</div>
	</a>

</div>


<style>
    #panel {
		margin: auto;
        height: 256px;
		border-top: solid 1px #1E3765;
		float: left;
		z-index: 9;
		background-color: rgb(250, 250, 250);
		bottom: 0;
        left: 0;
		position: absolute;
		opacity: 0.9;
	}
    .mobile {
        width: 100%;
        border-top-right-radius: 0px;
        border-right: none;
    }
    .web {
        width: 335px;
        height: 255px;
		border-right: solid 1px #1E3765;
		border-top-right-radius: 25px;
    }

	#title {
		max-width: 550px;
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
        border-bottom: solid 1px #1E3765;
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
	
	a {
		text-decoration: none;
	}

</style>