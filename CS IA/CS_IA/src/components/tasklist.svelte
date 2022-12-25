<script>
	import '../app.css';
	import { afterUpdate } from 'svelte';
	import { Task } from '../components/task.js';
	import {
		construct_svelte_component,
		createEventDispatcher,
	} from 'svelte/internal';

	const dispatch = createEventDispatcher();
	let title = 'Tasklist';
	let taskFocus = false;
	/**
	 * @type {HTMLInputElement}
	 */
	let lastInput;

	// @ts-ignore
	/**
	 * @type {Task}
	 */
	let activeTask;

	let tasks = [
		new Task('finish CS IA'),
		new Task('finish CS documentation'),
		new Task('get into MIT'),
	];
	$: allPomodoros = tasks.reduce((acc, t) => acc + t.expectedPomodoros, 0);
	function addTask() {
		tasks = tasks.concat(new Task());
		console.log(tasks);
		// for debugging why tasks are not being appended
		// the list should grow everytime the function is called
	}
	/**
	 * @param {Task} task
	 */
	function deleteTask(task) {
		const index = tasks.indexOf(task);
		tasks = [...tasks.slice(0, index), ...tasks.slice(index + 1)];
		// could make it more abstract at add attray extension js file for reusability
		// @ts-ignore
		if (activeTask === task) {
			// @ts-ignore
			selectTask(undefined);
		}
	}

	function focusonTask() {
		if (taskFocus && lastInput) {
			lastInput.focus();
			taskFocus = false;
		}
	}
	afterUpdate(focusonTask);
	afterUpdate(() => {
		console.log('I was updated!');
	});

	/**
	 * @param {Task} task
	 */
	function selectTask(task) {
		activeTask = task;
		console.log(activeTask);
		dispatch('taskSelected', {
			task: activeTask,
		});
	}
</script>

<div class="grid justify-items-center items-center h-screen">
	<div
		class="grid grid-cols-4 justify-items-center items-center bg-white border rounded-lg shadow-xl w-9/12 h-3/4 "
	>
		<div class="col-span-4 text-8xl">{title}</div>
		<div class="col-span-4">
			{#if tasks.length === 0}
				<div class="text-xl">
					You are slackin off my man! Add some tasks and start working!
				</div>
			{/if}
		</div>
		<div class="col-span-4 ">
			<ul>
				{#each tasks as task}
					<li class:active={activeTask === task}>
						<button
							class="rounded-lg bg-lb px-4 py-2"
							on:click={() => selectTask(task)}>&gt;</button
						>
						<input
							type="text"
							bind:value={task.description}
							bind:this={lastInput}
							class="min-w-[400px]  "
						/>
						<input
							class="max-w-[100px] "
							type="number"
							bind:value={task.expectedPomodoros}
						/>
						<input
							class="pomodoros small"
							bind:value={task.actualPomodoros}
							disabled
						/>
						<button
							class="bg-lg rounded-full px-4   "
							on:click={() => deleteTask(task)}>X</button
						>
					</li>
				{/each}
			</ul>
		</div>
		<div class="col-span-2 col-start-2">
			<button
				class="bg-dg px-6 py-2 text-md rounded-lg hover:bg-lg"
				on:click={addTask}>Add New Tasks</button
			>
		</div>
		<div class="col-span-2 col-start-2">
			{#if tasks.length != 0}
				<div class="col-start-2 col-span-2 text-xl">
					Complete {allPomodoros} Pomodoro today.
				</div>
			{/if}
		</div>
	</div>
</div>

<style>
	.active input,
	.active button {
		border-color: #c7d5e0;
		background-color: #c7d5e0;
		color: black;
		transition: background-color 0.2s, color 0.2s, border-color 0.2s;
	}
	.pomodoros.small {
		max-width: 40px;
		text-align: center;
	}
	.active input[disabled] {
		opacity: 0.6;
	}
</style>
