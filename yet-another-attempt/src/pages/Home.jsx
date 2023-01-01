import React from 'react'
import GameViewer from '../components/GameViewer'
import Header from '../components/Header'

function Home() {
  return (
    <div className='bg-gray w-screen overflow-hidden'>
        <Header />
        <GameViewer />
    </div>
  )
}

export default Home