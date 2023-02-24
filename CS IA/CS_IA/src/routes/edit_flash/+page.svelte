<script>
	let title = 'il Pomodoro';
	import NavBar from '../../components/nav_bar.svelte';
	import PomodoroTimer from '../../components/timer.svelte';
	import FlashcardEdit from '../../components/flashcardEdit.svelte';
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
	<FlashcardEdit />
</main>
