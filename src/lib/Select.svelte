<script>

    import ct from "../assets/ct-pts.geo.json";

    export let ctuid;

    let pop21 = 0;
    let pop96 = 0;
    let radius = 1;
    let stroke = "#fff";
    let fill = "#fff";

    $: data = ct.features.filter(ct => ct.properties.ctuid === ctuid)[0];

    $: if (data) {
        pop21 = data.properties.pop21;
        pop96 = data.properties.pop96;
        if (pop21 > pop96) {
            radius = 1 + 2 * ((pop21 - pop96) / 250) ** 0.5
            stroke = '#007fa3'
            fill = '#6fc7ea'
        } 
        else if (pop96 > pop21) {
            radius = 1 + 2 * ((pop96 - pop21) / 250) ** 0.5
            stroke = '#dc4633'
            fill = '#ff5842'
        } else {
            radius = 1;
            stroke = "#fff";
            fill = "#fff";
        }
    } else {
        pop21 = 0;
        pop96 = 0;
    }

</script>


<div id="select" class="{ctuid !== "0" ? 'show' : 'empty'}">
	<div id="yellow"></div>

    <div id="info">
        <div id="circle">
            <svg width="60" height="60">
                <rect width="60" height="60" style="fill-opacity:1; stroke-width:2; stroke:#8d6d6d; fill:#F1C500" />
                {#if data}
                <circle cx="30" cy="30" r={radius} stroke-width="1" stroke={stroke} fill={fill} />
                {/if}
            </svg>            
        </div>
        <div id="data">
            {#if data}
                <p>Population 2021: <span id="bold">{pop21.toLocaleString("en-US")}</span></p>
                <p>Population 1996: <span id="bold">{pop96.toLocaleString("en-US")}</span></p>
                <p>Difference: <span id="bold">{(pop21 - pop96).toLocaleString("en-US")}</span></p>
            {:else}
                <p>Missing data</p>
            {/if}

        </div>
    </div>
</div>



<style>
    #select {
		position: absolute;
		width: 255px;
        height: 90px;
		background-color: #fff;
		border: solid 2px rgb(225, 225, 225);
		border-radius: 4px;
		top: 107px;
		left: 6px;
		z-index: 1;
		opacity: 0.93;
	}
    .empty {display:none}
    #select p {
		padding-left: 10px;
		color: rgb(70, 70, 70);
		font-family: Roboto, sans-serif;
		font-size: 13px;
		line-height: 0.75;
	}
	#yellow {
		width: 100%;
		height: 3px;
		padding-top: 4px;
		background-color: #F1C500;
	}
	#circle {
        float:left;
        height: 60px;
        width: 60px;
        background-color: red;
        margin-left: 15px;
        margin-right: 10px;
    }
    #data {
        text-align: right;
        margin-right: 20px;
    }
    #bold {
        font-weight: bold;
        color: black;
    }
</style>
