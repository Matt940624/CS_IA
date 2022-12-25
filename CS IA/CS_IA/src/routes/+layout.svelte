<script lang="ts">
	import Nav from '../components/nav_bar.svelte';
	import Sign_In from '../../src/routes/sign_in/+page.svelte';
</script>

<main>
	<slot><Sign_In /></slot>
</main>
