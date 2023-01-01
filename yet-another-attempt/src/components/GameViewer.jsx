import React from 'react'
import {useState, useEffect} from 'react'
import { useTimer,    start,
    pause,
    resume,
    restart,
 } from 'react-timer-hook';

const organObj = [
    {organ: "Nose", icon: "images/nose.png"},
    {organ: "Chin", icon: "images/chin.png"},
    {organ: "Right Elbow", icon: "images/relbow.png"},
    {organ: "Left Hand", icon: "images/lhand.png"},

]
const alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
const randomOutuputGen = () => {
    const randomOrganNo = Math.floor(Math.random()*organObj.length)    
    const randomAlphabetNo = Math.floor(Math.random()*alphabet.length)

return {
    organObj: organObj[randomOrganNo],
    alphabet: alphabet[randomAlphabetNo],
}
}

function GameViewer() {
    
    const [screen, setScreen] = useState(0);
    const [returnObj, setReturnObj] = useState({organObj: {icon: "images/amogus.png"}});

    const [time, setTime] = useState(new Date())
    const {seconds} = useTimer({expiryTimestamp : time.getSeconds() , onExpire: () => console.log("expiry")})

    useEffect(() => {
        if (screen > 0) {
            const rando = randomOutuputGen()
            console.log(rando);
            setReturnObj(rando)
        }
    }, [screen]);
    console.log(seconds);
    const handleKeydown = event => {
        console.log(event.key);
        if (event.key.toLowerCase() === returnObj.alphabet.toLowerCase()) {
            setScreen(screen+1)
        }
    }

    const initHandler = () => {
        if (screen<1){
            setScreen(1)
            setTime(new Date())
            time.setSeconds(time.getSeconds() + 21)
            restart(time)
        }
    }
    console.log()
    return (
    <div  tabIndex={0} onClick={initHandler} onKeyDown={handleKeydown} 
         className='outline-none flex w-screen justify-center'>
        <div className='main-content-box w-[70vw] -translate-y-[15%] border-solid border-8 border-black h-[65vh]'>
        
        {/* Top Navbar */}
        <div className='flex h-[5vh] bg-black flex-row items-center px-4 justify-between'>
            <img className='w-12' src="images/tray.svg" />
            <p className='text-white font-ibm-plex-mono'>21 SECONDS</p>
            <img className='w-6' src="images/plusicon.svg" />
        </div>

        {screen === 0 ? (
            
        <div className='conditional-img h-full flex z-10 items-center justify-center'>
            <div className='w-full flex flex-col items-center h-full justify-center'>
                <h3 className='font-press-start-2p flex text-white'>enter a candy</h3>
                <img src="images/Intro.png" className=' w-1/2' />
            </div>
        </div>
        ) : (
            <div className='flex h-full items-center bg-white justify-center shadow-none'>
                <h1 className='font-black text-[200px] font-press-start-2p shadow-md'>{returnObj.alphabet}</h1>
            </div>
        )}  
        <div>
            
        </div>

        </div>
        <div className='absolute bottom-10 right-10 '>
            <img className='w-[20vw]' src={returnObj.organObj.icon} alt="" />
        </div>
    </div>
  )
}

export default GameViewer