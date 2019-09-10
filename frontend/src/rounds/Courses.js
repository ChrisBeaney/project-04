import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import CourseCard from '../common/Card'


class CoursesIndex extends React.Component {

  constructor() {
    super()
    this.state = {
      courses: []
    }
  }

  componentDidMount() {
    axios.get('/api/courses')
      .then(res => {
        this.setState({ courses: res.data })
      })
  }

  render() {
  return(
    <div className="columns is-multiline">
      {!this.state.courses && <h2 className="title is-2">Loading courses...</h2>}
      {this.state.courses.map(recipe =>
        <div key={course.id} className="column is-half-tablet is-one-quarter-desktop">
          <Link to={`/courses/${course.id}`}>
            <Card {...course} />
          </Link>
        </div>
      )}

    </div>
  )
}


}

export default CoursesIndex
