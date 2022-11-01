<script>
    import RecipeCard from "../components/recipeCard.svelte";
    import {recipes, isLoggedIn, currentUser} from "../stores/recipestore";
    import { goto } from '$app/navigation';
	import { onMount } from "svelte";

    let searchTerm = '';
    let filteredRecipes= [];

    onMount(() => {
        if($isLoggedIn == false){
            goto('login')
        }
    })

    $: {
        if(searchTerm){
            filteredRecipes = $recipes.filter(recipe => recipe.name.includes(searchTerm));
        } else{
            filteredRecipes = [...$recipes];
        }
    }

</script>
<svelte:head>
    <title>Recipe ok</title>
</svelte:head>

<h1 class="text-4xl text-center my-8 uppercase">{$currentUser}'s Recipe Book</h1>

<input class="w-full rounded-md text-lg p-4 border-2 border-gray-200 mb-4" type="text" placeholder="Search" bind:value={searchTerm}/>

<div class="grid gap-4 md:grid-cols-3 grid-cols-1">
    {#each filteredRecipes as recipe}
    <RecipeCard recipe={recipe}/>
    {/each}
</div>