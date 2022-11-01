import axios from "axios";

export const load = () =>{
    let recipe = '';
    axios.get(`http://localhost:8000/generic/${recipe.name}`)
    .then(res => recipe = (res.data))
    return {recipe}
}