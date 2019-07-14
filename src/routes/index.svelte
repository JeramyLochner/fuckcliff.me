<script>
	export let segment;
</script>

<style>
	/*Title CSS*/
	.title-image {
		background-image: url('logoW.png'), linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("background1-min.jpg");
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
</style>

<svelte:head>
	<title>Fuck Cliff - Go Fuck Yourself</title>
</svelte:head>

<!-- Header/Title -->
<div class="title-image"></div> 

<!-- Quote -->
<div class="green-container">
	<div class="w3-panel w3-leftbar">
		<p><i class="fa fa-quote-right w3-xxlarge"></i><br>
		<i class="w3-serif w3-xlarge">
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut non massa vitae risus fermentum ullamcorper. Phasellus risus urna, ornare in aliquam id, porttitor sit amet sapien. Nulla facilisi.</i></p>
		<p>Nietsie Trebla</p>
  </div>
</div>	


