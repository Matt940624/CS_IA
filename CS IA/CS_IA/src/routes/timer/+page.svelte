<script>
	let title = 'il Pomodoro';
	import TaskList from '../../components/tasklist.svelte';
	import PomodoroTimer from '../../components/timer.svelte';
	import NavBar from '../../components/nav_bar.svelte';
	import Tasklist from '../../components/tasklist.svelte';
	import { goto } from '$app/navigation';
	import { isAuthenticated, signOut } from '../../stores/auth';
	import { onMount } from 'svelte';

	onMount(() => {
		if (!$isAuthenticated) {
			goto('/sign_in');
		}
	});

	/**
	 * @type {any}
	 */
	let activeTask;
	/**
	 * @param {{ detail: { task: any; }; }} event
	 */
	function updateActiveTask(event) {
		activeTask = event.detail.task;
	}
</script>

<main>
	<NavBar />
	<div class="snap-y">
		<div class="snap-center">
			<PomodoroTimer {activeTask} />
		</div>
		<div class="snap-center">
			<Tasklist on:taskSelected={updateActiveTask} />
		</div>
	</div>
</main>
