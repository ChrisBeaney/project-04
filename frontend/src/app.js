import React from 'react'
import ReactDOM from 'react-dom'
// import axios from 'axios'

class App extends React.Component {
  // componentDidMount() {
  //   axios.get('/api/rounds/')
  //     .then(res => console.log(res.data))
  // }

  render() {
    return(
      <div>
        <h1>Hello Django!</h1>
        <h2>Project-04</h2>
      </div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
