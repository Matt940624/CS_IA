<script lang="ts">
	import '../../app.css';
	import axios from 'axios';
	import { goto } from '$app/navigation';

	import { sineIn } from 'svelte/easing';
	let hidden2 = true;
	let spanClass = 'flex-1 ml-3 whitespace-nowrap';
	let transitionParams = {
		x: -320,
		duration: 200,
		easing: sineIn,
	};
	function check_psw() {
		var pw1 = (<HTMLInputElement>document.getElementById('psw')).value;
		var pw2 = (<HTMLInputElement>document.getElementById('rpsw')).value;
		if (pw1 == '' || pw2 == '') {
			return;
		}
		if (pw1 != pw2) {
			alert('Password did not match');
		} else {
			alert('password created successfully');
		}
	}
	let username = '',
		email = '',
		password = '';

	async function submit(e: Event) {
		e.preventDefault();

		axios
			.post('http://localhost:8000/api/register', { username, email, password })
			.then((response) => {
				console.log('received response', response);
				if (response.status === 200) goto('/sign_in');
			})
			.catch((error) => {
				console.log(error);
			});
	}
</script>

<div class="grid grid-cols-5 gap-2">
	<div
		class="col-span-3 justify-center justify-items-center grid grid-cols-1 content-center"
	>
		<div class="text-5xl mb-6">Sign Up</div>
		<form class="w-6/12" on:submit|preventDefault={submit}>
			<div class="mb-6">
				<label
					for="username"
					class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
					>Your Username</label
				>
				<input
					bind:value={username}
					id="username"
					class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
					placeholder="Username"
					required
				/>
			</div>
			<div class="mb-6">
				<label
					for="email"
					class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
					>Your email</label
				>
				<input
					bind:value={email}
					type="email"
					id="email"
					class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
					placeholder="name@gmail.com"
					required
				/>
			</div>
			<div class="mb-6">
				<label
					for="password"
					class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
					>Your password</label
				>
				<input
					bind:value={password}
					type="password"
					id="psw"
					class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
					required
				/>
			</div>
			<div class="mb-6">
				<label
					for="repeat-password"
					class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
					>Repeat password</label
				>
				<input
					type="password"
					id="rpsw"
					class="shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light"
					required
				/>
			</div>
			<button
				type="submit"
				class="text-white bg-gb hover:bg-lb focus:ring-4 focus:outline-none focus:ring-db font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-db dark:hover:bg-db dark:focus:ring-db"
				on:click={check_psw}>Register new account</button
			>
			<button
				type="button"
				class="text-white bg-gb hover:bg-lb focus:ring-4 focus:outline-none focus:ring-db font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-db dark:hover:bg-db dark:focus:ring-db"
				on:click={() => goto('/sign_in')}>Already have an account?</button
			>
		</form>
	</div>
	<div
		class="font-mono grid grid-cols-1 content-center col-span-2 bg-gradient-to-r from-gb to-lb h-screen text-white text-center"
	>
		<div class="text-6xl ">Glad to see you!</div>
		<div class="text-3xl pt-16 pb-8 ">Sign-up today to get:</div>
		<div>
			<li class="">An intiuitive and easy-to-use calandar system</li>
			<li class="">High quality revision templates</li>
			<li class="">Follow up actions to keep you on track</li>
		</div>
	</div>
</div>
