import React, {useState} from 'react'

function Timer() {

  const [sec, setSec] =  useState(21)
  
  setTimeout(() => {
    if (sec > 0){
      console.log(sec);
      setSec(sec - 1)
    }
  }, 1000);

    return (
    <div>Timer</div>
  )
}

export default Timer