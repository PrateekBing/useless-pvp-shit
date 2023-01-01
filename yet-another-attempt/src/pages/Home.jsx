import React from 'react'
import GameViewer from '../components/GameViewer'
import Header from '../components/Header'
import useSound from 'use-sound';
import gangamStyle from '../music/main.mp3'


function Home() {
  const [play] = useSound(gangamStyle);
  play()
  return (
    <div className='bg-gray w-screen overflow-hidden'>
        <Header />
        <GameViewer />
        {/* <Timer></Timer> */}
    </div>
  )
}

export default Home