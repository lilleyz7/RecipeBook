import { writable } from 'svelte/store';
import axios from "axios";

export const recipes = writable([]);
export const baseRecipes = writable([]);
export const rec = writable('');
export const isLoggedIn = writable(false);
export const currentUser = writable('');
export const page = writable('');

function loadData(){
    axios.get('http://localhost:8000/generic')
    .then(res => recipes.set(res.data))
};
function loadBase(){
    axios.get('http://localhost:8000/generic')
    .then(res => baseRecipes.set(res.data))
};
loadData();
loadBase();



