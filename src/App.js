import React, { Component } from 'react';
import './App.css';
import Title from './components/Title'
import Fridge from './components/Fridge'
import RecipeDisplay from './components/RecipeDisplay'



class App extends Component {
  render() {
    return (
        <div className="main">
          <Title/>
          <Fridge/>
          <RecipeDisplay/>
        </div>
    );
  }
}


export default App;
