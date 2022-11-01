<script>
	import axios from "axios";
    import {navigate} from "svelte-routing";
    import { goto } from '$app/navigation';

    let email = ''
    let username = ''
    let password = ''
    let password2 = ''

    const submit = async () => {
        if (password === password2){
            navigate('/', { replace: true });
            await axios.post('http://127.0.0.1:8000/register_user', {
            'email': email,
            'password': password,
            'username': username}
        )
        }
        else{
            alert('Passwords do not match')
        }
    }

    function redirect(){
        goto('/login');
    }

</script>

<svelte:head>
    <title>Register</title>
</svelte:head>

<h1 class="text-4xl text-center my-8 uppercase">Welcome to the new home for your recipes</h1>

<div>
<form class="">
    <label for="username">Enter username</label><br/>
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
    <label for="email">Enter email</label><br/>
    <input type="email" bind:value={email} class="
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
    <label for="password2">Enter password again</label><br/>
    <input type="password" bind:value={password2} class="
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
            mb-5" on:click|preventDefault={submit}>Sign up</button> <br/>

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
            ease-in-out" on:click|preventDefault={redirect}>Already have an account? Login here</button>
</form>
</div>