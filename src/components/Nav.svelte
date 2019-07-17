<script>
  export let segment;
</script>

<style>
  nav {
    position: fixed;
    top: 0;
    width: 100%;
    border-bottom: 1px solid var(--m-black);
    background: var(--m-black);
    font-weight: 300;
    padding: 0 1em;
    z-index: 999
  }

  ul {
    margin: 0;
    padding: 0;
  }

  ul::after {
    content: '';
    display: block;
    clear: both;
  }

  li {
    display: block;
    float: left;
  }

  .selected {
    position: relative;
    display: inline-block;
  }

  .selected::after {
    position: absolute;
    content: '';
    width: calc(100% - 1em);
    height: 2px;
    background-color: var(--m-orange);
    display: block;
    bottom: -1px;
  }

  a {
    text-decoration: none;
    padding: 1em 0.5em;
    display: block;
    background: var(--m-black);
    color: var(--m-white);
  }
</style>

<nav>
  <ul>
    <li><a class='{segment === undefined ? "selected" : ""}' href='.'>home</a></li>
    <li><a rel=prefetch class='{segment === "about" ? "selected" : ""}' href='about'>about</a></li>
    <li><a rel=prefetch class='{segment === "projects" ? "selected" : ""}' href='projects'>projects</a></li>
    <li><a rel=prefetch class='{segment === "news" ? "selected" : ""}' href='news'>news</a></li>
  </ul>
</nav>