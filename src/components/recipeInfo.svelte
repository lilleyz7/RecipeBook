<script>
    export let recipe;
    let index = 0;

    const increment = () => {
        index++;
    }

</script>

<div class="p-6 bg-gray-100 text-gray-800 text-left rounded-md
            shadow-sm hover:shadow-md flex flex-col text-xl">
    <h1 class="text-4xl text-left my-2 uppercase"> Necessary ingredients:</h1>
    {#each recipe.ingredients as ingredient}
    <p class="text-xl text-left my-2 uppercase">- {ingredient}</p>
    {/each}
</div>
<div class="p-6 bg-gray-100 text-gray-800 text-left rounded-md
            shadow-sm hover:shadow-md flex flex-col  text-xl">
    <h1 class="text-4xl text-left my-2 uppercase"> Steps:</h1>
    {#each recipe.steps as step}
    <p class="text-xl text-left my-2 uppercase">- {step}</p>
    {/each}
</div>