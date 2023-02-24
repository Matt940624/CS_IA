<script lang="ts">
	import '../app.css';
	import {
		Navbar,
		NavBrand,
		NavLi,
		NavUl,
		NavHamburger,
		Button,
		Input,
	} from 'flowbite-svelte';
	import { signOut } from '../stores/auth';
	import { sineIn } from 'svelte/easing';
	let hidden2 = true;
	let spanClass = 'flex-1 ml-3 whitespace-nowrap';
	let transitionParams = {
		x: -320,
		duration: 200,
		easing: sineIn,
	};
	import icon from '$lib/assets/icon.jpg';
	import { goto } from '$app/navigation';
	// import icon from 'static\\images\\icon.jpg';
	const handleSignOut = () => {
		signOut();
		goto('/sign_in');
	};
</script>

<Navbar let:hidden let:toggle>
	<NavBrand href="/">
		<img src={icon} class="mr-3 h-14 sm:h-9" alt="Logo" />
		<span
			class="self-center whitespace-nowrap text-xl font-semibold dark:text-white"
		>
			Productivity Up
		</span>
	</NavBrand>
	<div class="flex md:order-2">
		<Button size="sm" on:click={handleSignOut}>Logout</Button>
		<NavHamburger on:click={toggle} />
	</div>
	<NavUl {hidden} class="order-1">
		<NavLi href="/" active={true}>Home</NavLi>
		<NavLi href="/tasklist">Tasklist</NavLi>
		<NavLi href="/timer">Timer</NavLi>
		<NavLi href="/flashcards">Flashcards</NavLi>
		<NavLi href="/edit_flash">Edit Flashcards</NavLi>
	</NavUl>
</Navbar>
