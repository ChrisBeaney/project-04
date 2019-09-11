import React from 'react'
import axios from 'axios'


class Profile extends React.Component {

  constructor() {
    super()

    this.state = {}
  }

  componentDidMount() {
    axios.get('/api/profile')
      .then(res => {
        this.setState({ profile: res.data })
      })
  }

  render() {
    if(!this.state.profile) return null
    console.log(this.state.profile.scores)

    const scores = this.state.profile.scores
    const rounds = []

    scores.forEach(score => {
      score.date
    })

    return(
      <section>
        <h1>Profile Page</h1>
        <h2>Player:&nbsp;{this.state.profile.username}</h2>
        <table className="table is-bordered">
          <thead>
            <tr>
              <th>Hole</th>
              <th>Yards</th>
              <th>SI</th>
              <th>Par</th>
              <th>Score</th>
            </tr>
          </thead>
          <tbody>
            {this.state.profile.scores.map(score => <tr key={score.id}>
              <td>{score.hole.number}</td>
              <td>{score.hole.yards}</td>
              <td>{score.hole.stroke_index}</td>
              <td>{score.hole.par}</td>
              <td>{score.shots}</td>
            </tr>
            )}
          </tbody>
        </table>
      </section>
    )
  }

}


export default Profile
