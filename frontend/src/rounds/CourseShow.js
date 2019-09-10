import React from 'react'
import axios from 'axios'

import Auth from '../../lib/Auth'

class CourseShow extends React.Component {

  constructor() {
    super()
    this.state = {
      course: {}
    }

  }

  componentDidMount() {
  axios.get(`/api/courses/${this.props.match.params.id}/`)
    .then(res => this.setState({ course: res.data }))
    .then(() => console.log(this.state.course))
  }


  render() {

  }

}


export default CourseShow
