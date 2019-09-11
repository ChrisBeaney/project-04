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


  // render() {
  //   return(
  //     <div className="columns is-multiline">
  //       {!this.state.course && <h2 className="title is-2">Loading course...</h2>}
  //       {this.state.course.map(course =>
  //         <div key={course.id} className="column is-half-tablet is-one-quarter-desktop">
  //           <Link to={`/courses/${course.id}`}>
  //             <CourseCard {...course} />
  //           </Link>
  //         </div>
  //       )}
  //
  //     </div>
  //   )
  // }

}


export default CourseShow
