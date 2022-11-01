<script>
    import RecipeInfo from "../../components/recipeInfo.svelte"
    import { rec } from "../../stores/recipestore";
</script>

<h1 class="text-4xl text-center my-8 uppercase">{$rec.name}</h1>
<div class="grid gap-4 md:grid-cols-2 grid-cols-1">
    <RecipeInfo recipe = {$rec}/>
</div>

