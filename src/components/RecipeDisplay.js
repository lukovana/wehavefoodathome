import React, { Component } from 'react';

const recipeStyle = {
    width: "550px",
    height: "500px",
    backgroundColor: "#ff0000",
    gridArea: "recipe",
    marginLeft: "auto"
}

class RecipeDisplay extends Component {

     // Initialize state of component
    state = {
       loading: true
    }

   // Asynchronous function gets quote from backend or API then changes the state of component when quote has been obtained
   
/*
    whats goin on

        the recipe url is valid
        things to configure:  await fetch(URL)
                              await response.json()

        my program does not return data as a json file
        it is definitely possible to onfigure it this way
        but it would probably genereate extra work for me
        then again it could be a better way to format the data

*/
  async componentDidMount(){
    const RECIPE_URL = "http://localhost:5000/test" // URL of Flask backend endpoint
    const response = await fetch(RECIPE_URL)
    const data = await response.text() // we could also potentially use response.formData()
    // Change state of component
    this.setState({recipe: data, loading: false})
  }

  render(){
    return(
      <div className="recipeSection">
        <div style={recipeStyle}>
          <em>{this.state.loading ? <div> Loading...</div> : <div>"{this.state.recipe}"</div>}</em>
        </div>
      </div>
    )
  }
}

// const RecipeDisplay = () => {
//     return (
//         <div style={recipeStyle}>
//             IFFFFFFFFFFFFFFFFFFFFFFFFFFFF
//             <br></br>
//             <br></br>
//             insert instructions as the initial state here.
//             and set the state to the recipe after it has been fetched and stuff.
//         </div>
//     )
// }

export default RecipeDisplay