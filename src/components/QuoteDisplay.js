import React, { Component } from 'react'
import './css/QuoteDisplay.css' // Styling component with external CSS



class QuoteDisplay extends Component {

    // Initialize state of component
    // In most cases this should be done within the constructor
    state = {
      loading: true
    }

    

  // Asynchronous function gets quote from backend or API then changes the state of component when quote has been obtained
  async componentDidMount(){
    const QuoteURL = "https://ron-swanson-quotes.herokuapp.com/v2/quotes" // URL of API
    //const QuoteURL = "http://localhost:5000/get_quote" // URL of Flask backend endpoint
    const response = await fetch(QuoteURL)
    const data = await response.json()
    // Change state of component
    this.setState({quote: data, loading: false})
  }


  render(){
    return(
      <div className="quotesSection">
        <div className="quoteText">
          <em>{this.state.loading ? <div> Loading...</div> : <div>"{this.state.quote}"</div>}</em>
        </div>
      </div>
    )
  }
}


export default QuoteDisplay
