<script>
	import '../app.css';
	import { vocab } from '../components/vocabData';
	let revealAnswer = false;
	const showAnswer = () => (revealAnswer = !revealAnswer);

	const prev = () => {
		revealAnswer = false;
		if (flashcardIndex === 0) {
			flashcardIndex = vocab.length - 1;
		} else {
			flashcardIndex -= 1;
		}
	};

	const next = () => {
		revealAnswer = false;
		if (flashcardIndex === vocab.length - 1) {
			flashcardIndex = 0;
		} else {
			flashcardIndex += 1;
		}
	};

	let flashcardIndex = 0;
	/**
	 * @type {any}
	 */
	$: answer = vocab[flashcardIndex].definition;
	/**
	 * @type {any}
	 */
	$: word = vocab[flashcardIndex].word;
</script>

<div class="grid justify-items-center items-center h-screen ">
	<div
		class="grid grid-cols-4 col-span-4 grid-rows-6 justify-items-center items-center bg-white border rounded-lg shadow-xl w-9/12 h-3/4 "
	>
		<div
			class="flip-box-inner col-span-4 row-span-5 bg-white border rounded-lg shadow-xl w-full h-full"
			class:flip-it={revealAnswer === true}
		>
			<!-- front side -->
			<div class="flip-box-front grid items-center ">
				<div class="text-black text-3xl">{word}</div>
			</div>
			<!-- back side -->
			<div class="flip-box-back grid items-center">
				<div class="text-black text-3xl">
					{answer}
				</div>
			</div>
		</div>
		<div class="col-span-4 row-start-6 row-span-1">
			<button class="rounded-lg bg-lb px-4 py-2" on:click={prev}>&#8592;</button
			>
			<button on:click={showAnswer} class="rounded-lg bg-lb px-4 py-2"
				>{revealAnswer ? 'Show Word' : 'Show Definition'}</button
			>
			<button class="rounded-lg bg-lb px-4 py-2" on:click={next}>&#8594;</button
			>
		</div>
	</div>
</div>

<div />

<style>
	/* This container is needed to position the front and back side */
	.flip-box-inner {
		position: relative;
		text-align: center;
		transition: transform 0.8s;
		transform-style: preserve-3d;
	}

	/* Do an horizontal flip when you move the mouse over the flip box container */
	/* .flip-box:hover .flip-box-inner {
		transform: rotateY(180deg);
	} */
	.flip-it {
		transform: rotateY(180deg);
	}
	/* Position the front and back side */
	.flip-box-front,
	.flip-box-back {
		position: absolute;
		width: 100%;
		height: 100%;
		-webkit-backface-visibility: hidden; /* Safari */
		backface-visibility: hidden;
	}

	/* Style the front side */

	/* Style the back side */
	.flip-box-back {
		transform: rotateY(180deg);
	}
</style>
