<script>
    export let recipe;
    import {rec, page} from '../stores/recipestore';

    const onClickHandler = () => {
        rec.set(recipe);
    }

</script>
<div>
<a class="p-6 bg-gray-100 text-gray-800 text-center rounded-md
         shadow-sm hover:shadow-md flex flex-col items-center" href="http://127.0.0.1:5173/recipeInformation" on:click={onClickHandler}>
    <h2 class="uppercase text-3xl mb-8">{recipe.name}</h2>
    <img class="h-40 w-40" src={recipe.imageUrl} alt={recipe.name}>
</a>
{#if $page != 'community'}
<div class="flex flex-col items-center mt-5">
<button type="button" class="inline-block px-6 py-2.5 bg-red-600
    text-white font-medium text-xs leading-tight uppercase rounded 
    shadow-md hover:bg-red-700 hover:shadow-lg focus:bg-red-700 focus:shadow-lg
    focus:outline-none focus:ring-0 active:bg-red-800
    active:shadow-lg transition duration-150 ease-in-out">Delete</button>
</div>
{/if}
</div>
