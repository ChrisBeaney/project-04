import React from 'react'

const CourseCard = ({ name, par }) => {

  return(
    <div className="card">
      <h2>{name}</h2>
      <h4>{par}</h4>
    </div>
  )
}

export default CourseCard
