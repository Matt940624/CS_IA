<script>
	let title = 'il Pomodoro';
	import TaskList from '../../components/tasklist.svelte';
	import PomodoroTimer from '../../components/timer.svelte';
	import Navbar from '../../components/nav_bar.svelte';
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
	<Navbar />
	<TaskList />
</main>
