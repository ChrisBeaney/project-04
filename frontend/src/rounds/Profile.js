import React from 'react'
import axios from 'axios'


class Profile extends React.Component {

  constructor() {
    super()

    this.state = {}

    this.totalShots = this.totalShots.bind(this)
    this.totalYards = this.totalYards.bind(this)
    this.selectRounds = this.selectRounds.bind(this)
  }

  componentDidMount() {
    axios.get('/api/profile')
      .then(res => {
        this.setState({ profile: res.data })
      })
  }

  totalShots() {
    const shotsArray = []
    this.state.profile.scores.forEach(score => {
      shotsArray.push(score.shots)
    })
    return shotsArray.reduce((acc, score) => acc + score, 0)
  }

  totalYards() {
    const yardsArray = []
    this.state.profile.scores.forEach(score => {
      yardsArray.push(score.hole.yards)
    })
    return yardsArray.reduce((acc, length) => acc + length, 0)
  }

  selectRounds() {
    const numRounds = this.state.profile.scores.length / 18
    return numRounds
  }

  render() {
    if(!this.state.profile) return null
    const { scores } = this.state.profile
    const firstRound = Object.keys(scores)[0]
    return(
      <section>
        <h1>Profile Page</h1>
        <h2>Player:&nbsp;{this.state.profile.username}</h2>
        <h2>Course:&nbsp;{scores[firstRound][0].hole.course.name}</h2>
        <table className="table is-bordered">
          <thead>
            <tr>
              <th>Hole</th>
              <th>Yards</th>
              <th>SI</th>
              <th>Par</th>
              {Object.keys(scores).map(date => <th key={date}>{date}</th>)}
            </tr>
          </thead>
          <tbody>
            {scores[firstRound].map((score, index) =>
              <tr key={score.id}>
                <td>{score.hole.number}</td>
                <td>{score.hole.yards}</td>
                <td>{score.hole.stroke_index}</td>
                <td>{score.hole.par}</td>
                {Object.keys(scores).map(date =>
                  <td key={date}>{scores[date][index].shots}</td>
                )}
              </tr>
            )}
          </tbody>
        </table>
      </section>
    )
  }

}


export default Profile
