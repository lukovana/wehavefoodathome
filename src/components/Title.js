import React from 'react'

// Styling Tittle component with JSX object
const TitleStyle = {
  color: "#000",
  gridArea: "title"
}

const Title = () => (
    <div style={TitleStyle}>
      <h2 className="titleText">"We Have Food at Home"</h2>
    </div>
)

export default Title
