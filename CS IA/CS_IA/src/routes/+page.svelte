<script>
	let title = 'il Pomodoro';
	import NavBar from '../components/nav_bar.svelte';
	import { goto } from '$app/navigation';
	import { isAuthenticated, signOut } from '../stores/auth';
	import { onMount } from 'svelte';

	onMount(() => {
		if (!$isAuthenticated) {
			goto('/sign_in');
		}
	});
</script>

<main>
	<NavBar />
	<div
		class="grid grid-cols-4 justify-items-center items-center place-items-center"
	>
		<br />
		<br />
		<div class="text-7xl grid col-span-4">Get Started Now!</div>
		<br />
		<br />
		<br />
		<div class="grid col-span-4">
			<button
				on:click={() => goto('/tasklist')}
				class="text-white bg-gb hover:bg-lb focus:ring-4 focus:outline-none focus:ring-db font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-db dark:hover:bg-db dark:focus:ring-db"
				>Add your first Task</button
			>
		</div>
	</div>
</main>
