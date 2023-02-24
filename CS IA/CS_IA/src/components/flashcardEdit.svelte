<script lang="ts">
	import '../app.css';
	import { Modal, Button } from 'flowbite-svelte';
	import { onMount } from 'svelte';
	import { vocab, initVocab } from '../components/vocabData';

	let defaultModal = false;

	let vocabulary = vocab;
	let questionValue = '';
	let answerValue = '';

	$: buttonDisabled = questionValue === '' || answerValue === '';

	function addPair() {
		vocabulary.push({ word: questionValue, definition: answerValue });
		vocabulary = [...vocabulary];
		questionValue = '';
		answerValue = '';
	}

	$: {
		vocabulary = vocabulary;
	}
	onMount(() => {
		vocabulary = vocabulary;
		console.log('init');
		console.log(initVocab);
		console.log('vocab');
		console.log(vocabulary);
	});

	function delCards() {
		confirm('Are you sure you want to delete all the flashcards');
		vocabulary = [];
	}

	function delCard(index: number) {
		vocabulary = vocabulary.filter((item, i) => i !== index);
	}
	function saveNew() {
		// need to add
	}
</script>

<div class="grid justify-items-center items-center h-screen">
	<div
		style="min-height: 75%; height: auto;"
		class="grid grid-cols-4 justify-items-center items-center bg-white border rounded-lg shadow-xl w-11/12 "
	>
		<div class="grid col-span-4 text-4xl justify-items-center">
			<ul
				class="w-full grid grid-cols-4 gap-x-4 gap-y-4 ml-8"
				style="display: flex; flex-direction:row; flex-wrap: wrap;"
			>
				{#each vocabulary as item, i}
					<li>
						<div
							class="bg-slate-100 border-solid border-2 border-slate-700 rounded-lg shadow-xl hover:rotate-y-180 transition-all duration-500 w-[300px]"
						>
							<div class="grid grid-cols-4 justify-items-end">
								<div class="col-end-5 text-sm">
									<button
										on:click={() => delCard(i)}
										class="bg-lg  px-2 py-1  rounded-tr-lg ">x</button
									>
								</div>
							</div>
							<div class="px-6 py-4">
								<div class="font-bold text-lg mb-2 text-gb">Question</div>
								<p class="text-base">{item.word}</p>
							</div>
							<div class="px-6 py-4">
								<div class="font-bold text-lg mb-2 text-gb">Answer</div>
								<p class="text-base">{item.definition}</p>
							</div>
						</div>
					</li>
				{/each}
			</ul>
		</div>

		<div class="col-span-4">
			<div class="container">
				<div id="flashcards" />
				{#if vocabulary.length === 0}
					<div class="text-xl">Create your first flashcard!</div>
				{/if}
			</div>
		</div>

		<div class="col-span-2 col-start-2 mt-4 mb-4">
			<div class="col-span-4 items-center">
				<Button on:click={() => (defaultModal = true)}>Add Card</Button>
				<Button on:click={delCards}>Delete All Flashcards</Button>
				<button
					class="bg-dg px-6 py-2 text-md rounded-lg hover:bg-lg"
					on:click={saveNew}>Save Word Set</button
				>
				<Modal title="Flashcard Information" bind:open={defaultModal} autoclose>
					<div id="create_card">
						<div id="class">
							<label for="question">Question</label>
						</div>
						<div>
							<input
								type="text"
								bind:value={questionValue}
								placeholder="Enter Question or Word"
								id="question"
								class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
							/>
						</div>
						<div>
							<label for="answer">Answer/Definition</label>
						</div>
						<div>
							<input
								type="text"
								bind:value={answerValue}
								placeholder="Enter Answer or Definition"
								id="answer"
								class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
							/>
						</div>
					</div>
					<svelte:fragment slot="footer">
						<button
							on:click={addPair}
							class="bg-dg px-6 py-2 text-md rounded-lg hover:bg-lg"
							disabled={buttonDisabled}
						>
							Save</button
						>
						<button class="bg-dg px-6 py-2 text-md rounded-lg hover:bg-lg"
							>Close</button
						>
					</svelte:fragment>
				</Modal>
			</div>
		</div>
	</div>
</div>
