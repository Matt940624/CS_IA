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
	let hidden2 = true;
	let spanClass = 'flex-1 ml-3 whitespace-nowrap';
	let transitionParams = {
		x: -320,
		duration: 200,
		easing: sineIn,
	};
	import icon from '$lib/assets/icon.jpg';
	// import icon from 'static\\images\\icon.jpg';
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
		<Button size="sm">Get started</Button>
		<NavHamburger on:click={toggle} />
	</div>
	<NavUl {hidden} class="order-1">
		<NavLi href="/" active={true}>Home</NavLi>
		<NavLi href="/tasklist">Tasklist</NavLi>
		<NavLi href="/timer">Timer</NavLi>
		<NavLi href="/flashcards">Flashcards</NavLi>
		<NavLi href="/edit_flashcards">Edit Flashcards</NavLi>
	</NavUl>
</Navbar>
