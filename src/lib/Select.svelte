<script>
    export let ctuid;
</script>


<div id="select">
	<div id="yellow"></div>
	<p>Selected Census Tract: {ctuid}</p>
	<p>Population 2021: </p>
	<p>Population 1996: </p>
</div>



<style>
    #select {
		position: absolute;
		width: 295px;
		background-color: #fff;
		border: solid 2px rgb(225, 225, 225);
		border-radius: 4px;
		top: 97px;
		right: 6px;
		z-index: 1;
		opacity: 0.93;
	}
	#yellow {
		width: 100%;
		height: 3px;
		padding-top: 4px;
		background-color: #F1C500;
	}
	#select p {
		/* margin-top: 5px; */
		padding-left: 10px;
		color: rgb(70, 70, 70);
		font-family: Roboto, sans-serif;
		font-size: 13px;
		line-height: 0.75;
	}
</style>
