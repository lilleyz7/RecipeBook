<script>
    import axios from "axios";
    import { currentUser } from "../../stores/recipestore";
    import { goto } from '$app/navigation';

    const formValues = {
        name: '',
        dishType: '',
        ingredients: '',
        steps: '',
        imgUrl: '',
        user: $currentUser
    }

    function addRecipeHandler () {
      goto('/')
        axios.post('http://127.0.0.1:8000/add_recipe', {
            'name': formValues.name,
            'imageUrl': formValues.imgUrl,
            'ingredients': formValues.ingredients.split(","),
            'steps': formValues.steps.split("."),
            'dishType': formValues.dishType,
            'user': formValues.user
    })

};

</script>
<svelte:head>
    <title>Add Recipe</title>
</svelte:head>

<form>
    <label for="name">Enter the name of your recipe:</label><br/>
    <input type="text" bind:value={formValues.name} class="
        form-control
        block
        w-full
        px-3
        py-1.5
        text-base
        font-normal
        text-gray-700
        bg-white bg-clip-padding
        border border-solid border-gray-300
        rounded
        transition
        ease-in-out
        m-0
        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"><br/>
    <label for="dishType">Type of dish:</label><br/>
    <input type="text" bind:value={formValues.dishType} class="
    form-control
    block
    w-full
    px-3
    py-1.5
    text-base
    font-normal
    text-gray-700
    bg-white bg-clip-padding
    border border-solid border-gray-300
    rounded
    transition
    ease-in-out
    m-0
    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
  "><br/>
    <label for="photo">Would you like to add a picture:</label><br/>
    <input type="text" bind:value={formValues.imgUrl} class="
    form-control
    block
    w-full
    px-3
    py-1.5
    text-base
    font-normal
    text-gray-700
    bg-white bg-clip-padding
    border border-solid border-gray-300
    rounded
    transition
    ease-in-out
    m-0
    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
  "><br/>
    <label for="ingredients">List ingredients seperated by commas:</label><br/>
    <textarea cols="60" rows="10" bind:value={formValues.ingredients} class="
    form-control
    block
    w-full
    px-3
    py-1.5
    text-base
    font-normal
    text-gray-700
    bg-white bg-clip-padding
    border border-solid border-gray-300
    rounded
    transition
    ease-in-out
    m-0
    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
  "/><br/>
    <label for="steps">List steps seperated by periods:</label><br/>
    <textarea cols="60" rows="10" bind:value={formValues.steps} class="
    form-control
    block
    w-full
    px-3
    py-1.5
    text-base
    font-normal
    text-gray-700
    bg-white bg-clip-padding
    border border-solid border-gray-300
    rounded
    transition
    ease-in-out
    m-0
    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
  "/><br/>
  <button class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded
   shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 
   active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
   on:click={addRecipeHandler}>Add recipe</button>
</form>