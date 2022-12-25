<script lang="ts">
	import '../app.css';
	const minutesToSeconds = (minutes: number) => minutes * 60;
	const secondsToMinutes = (seconds: number) => Math.floor(seconds / 60);
	const padWithZeroes = (number: number) => number.toString().padStart(2, '0');

	const longBreakSeconds = minutesToSeconds(20);
	const shortBreakSeconds = minutesToSeconds(5);
	let completedPomodoros = 0;

	// length of a pomodoro in seconds
	const POMODORO_S = minutesToSeconds(25);

	// time left in the current pomodoro
	let pomodoroTime = POMODORO_S;

	const State = { idle: 'idle', inProgress: 'in progress', resting: 'resting' };
	let currentState = State.idle;

	export let activeTask;

	function formatTime(timeSeconds: number) {
		const minutes = secondsToMinutes(timeSeconds);
		const remainingSeconds = timeSeconds % 60;
		return `${padWithZeroes(minutes)}:${padWithZeroes(remainingSeconds)}`;
	}
	let interval: string | number | NodeJS.Timer | undefined;
	function startPomodoro() {
		currentState = State.inProgress;
		interval = setInterval(() => {
			if (pomodoroTime === 0) {
				completePomodoro();
			}
			pomodoroTime -= 1;
		}, 1000);
	}
	function completePomodoro() {
		clearInterval(interval);
		activeTask.actualPomodoros++;
		completedPomodoros++;
		if (completedPomodoros === 4) {
			rest(longBreakSeconds);
			completedPomodoros = 0;
		} else {
			rest(shortBreakSeconds);
		}
	}
	function rest(time: number) {
		currentState = State.resting;
		pomodoroTime = time;
		interval = setInterval(() => {
			if (pomodoroTime === 0) {
				idle();
			}
			pomodoroTime -= 1;
		}, 1000);
	}
	function idle() {
		currentState = State.idle;
		clearInterval(interval);
		pomodoroTime = POMODORO_S;
	}
	function endPomodoro() {
		idle();
	}
</script>

<div class="grid justify-items-center items-center h-screen">
	<div
		class="grid grid-cols-4 justify-items-center items-center bg-white border rounded-lg shadow-xl w-9/12 h-3/4 "
	>
		<div class="col-span-4 text-8xl">Pomodoro Timer</div>
		<div class="col-span-4">
			<p class="text-9xl">{formatTime(pomodoroTime)}</p>
		</div>
		<div class="col-start-2 col-span-2">
			<button
				class="bg-dg px-6 py-2 text-3xl rounded-full hover:bg-lg"
				on:click={startPomodoro}
				disabled={currentState !== State.idle || !activeTask}>Start time</button
			>
			<button
				class="bg-dg px-6 py-2 text-3xl rounded-full hover:bg-lg"
				on:click={endPomodoro}
				disabled={currentState !== State.inProgress || !activeTask}
				>End time</button
			>
		</div>
	</div>
</div>
