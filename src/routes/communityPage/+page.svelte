<script>
    import RecipeCard from "../../components/recipeCard.svelte";
    import { baseRecipes } from "../../stores/recipestore";

</script>

<svelte:head>
    <title>Community Page</title>
</svelte:head>


<h1 class="text-4xl text-center my-5 uppercase">Recent Community Recipes</h1> <hr class="mt-0 mb-5"/>

<div class="grid gap-4 md:grid-cols-3 grid-cols-1">
    {#each $baseRecipes as recipe}
    <RecipeCard recipe={recipe}/>
    {/each}
</div>