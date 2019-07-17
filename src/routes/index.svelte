<script>
  export let segment;
</script>

<style>
  .title-container{
    position: center;
  }

  #logo {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  #title-image{
      opacity: 0.8;
      filter: brightness(50%);
      padding: 0;
      display: block;
      margin: 0 auto;
      max-height: 100%;
      max-width: 100%;
  }
</style>

<svelte:head>
  <title>Fuck Cliff</title>
</svelte:head>

<div class="title-container">
  <img src="background1-min.jpg" id="title-image" alt="Gussy">
  <img src="logoW.png" id="logo" alt="Fuck Cliff">
</div>  

<p>copyright</p>
<p>contact us</p>
