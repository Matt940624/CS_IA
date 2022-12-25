<script lang="ts">
	import '../../app.css';
	import axios from 'axios';

	import {
		Navbar,
		NavBrand,
		NavLi,
		NavUl,
		NavHamburger,
		Button,
		Input,
	} from 'flowbite-svelte';
	import {
		Drawer,
		CloseButton,
		Sidebar,
		SidebarBrand,
		SidebarCta,
		SidebarDropdownItem,
		SidebarDropdownWrapper,
		SidebarGroup,
		SidebarItem,
		SidebarWrapper,
	} from 'flowbite-svelte';
	import { sineIn } from 'svelte/easing';
	import { goto } from '$app/navigation';
	let hidden2 = true;
	let spanClass = 'flex-1 ml-3 whitespace-nowrap';
	let transitionParams = {
		x: -320,
		duration: 200,
		easing: sineIn,
	};

	let email = '',
		password = '';
	axios.defaults.headers.post['Content-Type'] =
		'application/json;charset=utf-8';
	axios.defaults.headers.post['Origin'] = 'http://localhost:5173/';
	axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';

	$: submit = async () => {
		const response = await axios.post(
			'http://localhost:8000/api/login/',
			{
				email,
				password,
			},
			{ withCredentials: true }
		);
		if (response.status === 200) {
			axios.defaults.headers.common[
				'Authorization'
			] = `Bearer ${response.data.token}`;
			await goto('/timer');
		}
	};
</script>

<div class="grid grid-cols-5 gap-2">
	<div
		class="col-span-3 justify-center justify-items-center grid grid-cols-1 content-center"
	>
		<div class="text-5xl mb-6">Sign In</div>
		<form class="w-6/12" on:submit|preventDefault={submit}>
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

			<button
				type="submit"
				class="text-white bg-gb hover:bg-lb focus:ring-4 focus:outline-none focus:ring-db font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-db dark:hover:bg-db dark:focus:ring-db"
				>Sign In</button
			>
		</form>
	</div>
	<div
		class="font-mono grid grid-cols-1 content-center col-span-2 bg-gradient-to-r from-gb to-lb h-screen text-white text-center"
	>
		<div class="text-6xl ">Welcome Back!</div>
		<div class="text-3xl pt-16 pb-8 ">
			Sign in to discover and be PRODUCTIVE
		</div>
		<div>
			<button
				type="button"
				on:click={() => goto('/sign_up')}
				class="text-white bg-gb hover:bg-lb focus:ring-4 focus:outline-none focus:ring-db font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-db dark:hover:bg-db dark:focus:ring-db"
				>Don't have an account?</button
			>
		</div>
	</div>
</div>
