<style>
	.table1 {
		display: table;
		table-layout: fixed; /*euqal column width*/
		width: 100%;
	}
	.column{
		display: table-cell;
		text-align: center;
		border: 0px solid;
		padding: 10px;
	}
	.column img{
		width: 180px; /* you can use % */
		height: auto;
	}

	@media screen and (max-width: 600px) {
		.column {
			display: block;
		}
	}
</style>

<svelte:head>
	<title>About</title>
</svelte:head>

<!-- ? -->
<div class="white-container">
	<h1 id="about" style="text-align:center">Why Fuck Cliff?</h1>
	<div class="table1">
		<div class="column">
			<img src="col1.png">
			<div>
				<h2>Simplicity</h2>	
				<p> It's quick, efficient, and affordable.</p>
			</div>	
		</div>
		<div class="column">
			<img src="col2.png">
			<div>
				<h2>Peer to Peer</h2>	
				<p>It's watching.</p>
			</div>	
		</div>
		<div class="column">
			<img src="col3.png">
			<div>
				<h2>Strategic</h2>	
				<p> Just fucking do it.</p>
			</div>	
		</div>
	</div>
</div>	
