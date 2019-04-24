import React from 'react';
import './css/componentCSS.css';

const Fridge = () => {
    return (
        // http://ss1.ciwcertified.com/cgi-bin/process.pl
        // must figure out where to send the data to .. post ?? right ?? 
        // and must send it over to the backend somehow

        // input idea: you just get one input line, send the data over to python, 
        // as a string, and python will just split it and add it to the ingredient
        // list

        <div className = "fridgeStyle">
            <p>Enter the ingredients separated by a comma (ingredient, ingredient, ingredient)</p>
            <form method="POST" action="http://localhost:5000/input" target="_blank">
                <label>Ingredient: </label><input type="text" name="ingredient"/> 
                <button type="submit">Submit</button>
                <button type="reset">Reset</button>
            </form>
        
        </div>
    )
}

export default Fridge;