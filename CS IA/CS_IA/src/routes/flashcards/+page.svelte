<script>
	let title = 'il Pomodoro';
	import TaskList from '../../components/tasklist.svelte';
	import PomodoroTimer from '../../components/timer.svelte';
	import NavBar from '../../components/nav_bar.svelte';
	import Flashcards from '../../components/flashcards.svelte';
	import { goto } from '$app/navigation';
	import { isAuthenticated, signOut } from '../../stores/auth';
	import { onMount } from 'svelte';

	onMount(() => {
		if (!$isAuthenticated) {
			goto('/sign_in');
		}
	});
</script>

<main>
	<NavBar />
	<Flashcards />
</main>
