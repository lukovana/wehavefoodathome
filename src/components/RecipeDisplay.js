import React from 'react';

const recipeStyle = {
    width: "550px",
    height: "500px",
    backgroundColor: "#234a88",
    gridArea: "recipe",
    marginLeft: "auto"
}

// class RecipeDisplay extends Component {

//     // Initialize state of component
//     state = {
//       loading: true
//     }

//   // Asynchronous function gets quote from backend or API then changes the state of component when quote has been obtained
//   async componentDidMount(){
//     const RECIPE_URL = "http://localhost:5000/get_recipe" // URL of Flask backend endpoint
//     const response = await fetch(RECIPE_URL)
//     const data = await response.json()
//     // Change state of component
//     this.setState({recipe: data, loading: false})
//   }


//   render(){
//     return(
//       <div className="recipeSection">
//         <div className="recipeText">
//           <em>{this.state.loading ? <div> Loading...</div> : <div>"{this.state.recipe}"</div>}</em>
//         </div>
//       </div>
//     )
//   }
// }

const RecipeDisplay = () => {
    return (
        <div style={recipeStyle}>
            IFFFFFFFFFFFFFFFFFFFFFFFFFFFF
            <br></br>
            <br></br>
            insert instructions as the initial state here.
            and set the state to the recipe after it has been fetched and stuff.
        </div>
    )
}

export default RecipeDisplay