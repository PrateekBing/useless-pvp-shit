const organObj = [
    {organ: "Nose", icon: "public/icons/Nose.svg"},
    {organ: "Chin", icon: "public/icons/Chin.svg"},
    {organ: "Right Elbow", icon: "public/icons/ElbowRight.svg"},
    {organ: "Left Hand", icon: "public/icons/LeftHand.svg"},

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

console.log(randomOutuputGen());