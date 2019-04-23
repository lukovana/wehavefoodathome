import React from 'react';
import './css/componentCSS.css'

const Fridge = () => {
    return (
        // must figure out where to send the data to .. post ?? right ?? 
        // and must send it over to the backend somehow
        <div className = "fridgeStyle">
            <p>Enter the ingredients separated by a comma (ingredient, ingredient, ingredient)</p>
            <form method="POST" action="http://ss1.ciwcertified.com/cgi-bin/process.pl">
                <label>Ingredient: </label><input type="text" name="ingredient"/> 
                <button type="submit">Submit</button>
                <button type="reset">Reset</button>
            </form>
        
        </div>
    )
}

export default Fridge;