
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="googlebot" content="noindex">

<!-- Navbar -->
<div id="navbar">
	<a class="active" href="javascript:void(0)">Home</a>
	<a href="#about">About</a>
	<a href="#projects">Projects</a>
	<a href="#archive">Archive</a>
	<a href="#contact">Contact</a>
</div> 

<!-- Header/Title -->
<div id="home" class="title-image"></div> 

<!-- Quote -->
<div class="green-container">
	<div class="w3-panel w3-leftbar">
		<p><i class="fa fa-quote-right w3-xxlarge"></i><br>
		<i class="w3-serif w3-xlarge">
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut non massa vitae risus fermentum ullamcorper. Phasellus risus urna, ornare in aliquam id, porttitor sit amet sapien. Nulla facilisi.</i></p>
		<p>Nietsie Trebla</p>
  </div>
</div>	

<!-- ? -->
<div class="white-container">
	<h1 id="about" style="text-align:center">Why Fuck Cliff?</h1>
	<div class="table1">
		<div class="column">
			<img src="img/col1.png">
			<div>
				<h2>Simplicity</h2>	
				<p> It's quick, efficient, and affordable.</p>
			</div>	
		</div>
		<div class="column">
			<img src="img/col2.png">
			<div>
				<h2>Peer to Peer</h2>	
				<p>It's watching.</p>
			</div>	
		</div>
		<div class="column">
			<img src="img/col3.png">
			<div>
				<h2>Strategic</h2>	
				<p> Just fucking do it.</p>
			</div>	
		</div>
	</div>
</div>	


<!-- Projects-->
<div class="green-container">
	<h1 id="projects"></h1>
</div>

<!-- Archive-->
<div class="white-container" style="text-align:center">
	<h1 id="archive">See what started it all.</h1>
	<a href="archive/v1/index.html">Load Archive</a>
</div>

<!-- Footer-->
<div class="green-container">
	<h4 id="contact"></h4>
</div>

<script>
</script>


<style>
	/*Navbar CSS*/
	#navbar {
		position: fixed;
		background-color: #333;
		overflow: hidden;
		width: 100%;
		top: 0;
		z-index: 999;
	}
	#navbar a {
		float: left;
		color: #f2f2f2;
		text-align: center;
		padding: 14px 16px;
		text-decoration: none;
		font-size: 17px;
	}
	#navbar a:hover {
		background-color: #ddd;
		color: black;
	}
	#navbar a.active {
		background-color: #4CAF50;
		color: white;
	}
	.sticky {
		position: fixed;
		top: 0;
		width: 100%;
	}
	.sticky + .content {
		padding-top: 60px;
	}
	.content {
		padding: 16px;
	}

	/*Title CSS*/
	.title-image {
		background-image: url(img/logoW.png), linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("img/background1-min.jpg");
		height: 100%;
		background-position: center center;
		background-repeat: no-repeat;
		background-attachment: fixed;
		background-size: auto,  cover, cover, cover;
	}


	/*Quote*/
	.green-container {
		background-color: #19974a;
		color: white;
		padding: 20px;
		color: white;
	}
	.white-container {
		background-color: white;
		color: black;
		padding: 20px;
	}


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
