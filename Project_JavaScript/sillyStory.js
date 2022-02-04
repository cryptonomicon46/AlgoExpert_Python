const customname = document.getElementById("customname");
const randomize = document.querySelector(".randomize");
const story = document.querySelector(".story");

function randomValueFromArray(array){
    const random = Math.floor(Math.random()*array.length);
    // console.log(array[random]);
    return array[random];
}



const storyText = 'It was 94 fahrenheit outside, so :insertx: went for a walk. When they got to :inserty:, they stared in horror for a few moments, then :insertz:. Bob saw the whole thing, but was not surprised — :insertx: weighs 300 pounds, and it was a hot day.'

const insertX = ["Willy the Goblin","Big Daddy","Father Christmas"]

const insertY = ["the soup kitchen",
"Disneyland",
"the White House"]

const insertZ = ["spontaneously combusted",
"melted into a puddle on the sidewalk",
"turned into a slug and crawled away"]


randomize.addEventListener("click",result);


function result(){
    let newStory =storyText;
    if (customname.value != 0){
        const name = customname.value;
        newStory =newStory.replace('Bob',name);

        
    }

    let xItem= randomValueFromArray(insertX);
    let yItem = randomValueFromArray(insertY);
    let zItem =  randomValueFromArray(insertZ);
    
    console.log(xItem);
    console.log(yItem);
    console.log(zItem);
    newStory = newStory.replaceAll(':insertx:',xItem);
    console.log(storyText);
    console.log(newStory)
    newStory = newStory.replaceAll(':inserty:',yItem);
    newStory = newStory.replaceAll(':insertz:',zItem);
    newStory = newStory.replaceAll(':insertx:',xItem);

    if (document.getElementById("uk").checked) {
  
        weight = Math.round(300/14);
        temperature = Math.round((94-32)*0.5556);
        let newWeight = weight + " stones";
        let newTemp = temperature + " Centegrade";
        

        newStory = newStory.replace("94 fahrenheit",newTemp);
        newStory = newStory.replace("300 pounds",newWeight);

    }




    



    // console.log(storyText);
    story.textContent = newStory;
    story.style.visibility = 'visible';


}





//Weather Selection

const select = document.querySelector('select');
// const para_weather = document.querySelector('.para_weather');
const para_weather = document.querySelector(".story");

select.addEventListener('change',set_weather);

function set_weather() {
    console.log(select.value);
    if (select.value === 'sunny') {
    para_weather.textContent = "It'll be sunny today, time to hit the beach";}
    else if (select.value ==='rainy'){
        para_weather.textContent = "Don't forget your umbrella";
    }
    else if (select.value ==='snowing'){
        para_weather.textContent = "Make sure to pack your snow chains!";
    }
    else if (select.value ==='overcast'){
        para_weather.textContent = "It'll be a gloomy day folks!";
    }
    else {
        para_weather.textContent="";
    }

    para_weather.style.visibility ='visible';
//     let caseValue = select.value;


// console.log(caseValue==='sunny');

    switch(caseValue) {
        case caseValue === "sunny":
            story.textContent = "It'll be sunny today, time to hit the beach";
            story.style.visibility = 'visible';

            console.log(story.textContent);
        case caseValue === "rainy":
            story.textContent = "Carry your umbrella";
        case caseValue === "snowing":
            story.textContent = "It'll snow today, stay home!";
        case caseValue === "overcast":
            story.textContent = "Today will be a gloomy day";


    }

}








