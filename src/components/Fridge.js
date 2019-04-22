import React from 'react'
const fridgeStyle = {
    width: "550px",
    height: "500px",
    backgroundColor: "#ff00da",
    gridArea: "fridge",
    marginRight: "auto"
}

const Fridge = () => {
    return (
        // must figure out where to send the data to .. post ?? right ?? 
        // and must send it over to the backend somehow
        <div style={fridgeStyle}>

            <form method="POST" action="">
                <label>Ingredient: </label><input name="ingredient" type="text" placeholder="Cauliflower"></input>
            </form>
        
        </div>
    )
}

export default Fridge;