<script>
	import axios from "axios";
    import { isLoggedIn } from "../../stores/recipestore";
    import { currentUser, recipes } from "../../stores/recipestore";
    import { goto } from '$app/navigation';
	import { prevent_default } from "svelte/internal";

    let username = ''
    let password = ''

    function goToRegisterPage(){
        goto('/register')
    }

    function updateStoreData(){
        currentUser.set(username);
        isLoggedIn.set(true);
        axios.get(`http://127.0.0.1:8000/generic/${username}`)
        .then(res => recipes.set(res.data))
    }

    async function submit(){   
        const response = await axios.get(`http://127.0.0.1:8000/login/${username}`)
        .then((res) => {
            goto('/');
            if (res.status === 200 && (res.data.password === password) ){
                updateStoreData();
            }
            else{
                alert('incorrect pass');
            }

        }).catch((err) => {
            alert(`username does not exist`)
        });

    }
  
</script>

<svelte:head>
    <title>Login</title>
</svelte:head>

<h1 class="text-4xl text-center my-8 uppercase">Welcome to the new home for your recipes</h1>

<div>
<form >
    <label for="text">Enter username</label><br/>
    <input type="text" bind:value={username} class="
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
    <label for="password">Enter password</label><br/>
    <input type="password" bind:value={password} class="
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

        <button type="submit" class="
            px-6
            py-2.5
            bg-blue-600
            text-white
            font-medium
            text-xs
            leading-tight
            uppercase
            rounded
            shadow-md
            hover:bg-blue-700 hover:shadow-lg
            focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0
            active:bg-blue-800 active:shadow-lg
            transition
            duration-150
            ease-in-out
            mb-5" 
            href="http://127.0.0.1:5173/"
            on:click|preventDefault={submit}>Login</button> <br/>

            <button type="submit" class="
            px-6
            py-2.5
            bg-blue-600
            text-white
            font-medium
            text-xs
            leading-tight
            uppercase
            rounded
            shadow-md
            hover:bg-blue-700 hover:shadow-lg
            focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0
            active:bg-blue-800 active:shadow-lg
            transition
            duration-150
            ease-in-out" 
            href="http://127.0.0.1:5173/"
            on:click|preventDefault={goToRegisterPage}>Register here</button>
</form>
</div>
