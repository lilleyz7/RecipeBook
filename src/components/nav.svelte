<script>
    import { isLoggedIn, currentUser, recipes, page} from "../stores/recipestore";

    function logoutHandler(){
        currentUser.set('');
        isLoggedIn.set(false);
        axios.get(`http://127.0.0.1:8000/generic`)
        .then(res => $recipes.set(res.data))
    }

    function communityHandler(){
        page.set('community')
    }

    function homeHandler(){
        page.set('home')
    }
</script>

<div class="mt-5">
<nav class="flex justify-center w-full">
    <a class="mx-4 text-xl" href='/' on:click={homeHandler}>Home</a>
    <a class="mx-4 text-xl" href='/communityPage' on:click={communityHandler}>Community Recipes</a>
    <a class="mx-4 text-xl mb-3" href='/addrecipe'>Add recipe</a>
    {#if $isLoggedIn == false}
    <a class="mx-4 text-xl mb-3" href='/register'>Login/ Register</a>
    {:else}
    <a class="mx-4 text-xl mb-3" href='/login' on:click={logoutHandler}>Logout</a>
    {/if}

</nav>
</div>