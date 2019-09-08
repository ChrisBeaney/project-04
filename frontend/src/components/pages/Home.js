import React from 'react'

class Home extends React.Component {
  constructor() {
    super()

    this.state = {}

  }


  render() {
    return (
      <section className="hero is-info is-large">
        <div className="hero-body">
          <div className="container">
            <h1 className="title">
              ScoreTracker
            </h1>
            <h2 className="subtitle">
              Enter scores
            </h2>
          </div>
        </div>
      </section>
    )
  }
}

export default Home
