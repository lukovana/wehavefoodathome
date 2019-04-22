import React from 'react'


// Styling Button component with JSX object
const buttonStyle = {

  width: "700px",
  height: "50px",
  backgroundColor: "#1a8cff",
  color: "#fff",
  fontSize: "18px",
  borderRadius: "5px",
  textRecoration: "none",
  marginTop: "-10%"
}


const Button = () => {
  const HandleClick = () => {
    window.location.reload()
  }

  return (
    <button style={buttonStyle} onClick={HandleClick}>
      Generate Quote
    </button>
    )
  }

export default Button